# ============================================================
# FINANCIAL MATHEMATICS
# CHAPTER 1: BASIC FINANCE
# TOPIC: INFLATION
#
# Case Study:
# Calculating Future Prices and Inflation-Adjusted Returns
# ============================================================

import pandas as pd
import matplotlib.pyplot as plt


# ------------------------------------------------------------
# 1. INPUT DATA
# ------------------------------------------------------------

# Current price of an item in Birr
initial_item_price = 100

# Annual inflation rate (25%)
annual_inflation_rate = 0.25

# Investment's annual nominal rate of return (12%)
annual_nominal_return = 0.12

# Annual inflation rate for the investment example (6%)
investment_inflation_rate = 0.06

# Future payment amount in Birr
future_payment = 10000

# Different payment periods in months
payment_periods_months = [1, 2, 6, 12]


# ------------------------------------------------------------
# 2. CALCULATE FUTURE PRICE UNDER INFLATION
# ------------------------------------------------------------

def calculate_future_price(current_price, inflation_rate, years):
    """
    Calculate the future price of an item under inflation.

    Formula:
        At = A0 * (1 + rf)^t

    Where:
        A0 = Current price
        rf = Annual inflation rate
        t  = Number of years
        At = Future price
    """

    future_price = current_price * (
        1 + inflation_rate
    ) ** years

    return future_price


# ------------------------------------------------------------
# 3. CALCULATE FUTURE PRICES FOR DIFFERENT YEARS
# ------------------------------------------------------------

future_price_results = []

# Calculate prices from year 0 to year 10
for number_of_years in range(0, 11):

    future_price = calculate_future_price(
        initial_item_price,
        annual_inflation_rate,
        number_of_years
    )

    future_price_results.append({
        "Year": number_of_years,
        "Price (Birr)": future_price
    })


# Convert results into a DataFrame
future_price_table = pd.DataFrame(future_price_results)

print("\n========== FUTURE PRICE UNDER INFLATION ==========")

print(future_price_table.to_string(
    index=False,
    formatters={
        "Price (Birr)": "{:,.2f}".format
    }
))


# ------------------------------------------------------------
# 4. REPRODUCE THE INSTRUCTOR'S EXAMPLE
# ------------------------------------------------------------

# Given:
# Current price = 100 Birr
# Annual inflation rate = 25%
# Time = 2 years

example_future_price = calculate_future_price(
    current_price=100,
    inflation_rate=0.25,
    years=2
)

print("\n========== INSTRUCTOR'S EXAMPLE ==========")

print(f"Current price: 100.00 Birr")

print(f"Annual inflation rate: 25%")

print(f"Time: 2 years")

print(
    f"Price after 2 years: "
    f"{example_future_price:,.2f} Birr"
)


# ------------------------------------------------------------
# 5. INFLATION-ADJUSTED RATE OF RETURN
# ------------------------------------------------------------

def calculate_real_rate_of_return(
    nominal_return_rate,
    inflation_rate
):
    """
    Calculate the actual annual rate of return after inflation.

    Formula from the lecture:

        ra = (1 + r)/(1 + rf) - 1

    Where:
        r  = Nominal annual rate of return
        rf = Annual inflation rate
        ra = Inflation-adjusted rate of return
    """

    real_rate = (
        (1 + nominal_return_rate) /
        (1 + inflation_rate)
    ) - 1

    return real_rate


# Calculate the exact inflation-adjusted return
exact_real_return = calculate_real_rate_of_return(
    annual_nominal_return,
    investment_inflation_rate
)

# Calculate the approximate inflation-adjusted return
approximate_real_return = (
    annual_nominal_return - investment_inflation_rate
)

print("\n========== INFLATION-ADJUSTED RATE OF RETURN ==========")

print(
    f"Nominal annual return: "
    f"{annual_nominal_return * 100:.2f}%"
)

print(
    f"Annual inflation rate: "
    f"{investment_inflation_rate * 100:.2f}%"
)

print(
    f"Exact inflation-adjusted return: "
    f"{exact_real_return * 100:.4f}%"
)

print(
    f"Approximate inflation-adjusted return: "
    f"{approximate_real_return * 100:.4f}%"
)


# ------------------------------------------------------------
# 6. PRESENT VALUE OF A FUTURE PAYMENT
#    CONSIDERING MONTHLY INFLATION
# ------------------------------------------------------------

def calculate_inflation_adjusted_present_value(
    future_amount,
    annual_interest_rate,
    annual_inflation_rate,
    number_of_months
):
    """
    Calculate the present value of a future payment
    using the formula given in the instructor's lecture.

    Formula:

        A0 = Q * (1 + i - if)^(-n)

    Where:
        Q  = Future payment
        i  = Monthly interest rate
        if = Monthly inflation rate
        n  = Number of months
        A0 = Present value

    Monthly rates:

        i  = r/12
        if = rf/12
    """

    # Convert annual interest rate into monthly rate
    monthly_interest_rate = annual_interest_rate / 12

    # Convert annual inflation rate into monthly rate
    monthly_inflation_rate = annual_inflation_rate / 12

    # Calculate the monthly adjusted rate
    monthly_adjusted_rate = (
        1 + monthly_interest_rate - monthly_inflation_rate
    )

    # Calculate present value
    present_value = future_amount * (
        monthly_adjusted_rate ** (-number_of_months)
    )

    return present_value


# ------------------------------------------------------------
# 7. CALCULATE PRESENT VALUES FOR DIFFERENT MONTHS
# ------------------------------------------------------------

present_value_results = []

for number_of_months in payment_periods_months:

    present_value = calculate_inflation_adjusted_present_value(
        future_payment,
        annual_nominal_return,
        investment_inflation_rate,
        number_of_months
    )

    present_value_results.append({
        "Payment Period (Months)": number_of_months,
        "Future Payment (Birr)": future_payment,
        "Present Value (Birr)": present_value
    })


# Convert results into a DataFrame
present_value_table = pd.DataFrame(present_value_results)

print("\n========== PRESENT VALUE OF FUTURE PAYMENTS ==========")

print(present_value_table.to_string(
    index=False,
    formatters={
        "Future Payment (Birr)": "{:,.2f}".format,
        "Present Value (Birr)": "{:,.2f}".format
    }
))


# ------------------------------------------------------------
# 8. CALCULATE THE EFFECT OF INFLATION ON PURCHASING POWER
# ------------------------------------------------------------

def calculate_purchasing_power(
    money_amount,
    inflation_rate,
    years
):
    """
    Calculate the purchasing power of a fixed amount
    of money after inflation.

    Formula:

        Purchasing Power = A0 / (1 + rf)^t
    """

    purchasing_power = money_amount / (
        (1 + inflation_rate) ** years
    )

    return purchasing_power


purchasing_power_results = []

for number_of_years in range(0, 11):

    remaining_purchasing_power = calculate_purchasing_power(
        initial_item_price,
        annual_inflation_rate,
        number_of_years
    )

    purchasing_power_results.append({
        "Year": number_of_years,
        "Money Amount (Birr)": initial_item_price,
        "Purchasing Power (Birr)": remaining_purchasing_power
    })


purchasing_power_table = pd.DataFrame(
    purchasing_power_results
)

print("\n========== EFFECT OF INFLATION ON PURCHASING POWER ==========")

print(purchasing_power_table.to_string(
    index=False,
    formatters={
        "Money Amount (Birr)": "{:,.2f}".format,
        "Purchasing Power (Birr)": "{:,.2f}".format
    }
))


# ------------------------------------------------------------
# 9. VISUALIZE FUTURE PRICE INCREASE
# ------------------------------------------------------------

plt.figure(figsize=(10, 6))

plt.plot(
    future_price_table["Year"],
    future_price_table["Price (Birr)"],
    marker="o"
)

plt.title("Effect of Inflation on Future Prices")

plt.xlabel("Number of Years")

plt.ylabel("Future Price (Birr)")

plt.grid(True, linestyle="--", alpha=0.5)

plt.tight_layout()

plt.show()


# ------------------------------------------------------------
# 10. VISUALIZE THE LOSS OF PURCHASING POWER
# ------------------------------------------------------------

plt.figure(figsize=(10, 6))

plt.plot(
    purchasing_power_table["Year"],
    purchasing_power_table["Purchasing Power (Birr)"],
    marker="o"
)

plt.title("Effect of Inflation on Purchasing Power")

plt.xlabel("Number of Years")

plt.ylabel("Purchasing Power of 100 Birr")

plt.grid(True, linestyle="--", alpha=0.5)

plt.tight_layout()

plt.show()


# ------------------------------------------------------------
# 11. FINAL SUMMARY
# ------------------------------------------------------------

print("\n========== FINAL SUMMARY ==========")

print(
    f"Initial item price: "
    f"{initial_item_price:,.2f} Birr"
)

print(
    f"Price after 2 years: "
    f"{example_future_price:,.2f} Birr"
)

print(
    f"Purchasing power of 100 Birr after 2 years: "
    f"{calculate_purchasing_power(100, 0.25, 2):,.2f} Birr"
)

print(
    f"Exact inflation-adjusted investment return: "
    f"{exact_real_return * 100:.4f}%"
)

print(
    f"Approximate inflation-adjusted investment return: "
    f"{approximate_real_return * 100:.4f}%"
)

print("\nInflation analysis completed successfully!")
