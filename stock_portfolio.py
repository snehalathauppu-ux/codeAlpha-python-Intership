
print("Welcome to Stock Portfolio Tracker")

stocks = []

n = int(input("Enter number of stocks: "))

for i in range(n):
    print("\nStock", i + 1)

    name = input("Enter stock name: ")
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price per share: "))

    total = quantity * price

    stocks.append([name, quantity, price, total])

print("\n----- STOCK PORTFOLIO -----")

grand_total = 0

for stock in stocks:
    print("Stock Name:", stock[0])
    print("Quantity:", stock[1])
    print("Price:", stock[2])
    print("Total Value:", stock[3])

    grand_total += stock[3]

print("\nTotal Investment Value:", grand_total)
