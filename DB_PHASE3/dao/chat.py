class ChatDAO:
    def __init__(self):
        C1 = [1, 'DB Course', '4', '3', '03/20/2018']
        C2 = [2, 'DB Project', '3', '3', '03/21/2018']

        self.data = []
        self.data.append(C1)
        self.data.append(C2)


    def getAllChats(self):
        return self.data

    def getChatById(self, id):
        for r in self.data:
            if id == r[0]:
                return r
        return None

    def searchByChatName(self, chat_name):
        result = []
        for r in self.data:
            if chat_name == r[1]:
                result.append(r)
        return result
