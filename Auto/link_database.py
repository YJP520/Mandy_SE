#
# Edited by Pycharm.
# Time : 2022/11/24
# Author : YU.J.P
#

# 连接数据库
import pymysql
# 引入decimal模块
import decimal

########################################################################################################################


def create_database():
    """
    python 创建表 测试
    :return:
    """
    # 连接数据库
    db = pymysql.connect(host='localhost', user='root', password='5255', charset='utf8')

    # 创建一个游标对象（相当于指针）
    cursor = db.cursor()

    # 执行创建数据库语句
    cursor.execute('create schema wzg default charset=utf8;')
    cursor.execute('show databases;')

    # fetchone获取一条数据（元组类型）
    print(cursor.fetchone())
    # 现在指针到了[1]的位置

    # fetchall获取全部数据（字符串类型）
    data = cursor.fetchall()
    for i in data:
        print(i[0])

    # 关闭游标和数据库连接
    cursor.close()
    db.close()


def insert_database():
    """
    插入指定数据
    :return:
    """
    # 连接数据库
    db = pymysql.connect(host='localhost', user='root', password='5255', database="schema_html", charset='utf8')
    # 创建游标对象
    cursor = db.cursor()

    try:
        # # 创建student表，并执行
        # sql = '''create table student(
        #    SNO char(10),
        #    SNAME varchar(20) NOT NULL,
        #    SSEX varchar(1),
        #    primary key(SNO)
        #    )default charset=utf8;'''
        # cursor.execute(sql)

        # 插入一条数据，并执行
        insert_sql = '''
        insert into table_link(link, name, comment) values('https://blog.csdn.net/', 'CSDN', '100+')
        '''
        cursor.execute(insert_sql)

        # 将数据提交给数据库（加入数据，修改数据要先提交）
        db.commit()

        # 执行查询语句
        cursor.execute('select * from table_link')

        # 打印全部数据
        data = cursor.fetchall()
        for i in data:
            print(i)

    # 发生错误时，打印报错原因
    except Exception as e:
        print(e)

    # 无论是否报错都执行
    finally:
        cursor.close()
        db.close()


def insert_jd_link(link, name, price, comment):
    """
    插入指定数据
    :return: None
    """
    # 连接数据库
    db = pymysql.connect(host='localhost', user='root', password='5255', database="schema_html", charset='utf8')
    # 创建游标对象
    cursor = db.cursor()
    try:
        # 加入数据
        insert_sql = "insert into table_link(link, name, price, comment) values(%s, %s, %s, %s)"
        values = (link, name, price, comment)
        cursor.execute(insert_sql, values)
        # 将数据提交给数据库（加入数据，修改数据要先提交）
        db.commit()
        print("OK...")
    # 发生错误时，打印报错原因
    except Exception as e:
        print(e)
    # 无论是否报错都执行
    finally:
        cursor.close()
        db.close()


# 查询数据
def search_index(keyword):
    # 连接数据库
    db = pymysql.connect(host='localhost', user='root', password='5255', database="schema_html", charset='utf8')
    # 创建游标对象
    cursor = db.cursor()
    # mysql 模糊查询、
    try:
        SQL = "select link, name, price, comment from table_link where name like '%s'" % ('%%%s%%' % keyword)
        # SQL = "select link, name, price, comment from table_link"
        cursor.execute(SQL)
        data = cursor.fetchall()
        # for link, name, price, comment in data:
        #     print(link)
        #     print(name)
        #     print(price)
        #     print(comment)
        return data
    except Exception as e:
        print("错误原因", e)
        return None
    finally:
        cursor.close()

########################################################################################################################


# MIAN
if __name__ == "__main__":
    # insert_database()

    # insert_jd_link('https://blog.csdn.net/', 'CSDN', '130+')
    search_index("男女")
    pass
