import pymysql


class College(object):
    def __init__(self,no,college_web,name):
        self.no = no
        self.college_web = college_web
        self.name = name

    def __str__(self):
        return f'{self.no}\t{self.college_web}\t{self.name}\t'

def main():
    # 1.创建对象
    # 第一步：指定主机、端口、用户名、口令、数据库、字符集创建连接
    conn = pymysql.connect(host='58.213.41.44', port=12307,
                           user='root', password='123456',
                           db='school',
                           charset='utf8',
                           cursorclass=pymysql.cursors.DictCursor)

    try:
        # 第二步：通过连接对象的cursor方法获取游标对象
        with conn.cursor() as cursor:
            # 第三步：通过游标对象的execute方法向数据库发出SQL
            cursor.execute('select colid as no,website as college_web,colmaster as name from tb_college')
            for row in cursor.fetchall():
                college = College(**row)
                print(college)

    except pymysql.MySQLError as err:
        print(err)

    finally:
        # 第五步：关闭连接释放资源
        conn.close()


if __name__ == '__main__':
    main()
