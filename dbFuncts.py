import psycopg2


def create_db():
    conn = psycopg2.connect(database='postgres', user='postgres', password='122666', host='127.0.0.1')
    conn.autocommit = True
    cursor = conn.cursor()
    sql = """CREATE database mydb"""
    cursor.execute(sql)
    print("Awesome sauce!")
    conn.close()


def create_table():
    conn = psycopg2.connect(database="postgres", user='postgres', password='122666', host='127.0.0.1')
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS EMPLOYEE;")
    sql = '''create table employee (first_name varchar(20) not null , 
        last_name varchar(20), 
        age int , sex char(1), 
        income float);'''
    cursor.execute(sql)
    print("Success!")
    conn.commit
    conn.close
