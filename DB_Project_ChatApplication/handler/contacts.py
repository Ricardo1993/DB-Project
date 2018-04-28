from flask import jsonify
from dao.contacts import ContactDAO
from dao.users import UsersDAO

class ContactHandler:

    def mapToDict(self, row):
        result = {}
        result['user'] = row[0]
        result['contact'] = row[1]
        return result

    def getAllContacts(self):
        dao = ContactDAO()
        result = dao.getAllContactsRelations()
        mapped_result = []
        for r in result:
            usersPair = self.searchUserDAO(r)
            mapped_result.append(self.mapToDict(usersPair))
        return jsonify(Contacts=mapped_result)


    def getContactsByUserID(self,users_id):
        dao = ContactDAO()
        result = dao.getContactsByUserId(users_id)
        if result == None:
            return jsonify(Error="CONTACT NOT FOUND")
        else:
            mapped_result = []
            for r in result:
                usersPair = self.searchUserDAO(r)
                mapped_result.append(self.mapToDict(usersPair))
            return jsonify(Contacts=mapped_result)


    def searchUserDAO(self, r):
        dao = UsersDAO()
        userByID = dao.getUserById(r[0])
        user = userByID[1] + ' ' + userByID[2]
        contactByID = dao.getUserById(r[1])
        contact = contactByID[1] + ' ' + contactByID[2]
        result = []
        result.append(user)
        result.append(contact)
        return result

