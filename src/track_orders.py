class TrackOrders:
    # aqui deve expor a quantidade de estoque
    def __init__(self):
        self.orders = list()
        self.customers = dict()
        self.allDishes = set()
        self.allDays = set()

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, customer, order, day):
        self.allDishes.add(order)
        self.allDays.add(day)
        self.orders.append({customer, order, day})

        if customer in self.customers.keys():
            self.customers[customer].append((order, day))
        else:
            self.customers[customer] = [(order, day)]

    def get_most_ordered_dish_per_customer(self, customer):
        all_order = self.customers[customer]
        most_ordered = all_order[0][0]
        dishes_frequency = dict()

        for dish, _ in all_order:
            if dish not in dishes_frequency:
                dishes_frequency[dish] = 1
            else:
                dishes_frequency[dish] += 1

            if dishes_frequency[dish] > dishes_frequency[most_ordered]:
                most_ordered = dish

        return most_ordered

    def get_never_ordered_per_customer(self, customer):
        all_order = self.customers[customer]
        all_ordered_from_customer = {
            dish for dish, _ in all_order
        }

        never_ordered = self.allDishes - all_ordered_from_customer
        return never_ordered

    def get_days_never_visited_per_customer(self, customer):
        pass

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
