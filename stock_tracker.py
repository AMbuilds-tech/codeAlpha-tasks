"""
Stock Portfolio Tracker
------------------------
Calculates total investment value based on hardcoded stock prices
and user-entered quantities. Optionally saves the result to a CSV file.
"""

import csv
from datetime import datetime

# Hardcoded stock prices (in USD)
STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 410,
    "AMZN": 185,
    "NVDA": 120,
}


def show_available_stocks():
    print("\nAvailable stocks and prices:")
    for symbol, price in STOCK_PRICES.items():
        print(f"  {symbol:<6} ${price}")
    print()


def get_portfolio_from_user():
    """Collects stock symbols and quantities from the user."""
    portfolio = {}

    print("Enter stock symbol and quantity (e.g. AAPL 10).")
    print("Type 'done' when finished.\n")

    while True:
        entry = input("Stock (or 'done'): ").strip()

        if entry.lower() == "done":
            break

        parts = entry.split()

        if len(parts) != 2:
            print("  Please enter in the format: SYMBOL QUANTITY (e.g. AAPL 10)")
            continue

        symbol, qty_str = parts[0].upper(), parts[1]

        if symbol not in STOCK_PRICES:
            print(f"  '{symbol}' not found in price list. Try one of: {', '.join(STOCK_PRICES)}")
            continue

        try:
            qty = float(qty_str)
            if qty <= 0:
                raise ValueError
        except ValueError:
            print("  Quantity must be a positive number.")
            continue

        portfolio[symbol] = portfolio.get(symbol, 0) + qty
        print(f"  Added {qty} share(s) of {symbol}.\n")

    return portfolio


def calculate_investment(portfolio):
    """Returns a breakdown list and the total investment value."""
    breakdown = []
    total = 0.0

    for symbol, qty in portfolio.items():
        price = STOCK_PRICES[symbol]
        value = price * qty
        total += value
        breakdown.append({
            "symbol": symbol,
            "quantity": qty,
            "price": price,
            "value": value
        })

    return breakdown, total


def display_summary(breakdown, total):
    print("\n---- Portfolio Summary ----")
    print(f"{'Symbol':<8}{'Qty':<8}{'Price':<10}{'Value':<10}")
    for item in breakdown:
        print(f"{item['symbol']:<8}{item['quantity']:<8}{item['price']:<10}${item['value']:<10.2f}")
    print("-" * 34)
    print(f"Total Investment Value: ${total:.2f}\n")


def save_to_csv(breakdown, total, filename=None):
    if filename is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"portfolio_{timestamp}.csv"

    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Symbol", "Quantity", "Price", "Value"])
        for item in breakdown:
            writer.writerow([item["symbol"], item["quantity"], item["price"], f"{item['value']:.2f}"])
        writer.writerow([])
        writer.writerow(["Total Investment Value", "", "", f"{total:.2f}"])

    print(f"Saved portfolio summary to '{filename}'")


def main():
    print("=== Stock Portfolio Tracker ===")
    show_available_stocks()

    portfolio = get_portfolio_from_user()

    if not portfolio:
        print("No stocks entered. Exiting.")
        return

    breakdown, total = calculate_investment(portfolio)
    display_summary(breakdown, total)

    choice = input("Save this summary to a CSV file? (y/n): ").strip().lower()
    if choice == "y":
        custom_name = input("Enter filename (leave blank for auto-generated name): ").strip()
        save_to_csv(breakdown, total, custom_name if custom_name else None)


if __name__ == "__main__":
    main()
