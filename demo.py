class Category():
    def __init__(self, name, code):
        self.name = name
        self.code = code
        # self.products = []{len(self.products)}

    def __str__(self):
        num_products = sum(1 for product in products_list if product.category == self)
        return f"Category name: {self.name}, Code: {self.code}, Number of Products: {num_products}"

    # def add_product(self, element):
    #     self.products.append(element)
    #     self.no_of_product = len(self.products)
class Product():
    def __init__(self, name, code, category, price):
        self.name = name
        self.code = code
        self.category = category
        self.price = price

    def __str__(self):
        return f"Product name is: {self.name} , Product Price is:{self.price},product code is:{self.code}"

# def categories_ascending(categories):
#     return sorted(categories,key=lambda x: x.code)
#     # print(categories)
# categories_ascending()

#     n = len(categories)
#     for i in range(n):
#         for j in range(0, n-i-1):
#             if categories[j].code > categories[j+1].code:
#                 categories[j], categories[j+1] = categories[j+1], categories[j]


def products_ascending(products_list):
    # n = len(products)
    # for i in range(n):
    #     for j in range(0, n-i-1):
    #          if products[j].price > products[j+1].price:
    #             products[j], products[j+1] = products[j+1], products[j]
    products_list.sort(key=lambda x:x.price)



def products_descending(products_list):
    # n = len(products)
    # for i in range(n):
    #     for j in range(0, n-i-1):
    #         if products[j].price < products[j+1].price:
    #             products[j], products[j+1] = products[j+1], products[j]
    products_list.sort(key=lambda x:x.price,reverse=True)


obj1 = Category('abc', 121)
obj2 = Category('xyz', 101)
obj3 = Category('wxy', 213)


product_obj1 = Product('laptop', 121, obj1, 12515)
product_obj2 = Product('phone', 122, obj1, 33345)
product_obj3 = Product('tv', 123, obj2, 11145)
product_obj4 = Product('remote', 124, obj2, 12345)
product_obj5 = Product('headphone', 125, obj2, 22385)
product_obj6 = Product('washing_machine', 126, obj2, 12555)
product_obj7 = Product('ipad', 127, obj3, 23455)
product_obj8 = Product('oven', 128, obj1, 15445)
product_obj9 = Product('heater', 129, obj3, 13345)
product_obj10 = Product('refrigerator', 130, obj1, 16345)

# obj1.add_product(product_obj1)
# obj1.add_product(product_obj2)
# obj1.add_product(product_obj6)
# obj1.add_product(product_obj8)
# obj1.add_product(product_obj10)
#
# obj2.add_product(product_obj3)
# obj2.add_product(product_obj5)
#
# obj3.add_product(product_obj4)
# obj3.add_product(product_obj7)
# obj3.add_product(product_obj9)

products_list = [product_obj1, product_obj2, product_obj3, product_obj4, product_obj5, product_obj6, product_obj7, product_obj8, product_obj9, product_obj10]

categories = [obj1, obj2, obj3]
for category in categories:
    print(category)


products_ascending(products_list)
print("Products Ascending order:")
for i in products_list:
    print(i)

products_descending(products_list)
print("\nProducts Descending order:")
for j in products_list:
    print(j)

search_product =int(input("Enter code:"))
for product in [product_obj1, product_obj2, product_obj3, product_obj4, product_obj5, product_obj6, product_obj7, product_obj8, product_obj9, product_obj10]:
    if product.code == search_product:
        print("code is exist")
        print(product)
        break
else:
    print("code is not exist")
    print('test')
    print('hello')


# sp =int(input("enter value:"))
# value =[print("code is exist") if product.code == sp else print("code is not exist") for product in [product_obj1, product_obj2, product_obj3, product_obj4, product_obj5, product_obj6, product_obj7, product_obj8, product_obj9, product_obj10]]

