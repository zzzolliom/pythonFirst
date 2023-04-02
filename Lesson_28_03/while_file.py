from Lesson_28_03.todays_func import login
from Lesson_28_03.todays_func import register


class Users():   #класс

	def __init__(self, u_login,u_password):
		self.u_login=login
		self.u_password=u_password



users_lst=[]
while True:
	test = Users()
	test.
	comand=input("Введите название команды login, all_users или register")
	if comand == "login":
		u_login = input("логин введите")
		login(u_login, users_lst)
	elif comand=="register":
		u_login = input("логин введите")
		u_password=input("пароль введите")
		if register(u_login,users_lst):
			new_user = Users()
			users_lst.append(new_user)
		else:
			print("имя занято")
