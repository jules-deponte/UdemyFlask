class Device:
    def __init__(self, name, conn_by):
        self.name = name
        self.conn_by = conn_by
        self.connected = True

    def __str__(self):
        return f'Device {self.name!r}, {self.conn_by}'

    def disconnect(self):
        self.connected = False
        print('Disconnected')


printer = Device('printer', 'USB')
print(printer)
printer.disconnect()

print('---------------------------------------------------')
# create a Printer class, which has all of the properties of the Device class, but with some Printer specific items.
class Printer(Device):

    def __init__(self, name, conn_by, capacity):
        # super().__init__() fetches the initialisations from the parent class.
        super().__init__(name, conn_by)
        self.capacity = capacity
        self.remaining_pages = capacity

    def __str__(self):
        return f'{super().__str__()} ({self.remaining_pages} pages remaining)'

    def print(self, pages):
        if self.connected == False:
            print('Printer is not connected')
            return
        self.remaining_pages = self.capacity - pages
        return f'Printing {pages} pages, remaining capacity: {self.remaining_pages}'
        

printer = Printer('printer', 'USB', 1000)
print(printer)
print(printer.print(20))
print(printer.print(60))
printer.disconnect()
print(printer.print(60))