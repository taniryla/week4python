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


class IceCreamShop:
    def __init__(self, flavors):
        self.flavors = flavors
        self.orders = Queue()

    def take_order(self, customer, flavor, scoops):
        self.customer = customer
        self.scoops = scoops
        if flavor in self.flavors and scoops <= 3 and scoops >= 1:
            print("Order created!")
            order = {"customer": customer, "flavor": flavor, "scoops": scoops}
            return self.orders.enqueue(order)
        else:
            print("Sorry we don't have that flavor.")
            print("Choose between 1-3 scoops")

    def show_all_orders(self):
        self.orders = all
        for i in all:
            print(f"{all[i]}")

    def next_order(self):
        return self.orders.dequeue()


shop = IceCreamShop(["rocky road", "mint chip", "pistachio"])
shop.take_order("Zachary", "pistachio", 3)
shop.take_order("Marcy", "mint chip", 1)
shop.take_order("Leopold", "vanilla", 2)
shop.take_order("Bruce", "rocky road", 0)
shop.show_all_orders()
shop.next_order()
shop.show_all_orders()