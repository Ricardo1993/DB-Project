from flask import jsonify, request
from dao.message import MessageDAO

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
