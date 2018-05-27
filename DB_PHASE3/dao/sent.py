from config.dbconfig import pg_config
import psycopg2

class SentDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])

        self.conn = psycopg2._connect(connection_url)

    def getMessageByUserId(self, users_id):
        cursor = self.conn.cursor()
        query = "select * from users natural inner join sent where sent.users_id = %s;"
        cursor.execute(query, (users_id,))
        result = cursor.fetchone()
        return result

    def getUserByMessageId(self, message_id):
        cursor = self.conn.cursor()
        query = "select * from users natural join sent where sent.message_id = %s;"
        cursor.execute(query, (message_id,))
        result = cursor.fetchone()
        return result

    def insert(self,users_id, message_id):
        cursor = self.conn.cursor()
        query = "insert into sent(users_id,message_id) values (%s,%s) returning users_id;"
        cursor.execute(query, (users_id,message_id))
        result = cursor.fetchone()[0]
        self.conn.commit()
        return result