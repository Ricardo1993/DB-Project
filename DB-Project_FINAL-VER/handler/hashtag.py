from flask import jsonify, request
from dao.message import MessageDAO
from dao.hashtag import HashtagDAO
from dao.has import HasTagDAO

class HashtagsHandler:

    def mapToDict1(self, row):
        result = {}
        result['message'] = row[0]
        result['hashtag'] = row[1]

        return result

    def mapToDict2(self, row):
        result = {}
        result['hashtag'] = row[1]
        result['date_created'] = row[3]

        return result

    def mapToDict3(self, row):
        result = {}
        result['date_created'] = row[0]
        result['hashtag'] = row[1]
        result['count'] = row[2]

        return result

    def getAllHashtags(self):
        hashtagDAO = HashtagDAO()
        result = hashtagDAO.getAllHashtags()
        mapped = []
        for r in result:
            # hashtag_info = []
            # hashtag_info.append(r[1]) # hashtag text
            # hashtag_info.append(r[3]) # hashtag date
            mapped.append(self.mapToDict2(r))
        return jsonify(Hashtags=mapped)

    def getTrends(self):
        hashtagDAO = HashtagDAO()
        result = hashtagDAO.getTrends()
        mapped = []
        for r in result:
            hashtag_info = []
            hashtag_info.append(r[0]) # hashtag date
            hashtag_info.append(r[1]) # hashtag text
            hashtag_info.append(r[2]) # hashtag count
            mapped.append(self.mapToDict3(r))
        return jsonify(Hashtags=mapped)


    def getHashtagsFromMessage(self, message_id):

        hashtagDAO = HashtagDAO()
        hasTagDAO = HasTagDAO()
        messageDAO = MessageDAO()


        result = hasTagDAO.getHashtagsInMessage(message_id)

        if result == None:
            return jsonify(Error="MESSAGE NOT FOUND")
        else:
            mapped = []
            for r in result:
                results_info = []
                message_text = messageDAO.getMessageById(message_id)
                results_info.append(message_text[1]) # append message text
                hashtag_text = hashtagDAO.getHashtagById(r[1])
                results_info.append(hashtag_text[0][1]) # append hashtag text
                mapped.append(self.mapToDict1(results_info))
            return jsonify(Hashtags=mapped)

    def getMessagesWithHashtag(self, hashtag_id):

        hashtagDAO = HashtagDAO()
        hasTagDAO = HasTagDAO()
        messageDAO = MessageDAO()

        result = hasTagDAO.getMessagesWithHashtagID(hashtag_id)

        mapped = []
        if result == None:
            return jsonify(Error="HASHTAG NOT FOUND")
        else:
            for r in result:

                results_info = []
                message_text = messageDAO.getMessageById(r[0])
                results_info.append(message_text[1])  # append message text
                hashtag_text = hashtagDAO.getHashtagById(r[1])
                results_info.append(hashtag_text[1])  # append hashtag text

                mapped.append(self.mapToDict1(results_info))
            return jsonify(Messages=mapped)

    def getMessagesWithHashtagText(self, hashtag_text):

        hashtagDAO = HashtagDAO()
        hasTagDAO = HasTagDAO()
        messageDAO = MessageDAO()

        hashtag_list = hashtagDAO.getHashtagByText(hashtag_text)
        if hashtag_list == None:
            return jsonify(Error="HASHTAG NOT FOUND")

        messages_with_tag = []
        for i in hashtag_list:
            message = hasTagDAO.getMessagesWithHashtagID(i[0])
            messages_with_tag.append(message)
        print(messages_with_tag)

        mapped = []
        for r in messages_with_tag:
            results_info = []
            results_info.append(r[0])  # append message text
            results_info.append(hashtag_text)  # append hashtag text

            mapped.append(self.mapToDict1(results_info))
        return jsonify(Messages=mapped)

        return None#jsonify(Messages=mapped)

    def getMessagesWithHashtagTextAndGroup(self, hashtag_text, group_id):

        hashtagDAO = HashtagDAO()
        hasTagDAO = HasTagDAO()
        messageDAO = MessageDAO()

        hashtag_list = hashtagDAO.getHashtagByTextAndGroup(hashtag_text,group_id)
        print(hashtag_list)
        if hashtag_list == None:
            return jsonify(Error="HASHTAG NOT FOUND")

        messages_with_tag = []
        for i in hashtag_list:
            message = hasTagDAO.getMessagesWithHashtagID(i[0])
            messages_with_tag.append(message)
        print(messages_with_tag)

        mapped = []
        for r in messages_with_tag:
            results_info = []
            results_info.append(r[0])  # append message text
            results_info.append(hashtag_text)  # append hashtag text

            mapped.append(self.mapToDict1(results_info))
        return jsonify(Messages=mapped)

        return None#jsonify(Messages=mapped)



    def getHashtagByID(self, hashtag_id):

        hashtagDAO = HashtagDAO()
        result = hashtagDAO.getHashtagById(hashtag_id)
        mapped = []
        for r in result:
            # print(r)
            # hashtag_info = []
            # hashtag_info.append(r[1])  # hashtag text
            # hashtag_info.append(r[3])  # hashtag date
            # print(hashtag_info[1])
            mapped.append(self.mapToDict2(r))
        return jsonify(Hashtags=mapped)

    def getHashtagByText(self, hashtag_text):

        hashtagDAO = HashtagDAO()
        result = hashtagDAO.getHashtagByText(hashtag_text)
        mapped = []
        for r in result:

            mapped.append(self.mapToDict2(r))
        return jsonify(Hashtags=mapped)



