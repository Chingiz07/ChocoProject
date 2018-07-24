import sqlite3, down_att, config

name = down_att.attachment_dir + '/' + 'Kaspi17.04.2018.xls'

def create_table():
    conn = sqlite3.connect('Matahari.db')
    c = conn.cursor()
    try:
        c.execute('''CREATE TABLE PayTrans (id integer PRIMARY KEY AUTOINCREMENT NOT NULL , payment_system VARCHAR, date VARCHAR, order_ID varchar)''')
    except:
        pass

    conn.commit()
    conn.close()

create_table()

date, order_ID = config.kaspi(name)
payment_system = 'Kaspi'

def update_table(date, order_ID, payment_system):
    conn = sqlite3.connect('Matahari.db')
    c = conn.cursor()
    for i in range(len(date)):
        c.execute("INSERT INTO PayTrans (payment_system ,date, order_ID) VALUES ('{}', '{}', '{}')".format(payment_system, date[i].date(), order_ID[i]))
    conn.commit()
    conn.close()


update_table(date, order_ID, payment_system)