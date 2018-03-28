class HashtagDAO:
    def __init__(self):
        H1 = [1, '#PRSeLevanta', '03/21/2018']
        H2 = [2, '#100x35', '03/21/2018']

        self.data = []
        self.data.append(H1)
        self.data.append(H2)

    def getAllHashtags(self):
        return self.data

    def getHashtagById(self, id):
        result = []
        for r in self.data:
            if id == r[0]:
               result.append(r[1]);
        return result

