from config.dbconfig import pg_config
import psycopg2

class ContactDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])

        self.conn = psycopg2._connect(connection_url)


    def getAllContactsRelations(self):
        cursor = self.conn.cursor()
        query = "select * from contacts;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getContactsByUserId(self, users_id):
        cursor = self.conn.cursor()
        query = "select * from contacts where super_id = %s;"
        cursor.execute(query, (users_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

