class HasTagDAO:
    def __init__(self):
        H1 = [9, 2]
        H2 = [4, 1]
        H3 = [9, 1]

        self.data = []
        self.data.append(H1)
        self.data.append(H2)
        self.data.append(H3)

    # def getAllHasRelationships(self):
    #     return self.data

    def getHashtagsInMessage(self, message_id):
        result = []
        for r in self.data:
            if message_id == r[0]:
               result.append(r)
        return result

    def getMessagesWithHashtag(self, hashtag_id):
        result = []
        for r in self.data:
            if hashtag_id == r[1]:
               result.append(r)
        return result


