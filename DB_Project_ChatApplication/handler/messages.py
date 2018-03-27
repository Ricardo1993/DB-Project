from flask import jsonify, request
from dao.message import MessageDAO

class MessageHandler:
    def getAllMessages(self):
        dao = MessageDAO()
        result = dao.getAllMessages()
        mapped_result = []
        for r in result:
            mapped_result.append(self.mapToDict(r))
        return jsonify(Messages=mapped_result)

    def mapToDict(self, row):
        result = {}
        result['message_id'] = row[0]
        result['text_field'] = row[1]
        #result['number_of_likes'] = row[2]
        #result['number_of_dislikes'] = row[3]
        #result['number_of_replies'] = row[4]
        result['message_date'] = row[2]
        result['user_id'] = row[3] # Foreign key
        result['group_id'] = row[4] # Foreign key

        return result

    def getMessageByID(self, id):
        dao = MessageDAO()
        result = dao.getMessageById(id)
        if result == None:
            return jsonify(Error="MESSAGE NOT FOUND")
        else:
            mapped = self.mapToDict(result)
            return jsonify(Message=mapped)

    def findChatMessages(self, chat_id):
        dao = MessageDAO()
        result = dao.searchByChatId(chat_id)
        if result == None:
            return jsonify(Error="CHAT NOT FOUND")
        else:
            mapped_result = []
            for r in result:
                mapped_result.append(self.mapToDict(r))
            return jsonify(Messages=mapped_result)