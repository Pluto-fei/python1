import pymysql

class Dept(object):
    def __init__(self, no, name, location):
        self.no = no
        self.name = name
        self.location = location

    def __str__(self):
        return f'{self.no}\t{self.name}\t{self.location}'

def main():
    # 1.连接mysql数据库
    conn = pymysql.connect(host='47.96.6.227', port=13306, user='root', password='feifei.17', db='mysql-one', charset='utf8', cursorclass=pymysql.cursors.DictCursor)
    try:
        # 2.获得游标对象
        with conn.cursor() as cursor:
            # 3.执行SQL得到结果
            cursor.execute('select 编号 as no, 部门 as name, 地点 as location from tb_dept')
            for row in cursor.fetchall():
                dept = Dept(**row)
                print(dept)
    except pymysql.MySQLError as error:
        print(error)
    finally:
        # 6.关闭连接释放资源
        conn.close()

if __name__ == '__main__':
    main()

