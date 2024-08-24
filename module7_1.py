from pprint import pprint


class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"Название: {self.name}, Вес: {self.weight}, Категория: {self.category}"


class Shop:
    def __init__(self, file_name='products.txt'):
        self.__file_name = file_name

    def get_products(self):
        file = open(self.__file_name, 'r')    # открываем файл
        string = file.read()                  # читаем файл
        file.close()                          # закрываем файл
        return f"{string}"                      # печатаем строку

    def add(self, *string):
        file = open(self.__file_name, 'a')
        l = self.get_products()
        for i in string:
            if i.name not in l:
                file.write(str(i) + '\n')
                l += i.name + '\n'
            else:
                print(f'Продукт {i.name} уже есть в магазине.')
        file.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)

s1.add(p1, p2, p3)

s1.get_products()
