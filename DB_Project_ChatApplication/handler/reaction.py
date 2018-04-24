from flask import jsonify
from dao.reaction import ReactionDAO
from dao.message import MessageDAO
from dao.users import UsersDAO

class ReactionHandler:
    def getAllReactions(self):
        dao = ReactionDAO()
        dao1 = MessageDAO()
        dao2 = UsersDAO()

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

    def mapToDict2(self, row):
        result = {}
       # result['r_id'] = row[0]
        result['message_reactedTo'] = row[0]
        # result['user_reactor'] = row[1]
        result['num_of_likes'] = row[1]  # like/dislike
        return result

    def mapToDict3(self, row):
        result = {}
       # result['r_id'] = row[0]
        result['message_reactedTo'] = row[0]
        # result['user_reactor'] = row[1]
        result['num_of_dislikes'] = row[1]  # like/dislike
        return result


    def getReactionsByUserID(self, uid):
        dao = ReactionDAO()
        dao1 = MessageDAO()
        dao2 = UsersDAO()
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

    def getMessageLikes(self, mid):
        dao = ReactionDAO()
        dao1 = MessageDAO()
        dao2 = UsersDAO()
        result = dao.getReactionByMessageId(mid)
        if result == None:
            return jsonify(Error="REACTION NOT FOUND")
        else:
            mapped_result = []
            for r in result:
                if r[2] == 'like':
                    r[0] = dao1.getMessageById(r[0])[1]
                    r[1] = dao2.getUserById(r[1])[1] + ' ' + dao2.getUserById(r[1])[2]
                    mapped_result.append(self.mapToDict(r))
            return jsonify(Reaction=mapped_result)

    def getMessageDislikes(self, mid):
        dao = ReactionDAO()
        dao1 = MessageDAO()
        dao2 = UsersDAO()
        result = dao.getReactionByMessageId(mid)
        if result == None:
            return jsonify(Error="REACTION NOT FOUND")
        else:
            mapped_result = []
            for r in result:
                if r[2] == 'dislike':
                    r[0] = dao1.getMessageById(r[0])[1]
                    r[1] = dao2.getUserById(r[1])[1] + ' ' + dao2.getUserById(r[1])[2]
                    mapped_result.append(self.mapToDict(r))
            return jsonify(Reaction=mapped_result)



    def getMessageLikesCount(self, mid):
        dao = ReactionDAO()
        dao1 = MessageDAO()
        dao2 = UsersDAO()
        result = dao.getReactionByMessageId(mid)
        if result == None:
            return jsonify(Error="REACTION NOT FOUND")
        else:
            mapped_result = []
            count = 0
            for r in result:
                if r[2] == 'like':
                    count = count + 1

            new_result = [dao1.getMessageById(mid)[1], count]
            mapped_result.append(self.mapToDict2(new_result))


            return jsonify(Reaction=mapped_result)

    def getMessageDislikesCount(self, mid):
        dao = ReactionDAO()
        dao1 = MessageDAO()
        dao2 = UsersDAO()
        result = dao.getReactionByMessageId(mid)
        if result == None:
            return jsonify(Error="REACTION NOT FOUND")
        else:
            mapped_result = []
            count = 0
            text = ''

            for r in result:
                if r[2] == 'dislike':
                    count = count + 1

            new_result = [dao1.getMessageById(mid)[1], count]
            mapped_result.append(self.mapToDict3(new_result))

            return jsonify(Reaction=mapped_result)

    def getReactionsByMessageID(self, mid):
        dao = ReactionDAO()
        dao1 = MessageDAO()
        dao2 = UsersDAO()
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