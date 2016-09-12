from 0001 import genCodes
import pymysql


def getconnection():
    connection = pymysql.connect(
        host='192.168.9.1',
        port=3306,
        user='xiaoabiang',
        password='xiaoabiang',
        db='db',
        charset='utf8mb4'
    )
    try:
        with connection.cursor() as cur:
            sql = 'select * from blogs'
            cur.excute(sql)
            rs = cur.fetchall()
            return rs
    except:
        return None


def main():
    aa = getconnection()
    print(aa)

if __name__ == "__main__":
    main()
            


