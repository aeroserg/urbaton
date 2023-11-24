import random


def generate_login(first_name, last_name):
    cleaned_first_name = first_name.lower().replace(" ", "")
    cleaned_last_name = last_name.lower().replace(" ", "")

    random_number_1 = random.randint(1000, 9999)
    random_number_2 = random.randint(1000, 9999)

    login = f"{cleaned_first_name}_{random_number_1}_{cleaned_last_name}_{random_number_2}"

    return login
