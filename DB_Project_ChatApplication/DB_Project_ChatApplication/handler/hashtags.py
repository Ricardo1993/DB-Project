from flask import jsonify, request
from dao.message import MessageDAO
from dao.hashtag import HashtagDAO
from dao.hasTag import HasTagDAO

class HashtagsHandler:

    def getAllHashtags(self):
        hashtagDAO = HashtagDAO()
        result = hashtagDAO.getAllHashtags()

        mapped = []
        for r in result:
            mapped.append(self.mapToDict2(r))
        return jsonify(Hashtags=mapped)

    def getHashtagsFromMessage(self, message_id):
        hashtagDAO = HashtagDAO()
        hasTagDAO = HasTagDAO()
        messageDAO = MessageDAO()

        result = hasTagDAO.getHashtagsInMessage(message_id)
        message = messageDAO.getMessageById(message_id)
        mapped = []
        if result == None:
            return jsonify(Error="HASHTAG NOT FOUND")
        else:
            for r in result:
                r[0] = message[1]
                r[1] = hashtagDAO.getHashtagById(r[1])[0]
                mapped.append(self.mapToDict(r))
            return jsonify(Hashtags=mapped)

    def getMessagesWithHashtag(self, hashtag_id):
        hashtagDAO = HashtagDAO()
        hasTagDAO = HasTagDAO()
        messageDAO = MessageDAO()

        result = hasTagDAO.getMessagesWithHashtag(hashtag_id)
        hashtag = hashtagDAO.getHashtagById(hashtag_id)
        mapped = []
        if result == None:
            return jsonify(Error="MESSAGE NOT FOUND")
        else:
            for r in result:
                r[0] = messageDAO.getMessageById(r[0])[1]
                r[1] = hashtag[0]
                mapped.append(self.mapToDict(r))
            return jsonify(Messages=mapped)


    def mapToDict(self, row):
        result = {}
        result['message'] = row[0]
        result['hashtag'] = row[1]

        return result
    def mapToDict2(self, row):
        result = {}
        result['hashtag'] = row[1]
        result['date_created'] = row[2]

        return result