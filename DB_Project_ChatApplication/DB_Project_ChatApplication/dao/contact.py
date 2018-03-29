class ContactDAO:
    def __init__(self):
        # C = [user, contact]
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

    def getContactsByUserId(self, id):
        print(id)
        result = []
        for r in self.data:
            if id == r[0]:
                result.append(r)
        return result

