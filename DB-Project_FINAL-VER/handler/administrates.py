from flask import jsonify
from dao.administrates import AdministratesDAO
from dao.users import UsersDAO
from dao.group_chat import Group_ChatDAO

class AdminsHandler:

    def mapToDict(self, row):
        result = {}
        result['admin'] = row[0]
        result['chat'] = row[1]
        result['admin_id'] = row[2]
        return result

    def getAllAdmins(self):

        dao = AdministratesDAO()
        dao1 = UsersDAO()
        dao2 = Group_ChatDAO()
        result = dao.getAllAdmins()

        mapped_result = []
        for r in result:
            result2 = dao1.getUserById(r[0])
            result3 = dao2.getChatById(r[1])
            name_chat = ['', '', '']
            name_chat[0] = result2[1] + " " + result2[2]
            name_chat[1] = result3[1]
            name_chat[2] = result2[0]
            mapped_result.append(self.mapToDict(name_chat))
        return jsonify(Admins=mapped_result)

    def getChatsAdministratedByUser(self, users_id):
        dao = AdministratesDAO()
        dao1 = UsersDAO()
        dao2 = Group_ChatDAO()
        result = dao.getChatsAdministratedByUser(users_id)
        if result == None:
            return jsonify(Error="CHAT NOT FOUND")
        else:
            mapped_result = []
            for r in result:
                info = []
                user = dao1.getUserById(r[0])
                group = dao2.getChatById(r[1])
                info.append(user[1] + " " + user[2]) # user name
                info.append(group[1]) # group name
                info.append(users_id)
                mapped_result.append(self.mapToDict(info))
            return jsonify(Admins=mapped_result)

    def getAdminOfChatID(self, group_id):
        dao = AdministratesDAO()
        dao1 = UsersDAO()
        dao2 = Group_ChatDAO()
        result = dao.getAdminOfGroupID(group_id)
        if result == None:
            return jsonify(Error="GROUP NOT FOUND")
        else:
            mapped_result = []
            info = []
            user = dao1.getUserById(result[0])
            group = dao2.getChatById(result[1])
            info.append(user[1] + " " + user[2])  # user name
            info.append(group[1])                 # group name
            info.append(user[0])
            mapped_result.append(self.mapToDict(info))
            return jsonify(Admins=mapped_result)
