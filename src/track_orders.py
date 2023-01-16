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
        self.orders.append((customer, order, day))

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
        all_order = self.customers[customer]
        days_gone = {
            day for _, day in all_order
        }

        never_visited = self.allDays - days_gone
        return never_visited

    def get_busiest_day(self):
        busiest_day = self.orders[0][2]
        day_frequency = dict()

        for _, _, day in self.orders:
            if day not in day_frequency:
                day_frequency[day] = 1
            else:
                day_frequency[day] += 1

            if day_frequency[day] > day_frequency[busiest_day]:
                busiest_day = day

        return busiest_day

    def get_least_busy_day(self):
        least_busy_day = self.orders[0][2]
        day_frequency = dict()

        for _, _, day in self.orders:
            if day not in day_frequency:
                day_frequency[day] = 1
            else:
                day_frequency[day] += 1

            if day_frequency[day] < day_frequency[least_busy_day]:
                least_busy_day = day

        return least_busy_day
