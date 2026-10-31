# Inflation — Algorithms and Step-by-Step Procedures

**Course:** Financial Mathematics (Math 4313)
**Chapter:** Basic Finance Concepts
**Topic:** Inflation
**Purpose:** To provide systematic procedures for solving inflation-related problems.

---

## 1. General Problem-Solving Procedure

Before solving an inflation problem, identify what the problem requires. It may ask you to calculate:

1. The future price of goods and services.
2. The purchasing power of a future amount of money.
3. The exact inflation-adjusted rate of return.
4. The approximate real rate of return.
5. The difference between nominal growth and real growth.

### Required Inputs

| Symbol | Meaning                                         |
| ------ | ----------------------------------------------- |
| A₀     | Current price or initial amount of money        |
| A(t)   | Future price or accumulated amount after time t |
| r_f    | Annual inflation rate                           |
| r      | Nominal annual rate of return                   |
| r_a    | Inflation-adjusted or real rate of return       |
| t      | Time in years                                   |

### General Algorithm

1. Read the problem carefully.
2. Identify the given financial information.
3. Determine whether the problem concerns price growth, purchasing power, or investment return.
4. Convert all percentage rates into decimal form.
5. Select the appropriate formula.
6. Substitute the known values.
7. Perform the calculation.
8. Interpret the result in the context of inflation.
9. Include the appropriate currency, unit, or percentage.

**Important:** Inflation calculations use compound growth because the inflation rate applies to the increasing price level, not only to the original price.

---

## 2. Algorithm for Calculating Future Prices Under Inflation

### Mathematical Formula

A(t) = A₀(1 + r_f)^t

Where:

* A₀ = current price.
* r_f = annual inflation rate.
* t = number of years.
* A(t) = future price after t years.

### Step-by-Step Algorithm

**Input:** A₀, r_f, t

**Output:** Future price A(t)

**Procedure:**

1. Read the current price A₀.

2. Read the annual inflation rate r_f.

3. Read the number of years t.

4. Convert r_f into decimal form if given as a percentage.

5. Calculate the annual inflation growth factor:

   F = 1 + r_f

6. Raise the growth factor to the power of the number of years:

   G = (1 + r_f)^t

7. Multiply the current price by the growth factor:

   A(t) = A₀ × G

8. Display the future price.

### Pseudocode

```text
START

INPUT A0, rf, t

CONVERT rf TO decimal

F = 1 + rf

G = F ^ t

A = A0 * G

DISPLAY A

END
```

**Interpretation:** An item that costs "A₀" birr today will cost  "A(t)" birr after "t" years if the annual inflation rate remains "r_f".

---


## 3. Algorithm for Calculating Purchasing Power

Inflation reduces the purchasing power of money. Therefore, an amount received in the future cannot be compared directly with today's money without adjusting for inflation.

### Mathematical Formula

Purchasing power in today's money:

P = A(t) / (1 + r_f)^t

Where:

* A(t) = future amount of money.
* r_f = annual inflation rate.
* t = number of years.
* P = purchasing power expressed in today's money.

### Step-by-Step Algorithm

**Input:** A(t), r_f, t

**Output:** Purchasing power in today's money

**Procedure:**

1. Read the future amount of money A(t).

2. Read the annual inflation rate r_f.

3. Read the number of years t.

4. Convert r_f into decimal form.

5. Calculate the cumulative inflation factor:

   F = (1 + r_f)^t

6. Divide the future amount by the inflation factor:

   P = A(t) / F

7. Display the purchasing power in today's money.

### Pseudocode

```text
START

INPUT A, rf, t

CONVERT rf TO decimal

F = (1 + rf) ^ t

P = A / F

DISPLAY P

END
```


**Interpretation:** Although you will receive "A(t)" birr after three years, its purchasing power will be approximately equal to "P" birr today, assuming the inflation rate remains constant.

**Important:** The future amount and its purchasing power are different quantities. The first is measured in future birr, while the second is expressed in today's purchasing units.

---

## 4. Algorithm for Calculating the Exact Inflation-Adjusted Rate of Return

An investment may increase in nominal value while its actual purchasing power increases by a smaller amount.

To determine the actual growth of an investment after accounting for inflation, calculate its real rate of return.

### Mathematical Formula

r_a = (r − r_f) / (1 + r_f)

Where:

* r = nominal annual rate of return.
* r_f = annual inflation rate.
* r_a = exact inflation-adjusted rate of return.

### Step-by-Step Algorithm

**Input:** r, r_f

**Output:** Exact real rate of return r_a

**Procedure:**

1. Read the nominal annual rate of return r.

2. Read the annual inflation rate r_f.

3. Convert both rates into decimal form.

4. Calculate the difference between the two rates:

   D = r − r_f

5. Calculate the inflation growth factor:

   F = 1 + r_f

6. Divide the difference by the inflation growth factor:

   r_a = D / F

7. Multiply the result by 100 to express it as a percentage.

8. Display the exact real rate of return.

### Pseudocode

```text
START

INPUT r, rf

CONVERT r TO decimal
CONVERT rf TO decimal

D = r - rf

F = 1 + rf

ra = D / F

ra_percentage = ra * 100

DISPLAY ra_percentage

END
```


**Interpretation:** Although the investment earns a nominal return of "r%", its actual annual growth in purchasing power is approximately "ra".

---

## 5. Algorithm for Calculating the Approximate Real Rate of Return

For small inflation rates, the exact real rate of return can be approximated by subtracting inflation from the nominal rate of return.

### Mathematical Formula

r_a ≈ r − r_f


---


## 6. Algorithm for Calculating the Real Value of an Investment After Inflation

This procedure combines compound interest and inflation to determine the actual purchasing-power value of an investment.

### Mathematical Formulas

Nominal future value:

A(t) = A₀(1 + r)^t

Real value in today's money:

P = A(t) / (1 + r_f)^t

Combining both formulas:

P = A₀[(1 + r)/(1 + r_f)]^t

### Step-by-Step Algorithm

**Input:** A₀, r, r_f, t

**Output:** Nominal future value and real purchasing-power value

**Procedure:**

1. Read the initial investment A₀.

2. Read the nominal annual interest rate r.

3. Read the annual inflation rate r_f.

4. Read the investment period t.

5. Convert r and r_f into decimal form.

6. Calculate the nominal future value:

   A(t) = A₀(1 + r)^t

7. Calculate the cumulative inflation factor:

   F = (1 + r_f)^t

8. Calculate the real value:

   P = A(t) / F

9. Display both the nominal future value and the real value in today's money.

10. Compare the two values to understand the effect of inflation.

### Pseudocode

```text
START

INPUT A0, r, rf, t

CONVERT r TO decimal
CONVERT rf TO decimal

A = A0 * (1 + r) ^ t

F = (1 + rf) ^ t

P = A / F

DISPLAY A
DISPLAY P

END
```

### Worked Example : Nominal Growth and Purchasing Power

**Problem:** An investment of 10,000 ETB earns 10% annually for 2 years. If inflation is also 10% annually, calculate the nominal future value and its purchasing power in today's money.

**Given:**

* A₀ = 10,000 ETB
* r = 0.10
* r_f = 0.10
* t = 2 years

**Step 1: Calculate the nominal future value.**

A(t) = A₀(1 + r)^t

A(2) = 10,000(1.10)^2

A(2) = 10,000 × 1.21

**A(2) = 12,100 ETB**

**Step 2: Calculate the cumulative inflation factor.**

F = (1 + r_f)^t

F = (1.10)^2

**F = 1.21**

**Step 3: Calculate purchasing power.**

P = A(t) / F

P = 12,100 / 1.21

**P = 10,000 ETB**

**Interpretation:** The investment grows from 10,000 ETB to 12,100 ETB in nominal terms. However, because prices also increase by the same percentage, the investment's purchasing power remains equivalent to 10,000 ETB today.

---


## 7. Important Checks Before Submitting an Answer

Before finalizing an inflation calculation, verify the following:

1. **Initial amount:** Did you correctly identify the current price or initial investment?
2. **Inflation rate:** Did you convert the percentage into decimal form?
3. **Time:** Is the period correctly expressed in years?
4. **Compound growth:** Did you use the power t in the inflation formula?
5. **Purchasing power:** Did you divide the future amount by the cumulative inflation factor?
6. **Real return:** Did you use the exact formula when an exact result was required?
7. **Approximation:** Did you distinguish the approximate formula from the exact formula?
8. **Interpretation:** Did you explain whether purchasing power increases, remains unchanged, or decreases?
9. **Units:** Did you distinguish future birr from purchasing power expressed in today's birr?
10. **Rounding:** Did you retain sufficient precision during intermediate calculations?

---

## 8. Formula Selection Guide

Use this table to identify the appropriate algorithm quickly.

| Problem Description                         | Formula                     |
| ------------------------------------------- | --------------------------- |
| Calculate future price under inflation      | A(t) = A₀(1 + r_f)^t        |
| Calculate purchasing power in today's money | P = A(t)/(1 + r_f)^t        |
| Calculate exact real rate of return         | r_a = (r − r_f)/(1 + r_f)   |
| Calculate approximate real rate of return   | r_a ≈ r − r_f               |
| Calculate nominal future investment value   | A(t) = A₀(1 + r)^t          |
| Calculate real investment value             | P = A₀[(1 + r)/(1 + r_f)]^t |

---

## 9. Final Summary

Inflation problems mainly involve three calculation procedures:

1. **Future price calculation:** Use compound growth to determine how prices increase over time.
2. **Purchasing-power calculation:** Divide a future amount by the cumulative inflation factor to express its value in today's money.
3. **Real-rate calculation:** Adjust the nominal rate of return to determine the actual growth in purchasing power.

The general problem-solving approach is:

1. Identify the required quantity.
2. Identify the given values.
3. Convert percentages into decimals.
4. Select the correct formula.
5. Substitute the values.
6. Perform the calculation.
7. Interpret the result in terms of purchasing power.

**Remember:** A higher amount of money in the future does not necessarily mean greater purchasing power. Always account for inflation when evaluating the actual value of money over time.


