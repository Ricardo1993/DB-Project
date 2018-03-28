from flask import jsonify, request
from dao.reply import ReplyDAO
from dao.user import UserDAO
from dao.message import MessageDAO
from dao.chat import ChatDAO

class ReplyHandler:
    def getAllReplies(self):
        dao = ReplyDAO()
        dao1 = MessageDAO()
        dao2 = MessageDAO()
        userDAO = UserDAO()
        chatDAO = ChatDAO()
        result = dao.getAllReplies()
        mapped_result = []
        for r in result:
            reply_info = []
            result1 = dao1.getMessageById(r[0])  # array de mensaje-reply
            result2 = dao2.getMessageById(r[1])  # array de mensaje original
            reply_info.append(result1[1]) #replyer_text
            reply_info.append(result2[1]) #original_text
            # buscar user con user id
            # result1[3] - replyer_id
            replyer = userDAO.getUserById(result1[3])

            reply_info.append(replyer[1] + ' ' +replyer[2])

            # buscar chat con chat id
            # result1[4] - chat_id
            chat_name = chatDAO.getChatById(result1[4])
            reply_info.append(chat_name[1])

            reply_info.append(result1[2]) #reply_date
            reply_info.append(result2[2]) #original_message_date

            mapped_result.append(self.mapToDict(reply_info))
        return jsonify(Replies=mapped_result)

    def mapToDict(self, row):
        result = {}
        result['reply'] = row[0]
        result['original_message'] = row[1]
        result['replyer_name'] = row[2]
        result['chat'] = row[3]
        result['reply_date'] = row[4]
        result['original_message_data'] = row[5]

        return result




    def findMessagesReplies(self, message_id):
        dao = ReplyDAO()
        dao1 = MessageDAO()
        dao2 = MessageDAO()
        userDAO = UserDAO()
        chatDAO = ChatDAO()
        result = dao.getAllReplies()
        mapped_result = []
        for r in result:
            if r[1] == message_id:
                reply_info = []
                result1 = dao1.getMessageById(r[0])  # array de mensaje-reply
                result2 = dao2.getMessageById(r[1])  # array de mensaje original
                reply_info.append(result1[1])  # replyer_text
                reply_info.append(result2[1])  # original_text
                # buscar user con user id
                # result1[3] - replyer_id
                replyer = userDAO.getUserById(result1[3])

                reply_info.append(replyer[1] + ' ' + replyer[2])

                # buscar chat con chat id
                # result1[4] - chat_id
                chat_name = chatDAO.getChatById(result1[4])
                reply_info.append(chat_name[1])

                reply_info.append(result1[2])  # reply_date
                reply_info.append(result2[2])  # original_message_date

                mapped_result.append(self.mapToDict(reply_info))
        return jsonify(Replies=mapped_result)