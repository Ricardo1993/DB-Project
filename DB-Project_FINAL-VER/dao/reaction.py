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

    # def getAllReactionsCount(self):
    #     cursor = self.conn.cursor()
    #     query = "select reaction, count(*) from parts natural inner join supplies group by pid, pname order by pname;"
    #     cursor.execute(query)
    #     result = []
    #     for row in cursor:
    #         result.append(row)
    #     return result

    def getLikesPerDay(self):
        cursor = self.conn.cursor()
        query = "SELECT date_trunc('day',message.message_date) AS Day , count(*) AS No " \
                "FROM message natural inner join reaction" \
                " where reaction.message_id = message.message_id" \
                " and reaction.reaction = 'like' " \
                "GROUP BY date_trunc('day',message.message_date)" \
                " ORDER BY date_trunc('day',message.message_date) desc;"

        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result
    def getDislikesPerDay(self):
        cursor = self.conn.cursor()
        query = "SELECT date_trunc('day',message.message_date) AS Day , count(*) AS No " \
                "FROM message natural inner join reaction" \
                " where reaction.message_id = message.message_id" \
                " and reaction.reaction = 'dislike' " \
                "GROUP BY date_trunc('day',message.message_date)" \
                " ORDER BY date_trunc('day',message.message_date) desc;"

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
            print(row)
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
