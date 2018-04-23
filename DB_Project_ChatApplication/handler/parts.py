from flask import jsonify, request
import psycopg2

conn = psycopg2.connect("dbname=Kutuphane user=postgres password=orion3710")


class PartsHandler:
    def getAllParts(self):
        # dao = UserDAO()
        result = conn.cursor()
        result.execute("Select * from Parts")
        mapped_result = []
        for r in result:
            mapped_result.append(self.mapToDict(r))
        return jsonify(Users=mapped_result)

    def mapToDict(self, row):
        result = {}
        result['pid'] = row[0]
        result['pname'] = row[1]
        result['pprice'] = row[2]
        result['pcolor'] = row[3]
        result['pweight'] = row[4]
        # result['user_password'] = row[5]
        # result['date'] = row[6]
        return result

    # def getUserByID(self, id):
    #     dao = UserDAO()
    #     result = dao.getUserById(id)
    #     if result == None:
    #         return jsonify(Error="USER NOT FOUND")
    #     else:
    #         mapped = self.mapToDict(result)
    #         return jsonify(User=mapped)