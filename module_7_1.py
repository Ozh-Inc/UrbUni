from pprint import pprint

class Product:
    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'
    def get_products(self):
        f = open(self.__file_name, 'r')
        d = f.read()
        f.close()
        return d
    def add(self, *products: Product):
        shop_list = self.get_products().splitlines()
        product_list = []
        for pi in shop_list:
            _ = pi.split(',')
            product_list.append(Product(_[0].strip(), float(_[1].strip()), _[2].strip()))
        for new_product in products:
            already_exists = False
            for existing_product in product_list:
                if new_product.name.lower() == existing_product.name.lower():
                    print(f'Продукт {new_product.name} уже есть в магазине.')
                    already_exists = True
                    existing_product.weight += new_product.weight
                    nv = ''
                    for v in product_list:
                        nv += str(v) + '\n'
                    a = open(self.__file_name, 'w')
                    a.write(nv)
                    a.close()
                    break
            if already_exists == False:
                e = open(self.__file_name, 'a')
                e.write(str(new_product) + '\n')
                e.close()

s = Shop()
s.add(Product('Carrot', 54.1, 'Vegetables'), Product('Clothing', 14.2, 'Necessities'), Product('Paper', 280.0, 'Office'))
print(s.get_products())