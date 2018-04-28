from config.dbconfig import pg_config
import psycopg2

class MessageDAO:

    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])

        self.conn = psycopg2._connect(connection_url)

    def getAllMessages(self):
        cursor = self.conn.cursor()
        query = "select * from message;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getMessageById(self, message_id):
        cursor = self.conn.cursor()
        query = "select * from message where message_id = %s;"
        cursor.execute(query, (message_id,))
        result = cursor.fetchone()
        return result

    def searchMessagesByGroupId(self, group_id):
        cursor = self.conn.cursor()
        query = "select * from message natural inner join messages where messages.group_id = %s;"
        cursor.execute(query, (group_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def searchByUserId(self, user_id):
        cursor = self.conn.cursor()
        query = "select * from message natural inner join sent where sent.users_id = %s;"
        cursor.execute(query, (user_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def searchByUser_And_GroupID(self, group_id, user_id):
        cursor = self.conn.cursor()
        query = "select * from message natural inner join sent natural inner join messages where messages.group_id = %s and sent.users_id = %s;"
        cursor.execute(query, (group_id,user_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

