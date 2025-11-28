import psycopg2
import csv

DB_CONFIG = {
    "dbname":"postgres",
    "user":"postgres",
    "password":"1234",
    "host":"localhost",
    "port":"5432"
}
def connect():
    return psycopg2.connect(**DB_CONFIG)

def insert_console():
    name=input("Введите имя: ")
    phone=input("Введите телефон: ")
    try:
        conn =connect()
        cur =conn.cursor()
        cur.execute(
            "INSERT INTO phonebook (first_name,phone) VALUES (%s,%s)",
            (name,phone)
        )
        conn.commit()
        print("Контакт должен быть - добавлен")
    except Exception as e:
        print("Ошибка:", e)
    finally:
        cur.close()
        conn.close()
def insert_csv(file_path="contacts.csv"):
    try:
        conn=connect()
        cur=conn.cursor()
        with open(file_path,"r") as f:
            reader =csv.reader(f)
            next(reader)
            for row in reader:
                cur.execute(
                    "INSERT INTO phonebook (first_name,phone) VALUES (%s,%s)",
                    (row[0],row[1])
                )
        conn.commit()
        print("CSV загружен в базу")
    except Exception as e:
        print("Ошибка",e)
    finally:
        cur.close()
        conn.close()
def update_contact():
    phone = input("Телефон который нужно найти")
    new_name = input("Новое имя: ")
    new_phone = input("Новый телефон: ")

    try:
        conn =connect()
        cur =conn.cursor()
        if new_name:
            cur.execute(
                "UPDATE phonebook SET first_name=%s WHERE phone=%s",
                (new_name,phone)
            )
        if new_phone:
            cur.execute(
                "UPDATE phonebook SET phone=%s WHERE phone=%s",
                (new_phone,phone)
            )
        conn.commit()
        print("Контакт обновлён")
    except Exception as e:
        print("Ошибка:",e)
    finally:
        cur.close()
        conn.close()

def query_contacts():
    filter_name =input("Фильтр по имени: ")
    filter_phone =input("Фильтр по телефону: ")
    try:
        conn =connect()
        cur =conn.cursor()
        sql ="SELECT * FROM phonebook WHERE 1=1"
        params=[]
        if filter_name:
            sql +=" AND first_name ILIKE %s"
            params.append(f"%{filter_name}%")
        if filter_phone:
            sql +=" AND phone LIKE %s"
            params.append(f"%{filter_phone}%")
        cur.execute(sql, params)
        rows =cur.fetchall()
        if rows:
            for r in rows:
                print(r)
        else:
            print("Нетууу")
    except Exception as e:
        print("Ошибка:",e)
    finally:
        cur.close()
        conn.close()

def delete_contact():
    value =input("Имя или телефон: ")
    try:
        conn =connect()
        cur =conn.cursor()
        cur.execute(
            "DELETE FROM phonebook WHERE first_name=%s OR phone=%s",
            (value,value)
        )
        conn.commit()
        print("Контакт удалён")
    except Exception as e:
        print("Ошибка:",e)
    finally:
        cur.close()
        conn.close()

def menu():
    while True:
        print("""
1. Добавить контакт 
2. Загрузит контакты CSV файла
3. Поменять контакты
4. Найти контакт
5. Удалить контакт
6. Выйти
""")
        choice = input("Выбор: ")
        if choice=="1":
            insert_console()
        elif choice=="2":
            insert_csv()
        elif choice=="3":
            update_contact()
        elif choice=="4":
            query_contacts()
        elif choice=="5":
            delete_contact()
        elif choice=="6":
            break
        else:
            print("Не туда")

if __name__ == "__main__":
    menu()

