class Queue:
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.size() == 0:  # if nothing is in the queue
            return None
        return self.items.pop(0)

    def show_queue(self):
        print(self.items)


class IceCreamShop(Queue):
    def __init__(self, flavors):
        self.flavors = flavors
        self.orders = Queue()  # create a queue for the flavor request

    def take_order(self, customer, flavor, scoops):
        self.customer = customer
        self.scoops = scoops
        if flavor in self.flavors and scoops in range(1, 4):
            print("Order created!")
            order = {"customer": customer, "flavor": flavor, "scoops": scoops}
            self.orders.enqueue(order)
        elif (flavor not in self.flavors):
            print("Sorry we don't have that flavor.")
        elif (scoops not in range(1, 4)):
            print("Choose between 1-3 scoops")

    def show_all_orders(self):
        print("\nAll Pending Ice Orders:")
        for i in self.orders.items:
            print("Customer:", i["customer"], "--", "Flavor:",
                  i["flavor"], "--", "Scoops:", i["scoops"])

    def next_order(self):
        print("\nNext Oder Up!")
        next = self.orders.dequeue()
        print("Customer:", next["customer"], "--", "Flavor:",
              next["flavor"], "--", "Scoops:", next["scoops"])


shop = IceCreamShop(["rocky road", "mint chip", "pistachio"])
shop.take_order("Zachary", "pistachio", 3)
shop.take_order("Marcy", "mint chip", 1)
shop.take_order("Leopold", "vanilla", 2)
shop.take_order("Bruce", "rocky road", 0)
shop.show_all_orders()
shop.next_order()
shop.show_all_orders()
