class MessageDAO:
    def __init__(self):
        # M1 = [1, 'Profe que viene para el examen???', '3', '1', '2', '03/21/2018', 134, 1]
        # M2 = [2, 'Todo', '1', '3', '0', '03/21/2018', 200, 1]
        # M3 = [3, 'Ah diache profe.', '1', '1', '0', '03/21/2018', 28, 1]
        # M4 = [4, 'Ese examen va a estar feo', '2', '0', '0', '03/22/2018', 28, 2]

        M1 = [1, 'Profe que viene para el examen???', '03/21/2018', 134, 1]
        M2 = [2, 'Todo', '03/21/2018', 200, 1]
        M3 = [3, 'Ah diache profe.', '03/21/2018', 28, 1]
        M4 = [4, 'Ese examen va a estar feo', '03/22/2018', 28, 2]

        self.data = []
        self.data.append(M1)
        self.data.append(M2)
        self.data.append(M3)
        self.data.append(M4)

    def getAllMessages(self):
        return self.data

    def getMessageById(self, id):
        for r in self.data:
            if id == r[0]:
                return r
        return None

    def searchByChatId(self, chat_id):
        result = []
        for r in self.data:
            if chat_id == r[4]:
                result.append(r)
        return result

    def searchByUserId(self, user_id):
        result = []
        for r in self.data:
            if user_id == r[3]:
                result.append(r)
        return result
