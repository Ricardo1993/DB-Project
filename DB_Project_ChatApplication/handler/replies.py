from flask import jsonify, request
from dao.reply import ReplyDAO

class ReplyHandler:
    def getAllReplies(self):
        dao = ReplyDAO()
        result = dao.getAllReplies()
        mapped_result = []
        for r in result:
            mapped_result.append(self.mapToDict(r))
        return jsonify(Replies=mapped_result)

    def mapToDict(self, row):
        result = {}
        result['reply_id'] = row[0]
        result['owner_id'] = row[1]
        result['message_id'] = row[2]
        result['text_field'] = row[3]
        result['reply_date'] = row[4]
        return result

    def getReplyByID(self, id):
        dao = ReplyDAO()
        result = dao.getReplyById(id)
        if result == None:
            return jsonify(Error="REPLY NOT FOUND")
        else:
            mapped = self.mapToDict(result)
            return jsonify(Reply=mapped)

    def findMessagesReplies(self, message_id):
        dao = ReplyDAO()
        result = dao.findReplyByMessageId(message_id)
        if result == None:
            return jsonify(Error="MESSAGE NOT FOUND")
        else:
            mapped_result = []
            for r in result:
                mapped_result.append(self.mapToDict(r))
            return jsonify(Replies=mapped_result)

    def findByOwnerID(self, user_id):
        dao = ReplyDAO()
        result = dao.searchByOwnerId(user_id)
        if result == None:
            return jsonify(Error="OWNER NOT FOUND")
        else:
            mapped_result = []
            for r in result:
                mapped_result.append(self.mapToDict(r))
            return jsonify(Replies=mapped_result)
