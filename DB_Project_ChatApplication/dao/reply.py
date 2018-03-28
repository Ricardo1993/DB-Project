class ReplyDAO:
    def __init__(self):
        #M1 = [1, 'Profe que viene para el examen???', '03/21/2018', 134, 1]
        #M2 = [2, 'Todo', '03/21/2018', 200, 1]
        #M3 = [3, 'Ah diache profe.', '03/21/2018', 28, 1]
        #M4 = [4, 'Ese examen va a estar feo', '03/22/2018', 28, 2]

        Re1 = [1,100,2,'Enserio?','03/21/2018']
        Re2 = [2,200,3, 'A estudiar','03/21/2018']
        Re3 = [3,134,4, 'Super feo','03/21/2018']
        Re4 = [4,28,1, 'Buena pregunta','03/22/2018']
        Re5 = [5,134,2, '????','03/21/2018']
        Re6 = [6,100,4, 'Ya lo sabes','03/22/2018']

        self.data = []
        self.data.append(Re1)
        self.data.append(Re2)
        self.data.append(Re3)
        self.data.append(Re4)
        self.data.append(Re5)
        self.data.append(Re6)


    def getAllReplies(self):
        return self.data

    def getReplyById(self, id):
        for r in self.data:
            if id == r[0]:
                return r
        return None

    def findReplyByMessageId(self, message_id):
        result = []
        for r in self.data:
            if message_id == r[2]:
                result.append(r)
        return result

    def searchByOwnerId(self, owner_id):
        result = []
        for r in self.data:
            if owner_id == r[1]:
                result.append(r)
        return result
