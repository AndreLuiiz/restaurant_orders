import csv


def analyze_log(path_to_file):
    data = get_log(path_to_file)

    all_dishes = {dish["order"] for dish in data}


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
