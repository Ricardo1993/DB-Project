class ReactionDAO:
    def __init__(self):
        # R = [r_id, message_id (foreign key), user_id, 'like/dislike']
        R1 = [1, 1, 28, 'like']
        R2 = [2, 1, 100, 'like']
        R3 = [3, 1, 200, 'dislike']
        R4 = [4, 1, 134, 'like']
        R5 = [5, 2, 200, 'like']
        R6 = [6, 2, 28, 'dislike']
        R7 = [7, 2, 100, 'dislike']
        R8 = [8, 2, 134, 'dislike']
        R9 = [9, 3, 200, 'dislike']
        R10 = [10, 3, 100, 'like']
        R11 = [11, 4, 100, 'like']
        R12 = [12, 4, 134, 'like']

        self.data = []
        self.data.append(R1)
        self.data.append(R2)
        self.data.append(R3)
        self.data.append(R4)
        self.data.append(R5)
        self.data.append(R6)
        self.data.append(R7)
        self.data.append(R8)
        self.data.append(R9)
        self.data.append(R10)
        self.data.append(R11)
        self.data.append(R12)

    def getAllReactions(self):
        return self.data

    def getReactionById(self, id):
        for r in self.data:
            if id == r[0]:
                return r
        return None

