stock_prices = {
    "TSHIRT": 350,
    "BOTTOM JEANS": 700,
    "FORMAL PANT": 650,
    "SHIRT": 550,
    "JACKET": 800
}

portfolio = {}
total_investment = 0

print("📈 STOCK PORTFOLIO TRACKER")
print("Available Stocks:", ", ".join(stock_prices.keys()))

while True:
    stock_name = input("\nEnter stock name (or 'done' to finish): ").upper()

    if stock_name == "DONE":
        break

    if stock_name in stock_prices:
        quantity = int(input("Enter quantity: "))
        portfolio[stock_name] = quantity
    else:
        print("❌ Stock not available. Try again!")

print("\n========== PORTFOLIO SUMMARY ==========")

for stock, qty in portfolio.items():
    price = stock_prices[stock]
    value = price * qty
    total_investment += value
    print(f"{stock} : {qty} × ₹{price} = ₹{value}")

print("\n💰 Total Investment Value = ₹", total_investment)

with open("portfolio.txt", "w") as file:
    file.write("Stock Portfolio Summary\n")
    file.write("------------------------\n")
    for stock, qty in portfolio.items():
        file.write(f"{stock} - {qty}\n")
    file.write(f"\nTotal Investment = ₹{total_investment}")

print("\n✅ Portfolio saved successfully in 'portfolio.txt'")
