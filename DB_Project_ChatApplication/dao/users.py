from config.dbconfig import pg_config
import psycopg2

class UsersDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])

        self.conn = psycopg2._connect(connection_url)

    def getAllUsers(self):
        cursor = self.conn.cursor()
        query = "select * from users;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUserById(self, users_id):
        cursor = self.conn.cursor()
        query = "select * from users where users_id = %s;"
        cursor.execute(query, (users_id,))
        result = cursor.fetchone()
        return result

    def getUserByName(self, first_name, last_name):
        cursor = self.conn.cursor()
        query = "select * from users where first_name = %s and last_name = %s;"
        cursor.execute(query,(first_name,last_name,))
        result = cursor.fetchone()
        return result



