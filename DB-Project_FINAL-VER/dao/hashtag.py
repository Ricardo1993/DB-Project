from config.dbconfig import pg_config
import psycopg2

class HashtagDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])

        self.conn = psycopg2._connect(connection_url)

    def getTrends(self):
        cursor = self.conn.cursor()
        query = "SELECT date_trunc('day',hashtag.hashtag_date) AS Day , hashtag_text , count(*) " \
                "FROM hashtag GROUP BY date_trunc('day',hashtag.hashtag_date), hashtag_text" \
                " ORDER BY date_trunc('day',hashtag.hashtag_date)desc;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllHashtags(self):
        cursor = self.conn.cursor()
        query = "select * from hashtag;"
        cursor.execute(query)
        result = []
        for row in cursor:

            result.append(row)
        return result

    def getHashtagById(self, hashtag_id):
        cursor = self.conn.cursor()
        query = "select * from hashtag where hashtag.hashtag_id = %s;"
        cursor.execute(query, (hashtag_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getHashtagByText(self,hashtag_text):
        cursor = self.conn.cursor()
        query = "select * from hashtag where hashtag.hashtag_text = %s;"
        cursor.execute(query, (hashtag_text,))
        result = []
        print(cursor)
        for row in cursor:
            print(row)
            result.append(row)
        return result

    def getHashtagByTextAndGroup(self,hashtag_text,group_id):
        cursor = self.conn.cursor()
        query = "Select hashtag_id,hashtag_text from hashtag natural inner join has natural inner join message natural inner join messages where hashtag.hashtag_text = %s and group_id = %s;"
        cursor.execute(query, (hashtag_text,group_id))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def insert(self, hashtag_text):
        cursor = self.conn.cursor()
        query = "Select count(*) from hashtag natural inner join has;"
        cursor.execute(query)
        id = 1
        for row in cursor:
            # print(row['hashtag_id'])
            id = id + 1
        query = "insert into hashtag(hashtag_text, hashtag_uses) values (%s," + str(id) + ") returning hashtag_id;"
        cursor.execute(query, (hashtag_text,))
        hashtag_id = cursor.fetchone()
        self.conn.commit()
        return hashtag_id

