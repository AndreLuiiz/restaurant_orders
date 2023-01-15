import csv


def analyze_log(path_to_file):
    data = get_log(path_to_file)

    all_dishes = {dish["order"] for dish in data}

    maria_most_requested = most_requested_dish("maria", all_dishes, data)
    arnaldo_hamburger = how_many_times_asked(
        "arnaldo", all_dishes, data, "hamburguer")
    joao_not_asked = not_asked_dishes("joao", all_dishes, data)
    joao_not_gone = days_not_gone("joao", data)

    result = (
        f"{maria_most_requested}\n"
        f"{arnaldo_hamburger}\n"
        f"{joao_not_asked}\n"
        f"{joao_not_gone}\n"
    )
    with open("data/mkt_campaign.txt", "w") as file:
        file.write(result)


def get_log(path_to_file):
    if not path_to_file.endswith(".csv"):
        raise FileNotFoundError(f"Extensão inválida: '{path_to_file}'")

    try:
        with open(path_to_file, "r") as file:
            data = csv.DictReader(file, fieldnames=["client", "order", "day"])

            log_data = []
            for row in data:
                log_data.append(row)
    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo inexistente: '{path_to_file}'")

    return log_data


def get_all_orders_from(person: str, dishes: set, data: list):
    all_order = {}
    for dish in dishes:
        all_order[dish] = 0

    for log in data:
        if log["client"] == person:
            all_order[log["order"]] += 1

    return all_order


def most_requested_dish(person, dishes, data):
    all_orders = get_all_orders_from(person, dishes, data)

    for key, value in all_orders.items():
        if value == sorted(all_orders.values())[-1]:
            most_requested = key

    return most_requested


def how_many_times_asked(person, dishes, data, dish):
    all_orders = get_all_orders_from(person, dishes, data)

    return all_orders[dish]


def not_asked_dishes(person, dishes, data):
    all_orders = get_all_orders_from(person, dishes, data)
    not_asked = set()

    for key, value in all_orders.items():
        if value == 0:
            not_asked.add(key)

    return not_asked


def days_not_gone(person, data):
    not_gone = set()
    days_count = week_day_counter(data)

    for log in data:
        if log["client"] == person:
            days_count[log["day"]] += 1

    for key, value in days_count.items():
        if value == 0:
            not_gone.add(key)

    return not_gone


def week_day_counter(data):
    all_week_days = {log["day"] for log in data}

    days_count = {}
    for day in all_week_days:
        days_count[day] = 0
    return days_count
