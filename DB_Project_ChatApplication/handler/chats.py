from flask import jsonify, request
from dao.chat import ChatDAO

import psycopg2

conn = psycopg2.connect("dbname=dbproject user=postgres password=orion3710")


class ChatsHandler:
    def getAllChats(self):
        # dao = ChatDAO()
        result = conn.cursor()
        result.execute("Select * from Group_Chat")
        mapped_result = []
        for r in result:
            mapped_result.append(self.mapToDict(r))
        return jsonify(Chats=mapped_result)

    # def getAllChats(self):
    #     dao = ChatDAO()
    #     result = dao.getAllChats()
    #     mapped_result = []
    #     for r in result:
    #         mapped_result.append(self.mapToDict(r))
    #     return jsonify(Chats=mapped_result)

    def mapToDict(self, row):
        result = {}
        result['group_id'] = row[0]
        result['group_name'] = row[1]
        result['gnumber_of_users'] = row[2]
        result['gactive_users'] = row[3]
        result['group_date'] = row[4]
        return result


    def getChatByID(self, id):
        result = conn.cursor()
        result.execute("Select * from Group_Chat Where group_id=" + str(id))
        mapped_result = []
        for r in result:
            mapped_result.append(self.mapToDict(r))
            return jsonify(Chat=mapped_result)
        return jsonify(Error="CHAT NOT FOUND")

    # def getChatByID(self, id):
    #     dao = ChatDAO()
    #     result = dao.getChatById(id)
    #     if result == None:
    #         return jsonify(Error="CHAT NOT FOUND")
    #     else:
    #         mapped = self.mapToDict(result)
    #         return jsonify(Chat=mapped)

    def findChat(self, name):
        dao = ChatDAO()
        result = dao.searchByChatName(name)
        if result == None:
            return jsonify(Error="CHAT NOT FOUND")
        else:
            mapped = self.mapToDict(result)
            return jsonify(Chat=mapped)