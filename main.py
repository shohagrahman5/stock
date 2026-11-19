# Stock prices are sample values in USD.
# They are manually defined for this beginner project.
STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420,
    "AMZN": 190
}


def get_positive_quantity():
    """Ask for a positive whole-number quantity."""
    while True:
        value = input("Enter quantity: ").strip()
        try:
            quantity = int(value)
            if quantity > 0:
                return quantity
            print("Quantity must be greater than zero.")
        except ValueError:
            print("Please enter a whole number, such as 2.")


def save_report(holdings, total):
    """Save the portfolio details to a text file."""
    with open("portfolio_report.txt", "w", encoding="utf-8") as file:
        file.write("STOCK PORTFOLIO REPORT\n")
        file.write("======================\n")
        for stock, quantity, price, value in holdings:
            file.write(
                f"{stock}: {quantity} shares x ${price} = ${value:.2f}\n"
            )
        file.write("----------------------\n")
        file.write(f"Total investment: ${total:.2f}\n")

    print("\nReport saved as portfolio_report.txt")


def main():
    holdings = []
    total_investment = 0.0

    print("===== STOCK PORTFOLIO TRACKER =====")
    print("Available stocks and sample prices (USD):")
    for stock, price in STOCK_PRICES.items():
        print(f"{stock}: ${price}")

    print("\nEnter the stocks you own.")
    print("Type DONE when you have finished.\n")

    while True:
        stock = input("Enter stock symbol: ").upper().strip()

        if stock == "DONE":
            break

        if stock not in STOCK_PRICES:
            print("Stock not found. Choose a symbol from the list.")
            continue

        quantity = get_positive_quantity()
        price = STOCK_PRICES[stock]
        investment_value = price * quantity

        holdings.append((stock, quantity, price, investment_value))
        total_investment += investment_value

        print(f"{stock} investment value: ${investment_value:.2f}\n")

    if not holdings:
        print("\nNo stocks were added. No report was created.")
        return

    print("\n===== YOUR PORTFOLIO =====")
    for stock, quantity, price, value in holdings:
        print(f"{stock}: {quantity} shares x ${price} = ${value:.2f}")

    print("--------------------------")
    print(f"Total investment: ${total_investment:.2f}")

    save_choice = input("\nSave this report? (yes/no): ").lower().strip()
    if save_choice in ("yes", "y"):
        save_report(holdings, total_investment)

    print("\nThank you for using Stock Portfolio Tracker!")


if __name__ == "__main__":
    main()
