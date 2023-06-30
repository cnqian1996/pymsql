import pymysql


def main():
    # 建立连接
    conn = pymysql.connect(host='58.213.61.44', port=12307, user='root', password='123456', db='school', charset='utf8')

    try:
        # 上下文语法
        with conn.cursor() as cursor:
            result = cursor.execute(
                'insert into tb_college (colid,colname,website,colmaster) values (6,"南通大学","http://www.nantong.com","钱黄飞");')
            if result == 1:
                print('添加成功')
            conn.commit()
    except pymysql.MySQLError as error:
        print(error)
        conn.rollback()
    finally:
        conn.close()


if __name__ == '__main__':
    main()
