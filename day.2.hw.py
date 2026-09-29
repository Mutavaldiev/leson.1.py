# test 1

# a = int(input())
# b = int(input())
# try:
#     print(f"result: {a/b}")
# except ValueError:
#     print("Please enter valid integers")
# except ZeroDivisionError:
#     print("Division by zero is not allowed")
# finally:
#     print("Calculation finished")


# test 2



# cities = ['Dushanbe', 'Khujand', 'Bokhtar']
# try:
#     index = int(input())
#     print(cities[index])

# except ValueError:
#     print("Invalid position")

# except IndexError:
#     print("Position does not exist")


# test 3




# prices = {
#     'mouse': 100,
#     'keyboard': 250,
#     'monitor': 1200
# }

# try:
#     product = input()
#     quantity = int(input())
#     price = prices[product]
#     total = price * quantity
#     print(f"Total: {total}")

# except KeyError:
#     print("Product not found")

# except ValueError:
#     print("Invalid quantity")



# test 4







# a = input().split()
# def calculate_average(values):
#     try:
#         for i in range(len(values)):
#             values[i]=int(values[i])
#         print(f"Averege {sum(values)/len(values)}")
#     except ValueError:
#         print("Enter Number")
#     except ZeroDivisionError:
#         print("ZeroDivisionError")
#     except Exception as error:
#         print(error)
# calculate_average(a)



# test 5





# test 6




# test 7





def process_payment(balance, amount):
    if amount <= 0:
        raise ("Payment amount must be positive")
    elif amount > balance:
        return "InsufficientFundsError"
    return balance - amount
balance = 1000
amount = 250

try:
    new_balance = process_payment(balance, amount)
except ValueError as e:
    print(e)

else:
    print(f"New balance: {new_balance}")
finally:
    print("Payment attempt finished")



# test 8



# def price_per_item(total, quantity):
#     return total / quantity


# def build_report(order):
#     return price_per_item(order["total"], order["quantity"])


# def main():
#     order = {"total": 600, "quantity": 3}
#     print(build_report(order))


# main()



# test 9



# def line_total(price, quantity):
#     return price * quantity


# def cart_total(items):
#     total = 0
#     for index, item in enumerate(items):
#         price = item["price"]
#         quantity = item["quantity"]
#         total += line_total(price, quantity)
#     return total


# cart = [
#     {"name": "Mouse", "price": 100, "quantity": 2},
#     {"name": "Keyboard", "price": 250, "quantity": 1},
#     {"name": "Cable", "price": 30, "quantity": 3},
# ]
# print(cart_total(cart))



# test 10



# from datetime import datetime


# def parse_date(text):
#     return datetime.strptime(text, "%d.%m.%Y")


# text = input()
# print(parse_date(text).strftime("%Y-%m-%d"))
