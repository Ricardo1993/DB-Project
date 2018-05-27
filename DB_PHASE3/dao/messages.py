from config.dbconfig import pg_config
import psycopg2

class MessagesDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])

        self.conn = psycopg2._connect(connection_url)

    def getMessageByChatId(self, group_id):
        cursor = self.conn.cursor()
        query = "select * from message natural inner join messages where messages.group_id = %s;"
        cursor.execute(query, (group_id,))
        result = cursor.fetchone()
        return result

    def getChatByMessageId(self, message_id):
        cursor = self.conn.cursor()
        query = "select * from group_chat natural join messages where messages.message_id = %s;"
        cursor.execute(query, (message_id,))
        result = cursor.fetchone()
        return result

    def check(self, users_id, group_name):
        cursor = self.conn.cursor()
        query = "select * from member_of where users_id = %s and group_id = %s;"
        cursor.execute(query, (users_id,group_name,))
        result = cursor.fetchone()
        return result

    def insert(self, message_id, group_id):
        cursor = self.conn.cursor()
        query = "insert into messages(message_id,group_id) values(%s,%s) returning message_id;"
        cursor.execute(query, (message_id,group_id))
        result = cursor.fetchone()[0]
        self.conn.commit()
        return result