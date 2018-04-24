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
