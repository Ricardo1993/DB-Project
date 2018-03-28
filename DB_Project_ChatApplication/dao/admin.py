class AdminDAO:
    def __init__(self):
        Ad1 = [200, 1]
        Ad2 = [28, 2]

        self.data = []
        self.data.append(Ad1)
        self.data.append(Ad2)

    def getAllAdmins(self):
        return self.data

    def getAdminsByChatID(self, chat_id):
        result = []
        for r in self.data:
            if chat_id == r[1]:
                return r
            return None

    def getChatsAdministratedByUser(self, user_id):
        result = []
        for r in self.data:
            if user_id == r[0]:
                result.append(r)
        return result
