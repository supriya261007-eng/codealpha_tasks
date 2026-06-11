# Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 330,
    "AMZN": 145
}

portfolio = {}
total_value = 0

print("===== STOCK PORTFOLIO TRACKER =====")
print("Available Stocks:")
for stock, price in stock_prices.items():
    print(stock, ":", "$", price)

n = int(input("\nEnter the number of stocks you want to buy: "))

for i in range(n):
    stock_name = input("\nEnter stock symbol: ").upper()

    if stock_name in stock_prices:
        quantity = int(input("Enter quantity: "))
        portfolio[stock_name] = quantity
    else:
        print("Stock not available!")

print("\n===== PORTFOLIO SUMMARY =====")

result = ""

for stock, quantity in portfolio.items():
    value = stock_prices[stock] * quantity
    total_value += value

    line = f"{stock} : {quantity} shares × ${stock_prices[stock]} = ${value}"
    print(line)
    result += line + "\n"

print("\nTotal Investment Value = $", total_value)
result += "\nTotal Investment Value = $" + str(total_value)

# Save to text file
file = open("portfolio_summary.txt", "w")
file.write(result)
file.close()

print("\nPortfolio summary saved to 'portfolio_summary.txt'")