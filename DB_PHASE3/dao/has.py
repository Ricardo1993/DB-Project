from config.dbconfig import pg_config
import psycopg2


class HasTagDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])

        self.conn = psycopg2._connect(connection_url)

    def getHashtagsInMessage(self, message_id):
        cursor = self.conn.cursor()
        query = "select * from has where has.message_id = %s;"
        cursor.execute(query, (message_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getMessagesWithHashtagID(self, hashtag_id):
        cursor = self.conn.cursor()
        query = "select * from message natural inner join has where has.hashtag_id = %s;"
        cursor.execute(query, (hashtag_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getMessagesWithHashtagText(self, hashtag_text):
        cursor = self.conn.cursor()
        query = "select * from message natural inner join has natural inner join hashtag where hashtag.hashtag_text = %s;"
        cursor.execute(query, (hashtag_text,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def insert(self, message_id,hashtag_id):
        cursor = self.conn.cursor()
        query = "insert into has(message_id, hashtag_id) values(%s,%s) returning message_id;"
        cursor.execute(query, (message_id,hashtag_id,))
        result = cursor.fetchone()[0]
        self.conn.commit()
        return result
