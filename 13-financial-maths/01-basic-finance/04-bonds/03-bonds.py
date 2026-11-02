# ============================================================
# FINANCIAL MATHEMATICS: BONDS
# ============================================================
# This program covers the bond concepts:
#
# 
# 1. Zero-coupon bond price
# 2. Bond value at any time t
# 3. Coupon bond price
# 5. Present value of individual coupon payments
# 6. Total present value of a coupon bond
# 7. Comparison of zero-coupon and coupon bonds
# 8. Visualization of bond value over time
#
# 
# ============================================================


import math
import pandas as pd
import matplotlib.pyplot as plt


# ============================================================
# 1. ZERO-COUPON BOND PRICE
# ============================================================

def calculate_zero_coupon_bond_price(face_value,
                                     interest_rate,
                                     maturity_time):

    """
    Calculate the present price of a zero-coupon bond.

    Formula:
        B0 = F * e^(-rT)

    Where:
        F = Face value
        r = Continuously compounded interest rate
        T = Time to maturity
    """

    bond_price = face_value * math.exp(
        -interest_rate * maturity_time
    )

    return bond_price


# ============================================================
# 2. BOND VALUE AT ANY TIME t
# ============================================================

def calculate_bond_value(face_value,
                         interest_rate,
                         maturity_time,
                         current_time):

    """
    Calculate the value of a zero-coupon bond at time t.

    Formula:
        Bt = F * e^(-r(T-t))

    Equivalent formula:
        Bt = B0 * e^(rt)

    Where:
        t = Current time
        T = Maturity time
    """

    if current_time < 0 or current_time > maturity_time:
        raise ValueError(
            "Current time must be between 0 and maturity time."
        )

    remaining_time = maturity_time - current_time

    bond_value = face_value * math.exp(
        -interest_rate * remaining_time
    )

    return bond_value


# ============================================================
# 3. COUPON BOND PRICE
# ============================================================

def calculate_coupon_bond_price(face_value,
                                coupon_payment,
                                interest_rate,
                                maturity_time,
                                coupon_frequency=1):

    """
    Calculate the present price of a coupon bond.

    Formula:
        B0 = Sum[C * e^(-r*tn)] + F * e^(-rT)

    Where:
        C = Coupon payment per period
        tn = Time of each coupon payment
        F = Face value
        r = Continuously compounded interest rate
        T = Maturity time

    coupon_frequency:
        1 = Annual coupon payments
        2 = Semiannual coupon payments
        4 = Quarterly coupon payments
        12 = Monthly coupon payments
    """

    if coupon_frequency <= 0:
        raise ValueError("Coupon frequency must be positive.")

    if maturity_time <= 0:
        raise ValueError("Maturity time must be positive.")

    if coupon_payment < 0 or face_value < 0:
        raise ValueError("Face value and coupon cannot be negative.")

    number_of_payments = int(
        maturity_time * coupon_frequency
    )

    if not math.isclose(
        number_of_payments,
        maturity_time * coupon_frequency
    ):
        raise ValueError(
            "Maturity time must contain a whole number of coupon periods."
        )

    coupon_present_value = 0

    for period in range(1, number_of_payments + 1):

        payment_time = period / coupon_frequency

        discounted_coupon = coupon_payment * math.exp(
            -interest_rate * payment_time
        )

        coupon_present_value += discounted_coupon

    face_value_present_value = face_value * math.exp(
        -interest_rate * maturity_time
    )

    total_bond_price = (
        coupon_present_value + face_value_present_value
    )

    return (
        total_bond_price,
        coupon_present_value,
        face_value_present_value
    )


# ============================================================
# 4. GENERATE COUPON PAYMENT SCHEDULE
# ============================================================

def generate_coupon_schedule(coupon_payment,
                             interest_rate,
                             maturity_time,
                             coupon_frequency=1):

    """
    Generate a table of coupon payments and their present values.

    Each coupon is discounted separately using continuous
    compounding.
    """

    number_of_payments = int(
        maturity_time * coupon_frequency
    )

    records = []

    for period in range(1, number_of_payments + 1):

        payment_time = period / coupon_frequency

        present_value = coupon_payment * math.exp(
            -interest_rate * payment_time
        )

        records.append({
            "Payment Number": period,
            "Payment Time (Years)": payment_time,
            "Coupon Payment": coupon_payment,
            "Present Value": present_value
        })

    return pd.DataFrame(records)


# ============================================================
# 5. GENERATE ZERO-COUPON BOND VALUE SCHEDULE
# ============================================================

def generate_bond_value_schedule(face_value,
                                 interest_rate,
                                 maturity_time):

    """
    Generate bond values from time 0 to maturity.

    This shows how the value of a zero-coupon bond changes
    as it approaches its maturity date.
    """

    records = []

    for current_time in range(int(maturity_time) + 1):

        bond_value = calculate_bond_value(
            face_value,
            interest_rate,
            maturity_time,
            current_time
        )

        records.append({
            "Current Time (Years)": current_time,
            "Remaining Time (Years)": maturity_time - current_time,
            "Bond Value": bond_value
        })

    return pd.DataFrame(records)


# ============================================================
# 6. MAIN INPUTS
# ============================================================

# General bond information

face_value = 10000
annual_interest_rate = 0.08
maturity_time = 5

# Coupon bond information

coupon_payment = 800
coupon_frequency = 1


# ============================================================
# 7. ZERO-COUPON BOND PRICE
# ============================================================

zero_coupon_price = calculate_zero_coupon_bond_price(
    face_value,
    annual_interest_rate,
    maturity_time
)

print("\n========== ZERO-COUPON BOND ==========")

print(f"Face Value:          {face_value:,.2f}")
print(f"Interest Rate:       {annual_interest_rate:.2%}")
print(f"Maturity Time:       {maturity_time} years")
print(f"Purchase Price:      {zero_coupon_price:,.2f}")

print(
    f"Difference at Maturity: "
    f"{face_value - zero_coupon_price:,.2f}"
)


# ============================================================
# 8. BOND VALUE AT A PARTICULAR TIME
# ============================================================

current_time = 2

bond_value_at_time = calculate_bond_value(
    face_value,
    annual_interest_rate,
    maturity_time,
    current_time
)

print("\n========== BOND VALUE AT TIME t ==========")

print(f"Face Value:          {face_value:,.2f}")
print(f"Current Time:        {current_time} years")
print(f"Maturity Time:       {maturity_time} years")
print(f"Remaining Time:      {maturity_time - current_time} years")
print(f"Bond Value:          {bond_value_at_time:,.2f}")


# ============================================================
# 9. COUPON BOND PRICE
# ============================================================

(
    coupon_bond_price,
    total_coupon_present_value,
    face_value_present_value
) = calculate_coupon_bond_price(
    face_value,
    coupon_payment,
    annual_interest_rate,
    maturity_time,
    coupon_frequency
)

print("\n========== COUPON BOND ==========")

print(f"Face Value:                  {face_value:,.2f}")
print(f"Coupon Payment:              {coupon_payment:,.2f}")
print(f"Interest Rate:               {annual_interest_rate:.2%}")
print(f"Maturity Time:               {maturity_time} years")
print(f"Coupon Frequency:            {coupon_frequency} time(s)/year")

print(f"PV of All Coupons:           {total_coupon_present_value:,.2f}")

print(f"PV of Face Value:            {face_value_present_value:,.2f}")

print(f"Total Coupon Bond Price:     {coupon_bond_price:,.2f}")


# ============================================================
# 10. COUPON PAYMENT SCHEDULE
# ============================================================

coupon_schedule = generate_coupon_schedule(
    coupon_payment,
    annual_interest_rate,
    maturity_time,
    coupon_frequency
)

print("\n========== COUPON PAYMENT SCHEDULE ==========")

print(coupon_schedule.to_string(index=False))


# ============================================================
# 11. ZERO-COUPON BOND VALUE SCHEDULE
# ============================================================

bond_schedule = generate_bond_value_schedule(
    face_value,
    annual_interest_rate,
    maturity_time
)

print("\n========== ZERO-COUPON BOND VALUE SCHEDULE ==========")

print(bond_schedule.to_string(index=False))


# ============================================================
# 12. COMPARISON OF ZERO-COUPON AND COUPON BONDS
# ============================================================

comparison_data = {
    "Bond Type": [
        "Zero-Coupon Bond",
        "Coupon Bond"
    ],

    "Face Value": [
        face_value,
        face_value
    ],

    "Purchase Price": [
        zero_coupon_price,
        coupon_bond_price
    ],

    "Coupon Payments": [
        0,
        coupon_payment * maturity_time * coupon_frequency
    ]
}

comparison_table = pd.DataFrame(comparison_data)

print("\n========== BOND COMPARISON ==========")

print(comparison_table.to_string(index=False))


# ============================================================
# 13. VISUALIZATION: ZERO-COUPON BOND VALUE OVER TIME
# ============================================================

plt.figure(figsize=(10, 6))

plt.plot(
    bond_schedule["Current Time (Years)"],
    bond_schedule["Bond Value"],
    marker="o",
    label="Bond Value"
)

plt.axhline(
    y=face_value,
    linestyle="--",
    label="Face Value"
)

plt.title("Zero-Coupon Bond Value Over Time")
plt.xlabel("Current Time (Years)")
plt.ylabel("Bond Value")
plt.grid(True)
plt.legend()

plt.show()


# ============================================================
# 14. VISUALIZATION: PRESENT VALUE OF COUPONS
# ============================================================

plt.figure(figsize=(10, 6))

plt.bar(
    coupon_schedule["Payment Number"],
    coupon_schedule["Present Value"]
)

plt.title("Present Value of Individual Coupon Payments")
plt.xlabel("Coupon Payment Number")
plt.ylabel("Present Value")
plt.grid(axis="y")

plt.show()


# ============================================================
# 15. VISUALIZATION: BOND PRICE COMPARISON
# ============================================================

plt.figure(figsize=(8, 6))

plt.bar(
    comparison_table["Bond Type"],
    comparison_table["Purchase Price"]
)

plt.title("Zero-Coupon Bond vs Coupon Bond")
plt.xlabel("Bond Type")
plt.ylabel("Purchase Price")
plt.grid(axis="y")

plt.show()


# ============================================================
# 16. FINAL SUMMARY
# ============================================================

print("\n========== FINAL SUMMARY ==========")

print(f"1. Zero-Coupon Bond Price: {zero_coupon_price:,.2f}")

print(f"2. Bond Value at Time {current_time}: "
      f"{bond_value_at_time:,.2f}")

print(f"3. Coupon Bond Price: {coupon_bond_price:,.2f}")

print(f"4. Present Value of Coupons: "
      f"{total_coupon_present_value:,.2f}")

print(f"5. Present Value of Face Value: "
      f"{face_value_present_value:,.2f}")

print("\nBond calculations completed successfully!")
