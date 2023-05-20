import os

import psycopg2
import psycopg2.extras


class Connection:
    def __init__(self, user=os.environ['user_db'], password=os.environ['password'], host=os.environ['host'],
                 database=os.environ['database']):
        self.__user = user
        self.__password = password
        self.__host = host
        self.__database = database

    def __con_postgresql(self):
        """
        Функция подключения к бд PostgreSQL.
        """
        conn_data = f"postgres://{self.__user}:{self.__password}@{self.__host}/{self.__database}"
        return psycopg2.connect(conn_data)

    def sql_query(self, current_query, flag_back=False, dict_flag=False):
        """
        Функция для отправки запроса в бд.
        Флаг flag_back отвечает за данные, которые должен вернуть запрос.
        """
        connection = self.__con_postgresql()
        if dict_flag:
            cur_postgresql = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        else:
            cur_postgresql = connection.cursor()
        self.__result = None
        cur_postgresql.execute(current_query)
        connection.commit()
        if flag_back:
            self.__result = cur_postgresql.fetchall()
        cur_postgresql.close()
        connection.close()
        return self.__result

