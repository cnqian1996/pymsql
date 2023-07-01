import pymysql


def main():
    colname1 = input('请输入要删除的学校名称：')
    # 第一步：指定主机、端口、用户名、口令、数据库、字符集创建连接
    conn = pymysql.connect(host='58.213.41.44', port=12307, user='root', password='123456', db='school', charset='utf8')

    try:
        # 第二步：通过连接对象的cursor方法获取游标对象
        with conn.cursor() as cursor:
            # 第三步：通过游标对象的execute方法向数据库发出SQL
            result = cursor.execute(
                'delete from tb_college where colname=%s', (colname1,)
            )
            if result == 1:
                print('删除成功!!!')
            # 第四步：所有操作都成功就提交
            conn.commit()
    except pymysql.MySQLError as err:
        print(err)
        # 第四步：如果出现异常就回滚（撤销）
        conn.rollback()
    finally:
        # 第五步：关闭连接释放资源
        conn.close()


if __name__ == '__main__':
    main()
