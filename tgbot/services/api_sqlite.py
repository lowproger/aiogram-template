# - *- coding: utf- 8 - *-
import sqlite3

conn = sqlite3.connect("main.db")
cur = conn.cursor()


# Получение информации о юзере
def get_info(user_id):
	result = cur.execute(f'''SELECT * FROM users WHERE id = "{user_id}"''').fetchone()
	return result


# Проверка, есть ли юзер в бд
def get_reg(user_id):
	result = cur.execute(f'''SELECT * FROM users WHERE id = "{user_id}"''').fetchall()
	return bool(len(result))


# Регистрация юзера
def reg_user(user_id, username):
	data = user_id, username, 0, ""
	cur.execute(
		"INSERT INTO users VALUES(?,?, ?, ?)",
		data)
	conn.commit()


# Создание всех таблиц для БД
def create_dbx():
	dd = 1
	if dd == 1:
		# Создание БД с хранением данных пользователей
		if len(cur.execute("PRAGMA table_info(users)").fetchall()) == 4:
			print("DB was found")
		else:
			cur.execute("CREATE TABLE users("
						"id INTEGER,"
						"username INTEGER,"
						"money TEXT,"
						"links TEXT"
						")")
			print("DB was not found | Creating...")
