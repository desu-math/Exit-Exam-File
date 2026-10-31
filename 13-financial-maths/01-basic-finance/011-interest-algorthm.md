# Interest — Algorithms and Step-by-Step Procedures

**Course:** Financial Mathematics (Math 4313)
**Chapter:** Basic Finance Concepts
**Topic:** Interest
**Purpose:** To provide systematic procedures for solving interest-related problems.

---

## 1. General Problem-Solving Procedure

Before calculating interest, identify the information given in the problem and determine which interest model is required.

### Required Inputs

| Symbol | Meaning                                |
| ------ | -------------------------------------- |
| A₀     | Initial principal or investment        |
| A      | Accumulated amount or future value     |
| r      | Annual nominal interest rate           |
| t      | Investment time in years               |
| m      | Number of compounding periods per year |
| I      | Interest earned                        |

### General Algorithm

1. Read the problem carefully.
2. Identify the initial principal (A₀).
3. Identify the annual interest rate (r).
4. Identify the investment period (t).
5. Determine whether interest is simple, discretely compounded, or continuously compounded.
6. If interest is compounded periodically, identify the compounding frequency (m).
7. Convert the interest rate from percentage to decimal.
8. Select the appropriate formula.
9. Substitute the known values.
10. Perform the calculation.
11. Calculate the interest earned if required.
12. Interpret the result and include the appropriate currency or unit.


---

## 2. Algorithm for Simple Interest

### Mathematical Formula

A(t) = A₀(1 + rt)

Interest earned:

I = A(t) − A₀

### Step-by-Step Algorithm

**Input:** A₀, r, t

**Output:** Accumulated amount A(t) and interest earned I

**Procedure:**

1. Read the initial principal A₀.

2. Read the annual interest rate r.

3. Read the investment period t.

4. Convert r into decimal form if it is given as a percentage.

5. Calculate the interest factor:

   F = 1 + rt

6. Calculate the accumulated amount:

   A(t) = A₀ × F

7. Calculate the interest earned:

   I = A(t) − A₀

8. Display the accumulated amount and interest earned.

### Pseudocode

```text
START

INPUT A0, r, t

CONVERT r TO decimal

F = 1 + (r * t)

A = A0 * F

I = A - A0

DISPLAY A
DISPLAY I

END
```

---

## 3. Algorithm for Discrete Compound Interest

### Mathematical Formula

A(t) = A₀(1 + r/m)^(mt)

Interest earned:

I = A(t) − A₀

### Step-by-Step Algorithm

**Input:** A₀, r, t, m

**Output:** Accumulated amount A(t) and interest earned I

**Procedure:**

1. Read the initial principal A₀.

2. Read the annual nominal interest rate r.

3. Read the investment period t in years.

4. Read the number of compounding periods per year m.

5. Convert r into decimal form.

6. Calculate the interest rate per compounding period:

   i = r/m

7. Calculate the total number of compounding periods:

   n = mt

8. Calculate the accumulation factor:

   F = (1 + i)^n

9. Calculate the accumulated amount:

   A(t) = A₀ × F

10. Calculate the interest earned:

    I = A(t) − A₀

11. Display the accumulated amount and interest earned.

### Pseudocode

```text
START

INPUT A0, r, t, m

CONVERT r TO decimal

i = r / m

n = m * t

F = (1 + i) ^ n

A = A0 * F

I = A - A0

DISPLAY A
DISPLAY I

END
```

### Common Compounding Frequencies

| Compounding Method |   m |
| ------------------ | --: |
| Annually           |   1 |
| Semi-annually      |   2 |
| Quarterly          |   4 |
| Monthly            |  12 |
| Daily              | 365 |


---

## 4. Algorithm for Continuous Compound Interest

### Mathematical Formula

A(t) = A₀e^(rt)

Interest earned:

I = A(t) − A₀

Here, e is the mathematical constant approximately equal to 2.71828.

### Step-by-Step Algorithm

**Input:** A₀, r, t

**Output:** Accumulated amount A(t) and interest earned I

**Procedure:**

1. Read the initial principal A₀.

2. Read the annual interest rate r.

3. Read the investment period t.

4. Convert r into decimal form.

5. Calculate the exponent:

   x = rt

6. Calculate the continuous accumulation factor:

   F = e^x

7. Calculate the accumulated amount:

   A(t) = A₀ × F

8. Calculate the interest earned:

   I = A(t) − A₀

9. Display the accumulated amount and interest earned.

### Pseudocode

```text
START

INPUT A0, r, t

CONVERT r TO decimal

x = r * t

F = e ^ x

A = A0 * F

I = A - A0

DISPLAY A
DISPLAY I

END
```


---

## 5. Algorithm for Effective Annual Interest Rate


### A. Discrete Compounding

**Formula:**

r_e = (1 + r/m)^m − 1

### Step-by-Step Algorithm

**Input:** r, m

**Output:** Effective annual interest rate r_e

**Procedure:**

1. Read the nominal annual interest rate r.

2. Read the compounding frequency m.

3. Convert r into decimal form.

4. Calculate the periodic interest rate:

   i = r/m

5. Calculate the annual accumulation factor:

   F = (1 + i)^m

6. Subtract 1:

   r_e = F − 1

7. Multiply the result by 100 to express it as a percentage.

8. Display the effective annual interest rate.

### Pseudocode

```text
START

INPUT r, m

CONVERT r TO decimal

i = r / m

F = (1 + i) ^ m

re = F - 1

re_percentage = re * 100

DISPLAY re_percentage

END
```

### B. Continuous Compounding

**Formula:**

r_e = e^r − 1

### Step-by-Step Algorithm

**Input:** r

**Output:** Effective annual interest rate r_e

**Procedure:**

1. Read the nominal annual interest rate r.

2. Convert r into decimal form.

3. Calculate the exponential factor:

   F = e^r

4. Subtract 1:

   r_e = F − 1

5. Multiply the result by 100 to express it as a percentage.

6. Display the effective annual interest rate.

### Pseudocode

```text
START

INPUT r

CONVERT r TO decimal

F = e ^ r

re = F - 1

re_percentage = re * 100

DISPLAY re_percentage

END
```

---

## 6. Algorithm for Comparing Different Interest Models

Sometimes a problem requires comparing simple interest, discrete compound interest, and continuous compound interest under the same initial conditions.

### Step-by-Step Algorithm

**Input:** A₀, r, t, and compounding frequency m

**Output:** Accumulated amounts under different interest models

**Procedure:**

1. Read A₀, r, t, and m.

2. Convert r into decimal form.

3. Calculate the simple interest accumulated amount:

   A_simple = A₀(1 + rt)

4. Calculate the discretely compounded amount:

   A_discrete = A₀(1 + r/m)^(mt)

5. Calculate the continuously compounded amount:

   A_continuous = A₀e^(rt)

6. Calculate interest earned under each method:

   I_simple = A_simple − A₀

   I_discrete = A_discrete − A₀

   I_continuous = A_continuous − A₀

7. Arrange the results in a comparison table.

8. Compare the accumulated amounts.

9. Identify which method produces the highest accumulated amount.

### Pseudocode

```text
START

INPUT A0, r, t, m

CONVERT r TO decimal

A_simple = A0 * (1 + r * t)

A_discrete = A0 * (1 + r/m) ^ (m*t)

A_continuous = A0 * e ^ (r*t)

I_simple = A_simple - A0

I_discrete = A_discrete - A0

I_continuous = A_continuous - A0

DISPLAY A_simple, A_discrete, A_continuous

DISPLAY I_simple, I_discrete, I_continuous

COMPARE accumulated amounts

END
```

---


## 7. Important Checks Before Submitting an Answer

After completing an interest calculation, verify the following:

1. **Principal:** Is the initial amount correctly identified?
2. **Rate:** Has the percentage been converted into decimal form?
3. **Time:** Is the time expressed in years when using an annual interest rate?
4. **Frequency:** Is the correct compounding frequency used?
5. **Periodic rate:** For discrete compounding, did you calculate r/m?
6. **Number of periods:** Did you calculate mt?
7. **Formula:** Does the selected formula match the interest model?
8. **Interest earned:** Did you subtract the initial principal from the accumulated amount?
9. **Percentage:** When reporting an effective annual rate, did you multiply the decimal result by 100?
10. **Rounding:** Did you keep sufficient precision during intermediate calculations and round only the final answer?

---

## 8. Formula Selection Guide

Use this table to identify the appropriate algorithm quickly.

| Problem Description                                   | Formula to Use              |
| ----------------------------------------------------- | --------------------------- |
| Interest is calculated only on the original principal | A(t) = A₀(1 + rt)           |
| Interest is compounded annually                       | A(t) = A₀(1 + r)^t          |
| Interest is compounded m times per year               | A(t) = A₀(1 + r/m)^(mt)     |
| Interest is compounded monthly                        | A(t) = A₀(1 + r/12)^(12t)   |
| Interest is compounded daily                          | A(t) = A₀(1 + r/365)^(365t) |
| Interest is compounded continuously                   | A(t) = A₀e^(rt)             |
| Effective annual rate for discrete compounding        | r_e = (1 + r/m)^m − 1       |
| Effective annual rate for continuous compounding      | r_e = e^r − 1               |
| Interest earned                                       | I = A(t) − A₀               |

---

## 9. Final Summary

The main purpose of these algorithms is to turn interest formulas into systematic calculation procedures.

The general approach is:

1. Identify the given financial information.
2. Determine the appropriate interest model.
3. Convert the annual interest rate into decimal form.
4. Calculate the periodic rate and number of periods when necessary.
5. Apply the appropriate mathematical formula.
6. Calculate the accumulated amount.
7. Determine the interest earned.
8. Interpret and verify the final result.

**Remember:** Choosing the correct interest model is the most important step. Once the model is identified, the calculation follows a clear and systematic procedure.


