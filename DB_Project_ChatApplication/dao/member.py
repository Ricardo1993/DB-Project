class MemberDAO:
    def __init__(self):
        Mem1 = [28,1]
        Mem2 = [100,1]
        Mem3 = [134,1]
        Mem4 = [200,1]
        Mem5 = [28, 2]
        Mem6 = [100, 2]
        Mem7 = [134, 2]

        self.data = []
        self.data.append(Mem1)
        self.data.append(Mem2)
        self.data.append(Mem3)
        self.data.append(Mem4)
        self.data.append(Mem5)
        self.data.append(Mem6)
        self.data.append(Mem7)

    def getAllMemberships(self):
        return self.data

    def getMembershipByChatID(self, chat_id):
        result = []
        for r in self.data:
            if chat_id == r[1]:
                result.append(r)
        return result

    def getMembershipByUserID(self, user_id):
        result = []
        for r in self.data:
            if user_id == r[0]:
                result.append(r)
        return result
