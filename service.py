items = []
id_counter = 1

def reset_data():
    global items, id_counter
    items = []
    id_counter = 1

def create_item(name, stock, price):
    global id_counter

    if not name:
        return None, "Name required"
    if stock < 0:
        return None, "Stock invalid"
    if price <= 0:
        return None, "Price invalid"

    item = {"id": id_counter, "name": name, "stock": stock, "price": price}
    id_counter += 1
    items.append(item)
    return item, None

def get_items():
    return items

def update_item(id, stock):
    item = next((i for i in items if i["id"] == id), None)
    if not item:
        return None, "Not found"
    if stock < 0:
        return None, "Invalid stock"

    item["stock"] = stock
    return item, None

def delete_item(id):
    global items
    item = next((i for i in items if i["id"] == id), None)
    if not item:
        return False, "Not found"

    items = [i for i in items if i["id"] != id]
    return True, None