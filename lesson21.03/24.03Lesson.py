class Soda():   #класс

	def __init__(self, ingredient='сахар'):

		if isinstance(ingredient, str) == False:
			self.ingredient = None
		else:
			self.ingredient = ingredient

	def show_my_drink(self):
		if self.ingredient is not None:
			print("Газировка и", self.ingredient)
		else:
			print("Обычная газировка")
class NoSuga(Soda):

	def __init__(self,ingredient,sugar=0):
		super().__init__(ingredient)
		self.sugar=sugar
	def is_suga(self):
		if self.sugar<1:
			print(f"Без сахара количество сахара {self.sugar}")
		else:
			print(f"С сахаром количество сахара {self.sugar}")

my_drink =  Soda("кола")  #-объект
my_diet_drink=NoSuga("сахар")
my_diet_drink.show_my_drink()
my_diet_drink.is_suga()



#Написать классс Soda для определения типа газированной воды .Этот класс принимает 1 аргумент при инициализации
#аргумент отвечает за добавку к выбранному лимонаду
#в этом класс написать метод show_my_drink(), который выводит на печать "Газировка и {ДОБАВКА} если есть
# иначе отображается фраза "Обычная газировка"
# в методе init проверить что ингридиент str через instance и если не соотв то присвоить значение None
# is_sugar
