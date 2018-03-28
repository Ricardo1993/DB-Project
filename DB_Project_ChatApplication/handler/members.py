from flask import jsonify, request
from dao.member import MemberDAO
from dao.user import UserDAO
from dao.chat import ChatDAO

class MembershipHandler:
    def getAllMemberships(self):
        dao = MemberDAO()
        result = dao.getAllMemberships()
        mapped_result = []
        for r in result:
            mapped_result.append(self.mapToDict(r))
        return jsonify(Members=mapped_result)

    def mapToDict(self, row):
        # daoU = UserDAO
        result = {}
        # result['membership_id'] = row[0]
        result['user_id'] = row[0]
        result['chat_id'] = row[1]
        return result

    # def getMembershipsByID(self, id):
    #     dao = MemberDAO()
    #     result = dao.getMembershipByID(id)
    #     if result == None:
    #         return jsonify(Error="MEMBERSHIP NOT FOUND")
    #     else:
    #         mapped = self.mapToDict(result)
    #         return jsonify(Members=mapped)

    def getMembershipByUID(self, user_id):
        dao = MemberDAO()
        result = dao.getMembershipByUserID(user_id)
        if result == None:
            return jsonify(Error="MEMBERSHIP NOT FOUND")
        else:
            mapped_result = []
            for r in result:
                mapped_result.append(self.mapToDict(r))
            return jsonify(Members=mapped_result)

    def getMembershipByChatID(self, chat_id):
        dao = MemberDAO()
        result = dao.getMembershipByChatID(chat_id)
        if result == None:
            return jsonify(Error="MEMBERSHIP NOT FOUND")
        else:
            mapped_result = []
            for r in result:
                mapped_result.append(self.mapToDict(r))
            return jsonify(Members=mapped_result)
