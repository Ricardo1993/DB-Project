from flask import jsonify, request
from dao.user import UserDAO

class UsersHandler:
    def getAllUsers(self):
        dao = UserDAO()
        result = dao.getAllUsers()
        mapped_result = []
        for r in result:
            mapped_result.append(self.mapToDict(r))
        return jsonify(Users=mapped_result)

    def mapToDict(self, row):
        result = {}
        result['user_id'] = row[0]
        result['first_name'] = row[1]
        result['last_name'] = row[2]
        result['phone'] = row[3]
        result['user_email'] = row[4]
        result['user_password'] = row[5]
        result['date'] = row[6]
        return result

    def getUserByID(self, id):
        dao = UserDAO()
        result = dao.getUserById(id)
        if result == None:
            return jsonify(Error="USER NOT FOUND")
        else:
            mapped = self.mapToDict(result)
            return jsonify(User=mapped)