from flask import jsonify, request
from dao.member import MemberDAO
from dao.user import UserDAO
from dao.chat import ChatDAO

class MembershipHandler:
    def getAllMemberships(self):
        dao = MemberDAO()
        dao1 = UserDAO()
        dao2 = ChatDAO()
        result = dao.getAllMemberships()

        mapped_result = []
        for r in result:
            result2 = dao1.getUserById(r[0])
            result3 = dao2.getChatById(r[1])
            r[0] = result2[1] + " " + result2[2]
            r[1] = result3[1]
            mapped_result.append(self.mapToDict(r))
        return jsonify(Members=mapped_result)


    def mapToDict(self, row):
        result = {}
        result['user'] = row[0]
        result['chat'] = row[1]
        return result


    def getMembershipByUID(self, user_id):
        dao = MemberDAO()
        dao1 = UserDAO()
        dao2 = ChatDAO()
        result = dao.getMembershipByUserID(user_id)
        if result == None:
            return jsonify(Error="MEMBERSHIP NOT FOUND")
        else:
            mapped_result = []
            for r in result:
                result2 = dao1.getUserById(r[0])
                result3 = dao2.getChatById(r[1])
                r[0] = result2[1] + " " + result2[2]
                r[1] = result3[1]
                mapped_result.append(self.mapToDict(r))
            return jsonify(Members=mapped_result)


    def getMembershipByChatID(self, chat_id):
        dao = MemberDAO()
        dao1 = UserDAO()
        dao2 = ChatDAO()
        result = dao.getMembershipByChatID(chat_id)
        # print(result)
        if result == None:
            return jsonify(Error="MEMBERSHIP NOT FOUND")
        else:
            mapped_result = []
            for r in result:
                result2 = dao1.getUserById(r[0])
                result3 = dao2.getChatById(r[1])
                r[0] = result2[1] + " " + result2[2]
                r[1] = result3[1]
                mapped_result.append(self.mapToDict(r))
            return jsonify(Members=mapped_result)

