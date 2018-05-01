from flask import jsonify
from dao.group_chat import Group_ChatDAO



class ChatsHandler:

    def getAllChats(self):
        dao = Group_ChatDAO()
        result = dao.getAllChats()
        mapped_result = []
        for r in result:
            mapped_result.append(self.mapToDict(r))
        return jsonify(Chats=mapped_result)

    def mapToDict(self, row):
        result = {}
        result['group_id'] = row[0]
        result['group_name'] = row[1]
        result['gnumber_of_users'] = row[2]
        result['gactive_users'] = row[3]
        result['group_date'] = row[4]
        return result


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