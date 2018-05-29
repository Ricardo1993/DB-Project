from config.dbconfig import pg_config
import psycopg2

class Group_ChatDAO:

    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])

        self.conn = psycopg2._connect(connection_url)


    def getAllChats(self):
        cursor = self.conn.cursor()
        query = "select * from group_chat;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getChatById(self, group_id):
        cursor = self.conn.cursor()
        query = "select * from group_chat where group_id = %s;"
        cursor.execute(query, (group_id,))
        result = cursor.fetchone()
        return result

    def searchByChatName(self, group_name):
        cursor = self.conn.cursor()
        query = "select * from group_chat where group_name = %s;"
        cursor.execute(query, (group_name,))
        result = cursor.fetchone()
        return result


    def check(self, group_name):
        cursor = self.conn.cursor()
        query = "select * from group_chat where group_name = %s;"
        cursor.execute(query, (group_name,))
        result = cursor.fetchone()
        return result

    def insert(self, group_name):
        cursor = self.conn.cursor()
        query = "insert into group_chat(group_name, group_number_users, group_active)" \
                " values(%s,1,0) returning group_id;"
        cursor.execute(query, (group_name,))
        group_id = cursor.fetchone()[0]
        self.conn.commit()
        return group_id

    def remove(self, group_name):
        cursor = self.conn.cursor()
        query = "DELETE from group_chat where group_name = %s returning group_id;"
        cursor.execute(query, (group_name,))
        group_id = cursor.fetchone()[0]
        self.conn.commit()
        return group_id