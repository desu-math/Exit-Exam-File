# ============================================================
# FINANCIAL MATHEMATICS: INTERNAL RATE OF RETURN (IRR)
# ============================================================
# This program covers the IRR concepts:
#
# 
# 1. Present value of future returns
# 2. Calculation of IRR
# 3. Verification of the IRR
# 4. Existence and uniqueness of IRR
# 5. Condition for a positive rate of return
# 6. Comparison of different investment projects
# 7. Visualization of present value against interest rate
#
# Main formula:
#
#       P = Sum[An * (1 + i)^(-n)]
#
# Where:
#       P  = Initial investment
#       An = Return at the end of period n
#       i  = Internal rate of return
#       N  = Total number of periods
# ============================================================


import pandas as pd
import matplotlib.pyplot as plt


# ============================================================
# 1. PRESENT VALUE OF FUTURE RETURNS
# ============================================================

def calculate_present_value(future_returns, interest_rate):

    """
    Calculate the present value of a sequence of future returns.

    Formula:
        R(i) = Sum[An / (1 + i)^n]

    Where:
        An = Return at the end of period n
        i  = Interest rate
    """

    if interest_rate <= -1:
        raise ValueError("Interest rate must be greater than -1.")

    present_value = 0

    for period, future_return in enumerate(future_returns, start=1):

        present_value += (
            future_return / (1 + interest_rate) ** period
        )

    return present_value


# ============================================================
# 2. DIFFERENCE BETWEEN PRESENT VALUE AND INITIAL INVESTMENT
# ============================================================

def calculate_irr_equation(future_returns,
                           initial_investment,
                           interest_rate):

    """
    Calculate the difference between the present value
    of future returns and the initial investment.

    Equation:
        R(i) - P

    The IRR is the rate at which this difference becomes zero.
    """

    present_value = calculate_present_value(
        future_returns,
        interest_rate
    )

    return present_value - initial_investment


# ============================================================
# 3. CALCULATE INTERNAL RATE OF RETURN USING BISECTION
# ============================================================

def calculate_irr(future_returns,
                  initial_investment,
                  tolerance=1e-10,
                  maximum_iterations=1000):

    """
    Calculate IRR using the bisection method.

    We solve:
        P = Sum[An / (1 + i)^n]

    Equivalently:
        R(i) - P = 0

    The method searches for the unique rate i > -1.

    Assumptions:
        Initial investment P > 0
        Future returns An >= 0
        At least one future return is positive
    """

    if initial_investment <= 0:
        raise ValueError("Initial investment must be positive.")

    if not future_returns or not any(x > 0 for x in future_returns):
        raise ValueError("At least one future return must be positive.")

    if any(x < 0 for x in future_returns):
        raise ValueError(
            "Future returns must be non-negative, as assumed in the lecture."
        )

    # Lower and upper limits for the IRR search.

    lower_rate = -0.999999999
    upper_rate = 1.0

    # Check whether the upper limit is large enough.

    while calculate_irr_equation(
        future_returns,
        initial_investment,
        upper_rate
    ) > 0:

        upper_rate = 2 * upper_rate + 1

    # Bisection method.

    for iteration in range(maximum_iterations):

        middle_rate = (lower_rate + upper_rate) / 2

        equation_value = calculate_irr_equation(
            future_returns,
            initial_investment,
            middle_rate
        )

        if abs(equation_value) < tolerance:
            return middle_rate, iteration + 1

        if equation_value > 0:
            lower_rate = middle_rate

        else:
            upper_rate = middle_rate

    raise ArithmeticError(
        "IRR calculation did not converge within the iteration limit."
    )


# ============================================================
# 4. GENERATE PRESENT VALUE TABLE
# ============================================================

def generate_present_value_table(future_returns,
                                 initial_investment,
                                 interest_rates):

    """
    Calculate the present value of future returns
    at different interest rates.
    """

    records = []

    for rate in interest_rates:

        present_value = calculate_present_value(
            future_returns,
            rate
        )

        difference = present_value - initial_investment

        records.append({
            "Interest Rate": rate,
            "Present Value": present_value,
            "Initial Investment": initial_investment,
            "Difference (R(i)-P)": difference
        })

    return pd.DataFrame(records)


# ============================================================
# 5. GENERATE FUTURE RETURN SCHEDULE
# ============================================================

def generate_return_schedule(future_returns, irr):

    """
    Calculate the present value of each future return
    using the calculated IRR.
    """

    records = []

    for period, future_return in enumerate(future_returns, start=1):

        present_value = (
            future_return / (1 + irr) ** period
        )

        records.append({
            "Period": period,
            "Future Return": future_return,
            "Discount Factor": 1 / (1 + irr) ** period,
            "Present Value": present_value
        })

    return pd.DataFrame(records)


# ============================================================
# 6. CHECK THE POSITIVE IRR CONDITION
# ============================================================

def check_positive_irr_condition(future_returns,
                                 initial_investment):

    """
    According to the lecture:

    IRR > 0 if and only if:

        P < Sum(An)

    IRR = 0 if:

        P = Sum(An)

    IRR < 0 if:

        P > Sum(An)
    """

    total_future_returns = sum(future_returns)

    if initial_investment < total_future_returns:

        result = "Positive IRR"

    elif initial_investment == total_future_returns:

        result = "Zero IRR"

    else:

        result = "Negative IRR"

    return total_future_returns, result


# ============================================================
# 7. MAIN INPUTS
# ============================================================

# Initial investment

initial_investment = 10000

# Future returns at the end of each period

future_returns = [
    3000,
    3500,
    4000,
    4500,
    5000
]


# ============================================================
# 8. CALCULATE INTERNAL RATE OF RETURN
# ============================================================

irr, number_of_iterations = calculate_irr(
    future_returns,
    initial_investment
)

print("\n========== INTERNAL RATE OF RETURN ==========")

print(f"Initial Investment:       {initial_investment:,.2f}")

print(f"Total Future Returns:     {sum(future_returns):,.2f}")

print(f"Internal Rate of Return:  {irr:.6%}")

print(f"IRR as Percentage:        {irr * 100:.4f}%")

print(f"Number of Iterations:     {number_of_iterations}")


# ============================================================
# 9. CALCULATE PRESENT VALUE AT THE IRR
# ============================================================

present_value_at_irr = calculate_present_value(
    future_returns,
    irr
)

print("\n========== IRR VERIFICATION ==========")

print(f"Initial Investment:       {initial_investment:,.6f}")

print(f"Present Value at IRR:     {present_value_at_irr:,.6f}")

print(
    f"Difference:               "
    f"{present_value_at_irr - initial_investment:.10f}"
)

print("The difference should be approximately zero.")


# ============================================================
# 10. PRESENT VALUE AT DIFFERENT INTEREST RATES
# ============================================================

interest_rates = [
    0.00,
    0.05,
    0.10,
    0.15,
    0.20,
    0.25,
    0.30,
    0.35
]

present_value_table = generate_present_value_table(
    future_returns,
    initial_investment,
    interest_rates
)

print("\n========== PRESENT VALUE TABLE ==========")

print(present_value_table.to_string(index=False))


# ============================================================
# 11. FUTURE RETURN SCHEDULE AT IRR
# ============================================================

return_schedule = generate_return_schedule(
    future_returns,
    irr
)

print("\n========== FUTURE RETURN SCHEDULE ==========")

print(return_schedule.to_string(index=False))

print(
    f"\nSum of Present Values: "
    f"{return_schedule['Present Value'].sum():,.6f}"
)


# ============================================================
# 12. CHECK THE POSITIVE IRR CONDITION
# ============================================================

total_returns, irr_condition = check_positive_irr_condition(
    future_returns,
    initial_investment
)

print("\n========== POSITIVE IRR CONDITION ==========")

print(f"Initial Investment:       {initial_investment:,.2f}")

print(f"Sum of Future Returns:    {total_returns:,.2f}")

print(f"Result:                   {irr_condition}")


# ============================================================
# 13. COMPARISON OF DIFFERENT INVESTMENT PROJECTS
# ============================================================

projects = {
    "Project A": {
        "initial_investment": 10000,
        "returns": [3000, 3500, 4000, 4500, 5000]
    },

    "Project B": {
        "initial_investment": 10000,
        "returns": [2000, 3000, 4000, 5000, 6000]
    },

    "Project C": {
        "initial_investment": 10000,
        "returns": [4000, 4000, 4000, 4000, 4000]
    }
}

project_results = []

for project_name, project_data in projects.items():

    project_irr, _ = calculate_irr(
        project_data["returns"],
        project_data["initial_investment"]
    )

    project_results.append({
        "Project": project_name,
        "Initial Investment": project_data["initial_investment"],
        "Total Returns": sum(project_data["returns"]),
        "IRR": project_irr
    })

project_comparison = pd.DataFrame(project_results)

project_comparison = project_comparison.sort_values(
    by="IRR",
    ascending=False
)

print("\n========== PROJECT COMPARISON ==========")

print(project_comparison.to_string(index=False))

print(
    f"\nHighest IRR: "
    f"{project_comparison.iloc[0]['Project']}"
)


# ============================================================
# 14. VISUALIZATION: PRESENT VALUE AGAINST INTEREST RATE
# ============================================================

rates_for_graph = [
    -0.50 + i * 0.01
    for i in range(101)
]

present_values_for_graph = [
    calculate_present_value(future_returns, rate)
    for rate in rates_for_graph
]

plt.figure(figsize=(10, 6))

plt.plot(
    rates_for_graph,
    present_values_for_graph,
    label="R(i)"
)

plt.axhline(
    y=initial_investment,
    linestyle="--",
    label="Initial Investment (P)"
)

plt.axvline(
    x=irr,
    linestyle=":",
    label=f"IRR = {irr:.2%}"
)

plt.title("Present Value of Future Returns Against Interest Rate")
plt.xlabel("Interest Rate")
plt.ylabel("Present Value")
plt.grid(True)
plt.legend()

plt.show()


# ============================================================
# 15. VISUALIZATION: PROJECT IRR COMPARISON
# ============================================================

plt.figure(figsize=(9, 6))

plt.bar(
    project_comparison["Project"],
    project_comparison["IRR"] * 100
)

plt.title("Comparison of Investment Projects Using IRR")
plt.xlabel("Investment Project")
plt.ylabel("Internal Rate of Return (%)")
plt.grid(axis="y")

plt.show()


# ============================================================
# 16. FINAL SUMMARY
# ============================================================

print("\n========== FINAL SUMMARY ==========")

print(f"1. Initial Investment: {initial_investment:,.2f}")

print(f"2. Total Future Returns: {sum(future_returns):,.2f}")

print(f"3. Internal Rate of Return: {irr:.4%}")

print(f"4. Present Value at IRR: {present_value_at_irr:,.2f}")

print(f"5. IRR Condition: {irr_condition}")

print("\nIRR calculations completed successfully!")
