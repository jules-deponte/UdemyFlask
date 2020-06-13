class Store:
    def __init__(self, name):
        self.name = name
        self.items = []
    
    def add_item(self, name, price):
        self.items.append({'name':name, 'price':price})
        print(self.items)

    def stock_price(self):
        total = 0
        total += sum(item['price'] for item in self.items)
        return total
        # for item in self.items:
        #     total += item['price']

        # return total

store = Store('Jhb')

items = {'name':"bread", 'price':15 }
store.add_item(**items)

print(store.stock_price())