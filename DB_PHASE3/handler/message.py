from flask import jsonify, request
from dao.message import MessageDAO
from dao.member_of import *
from dao.sent import *
from dao.messages import *
from dao.has import *
from dao.hashtag import *
import re

class MessageHandler:

     def getAllMessages(self):
         dao = MessageDAO()
         result = dao.getAllMessages()
         mapped_result = []
         for r in result:
             mapped_result.append(self.mapToDict2(r))
         return jsonify(Messages=mapped_result)

     def mapToDict(self, row):
        result = {}
        result['message_id'] = row[0]
        result['message_text'] = row[1]
        result['message_date'] = row[2]
        return result

     def mapToDict2(self, row):
        result = {}
        result['message_id'] = row[0]
        result['message_text'] = row[1]
        result['message_date'] = row[2]
        result['user_first_name'] = row[3]
        result['user_last_name'] = row[4]
        result['likes'] = row[5]
        result['dislikes'] = row[6]
        # result['user_id'] = row[3] # Foreign key
        # result['group_id'] = row[4] # Foreign key
        return result


     def getMessageByID(self, id):
         dao = MessageDAO()
         result = dao.getMessageById(id)
         if result == None:
             return jsonify(Error="MESSAGE NOT FOUND")
         else:
             mapped = self.mapToDict(result)
             return jsonify(Message=mapped)


     def findGroupMessages(self, group_id):
         dao = MessageDAO()
         result = dao.searchMessagesByGroupId(group_id)
         if result == None:
             return jsonify(Error="CHAT NOT FOUND")
         else:
             mapped_result = []
             for r in result:
                 mapped_result.append(self.mapToDict(r))
             return jsonify(Messages=mapped_result)


     def findUserMessages(self, user_id):
         dao = MessageDAO()
         result = dao.searchByUserId(user_id)
         if result == None:
             return jsonify(Error="CHAT NOT FOUND")
         else:
             mapped_result = []
             for r in result:
                 mapped_result.append(self.mapToDict(r))
             return jsonify(Messages=mapped_result)




     def findGroupMessagesByUser(self, group_id, user_id):

        dao = MessageDAO()
        results = dao.searchByUser_And_GroupID(group_id,user_id)


        if results == None:
            return jsonify(Error="NO DATA FOUND")
        else:

         mapped_result = []
         for r in results:
             mapped_result.append(self.mapToDict(r))

         return jsonify(Messages=mapped_result)

     def message_attributes(self, message_text):
         result = {}
         result['message_text'] = message_text

         return result

     def sendMessage(self, form, users_id, group_id):

         if len(form) != 1:
             return jsonify(Error="Malformed post request"), 400
         else:
             message_text = form['message_text']
             original_message = message_text
             print(message_text)


             if message_text:

                 dao = MessageDAO()
                 mDao = MemberDAO()
                 sDao = SentDAO()
                 mDao = MessagesDAO()
                 hasDao = HasTagDAO()
                 hashtagDao = HashtagDAO()

                 message_id = dao.insert(message_text) # insert message to table, returns message id
                 sent = sDao.insert(users_id,message_id) # link to user who sent message
                 messages = mDao.insert(message_id,group_id) #link to which group the message was posted to

                 # get message hashtags
                 message_text.strip("#")
                 for message_text in message_text.split():
                     if message_text.startswith("#"):
                         print(message_text)
                         hashtag_id = hashtagDao.insert(message_text) #returns hashtag_id insert to hashtag table
                         hasDao.insert(message_id,hashtag_id)

                 result = self.message_attributes(original_message)
                 return jsonify(users=result), 201
             else:
                 return jsonify(Error="Unexpected attributes in post request"), 400