class MessageDAO:
    def __init__(self):
        M1 = [1, 'Profe que viene para el examen???', '03/21/2018', 134, 1]
        M2 = [2, 'Todo', '03/21/2018', 200, 1]
        M3 = [3, 'Ah diache profe.', '03/21/2018', 28, 1]
        M4 = [4, 'Ese examen va a estar feo. #PRSeLevanta', '03/22/2018', 28, 2]

        R5 = [5, 'Enserio?', '03/21/2018', 100, 1]
        R6 = [6,'A estudiar','03/21/2018', 200, 1]
        R7 = [7,'Super feo','03/21/2018', 134, 2]
        R8 = [8, 'Buena pregunta','03/22/2018', 28, 1]
        R9 = [9,'???? #100x35 #PRSeLevanta','03/21/2018', 134, 1]
        R10 = [10, 'Ya lo sabes','03/22/2018', 100, 2]


        self.data = []
        self.data.append(M1)
        self.data.append(M2)
        self.data.append(M3)
        self.data.append(M4)

        self.data.append(R5)
        self.data.append(R6)
        self.data.append(R7)
        self.data.append(R8)
        self.data.append(R9)
        self.data.append(R10)

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
