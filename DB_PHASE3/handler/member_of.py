from flask import jsonify, request
from dao.member_of import MemberDAO
from dao.users import UsersDAO
from dao.group_chat import Group_ChatDAO
from dao.contacts import *
from dao.administrates import *

class MembershipHandler:

    def mapToDict(self, row):
        result = {}
        result['user'] = row[0]
        result['chat'] = row[1]
        return result

    def getAllMemberships(self):
        dao = MemberDAO()
        dao1 = UsersDAO()
        dao2 = Group_ChatDAO()
        result = dao.getAllMemberships()

        mapped_result = []
        for r in result:
            membership = []
            user = dao1.getUserById(r[0])
            group = dao2.getChatById(r[1])
            membership.append(user[1] + " " + user[2])
            membership.append(group[1])
            mapped_result.append(self.mapToDict(membership))
        return jsonify(Members=mapped_result)


    def getMembershipByUID(self, users_id):
        dao = MemberDAO()
        dao1 = UsersDAO()
        dao2 = Group_ChatDAO()
        result = dao.getMembershipsByUserID(users_id)

        if result == None:
            return jsonify(Error="MEMBERSHIP NOT FOUND")
        else:
            mapped_result = []
            for r in result:
                membership = []
                user = dao1.getUserById(r[0])
                group = dao2.getChatById(r[1])
                membership.append(user[1] + " " + user[2])
                membership.append(group[1])
                mapped_result.append(self.mapToDict(membership))
            return jsonify(Members=mapped_result)


    def getMembershipByChatID(self, group_id):
        dao = MemberDAO()
        dao1 = UsersDAO()
        dao2 = Group_ChatDAO()
        result = dao.getMembershipsOfGroupID(group_id)
        # print(result)
        if result == None:
            return jsonify(Error="MEMBERSHIP NOT FOUND")
        else:
            mapped_result = []
            for r in result:
                membership = []
                user = dao1.getUserById(r[0])
                group = dao2.getChatById(r[1])
                membership.append(user[1] + " " + user[2])
                membership.append(group[1])
                mapped_result.append(self.mapToDict(membership))
            return jsonify(Members=mapped_result)

    def member_attributes(self, first_name, last_name, group_name):
        result = {}
        result['first_name'] = first_name
        result['last_name'] = last_name
        result['group_name'] = group_name
        return result

    def addMember(self, form, users_id):

        if len(form) != 3:
            return jsonify(Error="Malformed post request"), 400
        else:
            first_name = form['first_name']
            last_name = form['last_name']
            group_name = form['group_name']
            if first_name and last_name and group_name:

                Mdao = MemberDAO()
                Udao = UsersDAO()
                Gdao = Group_ChatDAO()
                Adao = AdministratesDAO()

                group_info = Gdao.searchByChatName(group_name) #get group info
                print(group_info)
                member_info = Udao.getUserByName(first_name,last_name) #get member info to wisj is desired to add
                print(member_info)
                check = Mdao.getMembershipsByUserAndGroup(member_info[0],group_info[0]) #check if user already in group
                print(check)
                admin_of_group = Adao.getAdminOfGroupID(group_info[0]) #get admin id
                admin_info = Udao.getUserById(admin_of_group[0]) #get admin info
                print(users_id)
                print(admin_of_group)
                # check if user is not in group and the user trying to add is admin
                if (not check) and (users_id == admin_of_group[0]):
                    Mdao.insert(member_info[0],group_info[0]) #add user to group
                    result = self.member_attributes(first_name,last_name,group_name)
                    return jsonify(users=result), 201
                else:
                    return jsonify(Error="Invalid admin or user already in group"), 400
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def removeMember(self, form, users_id):

        if len(form) != 3:
            return jsonify(Error="Malformed post request"), 400
        else:
            first_name = form['first_name']
            last_name = form['last_name']
            group_name = form['group_name']
            if first_name and last_name and group_name:

                Mdao = MemberDAO()
                Udao = UsersDAO()
                Gdao = Group_ChatDAO()
                Adao = AdministratesDAO()

                group_info = Gdao.searchByChatName(group_name)  # get group info
                print(group_info)
                member_info = Udao.getUserByName(first_name, last_name)  # get member info to wish is desired to remove
                print(member_info)
                check = Mdao.getMembershipsByUserAndGroup(member_info[0], group_info[0])  # check if user already in group
                print(check)
                admin_of_group = Adao.getAdminOfGroupID(group_info[0])  # get admin id
                admin_info = Udao.getUserById(admin_of_group[0])  # get admin info
                print(users_id)
                print(admin_of_group)
                # check if user is in group and the user trying to add is admin
                if check and (users_id == admin_of_group[0]):
                    Mdao.remove(member_info[0], group_info[0])  # add user to group
                    result = self.member_attributes(first_name, last_name, group_name)
                    return jsonify(users=result), 201
                else:
                    return jsonify(Error="Invalid admin or user already in group"), 400
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def checkMember(self, users_id, group_id):

        dao = MemberDAO()
        dao1 = UsersDAO()
        dao2 = Group_ChatDAO()
        result = dao.getMembershipsByUserAndGroup(users_id,group_id)

        if result == None:
            return None
        else:
            mapped_result = []
            for r in result:
                membership = []
                user = dao1.getUserById(r[0])
                group = dao2.getChatById(r[1])
                membership.append(user[1] + " " + user[2])
                membership.append(group[1])
                mapped_result.append(self.mapToDict(membership))
            return jsonify(Members=mapped_result)


