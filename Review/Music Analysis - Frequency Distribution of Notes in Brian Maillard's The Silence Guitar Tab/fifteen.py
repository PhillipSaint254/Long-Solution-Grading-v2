from fourteen import get_order

def get_string_order():
    order = get_order()
    return {cl: 6 - i for i, cl in enumerate(order[::-1])} 

if __name__ == "__main__":
    print(get_string_order())
