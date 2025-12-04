import psycopg2
import csv

DB_CONFIG = {
    "dbname": "postgres",
    "user": "postgres",
    "password": "1234",
    "host": "localhost",
    "port": "5432"
}

def connect():
    return psycopg2.connect(**DB_CONFIG)


def insert_console():
    name =input("Введите имя: ")
    phone =input("Введите телефон: ")

    try:
        conn =connect()
        cur =conn.cursor()
        cur.execute("SELECT add_or_update_user(%s, %s);", (name,phone))
        conn.commit()
        print("Контакт добавлен или обновлён.")
    except Exception as e:
        print("Ошибка:",e)
    finally:
        cur.close()
        conn.close()


def insert_csv(file_path="contacts.csv"):
    try:
        names =[]
        phones =[]

        with open(file_path, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            next(reader)  # пропустить заголовок

            for row in reader:
                names.append(row[0])
                phones.append(row[1])

        conn =connect()
        cur =conn.cursor()

        cur.execute(
            "SELECT * FROM add_many_users(%s, %s);",
            (names,phones)
        )

        invalid = cur.fetchall()

        conn.commit()

        print("CSVзагружен!")

        if invalid:
            print("\nНекорректны строки:")
            for row in invalid:
                print(row)

    except Exception as e:
        print("Ошибка:",e)
    finally:
        cur.close()
        conn.close()

def update_contact():
    name = input("Имя контакта для обновления: ")
    new_phone = input("Новый телефон: ")

    try:
        conn = connect()
        cur = conn.cursor()
        cur.execute("SELECT add_or_update_user(%s,%s);",(name,new_phone))
        conn.commit()
        print("Контакт обновлён.")
    except Exception as e:
        print("Ошибка:",e)
    finally:
        cur.close()
        conn.close()


def query_contacts():
    pattern =input("Введите шаблон поиска (имя или телефон): ")

    try:
        conn =connect()
        cur =conn.cursor()

        cur.execute("SELECT * FROM search_contacts(%s);",(pattern,))
        rows =cur.fetchall()

        if rows:
            for r in rows:
                print(r)
        else:
            print("Ничего ненайдено.")
    except Exception as e:
        print("Ошибка:", e)
    finally:
        cur.close()
        conn.close()

def delete_contact():
    value = input("Имя или телефон для удаления: ")

    try:
        conn = connect()
        cur = conn.cursor()
        cur.execute("SELECT delete_contact(%s);", (value,))
        conn.commit()
        print("Контакт удалён.")
    except Exception as e:
        print("Ошибка:", e)
    finally:
        cur.close()
        conn.close()


def paginate():
    limit =int(input("Сколько записей вывести? "))
    offset =int(input("Сколько пропустить? "))

    try:
        conn = connect()
        cur = conn.cursor()
        cur.execute("SELECT * FROM get_contacts(%s, %s);", (limit, offset))
        rows = cur.fetchall()
        for row in rows:
            print(row)
    except Exception as e:
        print("Ошибка:", e)
    finally:
        cur.close()
        conn.close()
def menu():
    while True:
        print("""
========= PHONEBOOK =========
1. Добавить контакт
2. Загрузить контакты из CSV
3. Обновить контакт
4. Найти контакт
5. Удалить контакт
6. Пагинация (limit, offset)
7. Выйти
=============================
""")

        choice = input("Выбор:")

        if choice =="1":
            insert_console()
        elif choice=="2":
            insert_csv()
        elif choice =="3":
            update_contact()
        elif choice =="4":
            query_contacts()
        elif choice=="5":
            delete_contact()
        elif choice =="6":
            paginate()
        elif choice =="7":
            print("Выход...")
            break
        else:
            print("Неверный ввод.")

if __name__ == "__main__":
    menu()

