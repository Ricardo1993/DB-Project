from config.dbconfig import pg_config
import psycopg2

class MemberDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])

        self.conn = psycopg2._connect(connection_url)

    def getAllMemberships(self):
        cursor = self.conn.cursor()
        query = "select * from member_of;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getMembershipsOfGroupID(self, group_id):
        cursor = self.conn.cursor()
        query = "select * from member_of where group_id = %s;"
        cursor.execute(query, (group_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getMembershipsByUserID(self, users_id):
        cursor = self.conn.cursor()
        query = "select * from member_of where users_id = %s;"
        cursor.execute(query, (users_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getMembershipsByUserAndGroup(self, users_id, group_id):
        cursor = self.conn.cursor()
        query = "select * from member_of where users_id = %s and group_id = %s "
        cursor.execute(query, (users_id,group_id))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def insert(self,users_id, group_id):

        cursor = self.conn.cursor()
        query = 'insert into member_of(users_id, group_id)values(%s, %s) returning users_id;'
        cursor.execute(query, (users_id, group_id,))
        users_id = cursor.fetchone()[0]
        self.conn.commit()
        return users_id


    def remove(self, users_id,group_id):
            cursor = self.conn.cursor()
            query = 'delete from member_of where users_id = %s and group_id = %s returning users_id;'
            cursor.execute(query, (users_id,group_id,))
            users_id = cursor.fetchone()[0]
            self.conn.commit()
            return users_id