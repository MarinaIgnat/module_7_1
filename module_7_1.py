#Режимы открытия файлов

class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop():
    __file_name = 'products.txt'

    def get_products(self):
        open(self.__file_name)
        self.__file_name.read()
        return f'{self.__file_name}'
        self.__file_name.close()


    def add(self, *products, name):
        self.products = products
        super.__init__(name)
        if name in self.products:
            return f'Продукт {name} уже есть в магазине.'
        else:
            self.__file_name.__add__(self.products)


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')    #Почему не выводятся р1, р2, р3?
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1)

print(s1.get_products())