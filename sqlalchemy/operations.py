from sqlalchemy import delete, update, select

from create_table import users_table, engine


conn = engine.connect()


def insert_table(name, phone, email):
    ins = users_table.insert()

    new_user = ins.values(name=name,
                        phone=phone,
                        email=email)

    return conn.execute(new_user)

def select_table():
    sel = select([users_table])

    for row in sel.execute():
        print(row)

    return 0

def update_table(name, new_name):
    upd = update(users_table).where(users_table.c.name == name).values(name=new_name)

    result = conn.execute(upd)

    return print(result.rowcount)


def delete_table(name):
    dele = delete(users_table).where(users_table.c.name == name)

    result = conn.execute(dele)

    return print(result.rowcount)


insert_table('will', '234234234', 'will.com')



# def commit_close(func):
#     def commit(*args):
#         conn = connect('base.db')
#         cur = conn.cursor()
#         sql = func(*args)
#         cur.execute(sql)
#         conn.commit()
#         conn.close()
#     return commit
