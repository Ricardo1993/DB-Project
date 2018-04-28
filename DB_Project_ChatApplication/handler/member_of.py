from flask import jsonify, request
from dao.member_of import MemberDAO
from dao.users import UsersDAO
from dao.group_chat import Group_ChatDAO

class MembershipHandler:

    def mapToDict(self, row):
        result = {}
        result['user'] = row[0]
        result['chat'] = row[1]
        return result

    def getAllMemberships(self):
        dao = MemberDAO()
        dao1 = UsersDAO()
        dao2 = Group_ChatDAO()
        result = dao.getAllMemberships()

        mapped_result = []
        for r in result:
            membership = []
            user = dao1.getUserById(r[0])
            group = dao2.getChatById(r[1])
            membership.append(user[1] + " " + user[2])
            membership.append(group[1])
            mapped_result.append(self.mapToDict(membership))
        return jsonify(Members=mapped_result)


    def getMembershipByUID(self, users_id):
        dao = MemberDAO()
        dao1 = UsersDAO()
        dao2 = Group_ChatDAO()
        result = dao.getMembershipsByUserID(users_id)

        if result == None:
            return jsonify(Error="MEMBERSHIP NOT FOUND")
        else:
            mapped_result = []
            for r in result:
                membership = []
                user = dao1.getUserById(r[0])
                group = dao2.getChatById(r[1])
                membership.append(user[1] + " " + user[2])
                membership.append(group[1])
                mapped_result.append(self.mapToDict(membership))
            return jsonify(Members=mapped_result)


    def getMembershipByChatID(self, group_id):
        dao = MemberDAO()
        dao1 = UsersDAO()
        dao2 = Group_ChatDAO()
        result = dao.getMembershipsOfGroupID(group_id)
        # print(result)
        if result == None:
            return jsonify(Error="MEMBERSHIP NOT FOUND")
        else:
            mapped_result = []
            for r in result:
                membership = []
                user = dao1.getUserById(r[0])
                group = dao2.getChatById(r[1])
                membership.append(user[1] + " " + user[2])
                membership.append(group[1])
                mapped_result.append(self.mapToDict(membership))
            return jsonify(Members=mapped_result)
