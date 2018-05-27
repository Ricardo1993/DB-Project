from flask import jsonify, request
from dao.reply import ReplyDAO
from dao.users import UsersDAO
from dao.message import MessageDAO
from dao.sent import SentDAO
from dao.messages import MessagesDAO
from dao.group_chat import Group_ChatDAO
from dao.hashtag import *
from dao.has import *

class ReplyHandler:

    def mapToDict(self, row):
        result = {}
        result['reply'] = row[0]
        result['original_message'] = row[1]
        result['replyer_name'] = row[2]
        result['chat'] = row[3]
        result['reply_date'] = row[4]
        result['original_message_data'] = row[5]

        return result

    def getAllReplies(self):

        replyDAO = ReplyDAO()
        dao1 = MessageDAO()
        dao2 = MessageDAO()
        sentDAO = SentDAO()
        messagesDAO = MessagesDAO()

        result = replyDAO.getAllReplies() # get all messages that are replies
        mapped_result = [] #store all replies mapped

        for r in result:

            reply_info = []

            owner_message = dao1.getMessageById(r[0])  # original message info
            reply_message = dao2.getMessageById(r[1])  # reply message info

            reply_info.append(reply_message[1]) # append reply text
            reply_info.append(owner_message[1]) # append original message

            replyer_name = sentDAO.getUserByMessageId(reply_message[0]) # get replyer name
            reply_info.append(replyer_name[1] + ' ' + replyer_name[2]) # append name

            chat_name = messagesDAO.getChatByMessageId(r[0]) # what group was the reply sent
            reply_info.append(chat_name[1]) # append group chat name

            reply_info.append(reply_message[2]) # append reply_date
            reply_info.append(owner_message[2]) # append original_message_date

            mapped_result.append(self.mapToDict(reply_info))
        return jsonify(Replies=mapped_result)

    def findMessageReplies(self, message_id):
        replyDAO = ReplyDAO()
        dao1 = MessageDAO()
        dao2 = MessageDAO()
        sentDAO = SentDAO()
        messagesDAO = MessagesDAO()

        result = replyDAO.getReplysForMessageId(message_id) # get all replies to a message
        mapped_result = []

        for r in result:

                reply_info = []

                owner_message = dao1.getMessageById(r[0])  # original message info
                reply_message = dao2.getMessageById(r[1])  # reply message info

                reply_info.append(reply_message[1])  # append reply text
                reply_info.append(owner_message[1])  # append original message

                replyer_name = sentDAO.getUserByMessageId(reply_message[0])  # get replyer name
                reply_info.append(replyer_name[1] + ' ' + replyer_name[2])  # append name

                chat_name = messagesDAO.getChatByMessageId(r[0])  # what group was the reply sent
                reply_info.append(chat_name[1])  # append group chat name

                reply_info.append(reply_message[2])  # append reply_date
                reply_info.append(owner_message[2])  # append original_message_date

                mapped_result.append(self.mapToDict(reply_info))

        return jsonify(Replies=mapped_result)

    def reply_attributes(self, message_text):
        result = {}
        result['message_text'] = message_text

        return result

    def reply(self, form, message_id , users_id, group_id):

        if len(form) != 1:
            return jsonify(Error="Malformed post request"), 400
        else:
            message_text = form['message_text']

            print(message_text)

            if message_text:

                dao = MessageDAO()
                sDao = SentDAO()
                mDao = MessagesDAO()
                hasDao = HasTagDAO()
                hashtagDao = HashtagDAO()
                rDAO = ReplyDAO()

                og_message_text = dao.getMessageById(message_id)
                new_message = " 'RE:" + og_message_text[1] + "' " + message_text
                original_message = new_message
                print(new_message)

                reply_id = dao.insert(new_message)  # insert message to table, returns message id
                print(users_id)
                print(message_id)
                sent = sDao.insert(users_id,reply_id)  # link to user who sent message
                messages = mDao.insert(reply_id, group_id)  # link to which group the message was posted to
                reply = rDAO.insert(message_id,reply_id)

                # get message hashtags
                message_text.strip("#")
                for message_text in message_text.split():
                    if message_text.startswith("#"):
                        print(message_text)
                        hashtag_id = hashtagDao.insert(message_text)  # returns hashtag_id insert to hashtag table
                        hasDao.insert(reply_id, hashtag_id)

                result = self.reply_attributes(original_message)
                return jsonify(users=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400