import sqlite3




def create_form(user):
    try:
        conn = sqlite3.connect('nitindatabase.db')
        cur = conn.cursor()
        table_name = user + "_table"
        amount_table_name = user + "_table_amount"
        print(table_name)
        cur.execute(
            f"CREATE TABLE IF NOT EXISTS {table_name}(id integer primary key autoincrement , whattime date, shop text, item text, price double)"
        )
        cur.execute(
            f"CREATE TABLE IF NOT EXISTS {amount_table_name}(id integer primary key autoincrement , total_amount double, total_consumed double)"
        )
        print("Created table successfully")
        conn.commit()
        conn.close()
        return True
    except:
        return False
        print("not able to connect database")


def save(whattime,user,item,shop,price):
    try:
        conn = sqlite3.connect('nitindatabase.db')
        cur = conn.cursor()
        table_name = user + "_table"
        # print(table_name)

        main_query = f"INSERT INTO {table_name}(whattime,shop,item,price) VALUES (?, ?, ?,?);"

        cur.execute(main_query,(whattime,shop,item,price))


        print("Inserted successfully")
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print(e)
        return False



def save_amount(user,total_money,total_consumed):
    try:
        conn = sqlite3.connect('nitindatabase.db')
        cur = conn.cursor()
        amount_table_name = user + "_table_amount"
        # print(table_name)

        main_query = f"INSERT INTO {amount_table_name}(total_amount,total_consumed) VALUES (?,?);"

        cur.execute(main_query,(total_money,total_consumed))


        print("Inserted successfully")
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print(e)
        return False



def update_amount(user,total_money, consuemd_money):
    try:
        conn = sqlite3.connect('nitindatabase.db')
        cur = conn.cursor()
        amount_table_name = user + "_table_amount"
        # print(table_name)

        main_query = f"UPDATE {amount_table_name} SET total_amount = ? , total_consumed = ? where id = ?;"

        cur.execute(main_query,(total_money,consuemd_money,1))


        print("Inserted successfully")
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print(e)
        return False


def get_amount(user):
    try:
        conn = sqlite3.connect('nitindatabase.db')
        cur = conn.cursor()
        amount_table_name = user + "_table_amount"
        # print(table_name)
        cur.execute(
            f"SELECT * FROM {amount_table_name}"
        )
        val = cur.fetchall()
        conn.commit()
        conn.close()
        print("fetch the data")
        print(val[0])
        return val[0]

    except Exception as e:
        print(e)
        return False



def get_data(user):
    try:
        conn = sqlite3.connect('nitindatabase.db')
        cur = conn.cursor()
        table_name = user + "_table"
        print(table_name)
        cur.execute(
            f"SELECT * FROM {table_name}"
        )
        val = cur.fetchall()
        conn.commit()
        conn.close()
        print("fetch the data")
        return val

    except Exception as e:
        print(e)
        return False



def clear_data(user):
    try:
        conn = sqlite3.connect('nitindatabase.db')
        cur = conn.cursor()
        table_name = user + "_table"
        print(table_name)
        cur.execute(
            f"DELETE FROM {table_name}"
        )
        val = cur.fetchall()
        conn.commit()
        conn.close()
        print("Clear the data")
        return val

    except Exception as e:
        print(e)
        return False









if __name__ == "__main__":
    pass
    # create_form("abc")
    # save('2020-02-20', "abc","dsf", "fdf", 322342341.32)

    print(get_data("abc"))

