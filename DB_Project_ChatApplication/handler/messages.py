from flask import jsonify, request
from dao.message import MessageDAO
import psycopg2

conn = psycopg2.connect("dbname=dbproject user=postgres password=orion3710")

class MessageHandler:
    def getAllMessages(self):
        result = conn.cursor()
        result.execute("Select * from Message")
        mapped_result = []
        for r in result:
            mapped_result.append(self.mapToDict(r))
        return jsonify(Messages=mapped_result)

    # def getAllMessages(self):
    #     dao = MessageDAO()
    #     result = dao.getAllMessages()
    #     mapped_result = []
    #     for r in result:
    #         mapped_result.append(self.mapToDict(r))
    #     return jsonify(Messages=mapped_result)

    def mapToDict(self, row):
        result = {}
        result['message_id'] = row[0]
        result['message_text'] = row[1]
        result['message_date'] = row[2]
        # result['user_id'] = row[3] # Foreign key
        # result['group_id'] = row[4] # Foreign key

        return result

    def getMessageByID(self, id):
        result = conn.cursor()
        result.execute("Select * from Message Where message_id=" + str(id))
        mapped_result = []
        for r in result:
            mapped_result.append(self.mapToDict(r))
            return jsonify(Message=mapped_result)
        return jsonify(Error="MESSAGE NOT FOUND")

    # def getMessageByID(self, id):
    #     dao = MessageDAO()
    #     result = dao.getMessageById(id)
    #     if result == None:
    #         return jsonify(Error="MESSAGE NOT FOUND")
    #     else:
    #         mapped = self.mapToDict(result)
    #         return jsonify(Message=mapped)


    def findChatMessages(self,chat_id):
        result = conn.cursor()
        result.execute("Select message_id, message_text, message_date "
                       "from (Message NATURAL INNER JOIN Messages NATURAL INNER JOIN Group_Chat) "
                       "Where group_id=" + str(chat_id))
        mapped_result = []
        for r in result:
            mapped_result.append(self.mapToDict(r))
        if not mapped_result:
            return jsonify(Error="CHAT HAS NO MESSAGES OR DOES NOT EXIST")

        return jsonify(Messages=mapped_result)

    # def findChatMessages(self, chat_id):
    #     dao = MessageDAO()
    #     result = dao.searchByChatId(chat_id)
    #     if result == None:
    #         return jsonify(Error="CHAT NOT FOUND")
    #     else:
    #         mapped_result = []
    #         for r in result:
    #             mapped_result.append(self.mapToDict(r))
    #         return jsonify(Messages=mapped_result)


    def findUserMessages(self, user_id):
        result = conn.cursor()
        result.execute("Select message_id, message_text, message_date "
                       "from (Message NATURAL INNER JOIN Sent NATURAL INNER JOIN Users) "
                       "Where user_id=" + str(user_id))
        mapped_result = []
        for r in result:
            mapped_result.append(self.mapToDict(r))
        if not mapped_result:
            return jsonify(Error="USER HAS NO MESSAGES OR DOES NOT EXIST")

        return jsonify(Messages=mapped_result)
    # def findUserMessages(self, user_id):
    #     dao = MessageDAO()
    #     result = dao.searchByUserId(user_id)
    #     if result == None:
    #         return jsonify(Error="CHAT NOT FOUND")
    #     else:
    #         mapped_result = []
    #         for r in result:
    #             mapped_result.append(self.mapToDict(r))
    #         return jsonify(Messages=mapped_result)


    def findChatMessagesByUser(self, chat_id, user_id):
        result = conn.cursor()
        result.execute("Select message_id, message_text, message_date "
                       "from (Message NATURAL INNER JOIN Sent NATURAL INNER JOIN Users NATURAL INNER JOIN Group_Chat NATURAL INNER JOIN Member_of) "
                       "Where user_id=" + str(user_id) + " AND group_id=" + str(chat_id))
        mapped_result = []
        for r in result:
            mapped_result.append(self.mapToDict(r))
        if not mapped_result:
            return jsonify(Error="USER HAS NO MESSAGES IN THIS CHAT OR EITHER CHAT OR USER DOES NOT EXIST")


    # def findChatMessagesByUser(self, chat_id, user_id):
    #
    #     dao = MessageDAO()
    #     chat_result = dao.searchByChatId(chat_id)
    #     mapped_result_chat = []
    #     # if result == None:
    #     #     return jsonify(Error="CHAT NOT FOUND")
    #     # else:
    #     #     for r in result:
    #     #         mapped_result_chat.append(self.mapToDict(r))
    #
    #
    #     user_result = dao.searchByUserId(user_id)
    #     mapped_result_user = []
    #     # if result == None:
    #     #     return jsonify(Error="USER NOT FOUND")
    #     # else:
    #     #     for r in result:
    #     #         mapped_result_user.append(self.mapToDict(r))
    #
    #     mapped_result = []
    #     for r in chat_result:
    #         print(r)
    #         for r_user in user_result:
    #             print(r_user)
    #             if r[3] == r_user[3]:
    #                 # mapped_result.append(self.mapToDict(r))
    #                 mapped_result.append(self.mapToDict(r_user))
    #
    #     return jsonify(Messages=mapped_result)
