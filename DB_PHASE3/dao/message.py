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
        query = "select Message.message_id, message.message_text, Message.message_date, Users.first_name, Users.last_name " \
                "from message natural inner join users natural inner join sent " \
                "order by Message.message_id desc;"
        # query = "select * from Message"
        cursor.execute(query)
        result1 = []
        # print(cursor)
        newrow = []
        for row in cursor:
            newrow.append(row[0])
            newrow.append(row[1])
            newrow.append(row[2])
            newrow.append(row[3])
            newrow.append(row[4])
            newrow.append(0)
            newrow.append(0)

            result1.append(newrow)
            newrow = []

        query2 = "Select * from (Select count(reaction) as likes,  message_id, message_text from reaction natural inner join message natural inner join users " \
                "where reaction = 'like' " \
                "group by reaction, message_id, message_text " \
                "order by message_id) as l;"

        query3 = "Select * from (Select count(reaction) as dislikes,  message_id, message_text from reaction natural inner join message natural inner join users " \
                 "where reaction = 'dislike' " \
                 "group by reaction, message_id, message_text " \
                 "order by message_id) as d;"

        # query = "select * from Message"
        cursor.execute(query2)
        for r in result1:
            for row in cursor:
                if r[0] == row[1]:
                    r[5] = row[0]
                    # print(result1[0])
                    break
                # else:
                #     r[5] = 0
        cursor.execute(query3)
        for r in result1:
            for row in cursor:
                if r[0] == row[1]:
                    r[6] = row[0]
                    # print(result1[0])
                    break
        return result1

    def getMessageById(self, message_id):
        cursor = self.conn.cursor()
        query = "select * from message where message_id = %s;"
        cursor.execute(query, (message_id,))
        result = cursor.fetchone()
        return result

    def searchMessagesByGroupId(self, group_id):
        cursor = self.conn.cursor()
        query = "select * from message natural inner join messages where messages.group_id = %s " \
                "order by Message.message_id desc;"
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

    def insert(self,message_text):
        cursor = self.conn.cursor()
        query = "insert into message (message_text) values(%s) returning message_id;"
        cursor.execute(query, (message_text,))
        message_id = cursor.fetchone()[0]
        self.conn.commit()
        return message_id
