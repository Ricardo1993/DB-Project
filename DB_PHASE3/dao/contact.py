class ContactDAO:
    def __init__(self):
        C1 = [28, 100]
        C2 = [100, 28]
        C3 = [28, 134]
        C4 = [100, 134]
        C5 = [134, 28]
        C6 = [134, 100]
        C7 = [28, 200]
        C8 = [100, 200]
        C9 = [134, 200]

        self.data = []
        self.data.append(C1)
        self.data.append(C2)
        self.data.append(C3)
        self.data.append(C4)
        self.data.append(C5)
        self.data.append(C6)
        self.data.append(C7)
        self.data.append(C8)
        self.data.append(C9)


    def getAllContactRelations(self):
        return self.data

    # def getContactsOfUserID(self, user_id):
    #     dao = MemberDAO()
    #     result = dao.getMembershipByUserID(user_id)
    #     if result == None:
    #         return jsonify(Error="MEMBERSHIP NOT FOUND")
    #     else:
    #         mapped_result = []
    #         for r in result:
    #             mapped_result.append(self.mapToDict(r))
    #         return jsonify(Members=mapped_result)

