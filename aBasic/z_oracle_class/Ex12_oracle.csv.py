#Ex12_oracle_csv.py

import cx_Oracle as oci
import csv

def createDBTable():
    conn = oci.connect('scott/tiger@127.0.01:1521/xe')
    sql = '''
            create table supply
            (
                id             number primary key,
                supplier_Name  varchar2(50),
                Invoice_Number varchar2(50),
                part_Number    varchar2(30),
                Cost           number,
                Purchase_Date  date
            )
    '''

    cursor = conn.cursor()
    cursor.execute(sql)

    sql2 = 'create sequence seq_supply_id'
    cursor.execute(sql2)

    cursor.close()
    conn.close()

def saveDBTable(data):
    conn = oci.connect('scott/tiger@127.0.01:1521/xe')
    sql = '''
    INSERT INTO supply
    VALUES
    (seq_supply_id.NEXTVAL,:0,:1,:2,:3,:4)
    '''
    cursor = conn.cursor()
    cursor.execute(sql,data)
    cursor.close()
    conn.commit()#잊지말자
    conn.close()

def viewDBTable(tableName):
    # 넘겨받은 테이블 명의 데이터를 화면에 출력
    conn = oci.connect('scott/tiger@127.0.01:1521/xe')
    sql = '''
    select * from {0}'''.format(tableName)
    cursor = conn.cursor()
    cursor.execute(sql)
    data = cursor.fetchall()
    for data in data:
        print(data)


    cursor.close()
    conn.close()


if __name__ == '__main__' :
    #테이블 생성
    #createDBTable()

    #2 입력확인
    # imsi = ['kosmo','9999','8888',1000,'2022-12-24']
    # saveDBTable(imsi)

    # 2-1 CSV 파일을 읽어서 -> db입력

    # file = open('supply.csv','r')# csv파일을 file 에 넣는다
    # data = csv.reader(file)# file을 읽은것을 data에 넣는다
    # #print(data)
    # hearder = next(data,None)
    # print(hearder)
    # print('-' * 50)
    #
    # for row in data:
    #     saveDBTable(row)

    #3 테이블내용 출력
    viewDBTable('supply')


























