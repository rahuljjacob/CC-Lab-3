
from cart import dao
from products import Product


class Cart:
    def __init__(self, id: int, username: str, contents: list[Product], cost: float):
        self.id = id
        self.username = username
        self.contents = contents
        self.cost = cost

    def load(data):
        return Cart(data['id'], data['username'], data['contents'], data['cost'])

def get_cart(username: str) -> list: 
    conn = connect('carts.db') 
    cursor = conn.cursor() 
    if not cursor: 
        return [] 
    cursor.execute('SELECT * FROM carts WHERE username = ?', (username,)) 
    final_cart = cursor.fetchall() 
    cursor.close() 
    conn.close() 
    return final_cart



def add_to_cart(username: str, product_id: int):
    dao.add_to_cart(username, product_id)


def remove_from_cart(username: str, product_id: int):
    dao.remove_from_cart(username, product_id)

def delete_cart(username: str):
    dao.delete_cart(username)


