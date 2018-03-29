class ReplyDAO:
    def __init__(self):


        # R = [messageID, messageRepliedToID]
        R1 = [5, 2]
        R2 = [6, 3]
        R3 = [7, 4]
        R4 = [8, 1]
        R5 = [9, 2]
        R6 = [10, 4]


        self.data = []
        self.data.append(R1)
        self.data.append(R2)
        self.data.append(R3)
        self.data.append(R4)
        self.data.append(R5)
        self.data.append(R6)


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
