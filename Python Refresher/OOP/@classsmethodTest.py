class Store:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, name, price):
        self.items.append({
            'name': name,
            'price': price
        })

    def stock_price(self):
        total = 0
        for item in self.items:
            total += item['price']
        return total

    @classmethod
    def franchise(cls, store):
        # Return another store, with the same name as the argument's name, plus " - franchise"
        return Store(store.name + ' - franchise')

    @staticmethod
    def store_details(store):
        # Return a string representing the argument
        # It should be in the format 'NAME, total stock price: TOTAL'
        string = ', total stock price: '
        return store.name + string + str(store.stock_price())

store = Store('Test')
store2 = Store('Amazon')
store2.add_item('keyboard', 160)

print(Store.franchise(store).name)
print(Store.franchise(store2).name)

print(Store.store_details(store))
print(Store.store_details(store2))