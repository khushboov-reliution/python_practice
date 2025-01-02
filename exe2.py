class Product():
    def __init__(self, name, code,price,category):
        self.name = name
        self.code = code
        self.price = price
        self.category = category

    def __str__(self):
        return f"Product Name is: {self.name} , Product Price is:{self.price},Product Code is:{self.code},Product Category is:{self.category}"

class Category():
    def __init__(self,name,code,parent=None):
        self.name = name
        self.code = code
        self.parent = parent
        self.products = []
        self.display_name = self.generate_display_name()
    #
    def __str__(self):
        return f"{self.display_name}(code:{self.code})"

    def generate_display_name(self):
            if self.parent is None:
                return self.name
            else:
                return f"{self.parent.display_name} > {self.name} "

cat1 = Category("Vehicle",311)
cat2 = Category("Car",312,parent=cat1)
cat3 = Category('Petrol',313,parent=cat1)
cat4 = Category('Bus',314,parent=cat3)
cat5 = Category('Bike',315,parent=cat4)


product_list = [Product('tv',123,1653,cat1),
Product('ac',123,1153,cat2),
Product('oven',123,1623,cat3),
Product('tv',123,1653,cat1),
Product('ac',123,1153,cat3),
Product('oven',123,1623,cat2),
Product('tv',123,1653,cat2),
Product('ac',123,1153,cat3),
Product('oven',123,1623,cat4),
Product('tv',123,1653,cat5),
Product('ac',123,1153,cat1),
Product('oven',123,1623,cat5),
Product('tv',123,1653,cat4),
Product('ac',123,1153,cat5),
Product('oven',123,1623,cat4)]

cat_obj=[cat1,cat2,cat3,cat4,cat5]
for category in cat_obj:
    print(category)
sorted_categories = sorted(cat_obj, key=lambda c: c.name)

for product in product_list:
    product.category.products.append(product)

for category in sorted_categories:
    print(f"Category: {category}")
    if category.products:
        for product in category.products:
            print(product)
    else:
        print("Not exist")
