def get_pet_shop_name(shop):
    return shop["name"]

def get_total_cash(shop):
    return shop["admin"]["total_cash"]

def add_or_remove_cash(shop, amount):
    shop["admin"]["total_cash"] += amount

def get_pets_sold(shop):
    return shop["admin"]["pets_sold"]

def increase_pets_sold(shop, adding_amount):
    shop["admin"]["pets_sold"] += adding_amount

def get_stock_count(shop):
    return len(shop["pets"])

def get_pets_by_breed(shop, breed):
    pets_from_desired_breed = []

    for pet in shop["pets"]:
        if pet["breed"] == breed:
            pets_from_desired_breed.append(pet)

    return pets_from_desired_breed

def find_pet_by_name(shop, pet_name):
    for pet in shop["pets"]:
        if pet["name"] == pet_name:
            return pet

def remove_pet_by_name(shop, pet_name):
    pet_to_remove = find_pet_by_name(shop, pet_name)
    shop["pets"].remove(pet_to_remove)

def add_pet_to_stock(shop, pet_data):
    shop["pets"].append(pet_data)

def get_customer_cash(customer):
    return customer["cash"]

def remove_customer_cash(customer, amount):
    customer["cash"] -= amount