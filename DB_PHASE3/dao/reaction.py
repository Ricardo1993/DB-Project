from config.dbconfig import pg_config
import psycopg2

class ReactionDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])

        self.conn = psycopg2._connect(connection_url)

    def getAllReactions(self):
        cursor = self.conn.cursor()
        query = "select * from reaction;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getReactionsByUserId(self, users_id):
        cursor = self.conn.cursor()
        query = "select * from reaction where users_id = %s;"
        cursor.execute(query,(users_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result


    def getReactionsToMessageId(self, message_id):
        cursor = self.conn.cursor()
        query = "select * from reaction where message_id = %s;"
        cursor.execute(query, (message_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getLikesToMessageId(self, message_id):
        cursor = self.conn.cursor()
        query = "select * from reaction where message_id = %s and reaction = 'like' ;"
        cursor.execute(query, (message_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getDislikesToMessageId(self, message_id):
        cursor = self.conn.cursor()
        query = "select * from reaction where message_id = %s and reaction = 'dislike';"
        cursor.execute(query, (message_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getLikesCountToMessageId(self, message_id):
        cursor = self.conn.cursor()
        query = "select count(*) from reaction where message_id = %s and reaction = 'like';"
        cursor.execute(query, (message_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getDislikesCountToMessageId(self, message_id):
        cursor = self.conn.cursor()
        query = "select count(*) from reaction where message_id = %s and reaction = 'dislike';"
        cursor.execute(query, (message_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def insert(self,users_id, message_id,reaction):
        cursor = self.conn.cursor()
        query = "insert into reaction(users_id,message_id,reaction) values (%s,%s,%s) returning users_id;"
        cursor.execute(query, (users_id,message_id,reaction,))
        users_id = cursor.fetchone()[0]
        self.conn.commit()
        return users_id
