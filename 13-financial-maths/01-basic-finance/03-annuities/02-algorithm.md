# Annuities — Algorithms and Step-by-Step Procedures

**Course:** Financial Mathematics (Math 4313)
**Chapter:** Basic Finance Concepts
**Topic:** Annuities
**Purpose:** To provide systematic procedures for solving annuity-related problems.

---

## 1. General Problem-Solving Procedure

Before solving an annuity problem, identify the type of payment sequence and determine what the problem requires.

### Required Inputs

| Symbol | Meaning                                           |
| ------ | ------------------------------------------------- |
| A₀     | Initial amount or initial account balance         |
| Aₙ     | Account balance immediately after the nth payment |
| P      | Fixed periodic deposit or withdrawal              |
| Q      | Monthly retirement withdrawal                     |
| r      | Nominal annual interest rate                      |
| m      | Number of compounding periods per year            |
| i      | Interest rate per period                          |
| n      | Number of elapsed periods                         |
| N      | Total number of payments or periods               |
| t      | Number of years during the saving period          |
| s      | Number of years during the withdrawal period      |
| r′     | Annual interest rate during the withdrawal period |
| i′     | Interest rate per withdrawal period               |
| Iₙ     | Interest portion of the nth loan payment          |
| Pₙ     | Principal portion of the nth loan payment         |

### General Algorithm

1. Read the problem carefully.

2. Identify whether the problem concerns deposits, withdrawals, retirement, or loan repayment.

3. Identify the initial amount and periodic payment.

4. Identify the annual interest rate and compounding frequency.

5. Convert the annual interest rate into decimal form.

6. Calculate the periodic interest rate:

   i = r/m

7. Determine the total number of periods:

   N = mt

8. Select the appropriate annuity formula.

9. Substitute the known values.

10. Perform the calculation.

11. Interpret the final result.

**Important:** The periodic payment interval and compounding interval must be the same when applying the ordinary annuity formulas in this chapter. Payments are assumed to occur at the end of each period.

---

## 2. Algorithm for Calculating the Future Value of Deposits

This procedure calculates the accumulated value of regular deposits made at the end of each period.

### Mathematical Formula

Aₙ = P[(1 + i)^n − 1]/i

Where:

* P = regular deposit.
* i = periodic interest rate.
* n = number of deposits.
* Aₙ = accumulated value after the nth deposit.

### Step-by-Step Algorithm

**Input:** P, r, m, n

**Output:** Future value Aₙ

**Procedure:**

1. Read the regular deposit P.

2. Read the annual interest rate r.

3. Read the compounding frequency m.

4. Read the number of periods n.

5. Convert r into decimal form.

6. Calculate the periodic interest rate:

   i = r/m

7. Calculate the accumulation factor:

   F = (1 + i)^n

8. Subtract 1:

   G = F − 1

9. Divide by the periodic interest rate:

   H = G/i

10. Multiply by the regular deposit:

    Aₙ = P × H

11. Display the accumulated value.

### Pseudocode

```text
START

INPUT P, r, m, n

CONVERT r TO decimal

i = r / m

F = (1 + i) ^ n

G = F - 1

H = G / i

An = P * H

DISPLAY An

END
```

### Worked Example 1: Future Value of Regular Deposits

**Problem:** A person deposits 2,000 ETB at the end of every month into an account earning 12% annual interest compounded monthly. Calculate the account balance after 2 years.

**Given:**

* P = 2,000 ETB
* r = 12% = 0.12
* m = 12
* t = 2 years
* n = 12 × 2 = 24

**Step 1: Calculate the monthly interest rate.**

i = r/m

i = 0.12/12

i = 0.01

**Step 2: Calculate the future value.**

Aₙ = P[(1 + i)^n − 1]/i

A₂₄ = 2000[(1.01)^24 − 1]/0.01

**A₂₄ ≈ 53,947.04 ETB**

**Interpretation:** After making 24 monthly deposits of 2,000 ETB, the account will contain approximately 53,947.04 ETB.

---

## 3. Algorithm for Calculating Future Value with an Initial Deposit

Sometimes an account begins with an initial deposit and receives additional regular deposits.

In this case, both the initial deposit and the periodic deposits earn interest.

### Mathematical Formula

Aₙ = A₀(1 + i)^n + P[(1 + i)^n − 1]/i

### Step-by-Step Algorithm

**Input:** A₀, P, r, m, n

**Output:** Future value Aₙ

**Procedure:**

1. Read the initial deposit A₀.

2. Read the regular deposit P.

3. Read the annual interest rate r.

4. Read the compounding frequency m.

5. Read the number of periods n.

6. Convert r into decimal form.

7. Calculate the periodic interest rate:

   i = r/m

8. Calculate the growth factor:

   F = (1 + i)^n

9. Calculate the future value of the initial deposit:

   B = A₀ × F

10. Calculate the future value of regular deposits:

    C = P(F − 1)/i

11. Add both amounts:

    Aₙ = B + C

12. Display the accumulated account balance.

### Pseudocode

```text
START

INPUT A0, P, r, m, n

CONVERT r TO decimal

i = r / m

F = (1 + i) ^ n

B = A0 * F

C = P * (F - 1) / i

An = B + C

DISPLAY An

END
```

---

## 4. Algorithm for Calculating the Number of Deposits Required

This procedure determines how many regular deposits are required to reach a specified future savings target.

### Mathematical Formula

Starting from:

A = A₀(1 + i)^n + P[(1 + i)^n − 1]/i

Solving for n gives:

n = [ln(iA + P) − ln(iA₀ + P)] / ln(1 + i)

Where:

* A = desired future value.
* A₀ = initial deposit.
* P = regular deposit.
* i = periodic interest rate.
* n = required number of deposits.

### Step-by-Step Algorithm

**Input:** A, A₀, P, r, m

**Output:** Number of required deposits n

**Procedure:**

1. Read the desired future amount A.

2. Read the initial deposit A₀.

3. Read the regular deposit P.

4. Read the annual interest rate r.

5. Read the compounding frequency m.

6. Convert r into decimal form.

7. Calculate the periodic interest rate:

   i = r/m

8. Calculate the numerator:

   X = ln(iA + P) − ln(iA₀ + P)

9. Calculate the denominator:

   Y = ln(1 + i)

10. Divide:

    n = X/Y

11. Round the result upward to the nearest integer because the target must be reached or exceeded.

12. Display the required number of deposits.

### Pseudocode

```text
START

INPUT A, A0, P, r, m

CONVERT r TO decimal

i = r / m

X = LN(i*A + P) - LN(i*A0 + P)

Y = LN(1 + i)

n = X / Y

n = ROUND UP n TO NEXT INTEGER

DISPLAY n

END
```

**Important:** The rounded-up value is the smallest whole number of deposits that makes the account balance at least equal to the target amount.

---

## 5. Algorithm for Calculating the Balance of a Withdrawal Annuity

A withdrawal annuity occurs when a fixed amount is withdrawn from an interest-bearing account at the end of each period.

The account earns interest before each withdrawal is made.

### Mathematical Formula

Aₙ = A₀(1 + i)^n + P[1 − (1 + i)^n]/i

Here, P represents the withdrawal amount.

### Step-by-Step Algorithm

**Input:** A₀, P, r, m, n

**Output:** Remaining account balance Aₙ

**Procedure:**

1. Read the initial account balance A₀.

2. Read the fixed withdrawal P.

3. Read the annual interest rate r.

4. Read the compounding frequency m.

5. Read the number of withdrawals n.

6. Convert r into decimal form.

7. Calculate the periodic interest rate:

   i = r/m

8. Calculate the accumulation factor:

   F = (1 + i)^n

9. Calculate the accumulated initial balance:

   B = A₀ × F

10. Calculate the accumulated effect of withdrawals:

    C = P(1 − F)/i

11. Calculate the remaining account balance:

    Aₙ = B + C

12. Display the remaining balance.

### Pseudocode

```text
START

INPUT A0, P, r, m, n

CONVERT r TO decimal

i = r / m

F = (1 + i) ^ n

B = A0 * F

C = P * (1 - F) / i

An = B + C

DISPLAY An

END
```

### Worked Example 2: Remaining Balance After Withdrawals

**Problem:** An account initially contains 100,000 ETB and earns 12% annual interest compounded monthly. The owner withdraws 3,000 ETB at the end of every month. Calculate the remaining balance after one month.

**Given:**

* A₀ = 100,000 ETB
* P = 3,000 ETB
* r = 0.12
* m = 12
* n = 1

**Step 1: Calculate the monthly interest rate.**

i = 0.12/12 = 0.01

**Step 2: Calculate the remaining balance.**

A₁ = A₀(1 + i) + P[1 − (1 + i)]/i

A₁ = 100,000(1.01) + 3,000(1 − 1.01)/0.01

A₁ = 101,000 − 3,000

**A₁ = 98,000 ETB**

**Interpretation:** The account earns 1,000 ETB interest during the first month. After withdrawing 3,000 ETB, the remaining balance is 98,000 ETB.

---

## 6. Algorithm for Calculating the Present Value of an Annuity

The present value of an annuity is the initial amount required today to support a specified sequence of future withdrawals.

### Mathematical Formula

A₀ = P[1 − (1 + i)^(-N)]/i

Where:

* A₀ = present value or initial deposit.
* P = fixed periodic withdrawal.
* i = periodic interest rate.
* N = total number of withdrawals.

### Step-by-Step Algorithm

**Input:** P, r, m, N

**Output:** Present value A₀

**Procedure:**

1. Read the periodic withdrawal P.

2. Read the annual interest rate r.

3. Read the compounding frequency m.

4. Read the total number of withdrawals N.

5. Convert r into decimal form.

6. Calculate the periodic interest rate:

   i = r/m

7. Calculate the discount factor:

   F = (1 + i)^(-N)

8. Subtract the discount factor from 1:

   G = 1 − F

9. Divide by the periodic interest rate:

   H = G/i

10. Multiply by the periodic withdrawal:

    A₀ = P × H

11. Display the required initial deposit.

### Pseudocode

```text
START

INPUT P, r, m, N

CONVERT r TO decimal

i = r / m

F = (1 + i) ^ (-N)

G = 1 - F

H = G / i

A0 = P * H

DISPLAY A0

END
```

### Worked Example 3: Present Value of Future Withdrawals

**Problem:** A person wants to withdraw 4,000 ETB at the end of every month for 5 years. If the account earns 12% annual interest compounded monthly, how much money must be deposited initially?

**Given:**

* P = 4,000 ETB
* r = 0.12
* m = 12
* N = 5 × 12 = 60

**Step 1: Calculate the monthly interest rate.**

i = 0.12/12 = 0.01

**Step 2: Calculate the present value.**

A₀ = P[1 − (1 + i)^(-N)]/i

A₀ = 4000[1 − (1.01)^(-60)]/0.01

**A₀ ≈ 179,695.55 ETB**

**Interpretation:** Approximately 179,695.55 ETB must be deposited today to support 60 monthly withdrawals of 4,000 ETB, assuming the stated interest rate and withdrawal timing.

---

## 7. Algorithm for Calculating Periodic Withdrawals

This procedure calculates the fixed amount that can be withdrawn at the end of each period from an initial account balance.

### Mathematical Formula

P = A₀i/[1 − (1 + i)^(-N)]

### Step-by-Step Algorithm

**Input:** A₀, r, m, N

**Output:** Periodic withdrawal P

**Procedure:**

1. Read the initial account balance A₀.

2. Read the annual interest rate r.

3. Read the compounding frequency m.

4. Read the total number of withdrawals N.

5. Convert r into decimal form.

6. Calculate the periodic interest rate:

   i = r/m

7. Calculate the discount factor:

   F = (1 + i)^(-N)

8. Calculate the denominator:

   D = 1 − F

9. Calculate the periodic withdrawal:

   P = A₀i/D

10. Display the periodic withdrawal amount.

### Pseudocode

```text
START

INPUT A0, r, m, N

CONVERT r TO decimal

i = r / m

F = (1 + i) ^ (-N)

D = 1 - F

P = (A0 * i) / D

DISPLAY P

END
```

**Application:** This formula is useful for calculating fixed retirement withdrawals and mortgage payments.

---

## 8. Algorithm for Calculating Outstanding Balance

This procedure calculates the amount remaining in an account after a specified number of withdrawals when the account is designed to reach zero after exactly N withdrawals.

### Mathematical Formula

Aₙ = A₀[1 − (1 + i)^(n − N)]/[1 − (1 + i)^(-N)]

Where:

* A₀ = initial account balance.
* i = periodic interest rate.
* n = number of withdrawals already made.
* N = total planned withdrawals.
* Aₙ = remaining balance immediately after the nth withdrawal.

### Step-by-Step Algorithm

**Input:** A₀, r, m, n, N

**Output:** Outstanding balance Aₙ

**Procedure:**

1. Read the initial account balance A₀.

2. Read the annual interest rate r.

3. Read the compounding frequency m.

4. Read the number of completed withdrawals n.

5. Read the total number of planned withdrawals N.

6. Convert r into decimal form.

7. Calculate the periodic interest rate:

   i = r/m

8. Calculate the numerator:

   X = 1 − (1 + i)^(n − N)

9. Calculate the denominator:

   Y = 1 − (1 + i)^(-N)

10. Calculate the remaining balance:

    Aₙ = A₀(X/Y)

11. Display the outstanding balance.

### Pseudocode

```text
START

INPUT A0, r, m, n, N

CONVERT r TO decimal

i = r / m

X = 1 - (1 + i) ^ (n - N)

Y = 1 - (1 + i) ^ (-N)

An = A0 * (X / Y)

DISPLAY An

END
```

**Important checks:**

* When n = 0, the outstanding balance must equal A₀.
* When n = N, the outstanding balance must equal zero.

---

## 9. Algorithm for Retirement Planning

Retirement planning combines two annuity calculations:

1. Accumulating money through regular monthly deposits before retirement.
2. Withdrawing a fixed amount every month after retirement.

The final value of the savings account becomes the initial value of the retirement withdrawal account.

### Mathematical Formulas

Monthly interest rate during saving:

i = r/12

Monthly interest rate during retirement:

i′ = r′/12

Total saving periods:

12t

Total withdrawal periods:

12s

Future value of monthly savings:

A = P[(1 + i)^(12t) − 1]/i

Present value required for monthly retirement withdrawals:

A = Q[1 − (1 + i′)^(-12s)]/i′

Equating both values and solving for P:

P = {Q × i × [1 − (1 + i′)^(-12s)]}/{i′[(1 + i)^(12t) − 1]}

### Step-by-Step Algorithm

**Input:** Q, r, r′, t, s

**Output:** Required monthly retirement savings P

**Procedure:**

1. Read the desired monthly retirement withdrawal Q.

2. Read the annual interest rate during the saving period r.

3. Read the annual interest rate during retirement r′.

4. Read the number of saving years t.

5. Read the number of retirement years s.

6. Convert r and r′ into decimal form.

7. Calculate the monthly saving interest rate:

   i = r/12

8. Calculate the monthly retirement interest rate:

   i′ = r′/12

9. Calculate the total saving periods:

   N₁ = 12t

10. Calculate the total withdrawal periods:

    N₂ = 12s

11. Calculate the retirement withdrawal factor:

    X = 1 − (1 + i′)^(-N₂)

12. Calculate the saving accumulation factor:

    Y = (1 + i)^N₁ − 1

13. Calculate the required monthly saving:

    P = (Q × i × X)/(i′ × Y)

14. Display the required monthly saving amount.

### Pseudocode

```text
START

INPUT Q, r, r_prime, t, s

CONVERT r TO decimal
CONVERT r_prime TO decimal

i = r / 12

i_prime = r_prime / 12

N1 = 12 * t

N2 = 12 * s

X = 1 - (1 + i_prime) ^ (-N2)

Y = (1 + i) ^ N1 - 1

P = (Q * i * X) / (i_prime * Y)

DISPLAY P

END
```

**Interpretation:** The result is the monthly amount that must be saved during the working period to support the desired monthly withdrawals during retirement, under the assumed interest rates.

---

## 10. Algorithm for Calculating Loan Payments

A loan that is repaid through equal periodic payments can be modeled as a withdrawal annuity from the lender's perspective.

Each payment covers:

* Interest on the outstanding loan balance.
* Repayment of part of the principal.

### Mathematical Formula

P = A₀i/[1 − (1 + i)^(-N)]

Where:

* A₀ = original loan amount.
* i = periodic interest rate.
* N = total number of payments.
* P = fixed periodic loan payment.

For monthly mortgage payments:

i = r/12

N = 12t

### Step-by-Step Algorithm

**Input:** A₀, r, t

**Output:** Monthly loan payment P

**Procedure:**

1. Read the loan amount A₀.

2. Read the annual interest rate r.

3. Read the loan duration t in years.

4. Convert r into decimal form.

5. Calculate the monthly interest rate:

   i = r/12

6. Calculate the total number of monthly payments:

   N = 12t

7. Calculate the discount factor:

   F = (1 + i)^(-N)

8. Calculate the denominator:

   D = 1 − F

9. Calculate the monthly payment:

   P = A₀i/D

10. Calculate the total amount paid:

    Total = P × N

11. Calculate the total interest paid:

    Interest = Total − A₀

12. Display the monthly payment, total payments, and total interest.

### Pseudocode

```text
START

INPUT A0, r, t

CONVERT r TO decimal

i = r / 12

N = 12 * t

F = (1 + i) ^ (-N)

D = 1 - F

P = (A0 * i) / D

Total = P * N

Interest = Total - A0

DISPLAY P
DISPLAY Total
DISPLAY Interest

END
```

### Worked Example 4: Monthly Mortgage Payment

**Problem:** A person borrows 1,000,000 ETB at an annual interest rate of 12%, compounded monthly, and agrees to repay the loan over 10 years. Calculate the monthly payment and total interest.

**Given:**

* A₀ = 1,000,000 ETB
* r = 12% = 0.12
* t = 10 years

**Step 1: Calculate the monthly interest rate.**

i = 0.12/12

i = 0.01

**Step 2: Calculate the total number of payments.**

N = 12 × 10

N = 120

**Step 3: Calculate the monthly payment.**

P = A₀i/[1 − (1 + i)^(-N)]

P = (1,000,000 × 0.01)/[1 − (1.01)^(-120)]

**P ≈ 14,347.09 ETB**

**Step 4: Calculate total payments.**

Total = P × N

Total = 14,347.09 × 120

**Total ≈ 1,721,650.80 ETB**

**Step 5: Calculate total interest.**

Interest = Total − A₀

Interest = 1,721,650.80 − 1,000,000

**Interest ≈ 721,650.80 ETB**

### Final Results

| Quantity           |           Result |
| ------------------ | ---------------: |
| Original loan      |    1,000,000 ETB |
| Monthly payment    |    14,347.09 ETB |
| Number of payments |              120 |
| Total payments     | 1,721,650.80 ETB |
| Total interest     |   721,650.80 ETB |

---

## 11. Algorithm for Constructing an Amortization Schedule

An amortization schedule shows how each loan payment is divided between interest and principal and how the outstanding balance decreases over time.

### Mathematical Relationships

Monthly interest rate:

i = r/12

Number of payments:

N = 12t

Monthly payment:

P = A₀i/[1 − (1 + i)^(-N)]

Interest portion:

Iₙ = iAₙ₋₁

Principal portion:

Pₙ = P − Iₙ

New outstanding balance:

Aₙ = Aₙ₋₁ − Pₙ

### Step-by-Step Algorithm

**Input:** A₀, r, t

**Output:** Complete amortization schedule

**Procedure:**

1. Read the original loan amount A₀.

2. Read the annual interest rate r.

3. Read the loan duration t.

4. Convert r into decimal form.

5. Calculate the monthly interest rate:

   i = r/12

6. Calculate the total number of monthly payments:

   N = 12t

7. Calculate the fixed monthly payment:

   P = A₀i/[1 − (1 + i)^(-N)]

8. Set the initial outstanding balance:

   Balance = A₀

9. Repeat the following steps for each payment from 1 to N:

   a. Calculate the interest portion:

   Iₙ = i × Balance

   b. Calculate the principal portion:

   Pₙ = P − Iₙ

   c. Calculate the new outstanding balance:

   Balance = Balance − Pₙ

   d. Record the payment number, total payment, interest, principal, and remaining balance.

10. Display the complete amortization schedule.

### Pseudocode

```text
START

INPUT A0, r, t

CONVERT r TO decimal

i = r / 12

N = 12 * t

P = (A0 * i) / (1 - (1 + i)^(-N))

Balance = A0

FOR n = 1 TO N

    Interest = i * Balance

    Principal = P - Interest

    Balance = Balance - Principal

    IF n = N THEN
        Balance = 0
    END IF

    DISPLAY n, P, Interest, Principal, Balance

END FOR

END
```

**Note:** The final balance is set to zero to handle small rounding differences. In an actual loan calculation, the final payment may need a minor adjustment due to rounding.

---

## 12. Algorithm for Calculating Interest and Principal Portions

This procedure calculates how much of a particular loan payment goes toward interest and how much reduces the original loan.

### Mathematical Formulas

Interest portion:

Iₙ = iAₙ₋₁

Principal portion:

Pₙ = P − Iₙ

Where:

* Aₙ₋₁ = outstanding balance before the nth payment.
* i = periodic interest rate.
* P = fixed loan payment.

### Step-by-Step Algorithm

**Input:** Aₙ₋₁, i, P

**Output:** Interest portion Iₙ and principal portion Pₙ

**Procedure:**

1. Read the outstanding balance before the payment Aₙ₋₁.

2. Read the periodic interest rate i.

3. Read the fixed payment P.

4. Calculate the interest portion:

   Iₙ = i × Aₙ₋₁

5. Calculate the principal portion:

   Pₙ = P − Iₙ

6. Calculate the new outstanding balance:

   Aₙ = Aₙ₋₁ − Pₙ

7. Display the interest portion, principal portion, and new balance.

### Pseudocode

```text
START

INPUT Previous_Balance, i, P

Interest = i * Previous_Balance

Principal = P - Interest

New_Balance = Previous_Balance - Principal

DISPLAY Interest
DISPLAY Principal
DISPLAY New_Balance

END
```

### Worked Example 5: First Loan Payment

**Problem:** A borrower has an outstanding loan balance of 100,000 ETB. The monthly interest rate is 1%, and the monthly payment is 3,000 ETB. Calculate the interest portion, principal portion, and new balance.

**Given:**

* Previous balance = 100,000 ETB
* i = 0.01
* P = 3,000 ETB

**Step 1: Calculate interest.**

I₁ = i × A₀

I₁ = 0.01 × 100,000

**I₁ = 1,000 ETB**

**Step 2: Calculate principal repayment.**

P₁ = P − I₁

P₁ = 3,000 − 1,000

**P₁ = 2,000 ETB**

**Step 3: Calculate the new balance.**

A₁ = A₀ − P₁

A₁ = 100,000 − 2,000

**A₁ = 98,000 ETB**

---

## 13. Algorithm for Calculating the Interest-to-Principal Ratio

The interest-to-principal ratio measures the relationship between the interest portion and principal portion of a loan payment.

### Mathematical Formula

Iₙ/Pₙ = (1 + i)^(N + 1 − n) − 1

Where:

* i = periodic interest rate.
* N = total number of payments.
* n = payment number.
* Iₙ = interest portion.
* Pₙ = principal portion.

### Step-by-Step Algorithm

**Input:** i, N, n

**Output:** Interest-to-principal ratio

**Procedure:**

1. Read the periodic interest rate i.

2. Read the total number of payments N.

3. Read the payment number n.

4. Calculate the exponent:

   E = N + 1 − n

5. Calculate the growth factor:

   F = (1 + i)^E

6. Subtract 1:

   R = F − 1

7. Display the interest-to-principal ratio.

### Pseudocode

```text
START

INPUT i, N, n

E = N + 1 - n

F = (1 + i) ^ E

R = F - 1

DISPLAY R

END
```

### Interpretation

The ratio decreases as the payment number increases.

* At the beginning of the loan, a larger proportion of the payment goes toward interest.
* As the loan balance decreases, the interest portion becomes smaller.
* More of each payment goes toward reducing the principal.
* At the final payment, the ratio reaches its minimum value, i.

**Important:** The ratio compares interest with principal, not interest with the total payment.

---

## 14. Complete Worked Example: Loan Amortization

### Problem

A person borrows 1,000,000 ETB at 12% annual interest compounded monthly for 10 years.

Calculate:

1. The monthly payment.
2. The interest portion of the first payment.
3. The principal portion of the first payment.
4. The remaining loan balance after the first payment.
5. The interest-to-principal ratio of the first payment.

### Given Information

* A₀ = 1,000,000 ETB
* r = 0.12
* t = 10 years
* m = 12

### Step 1: Calculate the Monthly Interest Rate

i = r/12

i = 0.12/12

**i = 0.01**

### Step 2: Calculate the Total Number of Payments

N = 12 × 10

**N = 120**

### Step 3: Calculate the Monthly Payment

P = A₀i/[1 − (1 + i)^(-N)]

P = (1,000,000 × 0.01)/[1 − (1.01)^(-120)]

**P ≈ 14,347.09 ETB**

### Step 4: Calculate the Interest Portion of the First Payment

I₁ = iA₀

I₁ = 0.01 × 1,000,000

**I₁ = 10,000 ETB**

### Step 5: Calculate the Principal Portion

P₁ = P − I₁

P₁ = 14,347.09 − 10,000

**P₁ ≈ 4,347.09 ETB**

### Step 6: Calculate the Remaining Balance

A₁ = A₀ − P₁

A₁ = 1,000,000 − 4,347.09

**A₁ ≈ 995,652.91 ETB**

### Step 7: Calculate the Interest-to-Principal Ratio

I₁/P₁ = (1 + i)^(N + 1 − 1) − 1

I₁/P₁ = (1.01)^120 − 1

**I₁/P₁ ≈ 2.3004**

This means the interest portion of the first payment is approximately 2.3004 times the principal portion.

### First Payment Summary

| Component                   |         Amount |
| --------------------------- | -------------: |
| Monthly payment             |  14,347.09 ETB |
| Interest portion            |  10,000.00 ETB |
| Principal portion           |   4,347.09 ETB |
| Remaining balance           | 995,652.91 ETB |
| Interest-to-principal ratio |         2.3004 |

---

## 15. Important Checks Before Submitting an Answer

Before finalizing an annuity calculation, verify the following:

1. **Payment timing:** Are payments made at the end of each period? The formulas in this chapter assume ordinary annuities.
2. **Interest rate:** Did you convert the annual percentage rate into decimal form?
3. **Periodic rate:** Did you divide the annual rate by the compounding frequency?
4. **Number of periods:** Did you multiply the number of years by the number of periods per year?
5. **Deposit or withdrawal:** Did you select the correct formula for the type of annuity?
6. **Initial deposit:** If an initial deposit exists, did you include its accumulated value?
7. **Withdrawal balance:** Did you subtract withdrawals after accounting for interest?
8. **Present value:** Did you use the discount factor with a negative exponent?
9. **Loan payment:** Did you calculate the monthly payment using the total number of monthly payments?
10. **Amortization:** Does each payment equal its interest portion plus its principal portion?
11. **Outstanding balance:** Does the balance decrease after each payment?
12. **Final balance:** Does the balance become zero after the planned final withdrawal or payment?
13. **Rounding:** Did you retain sufficient precision during intermediate calculations?

---

## 16. Formula Selection Guide

Use this table to identify the appropriate algorithm quickly.

| Problem Description                  | Formula                                               |
| ------------------------------------ | ----------------------------------------------------- |
| Future value of regular deposits     | Aₙ = P[(1 + i)^n − 1]/i                               |
| Future value with initial deposit    | Aₙ = A₀(1 + i)^n + P[(1 + i)^n − 1]/i                 |
| Number of deposits required          | n = [ln(iA + P) − ln(iA₀ + P)]/ln(1 + i)              |
| Remaining balance after withdrawals  | Aₙ = A₀(1 + i)^n + P[1 − (1 + i)^n]/i                 |
| Present value of withdrawals         | A₀ = P[1 − (1 + i)^(-N)]/i                            |
| Fixed periodic withdrawal            | P = A₀i/[1 − (1 + i)^(-N)]                            |
| Outstanding balance after n payments | Aₙ = A₀[1 − (1 + i)^(n − N)]/[1 − (1 + i)^(-N)]       |
| Monthly retirement savings           | P = {Qi[1 − (1 + i′)^(-12s)]}/{i′[(1 + i)^(12t) − 1]} |
| Monthly loan payment                 | P = A₀i/[1 − (1 + i)^(-N)]                            |
| Interest portion                     | Iₙ = iAₙ₋₁                                            |
| Principal portion                    | Pₙ = P − Iₙ                                           |
| New outstanding loan balance         | Aₙ = Aₙ₋₁ − Pₙ                                        |
| Interest-to-principal ratio          | Iₙ/Pₙ = (1 + i)^(N + 1 − n) − 1                       |

---

## 17. Final Summary

Annuity calculations involve regular deposits or withdrawals made over a specified period.

The main calculation procedures are:

1. **Deposits:** Calculate the accumulated value of regular savings.
2. **Initial deposits:** Combine the accumulated initial amount with regular deposits.
3. **Number of deposits:** Determine how many payments are required to reach a savings target.
4. **Withdrawals:** Calculate the remaining account balance after regular withdrawals.
5. **Present value:** Determine the initial amount required to support future withdrawals.
6. **Retirement planning:** Calculate the monthly savings required to finance future retirement withdrawals.
7. **Loan repayment:** Calculate fixed periodic loan payments.
8. **Amortization:** Separate each loan payment into interest and principal and update the outstanding balance.

The general approach is:

1. Identify the type of annuity.
2. Identify the known values and required quantity.
3. Convert the annual interest rate into a periodic rate.
4. Calculate the total number of periods.
5. Select the correct formula.
6. Substitute the known values.
7. Perform the calculation.
8. Check and interpret the result.

**Remember:** The most important step in solving an annuity problem is identifying whether the problem involves deposits, withdrawals, or loan repayment. Once this is clear, selecting the correct formula becomes much easier.

