from flask import jsonify, request
from dao.reaction import ReactionDAO
from dao.message import MessageDAO
from dao.user import UserDAO

class ReactionsHandler:
    def getAllReactions(self):
        dao = ReactionDAO()
        dao1 = MessageDAO()
        dao2 = UserDAO()

        result = dao.getAllReactions()
        mapped_result = []
        for r in result:
            r[0] = dao1.getMessageById(r[0])[1]
            r[1] = dao2.getUserById(r[1])[1] + ' ' + dao2.getUserById(r[1])[2]
            mapped_result.append(self.mapToDict(r))
        return jsonify(Reactions=mapped_result)

    def mapToDict(self, row):
        result = {}
       # result['r_id'] = row[0]
        result['message_reactedTo'] = row[0]
        result['user_reactor'] = row[1]
        result['reaction'] = row[2]  # like/dislike
        return result

    def getReactionsByUserID(self, uid):
        dao = ReactionDAO()
        dao1 = MessageDAO()
        dao2 = UserDAO()
        result = dao.getReactionByUserId(uid)
        if result == None:
            return jsonify(Error="REACTION NOT FOUND")
        else:
            mapped_result = []
            for r in result:
                r[0] = dao1.getMessageById(r[0])[1]
                r[1] = dao2.getUserById(r[1])[1] + ' ' + dao2.getUserById(r[1])[2]
                mapped_result.append(self.mapToDict(r))
            return jsonify(Reaction=mapped_result)

    def getReactionsByMessageID(self, mid):
        dao = ReactionDAO()
        dao1 = MessageDAO()
        dao2 = UserDAO()
        result = dao.getReactionByMessageId(mid)
        if result == None:
            return jsonify(Error="REACTION NOT FOUND")
        else:
            mapped_result = []
            for r in result:
                r[0] = dao1.getMessageById(r[0])[1]
                r[1] = dao2.getUserById(r[1])[1] + ' ' + dao2.getUserById(r[1])[2]
                mapped_result.append(self.mapToDict(r))
            return jsonify(Reaction=mapped_result)
