from flask import jsonify
from dao.users import UsersDAO

class UsersHandler:

    def users_dict(self, row):
        result = {}
        result['user_id'] = row[0]
        result['first_name'] = row[1]
        result['last_name'] = row[2]
        result['phone'] = row[3]
        result['user_email'] = row[4]
        result['user_password'] = row[5]
        result['date'] = row[6]
        return result

    def users_dict2(self, row):
        result = {}
        result['day'] = row[0]
        result['active_users'] = row[1]
        return result

    def getActiveUsers(self):
         dao = UsersDAO()
         result = dao.getActiveUsers()
         mapped_result = []
         for r in result:
             mapped_result.append(self.users_dict2(r))
         return jsonify(Users=mapped_result)


    def getAllUsers(self):
         dao = UsersDAO()
         result = dao.getAllUsers()
         mapped_result = []
         for r in result:
             mapped_result.append(self.users_dict(r))
         return jsonify(Users=mapped_result)

    def getUserByID(self, id):
         dao = UsersDAO()
         result = dao.getUserById(id)
         if result == None:
             return jsonify(Error="USER NOT FOUND")
         else:
             mapped_results = self.users_dict(result)
             return jsonify(User=mapped_results)

    def getUserByName(self, first_name,last_name):
        dao = UsersDAO()
        result = dao.getUserByName(first_name,last_name)
        if result == None:
            return jsonify(Error="USER NOT FOUND")
        else:
            mapped_results = self.users_dict(result)
            return jsonify(User=mapped_results)

    def users_attributes(self, first_name, last_name,users_phone, users_email, users_password):
        result = {}
        result['first_name'] = first_name
        result['last_name'] = last_name
        result['users_phone'] = users_phone
        result['users_email'] = users_email
        result['users_password'] = users_password

        return result

    def checkUser(self, form):

        if len(form) != 5:
            return jsonify(Error="Malformed post request"), 400
        else:
            first_name = form['first_name']
            last_name = form['last_name']
            users_phone = form['users_phone']
            users_email = form['users_email']
            users_password = form['users_password']
            if first_name and last_name and users_phone and users_email and users_password:
                dao = UsersDAO()
                check = dao.check(first_name, last_name, users_phone, users_email)
                if(check is None):
                    return None
                else:
                    result = self.users_attributes(first_name, last_name, users_phone, users_email, users_password)
                    return jsonify(users=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400


    def registerUser(self, form):

        if len(form) != 5:
            return jsonify(Error="Malformed post request"), 400
        else:
            first_name = form['first_name']
            last_name = form['last_name']
            users_phone = form['users_phone']
            users_email = form['users_email']
            users_password = form['users_password']
            if first_name and last_name and users_phone and users_email and users_password:
                dao = UsersDAO()
                holder = dao.insert(first_name, last_name,users_phone, users_email, users_password)
                result = self.users_attributes(first_name, last_name,users_phone, users_email, users_password)
                return jsonify(users=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

