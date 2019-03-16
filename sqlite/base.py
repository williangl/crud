from sqlite3 import connect


conn = connect('base.db')
cur = conn.cursor()


def commit_close(func):
    def commit(*args):
        conn = connect('base.db')
        cur = conn.cursor()
        sql = func(*args)
        cur.execute(sql)
        conn.commit()
        conn.close()
    return commit


def create_table():
    sql = """
        CREATE TABLE users (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    phone TEXT NOT NULL,
                    email TEXT UNIQUE NOT NULL)"""
    cur.execute(sql)
    return conn.commit()


@commit_close
def insert_table(name, phone, email):
    return f"""
        INSERT INTO users(name, phone, email)
        VALUES('{name}', '{phone}', '{email}')"""


@commit_close
def update_table(name, email):
    return f"""
        UPDATE users SET name = '{name}' WHERE email = '{email}'
        """


@commit_close
def delete_table(email):
    return f"""
        DELETE FROM users WHERE email = '{email}'
        """


def select_table(field, data):
    conn = connect('base.db')
    cur = conn.cursor()
    sql = f"""
        SELECT id, name, phone, email FROM users WHERE {field}={data}
        """
    cur.execute(sql)
    data = cur.fetchall()
    conn.close()

    return data


conn.close()
