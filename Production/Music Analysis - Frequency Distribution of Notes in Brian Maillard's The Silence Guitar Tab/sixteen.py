from fifteen import get_order

def get_string_order():
    return {cl: 6 - i for i, cl in enumerate(order[::-1])}  # Wait we need to map bottom to 6 etc?

if __name__ == "__main__":
    print(get_string_order())
