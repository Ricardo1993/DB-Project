from flask import jsonify, request
from dao.contact import ContactDAO
from dao.user import UserDAO
class ContactHandler:
    def searchUserDAO(self, r):
        dao = UserDAO()

        userByID = dao.getUserById(r[0])
        print(userByID)
        user = userByID[1] + ' ' + userByID[2]
        contactByID = dao.getUserById(r[1])
        contact = contactByID[1] + ' ' + contactByID[2]
        print(contactByID)
        result = []
        result.append(user)
        result.append(contact)
        return result

    def getAllContacts(self):
        dao = ContactDAO()

        result = dao.getAllContactRelations()
        mapped_result = []
        for r in result:
            usersPair = self.searchUserDAO(r)
            mapped_result.append(self.mapToDict(usersPair))
        return jsonify(Contacts=mapped_result)


    def mapToDict(self, row):
        result = {}
        result['user'] = row[0]
        result['contact'] = row[1]
        return result

    def getContactsByUserID(self, id):
        dao = ContactDAO()
        result = dao.getContactsByUserId(id)
        if result == None:
            return jsonify(Error="REPLY NOT FOUND")
        else:
            # print(result)
            mapped_result = []
            # usersPair = self.searchUserDAO(result)
            # print(usersPair)
            # mapped = self.mapToDict(usersPair)
            # return jsonify(Contacts=mapped)            #usersPair = []
            for r in result:
                usersPair = self.searchUserDAO(r)
                print(usersPair)
                mapped_result.append(self.mapToDict(usersPair))

            print(usersPair)
            mapped = self.mapToDict(usersPair)
            return jsonify(Reply=mapped_result)


