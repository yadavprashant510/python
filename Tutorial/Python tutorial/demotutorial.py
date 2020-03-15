from random import choice

customers = ['Larry', 'Alice', 'Sam']


def main():
    for i in range(10):
        customer = choice(customers)
        print(customer)
    return customer  # last one


if __name__ == '__main__':
    main()
