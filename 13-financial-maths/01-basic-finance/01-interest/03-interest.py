# ============================================================
# FINANCIAL MATHEMATICS
# CHAPTER 1: BASIC FINANCE
# TOPIC: INTEREST
#
# 
# Comparing Simple, Compound, and Continuous Interest
# ============================================================

import pandas as pd
import matplotlib.pyplot as plt


# ------------------------------------------------------------
# 1. INPUT DATA
# ------------------------------------------------------------

# Initial deposit (Present Value)
initial_deposit = 1000

# Annual nominal interest rate (3.5%)
annual_interest_rate = 0.035

# Investment duration in years
investment_time = 5.4

# Different compounding frequencies
# 12  = Monthly compounding
# 4   = Quarterly compounding
# 365 = Daily compounding
compounding_frequencies = [12, 4, 365]


# ------------------------------------------------------------
# 2. SIMPLE INTEREST
# ------------------------------------------------------------

def calculate_simple_interest(principal, annual_rate, time):
    """
    Calculate the future value using simple interest.

    Formula:
        A(t) = A0 * (1 + r*t)

    Interest is calculated only on the initial deposit.
    """

    future_value = principal * (1 + annual_rate * time)

    interest_earned = future_value - principal

    return future_value, interest_earned


# ------------------------------------------------------------
# 3. DISCRETE-TIME COMPOUND INTEREST
# ------------------------------------------------------------

def calculate_compound_interest(
    principal, annual_rate, time, compounding_frequency
):
    """
    Calculate the future value using compound interest.

    Formula:
        A(t) = A0 * (1 + r/m)^(m*t)

    Where:
        r = Annual nominal interest rate
        m = Number of compounding periods per year
        t = Time in years
    """

    # Interest rate per compounding period
    periodic_interest_rate = annual_rate / compounding_frequency

    # Total number of compounding periods
    total_compounding_periods = compounding_frequency * time

    # Calculate future value
    future_value = principal * (
        1 + periodic_interest_rate
    ) ** total_compounding_periods

    # Calculate total interest earned
    interest_earned = future_value - principal

    return future_value, interest_earned


# ------------------------------------------------------------
# 4. CONTINUOUS-TIME COMPOUND INTEREST
# ------------------------------------------------------------

def calculate_continuous_interest(principal, annual_rate, time):
    """
    Calculate the future value using continuous compounding.

    Formula:
        A(t) = A0 * e^(r*t)

    Where:
        e = Euler's mathematical constant
    """

    # Calculate future value using exponential growth
    future_value = principal * (
        2.718281828459045 ** (annual_rate * time)
    )

    # Calculate interest earned
    interest_earned = future_value - principal

    return future_value, interest_earned


# ------------------------------------------------------------
# 5. EFFECTIVE ANNUAL INTEREST RATE
# ------------------------------------------------------------

def calculate_effective_rate(annual_rate, compounding_frequency):
    """
    Calculate the effective annual interest rate.

    Formula:
        re = (1 + r/m)^m - 1

    The effective rate represents the actual annual growth
    after considering the compounding frequency.
    """

    effective_rate = (
        1 + annual_rate / compounding_frequency
    ) ** compounding_frequency - 1

    return effective_rate


# ------------------------------------------------------------
# 6. CALCULATE FUTURE VALUE USING SIMPLE INTEREST
# ------------------------------------------------------------

simple_future_value, simple_interest_earned = (
    calculate_simple_interest(
        initial_deposit,
        annual_interest_rate,
        investment_time
    )
)


# ------------------------------------------------------------
# 7. CALCULATE FUTURE VALUE USING COMPOUND INTEREST
# ------------------------------------------------------------

compound_results = []

for frequency in compounding_frequencies:

    future_value, interest_earned = calculate_compound_interest(
        initial_deposit,
        annual_interest_rate,
        investment_time,
        frequency
    )

    compound_results.append({
        "Method": f"{frequency} times per year",
        "Future Value": future_value,
        "Interest Earned": interest_earned
    })


# ------------------------------------------------------------
# 8. CALCULATE FUTURE VALUE USING CONTINUOUS COMPOUNDING
# ------------------------------------------------------------

continuous_future_value, continuous_interest_earned = (
    calculate_continuous_interest(
        initial_deposit,
        annual_interest_rate,
        investment_time
    )
)


# ------------------------------------------------------------
# 9. COMPARE ALL INTEREST METHODS
# ------------------------------------------------------------

comparison_results = []

# Simple interest result
comparison_results.append({
    "Method": "Simple Interest",
    "Future Value": simple_future_value,
    "Interest Earned": simple_interest_earned
})

# Compound interest results
comparison_results.extend(compound_results)

# Continuous interest result
comparison_results.append({
    "Method": "Continuous Compounding",
    "Future Value": continuous_future_value,
    "Interest Earned": continuous_interest_earned
})


# Convert results into a DataFrame
comparison_table = pd.DataFrame(comparison_results)

# Display the comparison table
print("\n========== INTEREST METHOD COMPARISON ==========")

print(comparison_table.to_string(
    index=False,
    formatters={
        "Future Value": "{:,.2f}".format,
        "Interest Earned": "{:,.2f}".format
    }
))


# ------------------------------------------------------------
# 10. CALCULATE EFFECTIVE ANNUAL RATES
# ------------------------------------------------------------

effective_rate_results = []

for frequency in compounding_frequencies:

    effective_rate = calculate_effective_rate(
        annual_interest_rate,
        frequency
    )

    effective_rate_results.append({
        "Compounding Frequency": frequency,
        "Effective Annual Rate (%)": effective_rate * 100
    })


# Convert effective rate results into a DataFrame
effective_rate_table = pd.DataFrame(effective_rate_results)

print("\n========== EFFECTIVE ANNUAL INTEREST RATES ==========")

print(effective_rate_table.to_string(
    index=False,
    formatters={
        "Effective Annual Rate (%)": "{:.4f}".format
    }
))


# ------------------------------------------------------------
# 11. DISPLAY THE HIGHEST AND LOWEST FUTURE VALUES
# ------------------------------------------------------------

highest_result = comparison_table.loc[
    comparison_table["Future Value"].idxmax()
]

lowest_result = comparison_table.loc[
    comparison_table["Future Value"].idxmin()
]

print("\n========== FINAL COMPARISON ==========")

print(
    f"Higher future value: {highest_result['Method']} "
    f"= {highest_result['Future Value']:,.2f} Birr"
)

print(
    f"Lower future value: {lowest_result['Method']} "
    f"= {lowest_result['Future Value']:,.2f} Birr"
)


# ------------------------------------------------------------
# 12. VISUALIZE THE FUTURE VALUES
# ------------------------------------------------------------

plt.figure(figsize=(10, 6))

plt.bar(
    comparison_table["Method"],
    comparison_table["Future Value"]
)

plt.title("Comparison of Different Interest Methods")

plt.xlabel("Interest Method")

plt.ylabel("Future Value (Birr)")

plt.xticks(rotation=25, ha="right")

plt.grid(axis="y", linestyle="--", alpha=0.5)

plt.tight_layout()

plt.show()
