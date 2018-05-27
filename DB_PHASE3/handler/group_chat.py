from flask import jsonify
from dao.group_chat import Group_ChatDAO
from dao.administrates import *
from dao.users import *


class ChatsHandler:


    def mapToDict(self, row):
        result = {}
        result['group_id'] = row[0]
        result['group_name'] = row[1]
        result['gnumber_of_users'] = row[2]
        result['gactive_users'] = row[3]
        result['group_date'] = row[4]
        return result

    def getAllChats(self):
        dao = Group_ChatDAO()
        result = dao.getAllChats()
        mapped_result = []
        for r in result:
            mapped_result.append(self.mapToDict(r))
        return jsonify(Chats=mapped_result)


    def getChatByID(self, id):
        dao = Group_ChatDAO()
        result = dao.getChatById(id)
        if result == None:
            return jsonify(Error="CHAT NOT FOUND")
        else:
            mapped = self.mapToDict(result)
            return jsonify(Chat=mapped)

    def findChat(self, name):
        dao = Group_ChatDAO()
        result = dao.searchByChatName(name)
        if result == None:
            return jsonify(Error="CHAT NOT FOUND")
        else:
            mapped = self.mapToDict(result)
            return jsonify(Chat=mapped)


    def group_attributes(self, group_name, first_name, last_name):
        result = {}
        result['group_name'] = group_name
        result['first_name'] = first_name
        result['last_name'] = last_name

        return result

    def checkGroup(self, form):

        if len(form) != 3:
            return jsonify(Error="Malformed post request"), 400
        else:
            group_name = form['group_name']
            first_name = form['first_name']
            last_name = form['last_name']
            if group_name and first_name and last_name:
                dao = Group_ChatDAO()
                check = dao.check(group_name) # only checking if group exists or not
                if(check is None):
                    return None
                else:
                    result = self.group_attributes(group_name,first_name,last_name)
                    return jsonify(users=result), 201
            else:
                 return jsonify(Error="Unexpected attributes in post request"), 400

    def registerGroup(self, form):

        if len(form) != 3:
            return jsonify(Error="Malformed post request"), 400
        else:
            group_name = form['group_name']
            first_name = form['first_name']
            last_name = form['last_name']
            if group_name and first_name and last_name:
                Gdao = Group_ChatDAO()
                Adao = AdministratesDAO()
                Udao = UsersDAO()
                # it is presume user already exists
                users_info = Udao.getUserByName(first_name, last_name)
                group_info = Gdao.insert(group_name)
                administrates_info = Adao.insert(users_info[0],group_info) #insert users_id and group_id
                result = self.group_attributes(group_name,first_name,last_name)
                return jsonify(users=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def removeGroup(self, form):

        if len(form) != 3:
            return jsonify(Error="Malformed post request"), 400
        else:
            group_name = form['group_name']
            first_name = form['first_name']
            last_name = form['last_name']

            # Check if user is the admin by name


            if group_name and first_name and last_name:
                Gdao = Group_ChatDAO()
                Adao = AdministratesDAO()
                Udao = UsersDAO()

                # it is presume user already exists
                group_info = Gdao.searchByChatName(group_name) #returns chat info
                print(group_info)
                admin_info = Adao.getAdminOfGroupID(group_info[0])  # get admin of group
                print(admin_info)
                users_info = Udao.getUserById(admin_info[0]) # get admin info
                print(users_info)
                # Check if admin is the same as user
                if (users_info[1] == first_name and users_info[2] == last_name):
                    administrates_info = Adao.remove(users_info[0], group_info[0])  # remove by users_id and group_id
                    group_removed = Gdao.remove(group_name) #remove group
                    result = self.group_attributes(group_name, first_name, last_name)
                    return jsonify(users=result), 201
                else:
                    return jsonify(Error="Invalid admin"), 400
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

