from flask import jsonify
from dao.reaction import ReactionDAO
from dao.message import MessageDAO
from dao.users import UsersDAO

class ReactionHandler:

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

    def mapToDict4(self, row):
        result = {}
        result['day'] = row[0]
        result['reactions'] = row[1]  # like/dislike
        return result

    def getLikesPerDay(self):
        dao = ReactionDAO()
        result = dao.getLikesPerDay()
        mapped_result = []
        for r in result:
            mapped_info = []
            day = r[0]
            likes = r[1]
            mapped_info.append(day)
            mapped_info.append(likes)
            mapped_result.append(self.mapToDict4(mapped_info))
        return jsonify(Reactions=mapped_result)
    def getDislikesPerDay(self):
        dao = ReactionDAO()
        result = dao.getDislikesPerDay()
        mapped_result = []
        for r in result:
            mapped_info = []
            day = r[0]
            dislikes = r[1]
            mapped_info.append(day)
            mapped_info.append(dislikes)
            mapped_result.append(self.mapToDict4(mapped_info))
        return jsonify(Reactions=mapped_result)

    def getAllReactions(self):
        dao = ReactionDAO()
        dao1 = MessageDAO()
        dao2 = UsersDAO()

        result = dao.getAllReactions()
        mapped_result = []
        for r in result:
            mapped_info = []
            user = dao2.getUserById(r[0])
            message = dao1.getMessageById(r[1])
            mapped_info.append(message[1]) # message text in which it reacted
            mapped_info.append(user[1] + ' ' + user[2])
            mapped_info.append(r[2])
            mapped_result.append(self.mapToDict(mapped_info))
        return jsonify(Reactions=mapped_result)


    def getReactionsByUserID(self, users_id):
        dao = ReactionDAO()
        dao1 = MessageDAO()
        dao2 = UsersDAO()
        result = dao.getReactionsByUserId(users_id)
        if result == None:
            return jsonify(Error="REACTION NOT FOUND")
        else:
            mapped_result = []
            for r in result:
                mapped_info = []
                user = dao2.getUserById(r[0])
                message = dao1.getMessageById(r[1])
                mapped_info.append(message[1])  # message text in which it reacted
                mapped_info.append(user[1] + ' ' + user[2])
                mapped_info.append(r[2])
                mapped_result.append(self.mapToDict(mapped_info))
            return jsonify(Reactions=mapped_result)

    def getReactionsByMessageID(self, message_id):
        dao = ReactionDAO()
        dao1 = MessageDAO()
        dao2 = UsersDAO()
        result = dao.getReactionsToMessageId(message_id)
        if result == None:
            return jsonify(Error="REACTION NOT FOUND")
        else:
            mapped_result = []
            for r in result:
                mapped_info = []
                user = dao2.getUserById(r[0])
                message = dao1.getMessageById(r[1])
                mapped_info.append(message[1])  # message text in which it reacted
                mapped_info.append(user[1] + ' ' + user[2])
                mapped_info.append(r[2])
                mapped_result.append(self.mapToDict(mapped_info))
            return jsonify(Reactions=mapped_result)

    def getMessageLikes(self, message_id):
        dao = ReactionDAO()
        dao1 = MessageDAO()
        dao2 = UsersDAO()
        result = dao.getLikesToMessageId(message_id)
        if result == None:
            return jsonify(Error="REACTION NOT FOUND")
        else:
            mapped_result = []
            for r in result:
                mapped_info = []
                user = dao2.getUserById(r[0])
                message = dao1.getMessageById(r[1])
                mapped_info.append(message[1])  # message text in which it reacted
                mapped_info.append(user[1] + ' ' + user[2])
                mapped_info.append(r[2])
                mapped_result.append(self.mapToDict(mapped_info))
            return jsonify(Reactions=mapped_result)

    def getMessageDislikes(self, message_id):
        dao = ReactionDAO()
        dao1 = MessageDAO()
        dao2 = UsersDAO()
        result = dao.getDislikesToMessageId(message_id)
        if result == None:
            return jsonify(Error="REACTION NOT FOUND")
        else:
            mapped_result = []
            for r in result:
                mapped_info = []
                user = dao2.getUserById(r[0])
                message = dao1.getMessageById(r[1])
                mapped_info.append(message[1])  # message text in which it reacted
                mapped_info.append(user[1] + ' ' + user[2])
                mapped_info.append(r[2])
                mapped_result.append(self.mapToDict(mapped_info))
            return jsonify(Reactions=mapped_result)



    def getMessageLikesCount(self, message_id):
        dao = ReactionDAO()
        dao1 = MessageDAO()
        dao2 = UsersDAO()
        result = dao.getLikesCountToMessageId(message_id) # returns count
        if result == None:
            return jsonify(Error="REACTION NOT FOUND")
        else:
            mapped_result = []
            for r in result:
                mapped_info = []
                message = dao1.getMessageById(message_id)
                mapped_info.append(message[1])  # message text in which it reacted
                mapped_info.append(r[0]) #count
                mapped_result.append(self.mapToDict2(mapped_info))
            return jsonify(Reaction=mapped_result)

    def getMessageDislikesCount(self, message_id):
        dao = ReactionDAO()
        dao1 = MessageDAO()
        dao2 = UsersDAO()
        result = dao.getDislikesCountToMessageId(message_id) # returns count
        if result == None:
            return jsonify(Error="REACTION NOT FOUND")
        else:
            mapped_result = []
            for r in result:
                mapped_info = []
                message = dao1.getMessageById(message_id)
                mapped_info.append(message[1])  # message text in which it reacted
                mapped_info.append(r[0]) # count
                mapped_result.append(self.mapToDict3(mapped_info))
            return jsonify(Reaction=mapped_result)

    def reaction_attributes(self, reaction):
        result = {}
        result['reaction'] = reaction
        return result

    def react(self, form, users_id, message_id):

        if len(form) != 1:
            return jsonify(Error="Malformed post request"), 400
        else:
            reaction = form['reaction']
            if reaction:
                dao = ReactionDAO()
                holder = dao.insert(users_id,message_id,reaction)
                result = self.reaction_attributes(reaction)
                return jsonify(users=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400