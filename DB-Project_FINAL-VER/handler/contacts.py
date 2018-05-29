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

    def contacts_attributes(self, first_name, last_name):
        result = {}
        result['first_name'] = first_name
        result['last_name'] = last_name
        return result

    def checkContact(self, form):


        if len(form) != 2:
            return jsonify(Error="Malformed post request"), 400
        else:
            first_name = form['first_name']
            last_name = form['last_name']
            if first_name and last_name:
                Udao = UsersDAO()
                check = Udao.getUserByName(first_name,last_name) # only checking if usr exists

                if(check is None):
                    return None
                else:
                    result = self.contacts_attributes(first_name,last_name)

                    return jsonify(users=result), 201
            else:
                 return jsonify(Error="Unexpected attributes in post request"), 400

    def addContact(self, form, super_id):

        if len(form) != 2:
            return jsonify(Error="Malformed post request"), 400
        else:
            first_name = form['first_name']
            last_name = form['last_name']
            if first_name and last_name:
                Cdao = ContactDAO()
                Udao = UsersDAO()
                contact_info = Udao.getUserByName(first_name,last_name)
                print(contact_info)
                check = Cdao.getContactsBySuperAndContact(super_id,contact_info[0])
                print(check)
                if not check:
                    Cdao.insert(super_id,contact_info[0]) #insert users_id and group_id
                    result = self.contacts_attributes(first_name,last_name)
                    return jsonify(users=result), 201
                else:
                    return jsonify(Error="Contact already exists"), 400
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def removeContact(self, form, super_id):

        if len(form) != 2:
            return jsonify(Error="Malformed post request"), 400
        else:
            first_name = form['first_name']
            last_name = form['last_name']
            if first_name and last_name:
                Cdao = ContactDAO()
                Udao = UsersDAO()
                contact_info = Udao.getUserByName(first_name,last_name) #get user info of the contact to be added
                print(contact_info)
                check = Cdao.getContactsBySuperAndContact(super_id,contact_info[0]) # search if contact is already a contact in the list
                print(check)
                if check:
                    Cdao.remove(super_id,contact_info[0]) #remove users_id and group_id
                    result = self.contacts_attributes(first_name,last_name)
                    return jsonify(users=result), 201
                else:
                    return jsonify(Error="No contact by that name"), 400
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400