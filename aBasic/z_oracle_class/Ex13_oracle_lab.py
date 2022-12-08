#
# 0. DB에 저장할 테이블 생성

import cx_Oracle as oci
import csv
#연락처 입력 sql 구문
def insertdb(ins):# 입력받은 값을 인자로 받아온다
    print('insert')
    conn = oci.connect('scott/tiger@127.0.0.1:1521/xe')
    sql = '''
    INSERT INTO phone
    VALUES
    (:0,:1,:2,:3)
    '''
    cursor = conn.cursor()
    cursor.execute(sql,ins) # db에 sql 문장을 ins값을 넣어 실행시킨다
    cursor.close()
    conn.commit()  # 커밋 잊지말자
    conn.close()
    print('end insert')

def make_phone(): # phone 테이블 생성 구문
    conn = oci.connect('scott/tiger@127.0.0.1:1521/xe')
    sql = '''create table phone(
                name     varchar2(50),
                tel      varchar2(50) primary key,
                email    varchar2(300),
                addr     varchar2(500)
                )'''

    cursor = conn.cursor()
    try:
        cursor.execute(sql)
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

# 1. 사용자 입력 받아 확인
# 2. 모든 연락처 출력하기
# 3. 연락처 삭제하기
#


class Contact: #생성자
    def __init__(self, name, phone_number, email, addr):
        self.name=name
        self.phone_name=phone_number
        self.email=email
        self.addr=addr

    def print_info(self):
        print("이름:", self.name)
        print("전화번호:", self.phone_name)
        print("이메일:", self.email)
        print("주소;", self.addr)


def print_menu():# 실행출력구문
    print('1. 연락처 입력')
    print('2. 연락처 출력')
    print('3. 연락처 삭제')
    print('4. 종료')
    menu=input('메뉴선택:')
    return int(menu)

# (1)
# 이름, 전화번호, 이메일, 주소를 입력받아
# Contact 객체를 생성하고 DB 에 입력
def set_contact():
    name = input('이름은?')
    phone = input('전화번호는?')
    email = input('이메일은?')
    addr = input('주소는?')

    ins = [name,phone,email,addr]
    insertdb(ins)


def print_contact():
    # (2)
    #  테이블의 전체 레코드 출력
    conn = oci.connect('scott/tiger@127.0.0.1:1521/xe')
    sql='''
    select * from phone
    '''
    cursor =conn.cursor()# 연결을 통해 cursor객체를 가져옴
    cursor.execute(sql)#cursor를 통해 db에 sql문장을 실행한다
    data = cursor.fetchall()#data 객체에 db의 전체나열한 값들을 넣어 준다
    for data in data: # for 문을 통해 하나씩 추출한다
        print(data)   # 출력을한다


def delete_contact(name):
    # (3)
    # 해당이름과 같은 요소를 찾아서 삭제
    conn = oci.connect('scott/tiger@127.0.0.1:1521/xe')
    sql="""
    DELETE FROM phone
    WHERE NAME='{}' """.format(name)# 입력받은 이름을 넣기위해 format사용 오라클특성때매 "과 '을 구분지어 사용해줘야 인식함
    cursor = conn.cursor() # 연결을 통해 cursor 객체를 가져옴
    cursor.execute(sql) # cursor객체를 db에 전송한다
    cursor.close() # 전송닫기
    conn.commit()  # 커밋 잊지말자
    conn.close()   # 연결닫기

def run():
    while True:
        menu=print_menu()
        if menu==4:  # 종료를 선택하면
            break
        elif menu==1: # 입력을 선택하면
            set_contact()
        elif menu==2: # 출력을 선택하면
            print_contact()
        elif menu==3: # 삭제를 선택하면
            name = input('삭제할 이름은?')
            delete_contact(name)


if __name__ == "__main__":
    run()
