import sqlite3


class con_sqlite:

    def __init__(self, path):

        """path 数据库的地址路径"""
        self.path = path

        """连接数据库"""
        try:
            self.con = sqlite3.connect(self.path)

            """获取游标"""
            self.cu = self.con.cursor()

            """连接失败抛出异常"""
        except sqlite3.OperationalError as Info:
            print("连接失败：s%ds" % Info)

    def select_sql(self, sql):

        """查询语句"""
        self.cu.execute(sql)

        """获取查询的数据"""
        res = self.cu.fetchall()
        return res

    def execute(self, sql):
        """增改删的方式"""
        try:
            self.cu.execute(sql)
            """提交sql"""
            self.con.commit()

            """提交失败抛出异常"""
        except Exception as info:
            print("提交错误： s%ds" % info)
            """失败后回滚事务"""
            self.con.rollback()

    def close(self):
        """关闭游标"""
        self.cu.close()
        """关闭数据库"""
        self.con.close()


def select_sqlite_pms_v4(sql):
    a = con_sqlite("C:/FeigeDownload/192.168.2.64/AGVS1.8.23.0/AGVS-1.8.23.0/Plugins/PMS/PMS/PmsV4.db")
    res = a.select_sql(sql)
    a.close()
    return res


def execute_sqlite_pms_v4(sql):
    a = con_sqlite("C:/FeigeDownload/192.168.2.64/AGVS1.8.23.0/AGVS-1.8.23.0/Plugins/PMS/PMS/PmsV4.db")
    a.execute(sql)
    a.close()


def select_sqlite_system(sql):
    a = con_sqlite("C:/FeigeDownload/192.168.2.64/AGVS1.8.23.0/AGVS-1.8.23.0/Custom/Config/System.db")
    res = a.select_sql(sql)
    a.close()
    return res


def execute_sqlite_system(sql):
    a = con_sqlite("C:/FeigeDownload/192.168.2.64/AGVS1.8.23.0/AGVS-1.8.23.0/Custom/Config/System.db")
    a.execute(sql)
    a.close()

if __name__ == '__main__':
    id_ = select_sqlite_system("select ID from role where RoleName = 'test007'")[0][0]
    print(id_)