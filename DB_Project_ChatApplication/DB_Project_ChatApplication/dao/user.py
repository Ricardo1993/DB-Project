class UserDAO:
    def __init__(self):
        U1 = [28, 'Ricardo', 'Casares', '7879999999','email1@upr.edu', 'db10rocks', '03/28/2018']
        U2 = [100, 'Diego', 'Capre', '7879999998','email2@upr.edu', 'db10forlife', '03/27/2018']
        U3 = [134, 'Victor', 'Fermin', '7879999997','email3@upr.edu', 'db10awesome', '03/28/2018']
        U4 = [200, 'Manuel', 'Rodriguez', '7879999996', 'professor@upr.edu', 'db10thebest', '03/01/2018']
        self.data = []
        self.data.append(U1)
        self.data.append(U2)
        self.data.append(U3)
        self.data.append(U4)

    def getAllUsers(self):
        return self.data

    def getUserById(self, id):
        for r in self.data:
            if id == r[0]:
                return r
        return None

