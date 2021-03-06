from config.dbconfig import pg_config
import psycopg2

class ReplyDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                                pg_config['user'],
                                                                pg_config['passwd'])

        self.conn = psycopg2._connect(connection_url)

    def getAllReplies(self):
        cursor = self.conn.cursor()
        query = "select * from reply;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRepliesPerDay(self):
        cursor = self.conn.cursor()
        query = "SELECT date_trunc('day',message.message_date) AS Day , count(*) AS No " \
                "FROM message natural inner join reply where reply.reply_id = message.message_id" \
                " GROUP BY date_trunc('day',message.message_date) " \
                "ORDER BY date_trunc('day',message.message_date) desc"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result


    # def getReplyById(self, id):
    #     for r in self.data:
    #         if id == r[0]:
    #             return r
    #     return None

    def getReplysForMessageId(self, owner_id):
        cursor = self.conn.cursor()
        query = "select * from reply where reply.owner_id = %s;"
        cursor.execute(query, (owner_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getReplyToMessageId(self, reply_id):
        cursor = self.conn.cursor()
        query = "select * reply where reply.reply_id = %s;"
        cursor.execute(query, (reply_id,))
        result = cursor.fetchone()
        return result


    def insert(self,owner_id,reply_id):
        cursor = self.conn.cursor()
        query = "insert into reply(owner_id, reply_id) values (%s,%s) returning owner_id;"
        cursor.execute(query, (owner_id,reply_id,))
        owner_id = cursor.fetchone()[0]
        self.conn.commit()
        return owner_id


