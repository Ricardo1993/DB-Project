from flask import jsonify, request
from dao.admin import AdminDAO
from dao.user import UserDAO
from dao.chat import ChatDAO

class AdminsHandler:
    def getAllAdmins(self):
        dao = AdminDAO()
        dao1 = UserDAO()
        dao2 = ChatDAO()
        result = dao.getAllAdmins()

        mapped_result = []
        for r in result:
            result2 = dao1.getUserById(r[0])
            result3 = dao2.getChatById(r[1])
            r[0] = result2[1] + " " + result2[2]
            r[1] = result3[1]
            mapped_result.append(self.mapToDict(r))
        return jsonify(Admins=mapped_result)


    def mapToDict(self, row):
        result = {}
        result['admin'] = row[0]
        result['chat'] = row[1]
        return result


    def getChatsAdministratedByUser(self, user_id):
        dao = AdminDAO()
        dao1 = UserDAO()
        dao2 = ChatDAO()
        result = dao.getChatsAdministratedByUser(user_id)
        if result == None:
            return jsonify(Error="CHAT NOT FOUND")
        else:
            mapped_result = []
            for r in result:
                result2 = dao1.getUserById(r[0])
                result3 = dao2.getChatById(r[1])
                r[0] = result2[1] + " " + result2[2]
                r[1] = result3[1]
                mapped_result.append(self.mapToDict(r))
            return jsonify(Admins=mapped_result)


    def getAdminByChatID(self, chat_id):
        dao = AdminDAO()
        dao1 = UserDAO()
        dao2 = ChatDAO()
        result = dao.getAdminsByChatID(chat_id)
        # print(result)
        if result == None:
            return jsonify(Error="ADMIN NOT FOUND")
        else:
            mapped_result = []
            for r in result:
                result2 = dao1.getUserById(r[0])
                result3 = dao2.getChatById(r[1])
                r[0] = result2[1] + " " + result2[2]
                r[1] = result3[1]
                mapped_result.append(self.mapToDict(r))
            return jsonify(Admins=mapped_result)

