import pymysql


def main():
    colid1 = input('请输入要编辑的学校ID：')
    colweb1 = input('学校新网站地址：')
    colmaster1 = input('新院长名字：')
    # 第一步：指定主机、端口、用户名、口令、数据库、字符集创建连接
    conn = pymysql.connect(host='58.213.61.44', port=12307, user='root', password='123456', db='school', charset='utf8')

    try:
        # 第二步：通过连接对象的cursor方法获取游标对象
        with conn.cursor() as cursor:
            # 第三步：通过游标对象的execute方法向数据库发出SQL
            result = cursor.execute(
                'update tb_college set colmaster=%s,website=%s  where colid=%s', (colmaster1,colweb1,colid1)
            )
            if result == 1:
                print('修改成功!!!')
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
