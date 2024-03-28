from sqlite3 import connect


class Database:
    @staticmethod
    def insert(name, family,nationalcode, birthday, image):
        try:
            my_con = connect('personeli.db')
            my_cursor = my_con.cursor()
            my_cursor.execute(f"INSERT INTO personeli_info(name, family, birthday, national_code,image)"
                              f"VALUES('{name}','{family}','{birthday}','{nationalcode}','{image}.jpg')")
            my_con.commit()
            my_con.close()
            return True
        except Exception as e:
            print("error:", e)
            return False

    @staticmethod
    def select():
        print('in select func')
        try:
            my_con = connect('personeli.db')
            my_cursor = my_con.cursor()
            my_cursor.execute("SELECT * FROM personeli_info")
            result = my_cursor.fetchall()
            my_con.close()
            return result
        except Exception as e:
            print("error:", e)
            return []

    @staticmethod
    def delete(id):
        try:
            my_con = connect('personeli.db')
            my_cursor = my_con.cursor()
            my_cursor.execute(f"DELETE FROM personeli_info WHERE ID = {id}")
            my_con.commit()
            my_con.close()
            return True

        except Exception as e:
            print("error:", e)
            return False