# ============================================================
# FINANCIAL MATHEMATICS: ANNUITIES
# ============================================================
# This program covers the annuity concepts:
#
# 
# 1. Periodic deposits (Sinking Fund)
# 2. Future value of an annuity
# 3. Future value with an initial deposit
# 4. Periodic withdrawals
# 5. Initial deposit required for withdrawals
# 6. Periodic withdrawal payment
#
# Assumption:
# Payments are made at the end of each compounding period.
# ============================================================


import pandas as pd
import matplotlib.pyplot as plt


# ============================================================
# 1. FUTURE VALUE OF AN ANNUITY (DEPOSITS)
# ============================================================

def calculate_annuity_future_value(payment, annual_rate,
                                   compounding_frequency, periods):

    """
    Calculate the future value of an ordinary annuity.

    Formula:
        An = P * ((1 + i)^n - 1) / i

    Where:
        P = Periodic deposit
        i = Periodic interest rate
        n = Number of periods
    """

    periodic_rate = annual_rate / compounding_frequency

    if periodic_rate == 0:
        future_value = payment * periods
    else:
        future_value = (
            payment * ((1 + periodic_rate) ** periods - 1)
            / periodic_rate
        )

    total_deposits = payment * periods
    interest_earned = future_value - total_deposits

    return future_value, total_deposits, interest_earned


# ============================================================
# 2. FUTURE VALUE WITH AN INITIAL DEPOSIT
# ============================================================

def calculate_future_value_with_initial_deposit(
        initial_deposit, payment, annual_rate,
        compounding_frequency, periods):

    """
    Calculate the future value when an initial deposit
    is made at time zero, followed by periodic deposits.

    Formula:
        An = A0(1 + i)^n + P[((1 + i)^n - 1) / i]
    """

    periodic_rate = annual_rate / compounding_frequency

    initial_deposit_value = (
        initial_deposit * (1 + periodic_rate) ** periods
    )

    if periodic_rate == 0:
        annuity_value = payment * periods
    else:
        annuity_value = (
            payment * ((1 + periodic_rate) ** periods - 1)
            / periodic_rate
        )

    future_value = initial_deposit_value + annuity_value

    return future_value, initial_deposit_value, annuity_value


# ============================================================
# 3. FUTURE VALUE USING PERIOD-BY-PERIOD CALCULATION
# ============================================================

def generate_deposit_schedule(payment, annual_rate,
                              compounding_frequency, periods,
                              initial_deposit=0):

    """
    Generate a table showing how an annuity grows over time.

    At the end of each period:
        New balance = Previous balance + Interest + Deposit
    """

    periodic_rate = annual_rate / compounding_frequency

    balance = initial_deposit
    records = []

    for period in range(1, periods + 1):

        interest = balance * periodic_rate

        balance_before_deposit = balance + interest

        balance = balance_before_deposit + payment

        records.append({
            "Period": period,
            "Opening Balance": balance_before_deposit - interest,
            "Interest Earned": interest,
            "Deposit": payment,
            "Closing Balance": balance
        })

    return pd.DataFrame(records)


# ============================================================
# 4. ACCOUNT VALUE AFTER PERIODIC WITHDRAWALS
# ============================================================

def calculate_withdrawal_future_value(
        initial_deposit, withdrawal, annual_rate,
        compounding_frequency, periods):

    """
    Calculate the remaining account value after withdrawals.

    Formula:
        An = A0(1 + i)^n
             + P * [1 - (1 + i)^n] / i

    P represents the positive withdrawal amount.
    """

    periodic_rate = annual_rate / compounding_frequency

    if periodic_rate == 0:
        remaining_balance = initial_deposit - withdrawal * periods

    else:
        remaining_balance = (
            initial_deposit * (1 + periodic_rate) ** periods
            + withdrawal *
            (1 - (1 + periodic_rate) ** periods)
            / periodic_rate
        )

    return remaining_balance


# ============================================================
# 5. INITIAL DEPOSIT REQUIRED FOR N WITHDRAWALS
# ============================================================

def calculate_required_initial_deposit(
        withdrawal, annual_rate,
        compounding_frequency, number_of_withdrawals):

    """
    Calculate the initial deposit required to support
    a fixed number of equal withdrawals.

    Formula:
        A0 = P * [1 - (1 + i)^(-N)] / i
    """

    periodic_rate = annual_rate / compounding_frequency

    if periodic_rate == 0:
        initial_deposit = withdrawal * number_of_withdrawals

    else:
        initial_deposit = (
            withdrawal *
            (1 - (1 + periodic_rate) ** (-number_of_withdrawals))
            / periodic_rate
        )

    return initial_deposit


# ============================================================
# 6. CALCULATE PERIODIC WITHDRAWAL PAYMENT
# ============================================================

def calculate_periodic_withdrawal(
        initial_deposit, annual_rate,
        compounding_frequency, number_of_withdrawals):

    """
    Calculate the equal withdrawal payment supported
    by a given initial deposit.

    Formula:
        P = A0 * i / [1 - (1 + i)^(-N)]
    """

    periodic_rate = annual_rate / compounding_frequency

    if periodic_rate == 0:
        withdrawal = initial_deposit / number_of_withdrawals

    else:
        withdrawal = (
            initial_deposit * periodic_rate
            / (1 - (1 + periodic_rate) ** (-number_of_withdrawals))
        )

    return withdrawal


# ============================================================
# 7. MAIN INPUTS
# ============================================================

# General annuity inputs

payment = 1000
annual_interest_rate = 0.12
compounding_frequency = 12
number_of_periods = 36

# Initial deposit

initial_deposit = 5000

# Withdrawal inputs

initial_withdrawal_fund = 50000
withdrawal_payment = 2000
number_of_withdrawals = 36


# ============================================================
# 8. FUTURE VALUE OF AN ANNUITY
# ============================================================

future_value, total_deposits, interest_earned = (
    calculate_annuity_future_value(
        payment,
        annual_interest_rate,
        compounding_frequency,
        number_of_periods
    )
)

print("\n========== FUTURE VALUE OF AN ANNUITY ==========")

print(f"Periodic Deposit:       {payment:,.2f}")
print(f"Annual Interest Rate:   {annual_interest_rate:.2%}")
print(f"Compounding Frequency:  {compounding_frequency} times/year")
print(f"Number of Periods:      {number_of_periods}")
print(f"Total Deposits:         {total_deposits:,.2f}")
print(f"Interest Earned:        {interest_earned:,.2f}")
print(f"Future Value:           {future_value:,.2f}")


# ============================================================
# 9. FUTURE VALUE WITH AN INITIAL DEPOSIT
# ============================================================

future_value_total, initial_value_growth, annuity_growth = (
    calculate_future_value_with_initial_deposit(
        initial_deposit,
        payment,
        annual_interest_rate,
        compounding_frequency,
        number_of_periods
    )
)

print("\n========== FUTURE VALUE WITH INITIAL DEPOSIT ==========")

print(f"Initial Deposit:        {initial_deposit:,.2f}")
print(f"Periodic Deposit:       {payment:,.2f}")
print(f"Value of Initial Deposit: {initial_value_growth:,.2f}")
print(f"Value of Periodic Deposits: {annuity_growth:,.2f}")
print(f"Total Future Value:     {future_value_total:,.2f}")


# ============================================================
# 10. DEPOSIT SCHEDULE
# ============================================================

deposit_schedule = generate_deposit_schedule(
    payment,
    annual_interest_rate,
    compounding_frequency,
    number_of_periods,
    initial_deposit
)

print("\n========== DEPOSIT SCHEDULE ==========")

print(deposit_schedule.head())

print("\nLast Five Periods:")

print(deposit_schedule.tail())


# ============================================================
# 11. WITHDRAWAL CALCULATION
# ============================================================

remaining_balance = calculate_withdrawal_future_value(
    initial_withdrawal_fund,
    withdrawal_payment,
    annual_interest_rate,
    compounding_frequency,
    number_of_withdrawals
)

print("\n========== WITHDRAWAL CALCULATION ==========")

print(f"Initial Fund:           {initial_withdrawal_fund:,.2f}")
print(f"Periodic Withdrawal:    {withdrawal_payment:,.2f}")
print(f"Number of Withdrawals:  {number_of_withdrawals}")
print(f"Remaining Balance:      {remaining_balance:,.2f}")


# ============================================================
# 12. INITIAL DEPOSIT REQUIRED FOR WITHDRAWALS
# ============================================================

required_initial_deposit = calculate_required_initial_deposit(
    withdrawal_payment,
    annual_interest_rate,
    compounding_frequency,
    number_of_withdrawals
)

print("\n========== REQUIRED INITIAL DEPOSIT ==========")

print(f"Periodic Withdrawal:    {withdrawal_payment:,.2f}")
print(f"Number of Withdrawals:  {number_of_withdrawals}")
print(f"Required Initial Fund:  {required_initial_deposit:,.2f}")


# ============================================================
# 13. PERIODIC WITHDRAWAL PAYMENT
# ============================================================

calculated_withdrawal = calculate_periodic_withdrawal(
    initial_withdrawal_fund,
    annual_interest_rate,
    compounding_frequency,
    number_of_withdrawals
)

print("\n========== PERIODIC WITHDRAWAL PAYMENT ==========")

print(f"Initial Fund:           {initial_withdrawal_fund:,.2f}")
print(f"Number of Withdrawals:  {number_of_withdrawals}")
print(f"Periodic Withdrawal:    {calculated_withdrawal:,.2f}")


# ============================================================
# 14. COMPARISON OF ANNUITY VALUES
# ============================================================

comparison_data = {
    "Description": [
        "Future Value of Annuity",
        "Future Value with Initial Deposit",
        "Required Initial Withdrawal Fund",
        "Remaining Withdrawal Balance"
    ],

    "Amount": [
        future_value,
        future_value_total,
        required_initial_deposit,
        remaining_balance
    ]
}

comparison_table = pd.DataFrame(comparison_data)

print("\n========== ANNUITY COMPARISON ==========")

print(comparison_table.to_string(index=False))


# ============================================================
# 15. VISUALIZATION: GROWTH OF ANNUITY
# ============================================================

plt.figure(figsize=(10, 6))

plt.plot(
    deposit_schedule["Period"],
    deposit_schedule["Closing Balance"],
    marker="o",
    label="Account Balance"
)

plt.title("Growth of an Ordinary Annuity")
plt.xlabel("Compounding Period")
plt.ylabel("Account Balance")
plt.grid(True)
plt.legend()

plt.show()


# ============================================================
# 16. VISUALIZATION: INTEREST AND DEPOSITS
# ============================================================

plt.figure(figsize=(10, 6))

plt.plot(
    deposit_schedule["Period"],
    deposit_schedule["Interest Earned"],
    label="Interest Earned"
)

plt.plot(
    deposit_schedule["Period"],
    deposit_schedule["Deposit"],
    label="Periodic Deposit"
)

plt.title("Periodic Deposits and Interest Earned")
plt.xlabel("Compounding Period")
plt.ylabel("Amount")
plt.grid(True)
plt.legend()

plt.show()


# ============================================================
# 17. FINAL SUMMARY
# ============================================================

print("\n========== FINAL SUMMARY ==========")

print(f"1. Future Value of Annuity: {future_value:,.2f}")

print(f"2. Future Value with Initial Deposit: "
      f"{future_value_total:,.2f}")

print(f"3. Total Interest Earned on Annuity: "
      f"{interest_earned:,.2f}")

print(f"4. Required Initial Withdrawal Fund: "
      f"{required_initial_deposit:,.2f}")

print(f"5. Periodic Withdrawal Payment: "
      f"{calculated_withdrawal:,.2f}")

print("\nProgram completed successfully!")
