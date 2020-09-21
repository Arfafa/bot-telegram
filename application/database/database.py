import os
import sqlite3


DIR_SEP = os.path.sep
DATABASE_PATH = 'application{sep}database{sep}'.format(sep=DIR_SEP)


class Database:
    def __init__(self, name):
        self.name = DATABASE_PATH + name

        self.create_tables()

    def __str__(self):
        return self.name.split(DIR_SEP)[-1]

    def create_tables(self):
        conn = sqlite3.connect(self.name)
        cursor = conn.cursor()

        cursor.execute('''create table if not exists users
                          (id integer,
                           name text,
                           is_bot integer check (is_bot in (0, 1)),
                           language_code text,
                           username text,
                           unique(id))''')

        cursor.execute('''create table if not exists messages
                          (id integer,
                           date integer,
                           text text,
                           user_id integer,
                           foreign key (user_id) references users(id),
                           unique(id))''')

        conn.commit()
        conn.close()

    def insert_user(self, *args):
        conn = sqlite3.connect(self.name)
        cursor = conn.cursor()

        cursor.execute('''insert or ignore into users
                          (id, name, is_bot, language_code, username) values
                          (?, ?, ?, ?, ?)''', args)

        conn.commit()
        conn.close()

    def insert_message(self, *args, **kwargs):
        conn = sqlite3.connect(self.name)
        cursor = conn.cursor()

        conn.execute('pragma foreign_keys = 1')

        cursor.execute('''replace into messages
                          (id, date, text, user_id)
                          values (?, ?, ?, ?)''', args)

        conn.commit()
        conn.close()

    def insert_information(self, data):
        self.create_tables()

        name = data['message']['from']['first_name']

        is_bot = int(data['message']['from']['is_bot'])
        language_code = data['message']['from']['language_code']
        username = data['message']['from']['username']
        user_id = data['message']['from']['id']

        self.insert_user(user_id, name, is_bot, language_code, username)

        message_id = data['message']['message_id']
        date = data['message']['date']
        text = data['message']['text']

        self.insert_message(message_id, date, text, user_id)
