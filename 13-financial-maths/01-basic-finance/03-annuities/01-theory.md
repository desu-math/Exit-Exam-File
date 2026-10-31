# 📘 Annuities — Financial Mathematics

> **Course:** Financial Mathematics (Math4313)
> **Topic:** Annuities
> **Purpose:** Understand how regular deposits and withdrawals accumulate over time, calculate present and future values of annuities, and apply annuity mathematics to retirement planning and loan amortization.

---

## 📑 Table of Contents

1. [Learning Objectives](#1-learning-objectives)
2. [What Is an Annuity?](#2-what-is-an-annuity)
3. [Important Notation and Assumptions](#3-important-notation-and-assumptions)
4. [Ordinary Annuities](#4-ordinary-annuities)
5. [Deposits and Sinking Funds](#5-deposits-and-sinking-funds)
6. [Derivation of the Future Value of an Annuity](#6-derivation-of-the-future-value-of-an-annuity)
7. [Future Value with an Initial Deposit](#7-future-value-with-an-initial-deposit)
8. [Withdrawals](#8-withdrawals)
9. [Derivation of the Withdrawal Formula](#9-derivation-of-the-withdrawal-formula)
10. [Present Value of an Annuity](#10-present-value-of-an-annuity)
11. [Derivation of the Present Value Formula](#11-derivation-of-the-present-value-formula)
12. [Calculating the Periodic Withdrawal](#12-calculating-the-periodic-withdrawal)
13. [Retirement Planning](#13-retirement-planning)
14. [Loan Amortization](#14-loan-amortization)
15. [Mortgage Payment Formula](#15-mortgage-payment-formula)
16. [Outstanding Loan Balance](#16-outstanding-loan-balance)
17. [Interest and Principal Components](#17-interest-and-principal-components)
18. [Amortization Schedule and Payment Ratios](#18-amortization-schedule-and-payment-ratios)
19. [Ordinary Annuity versus Annuity Due](#19-ordinary-annuity-versus-annuity-due)
20. [Practical Applications](#20-practical-applications)
21. [Common Mistakes](#21-common-mistakes)
22. [Formula Summary](#22-formula-summary)
23. [Practice Questions](#23-practice-questions)
24. [Solutions to Practice Questions](#24-solutions-to-practice-questions)
25. [Conclusion](#25-conclusion)

---

## 1. Learning Objectives

After studying this topic, you should be able to:

* Define an annuity and identify its practical applications.
* Explain the difference between deposits and withdrawals.
* Understand ordinary annuities and payment timing.
* Derive the future value formula for regular deposits.
* Calculate the accumulated value of a sinking fund.
* Derive the withdrawal and present value formulas.
* Calculate regular withdrawals from an investment account.
* Apply annuity mathematics to retirement planning.
* Understand loan amortization and mortgage payments.
* Calculate outstanding loan balances.
* Separate loan payments into interest and principal components.
* Interpret an amortization schedule.

---

## 2. What Is an Annuity?

### Definition

An **annuity** is a sequence of periodic payments of a fixed amount.

In simple language, an annuity involves paying or receiving the same amount of money repeatedly at regular intervals.

Examples include:

* Social Security funds.
* Pension payments.
* Car-loan payments.
* Credit card debt payments.
* Mortgage payments.

### Example

Suppose you deposit 1,000 birr into a savings account at the end of every month.

Your payments look like this:

| Month |    Deposit |
| ----- | ---------: |
| 1     | 1,000 birr |
| 2     | 1,000 birr |
| 3     | 1,000 birr |
| 4     | 1,000 birr |
| 5     | 1,000 birr |

This is an annuity because you make equal payments at regular intervals.

However, if the account earns interest, the final balance will generally be greater than the total amount deposited.

Why?

Because earlier deposits have more time to earn interest than later deposits.

This is the central idea behind annuity mathematics.

---

## 3. Important Notation and Assumptions

Before studying the formulas, understand the following symbols.

| Symbol | Meaning                                         |
| ------ | ----------------------------------------------- |
| A₀     | Initial amount or present value                 |
| Aₙ     | Account value immediately after the nth payment |
| P      | Fixed periodic deposit or withdrawal            |
| r      | Nominal annual interest rate                    |
| m      | Number of compounding periods per year          |
| i      | Interest rate per compounding period            |
| n      | Number of periods                               |
| N      | Total number of planned payments                |
| t      | Time in years                                   |
| Q      | Monthly retirement withdrawal                   |

### Periodic interest rate

Your instructor assumes that interest is charged or earned at an annual rate r, compounded m times per year.

Therefore, the interest rate per compounding period is:

**i = r/m**

For example, if the nominal annual interest rate is 12% and interest is compounded monthly:

r = 0.12

m = 12

Therefore:

i = 0.12/12

**i = 0.01 = 1% per month**

### Number of periods

If payments are made monthly for t years:

**n = 12t**

For example, monthly payments for 5 years give:

n = 12 × 5 = 60 periods.

### Important assumptions

Unless otherwise stated, the formulas in this note assume:

1. The interest rate is constant.
2. Payments are equal in amount.
3. Payments occur at the end of each compounding period.
4. The interest rate and payment frequency are consistent.

These assumptions are important when selecting the correct formula.

---

## 4. Ordinary Annuities

### Definition

An **ordinary annuity** is an annuity in which payments are made at the end of each period.

For example, if you deposit money at the end of every month, your deposits form an ordinary annuity.

Your instructor's annuity formulas are based on this payment arrangement.

### Payment timeline

Suppose you deposit P birr at the end of each period.

| Time | Event          |
| ---- | -------------- |
| 0    | Initial time   |
| 1    | First deposit  |
| 2    | Second deposit |
| 3    | Third deposit  |
| 4    | Fourth deposit |
| n    | nth deposit    |

The timing matters because each deposit earns interest for a different number of periods.

For example, at the end of the third period:

* The first deposit earns interest for two periods.
* The second deposit earns interest for one period.
* The third deposit earns no interest yet.

This difference in earning periods is the reason we need an annuity formula.

---

## 5. Deposits and Sinking Funds

### Definition

A **sinking fund** is an account into which regular deposits are made to accumulate money for a future purpose.

For example, suppose you want to save money to buy a car after five years.

You decide to deposit a fixed amount every month into an interest-bearing account.

Your goal is to accumulate a sufficiently large amount by the end of five years.

This is a sinking-fund problem.

### Central question

If I deposit P birr at the end of every period, how much money will I have after n periods?

To answer this question, we need the future value of an annuity.

---

## 6. Derivation of the Future Value of an Annuity

Your instructor gives the following formula for an ordinary annuity with equal deposits:

# **Aₙ = P[(1 + i)ⁿ − 1]/i**

Let's derive it step by step.

### Step 1: Consider the first deposit

Suppose you deposit P birr at the end of the first period.

Because the deposit is made at the end of the period, it has not yet earned interest.

Therefore:

A₁ = P

### Step 2: Consider the second deposit

During the second period, the first deposit earns interest.

Its value becomes:

P(1 + i)

At the end of the second period, you make another deposit of P.

Therefore:

A₂ = P(1 + i) + P

Factor out P:

A₂ = P[(1 + i) + 1]

### Step 3: Consider the third deposit

During the third period:

* The first deposit earns interest for two periods.
* The second deposit earns interest for one period.
* The third deposit is made at the end of the period.

Their values are:

First deposit: P(1 + i)²

Second deposit: P(1 + i)

Third deposit: P

Therefore:

A₃ = P(1 + i)² + P(1 + i) + P

Factor out P:

A₃ = P[(1 + i)² + (1 + i) + 1]

### Step 4: Generalize to n periods

After n periods, the first deposit has earned interest for n − 1 periods.

The second deposit has earned interest for n − 2 periods.

The last deposit has not yet earned interest.

Therefore:

Aₙ = P(1 + i)ⁿ⁻¹ + P(1 + i)ⁿ⁻² + ... + P(1 + i) + P

Factor out P:

Aₙ = P[(1 + i)ⁿ⁻¹ + (1 + i)ⁿ⁻² + ... + (1 + i) + 1]

### Step 5: Apply the geometric-series formula

Recall the finite geometric-series formula:

1 + q + q² + ... + qⁿ⁻¹ = (qⁿ − 1)/(q − 1)

In our expression:

q = 1 + i

Therefore:

1 + (1 + i) + ... + (1 + i)ⁿ⁻¹

= [(1 + i)ⁿ − 1]/[(1 + i) − 1]

Since:

(1 + i) − 1 = i

We obtain:

**Aₙ = P[(1 + i)ⁿ − 1]/i**

This is the future value of an ordinary annuity.

### Interpretation

The formula calculates the total accumulated value of all regular deposits, including the interest earned by each deposit.

The future value depends on:

* The amount of each deposit, P.
* The interest rate per period, i.
* The number of periods, n.

Increasing the deposit amount, interest rate, or saving period generally increases the accumulated value.

---

## 7. Future Value with an Initial Deposit

Sometimes an account already contains money before regular deposits begin.

Suppose:

* You initially deposit A₀ birr.
* You then deposit P birr at the end of every period.
* The interest rate per period is i.
* You make n regular deposits.

### Step 1: Calculate the future value of the initial deposit

The initial deposit earns interest for all n periods.

Therefore:

Future value of initial deposit = A₀(1 + i)ⁿ

### Step 2: Calculate the future value of regular deposits

From the previous section:

Future value of regular deposits = P[(1 + i)ⁿ − 1]/i

### Step 3: Add the two amounts

The total account value is the sum of the two future values.

Therefore:

# **Aₙ = A₀(1 + i)ⁿ + P[(1 + i)ⁿ − 1]/i**

This is the future value of an account containing an initial deposit followed by regular deposits.

### Worked Example

Suppose an account starts with 5,000 birr. You deposit another 1,000 birr at the end of each month for 12 months. The account earns 1% interest per month.

#### Given

A₀ = 5,000 birr

P = 1,000 birr

i = 0.01

n = 12

#### Formula

Aₙ = A₀(1 + i)ⁿ + P[(1 + i)ⁿ − 1]/i

#### Calculation

A₁₂ = 5,000(1.01)¹² + 1,000[(1.01)¹² − 1]/0.01

The future value of the initial deposit is:

5,000(1.01)¹² ≈ 5,634.13

The future value of the regular deposits is:

1,000[(1.01)¹² − 1]/0.01 ≈ 12,682.50

Therefore:

A₁₂ ≈ 5,634.13 + 12,682.50

**A₁₂ ≈ 18,316.63 birr**

#### Interpretation

The account contains approximately 18,316.63 birr immediately after the twelfth deposit.

---

<!-- PAGE BREAK -->

## 8. Withdrawals

So far, we have studied regular deposits.

Now consider the opposite situation.

Suppose you already have money in an account and withdraw a fixed amount at the end of every period.

Examples include:

* Monthly pension payments.
* Retirement withdrawals.
* Regular withdrawals from savings.
* Fixed payments made from an investment account.

The central question is:

**If I begin with A₀ birr and withdraw P birr every period, how much money will remain after n withdrawals?**

Your instructor gives the following formula:

**Aₙ = A₀(1 + i)ⁿ + P[1 − (1 + i)ⁿ]/i**

We will derive it in the next section.

---

## 9. Derivation of the Withdrawal Formula

We assume that the account earns interest during each period and the withdrawal occurs at the end of that period.

### Step 1: Calculate the balance after the first withdrawal

The initial balance is A₀.

After one period, it earns interest:

A₀(1 + i)

Then you withdraw P.

Therefore:

A₁ = A₀(1 + i) − P

### Step 2: Calculate the balance after the second withdrawal

The balance after the first withdrawal is A₁.

During the second period, this balance earns interest:

A₁(1 + i)

Then you withdraw P again:

A₂ = A₁(1 + i) − P

Substitute A₁:

A₂ = [A₀(1 + i) − P](1 + i) − P

Expand:

A₂ = A₀(1 + i)² − P(1 + i) − P

Therefore:

A₂ = A₀(1 + i)² − P[(1 + i) + 1]

### Step 3: Calculate the balance after the third withdrawal

Similarly:

A₃ = A₂(1 + i) − P

Substitute the expression for A₂:

A₃ = A₀(1 + i)³ − P(1 + i)² − P(1 + i) − P

Therefore:

A₃ = A₀(1 + i)³ − P[(1 + i)² + (1 + i) + 1]

### Step 4: Generalize to n withdrawals

Continuing the pattern:

Aₙ = A₀(1 + i)ⁿ − P[(1 + i)ⁿ⁻¹ + ... + (1 + i) + 1]

Apply the geometric-series formula:

Aₙ = A₀(1 + i)ⁿ − P[(1 + i)ⁿ − 1]/i

Rearrange the withdrawal term:

# **Aₙ = A₀(1 + i)ⁿ + P[1 − (1 + i)ⁿ]/i**

This is the withdrawal annuity formula.

### Interpretation

The formula contains two parts:

1. A₀(1 + i)ⁿ represents the initial balance accumulated with interest.
2. P[1 − (1 + i)ⁿ]/i represents the effect of the repeated withdrawals.

For a positive interest rate, the withdrawal term is negative. Therefore, withdrawals reduce the account balance.

---

## 10. Present Value of an Annuity

One of the most important annuity problems is determining how much money is needed today to support a specified sequence of future withdrawals.

For example, suppose you want to withdraw 5,000 birr at the end of every month for 10 years.

How much money must you deposit initially if the account earns interest?

Your instructor gives the following formula:

# **A₀ = P[1 − (1 + i)⁻ᴺ]/i**

This is the present value of an ordinary annuity.

### Meaning

The formula calculates the amount of money required today to support exactly N equal withdrawals at the end of each period.

It is particularly useful in:

* Retirement planning.
* Pension calculations.
* Trust funds.
* Loan and mortgage calculations.

---

## 11. Derivation of the Present Value Formula

Start with the withdrawal formula:

Aₙ = A₀(1 + i)ⁿ + P[1 − (1 + i)ⁿ]/i

Suppose the account must be exhausted exactly after N withdrawals.

This means:

Aₙ = 0 when n = N

### Step 1: Substitute the final balance

0 = A₀(1 + i)ᴺ + P[1 − (1 + i)ᴺ]/i

### Step 2: Move the withdrawal term

A₀(1 + i)ᴺ = P[(1 + i)ᴺ − 1]/i

### Step 3: Divide by (1 + i)ᴺ

A₀ = P[(1 + i)ᴺ − 1]/[i(1 + i)ᴺ]

### Step 4: Simplify

Notice that:

[(1 + i)ᴺ − 1]/(1 + i)ᴺ = 1 − (1 + i)⁻ᴺ

Therefore:

# **A₀ = P[1 − (1 + i)⁻ᴺ]/i**

This is the present value of an ordinary annuity.

### Important interpretation

The formula converts a sequence of future withdrawals into an equivalent amount of money at the present time.

It accounts for the fact that money available today can earn interest before the future withdrawals occur.

---

## 12. Calculating the Periodic Withdrawal

Sometimes the initial account balance is known, but the regular withdrawal amount is unknown.

For example, suppose you have 500,000 birr in a retirement account and want to withdraw the same amount every month for 20 years.

How much can you withdraw monthly if the account must be exhausted after the final withdrawal?

Start with the present value formula:

A₀ = P[1 − (1 + i)⁻ᴺ]/i

### Step 1: Multiply both sides by i

iA₀ = P[1 − (1 + i)⁻ᴺ]

### Step 2: Divide by the expression in brackets

# **P = A₀i/[1 − (1 + i)⁻ᴺ]**

This is the periodic withdrawal formula.

It is also the formula used to calculate fixed mortgage payments.

### Worked Example

Suppose you have 500,000 birr in an account. You want to withdraw a fixed amount at the end of every month for 20 years. The account earns a nominal annual interest rate of 12%, compounded monthly.

#### Given

A₀ = 500,000 birr

r = 0.12

i = 0.12/12 = 0.01

N = 20 × 12 = 240 months

#### Formula

P = A₀i/[1 − (1 + i)⁻ᴺ]

#### Calculation

P = 500,000 × 0.01/[1 − (1.01)⁻²⁴⁰]

**P ≈ 5,505.11 birr per month**

#### Interpretation

Under the stated assumptions, the account can support monthly withdrawals of approximately 5,505.11 birr for 240 months.

The account reaches zero immediately after the final withdrawal.

---

<!-- PAGE BREAK -->

## 13. Retirement Planning

Annuities are important in retirement planning because they help connect regular savings before retirement with regular withdrawals after retirement.

### Retirement situation

Suppose a person:

1. Makes monthly deposits of P birr for t years.
2. Earns an annual interest rate r, compounded monthly.
3. Transfers the accumulated balance to another account after t years.
4. Receives an annual interest rate r′ in the retirement account, compounded monthly.
5. Withdraws Q birr every month for s years.
6. Wants the retirement account to reach zero after the final withdrawal.

The main question is:

**How much must the person save every month before retirement to support the desired monthly retirement income?**

### Step 1: Calculate the balance accumulated before retirement

The monthly interest rate during saving is:

i = r/12

The total number of monthly deposits is:

12t

Using the future value formula:

Retirement balance = P[(1 + i)¹²ᵗ − 1]/i

### Step 2: Calculate the amount needed at retirement

The monthly interest rate during retirement is:

i′ = r′/12

The total number of withdrawals is:

12s

Using the present value formula:

Required retirement balance = Q[1 − (1 + i′)⁻¹²ˢ]/i′

### Step 3: Equate the two balances

The accumulated savings must equal the amount needed to fund the retirement withdrawals.

Therefore:

P[(1 + i)¹²ᵗ − 1]/i = Q[1 − (1 + i′)⁻¹²ˢ]/i′

### Step 4: Solve for P

Multiply both sides by i:

P[(1 + i)¹²ᵗ − 1] = Qi[1 − (1 + i′)⁻¹²ˢ]/i′

Divide by [(1 + i)¹²ᵗ − 1]:

# **P = Qi[1 − (1 + i′)⁻¹²ˢ] / {i′[(1 + i)¹²ᵗ − 1]}**

This formula calculates the monthly saving required before retirement.

### Interpretation

The required monthly saving amount depends on:

* Desired monthly retirement income Q.
* Number of years spent saving t.
* Number of years spent withdrawing s.
* Interest rate during the saving period.
* Interest rate during the retirement period.

Generally, saving for a longer period allows deposits more time to accumulate and earn interest. This can reduce the amount that must be deposited each month, assuming the other conditions remain unchanged.

---

## 14. Loan Amortization

### Definition

**Amortization** is the process of paying off a loan through a series of scheduled payments.

Examples include:

* Home mortgages.
* Car loans.
* Other installment loans.

Each loan payment typically contains two components:

1. **Interest payment:** the cost of borrowing money.
2. **Principal repayment:** the portion that reduces the amount still owed.

### How amortization works

At the beginning of a loan, the outstanding balance is relatively large. Therefore, the interest charged per period is also relatively large.

As the borrower makes payments, the outstanding balance decreases.

Consequently:

* The interest portion generally decreases.
* The principal portion generally increases.
* The total scheduled payment remains constant.

This is an important application of withdrawal annuities.

### Connection with annuities

From the lender's point of view, the loan is an initial amount of money that is recovered through regular withdrawals.

Therefore, the mortgage payment problem can be treated as a present-value annuity problem.

---

## 15. Mortgage Payment Formula

Suppose a homeowner borrows A₀ birr for t years at an annual interest rate r, compounded monthly.

The borrower makes equal monthly payments P.

### Step 1: Calculate the monthly interest rate

i = r/12

### Step 2: Calculate the total number of payments

N = 12t

### Step 3: Apply the present value formula

A₀ = P[1 − (1 + i)⁻ᴺ]/i

Solving for P:

# **P = A₀i/[1 − (1 + i)⁻ᴺ]**

This is the fixed monthly mortgage payment formula.

Substituting i = r/12 and N = 12t:

**P = A₀(r/12)/[1 − (1 + r/12)⁻¹²ᵗ]**

### Worked Example

Suppose a homeowner borrows 1,000,000 birr for 10 years at a nominal annual interest rate of 12%, compounded monthly.

Calculate the fixed monthly payment.

#### Given

A₀ = 1,000,000 birr

r = 0.12

i = 0.12/12 = 0.01

t = 10 years

N = 12 × 10 = 120 months

#### Formula

P = A₀i/[1 − (1 + i)⁻ᴺ]

#### Calculation

P = 1,000,000 × 0.01/[1 − (1.01)⁻¹²⁰]

**P ≈ 14,347.09 birr per month**

### Total payment

Total scheduled payments:

14,347.09 × 120

≈ 1,721,650.80 birr

Total interest:

1,721,650.80 − 1,000,000

**≈ 721,650.80 birr**

### Interpretation

The homeowner pays approximately 14,347.09 birr every month for 120 months.

The difference between the total scheduled payments and the original loan is the interest paid over the loan term.

*These calculations assume a fixed interest rate, equal end-of-month payments, and no additional fees or taxes.*

---

## 16. Outstanding Loan Balance

The outstanding loan balance is the amount that remains unpaid after a certain number of payments.

Your instructor gives the following formula:

# **Aₙ = A₀[1 − (1 + i)ⁿ⁻ᴺ]/[1 − (1 + i)⁻ᴺ]**

Where:

* A₀ is the original loan amount.
* i is the periodic interest rate.
* N is the total number of payments.
* n is the number of payments already made.
* Aₙ is the outstanding balance after the nth payment.

### Why does this formula make sense?

Let's check two important situations.

**Situation 1: At the beginning of the loan (n = 0)**

Aₙ = A₀[1 − (1 + i)⁻ᴺ]/[1 − (1 + i)⁻ᴺ]

Therefore:

A₀ = A₀

The outstanding balance equals the original loan amount.

**Situation 2: After the final payment (n = N)**

Aₙ = A₀[1 − (1 + i)⁰]/[1 − (1 + i)⁻ᴺ]

Since:

(1 + i)⁰ = 1

We obtain:

Aₙ = A₀(1 − 1)/[1 − (1 + i)⁻ᴺ]

Therefore:

**Aₙ = 0**

This is exactly what we expect: after the final scheduled payment, the loan has been fully repaid.

---

## 17. Interest and Principal Components

A fixed monthly loan payment does not mean that the interest and principal portions are fixed.

Let:

| Symbol | Meaning                                                    |
| ------ | ---------------------------------------------------------- |
| Aₙ₋₁   | Outstanding balance immediately after the previous payment |
| i      | Periodic interest rate                                     |
| P      | Fixed payment                                              |
| Iₙ     | Interest portion of payment n                              |
| Pₙ     | Principal portion of payment n                             |

### 17.1 Interest portion

The interest charged during period n is calculated using the balance at the beginning of that period.

Therefore:

# **Iₙ = iAₙ₋₁**

### 17.2 Principal portion

Each payment consists of interest and principal repayment.

Therefore:

P = Iₙ + Pₙ

Rearranging:

# **Pₙ = P − Iₙ**

These two formulas allow us to separate every payment into its interest and principal components.

### Worked Example

Recall our mortgage example:

* Initial loan = 1,000,000 birr.
* Monthly interest rate = 1%.
* Monthly payment ≈ 14,347.09 birr.

Calculate the interest and principal portions of the first payment.

#### Step 1: Calculate interest

I₁ = iA₀

I₁ = 0.01 × 1,000,000

**I₁ = 10,000 birr**

#### Step 2: Calculate principal repayment

P₁ = P − I₁

P₁ = 14,347.09 − 10,000

**P₁ = 4,347.09 birr**

#### Step 3: Calculate the remaining balance

Remaining balance = Initial balance − Principal repayment

A₁ = 1,000,000 − 4,347.09

**A₁ ≈ 995,652.91 birr**

### First payment summary

| Component           |         Amount |
| ------------------- | -------------: |
| Interest            | 10,000.00 birr |
| Principal repayment |  4,347.09 birr |
| Total payment       | 14,347.09 birr |

Notice that the first payment reduces the principal by only a portion of the total payment because the remaining portion covers interest.

---

## 18. Amortization Schedule and Payment Ratios

### What Is an Amortization Schedule?

An **amortization schedule** is a table showing how a loan is repaid over time.

It usually contains:

* Payment number.
* Beginning loan balance.
* Interest portion.
* Principal portion.
* Total payment.
* Remaining loan balance.

Your instructor refers to the sequences of outstanding balances, principal payments, and interest payments as an amortization schedule.

### 18.1 Relationship between interest and principal

The interest and principal portions of payment n satisfy:

Iₙ = iAₙ₋₁

Pₙ = P − Iₙ

The ratio between the interest portion and the principal portion is:

Iₙ/Pₙ

Using the expressions for interest and principal, the lecture notes give:

# **Iₙ/Pₙ = (1 + i)ᴺ⁺¹⁻ⁿ − 1**

### 18.2 Interpretation

The ratio decreases as n increases.

This means that as the loan progresses:

* The interest portion becomes smaller relative to the principal portion.
* A larger share of each fixed payment goes toward reducing the loan balance.

### 18.3 Maximum and minimum ratios

According to the lecture notes, the maximum ratio occurs at the first payment:

**I₁/P₁ = (1 + i)ᴺ − 1**

The minimum ratio occurs at the final payment:

**Iₙ/Pₙ = i, when n = N**

This confirms that the interest-to-principal ratio decreases over the repayment period.

### Important conclusion

At the beginning of a loan, interest represents a relatively large portion of each payment.

At the end of a loan, most of the payment goes toward principal repayment.

---

## 19. Ordinary Annuity versus Annuity Due

Your instructor's formulas assume that payments occur at the end of each compounding period. This is called an ordinary annuity.

A related arrangement is an **annuity due**, in which payments occur at the beginning of each period.

| Feature               | Ordinary annuity       | Annuity due                            |
| --------------------- | ---------------------- | -------------------------------------- |
| Payment timing        | End of each period     | Beginning of each period               |
| First payment         | End of first period    | Beginning of first period              |
| Interest-earning time | Standard period timing | One additional period for each payment |
| Future value          | P[(1 + i)ⁿ − 1]/i      | P[(1 + i)ⁿ − 1](1 + i)/i               |

The annuity-due formula is supplementary financial-mathematics knowledge. The main formulas in this note follow the ordinary-annuity assumption used in the lecture.

---

## 20. Practical Applications

### 20.1 Savings plans

Annuity formulas help determine how much regular saving will accumulate over time.

### 20.2 Pension and retirement planning

They help calculate the savings required to support regular income after retirement.

### 20.3 Mortgage payments

Banks use annuity mathematics to determine fixed periodic payments for home loans.

### 20.4 Car loans

The same principles apply when borrowers repay car loans through regular installments.

### 20.5 Trust funds

An initial amount can be calculated to support a specified sequence of future withdrawals.

### 20.6 Financial planning

Annuities help individuals compare saving strategies, borrowing arrangements, and retirement plans.

---

## 21. Common Mistakes

### Mistake 1: Forgetting to convert the annual rate to the periodic rate

For monthly compounding:

i = r/12

Do not use the annual rate directly in a monthly annuity formula.

### Mistake 2: Using the wrong number of periods

For a loan lasting 15 years with monthly payments:

N = 15 × 12 = 180

The number of periods must match the payment frequency.

### Mistake 3: Confusing deposits with withdrawals

Deposits increase the account balance, while withdrawals reduce it.

Pay attention to the signs in the formulas.

### Mistake 4: Forgetting payment timing

The formulas in this note assume payments occur at the end of each period.

If payments occur at the beginning, the annuity formula must be adjusted.

### Mistake 5: Confusing total payment with principal repayment

A loan payment contains both interest and principal.

Principal repayment = Total payment − Interest portion

### Mistake 6: Confusing present value and future value

* Future value calculates what regular deposits accumulate to.
* Present value calculates how much is required today to support future payments.

### Mistake 7: Assuming every withdrawal amount will exhaust the account

An account reaches zero after exactly N withdrawals only when the withdrawal amount is calculated using the appropriate present-value formula and the assumed interest rate and payment timing hold.

### Mistake 8: Rounding too early

Keep sufficient decimal places during calculations and round the final answer as required.

---

## 22. Formula Summary

The following table contains the main formulas from this topic.

| Concept                           | Formula                                       |
| --------------------------------- | --------------------------------------------- |
| Periodic interest rate            | i = r/m                                       |
| Number of periods                 | n = mt                                        |
| Future value of regular deposits  | Aₙ = P[(1 + i)ⁿ − 1]/i                        |
| Future value with initial deposit | Aₙ = A₀(1 + i)ⁿ + P[(1 + i)ⁿ − 1]/i           |
| Balance after n withdrawals       | Aₙ = A₀(1 + i)ⁿ + P[1 − (1 + i)ⁿ]/i           |
| Present value of N withdrawals    | A₀ = P[1 − (1 + i)⁻ᴺ]/i                       |
| Fixed withdrawal amount           | P = A₀i/[1 − (1 + i)⁻ᴺ]                       |
| Fixed mortgage payment            | P = A₀i/[1 − (1 + i)⁻ᴺ]                       |
| Outstanding loan balance          | Aₙ = A₀[1 − (1 + i)ⁿ⁻ᴺ]/[1 − (1 + i)⁻ᴺ]       |
| Interest portion                  | Iₙ = iAₙ₋₁                                    |
| Principal portion                 | Pₙ = P − Iₙ                                   |
| Interest-to-principal ratio       | Iₙ/Pₙ = (1 + i)ᴺ⁺¹⁻ⁿ − 1                      |
| Initial retirement saving formula | P = Qi[1 − (1 + i′)⁻¹²ˢ]/{i′[(1 + i)¹²ᵗ − 1]} |

### How to Choose the Correct Formula

| What the problem asks                        | Formula to use                    |
| -------------------------------------------- | --------------------------------- |
| Accumulated value of regular deposits        | Future value of an annuity        |
| Future value with an initial deposit         | Future value with initial deposit |
| Balance after regular withdrawals            | Withdrawal formula                |
| Initial amount needed for future withdrawals | Present value of an annuity       |
| Fixed monthly withdrawal                     | Periodic withdrawal formula       |
| Fixed monthly mortgage payment               | Mortgage payment formula          |
| Remaining loan balance                       | Outstanding loan balance          |
| Interest portion of a payment                | Iₙ = iAₙ₋₁                        |
| Principal portion of a payment               | Pₙ = P − Iₙ                       |
| Monthly saving needed for retirement         | Retirement planning formula       |

---

## 23. Practice Questions

Try these questions before checking the solutions.

### Question 1: Future Value of an Annuity

You deposit 2,000 birr at the end of every month for 24 months. The monthly interest rate is 1%.

Calculate the accumulated value immediately after the 24th deposit.

### Question 2: Initial Deposit and Regular Deposits

An account starts with 10,000 birr. You then deposit 1,500 birr at the end of every month for 12 months. The account earns 1% interest per month.

Calculate the balance immediately after the 12th deposit.

### Question 3: Present Value of Withdrawals

You want to withdraw 4,000 birr at the end of every month for 60 months. The account earns 1% interest per month.

How much money is required initially if the account must be exhausted after the final withdrawal?

### Question 4: Mortgage Payment

A homeowner borrows 800,000 birr for 15 years at a nominal annual interest rate of 12%, compounded monthly.

Calculate the fixed monthly payment.

### Question 5: Loan Amortization

A loan has an outstanding balance of 100,000 birr at the beginning of a month. The monthly interest rate is 1%, and the monthly payment is 3,000 birr.

Calculate:

1. The interest portion of the payment.
2. The principal portion of the payment.
3. The remaining balance after the payment.

### Question 6: Derivation

Starting from the accumulated values of individual deposits, derive:

Aₙ = P[(1 + i)ⁿ − 1]/i

### Question 7: Interpretation

Explain why the interest portion of a fixed mortgage payment generally decreases over time while the principal portion increases.

### Question 8: Retirement Planning

A person wants to receive 10,000 birr monthly for 15 years after retirement. The retirement account earns 1% monthly interest.

Calculate the amount required in the retirement account immediately before the first withdrawal.

---

## 24. Solutions to Practice Questions

### Solution 1

Given:

P = 2,000

i = 0.01

n = 24

Formula:

Aₙ = P[(1 + i)ⁿ − 1]/i

Substitute:

A₂₄ = 2,000[(1.01)²⁴ − 1]/0.01

Since:

(1.01)²⁴ ≈ 1.269735

A₂₄ ≈ 2,000(0.269735)/0.01

**A₂₄ ≈ 53,947.04 birr**

### Solution 2

Given:

A₀ = 10,000

P = 1,500

i = 0.01

n = 12

Formula:

Aₙ = A₀(1 + i)ⁿ + P[(1 + i)ⁿ − 1]/i

Substitute:

A₁₂ = 10,000(1.01)¹² + 1,500[(1.01)¹² − 1]/0.01

The initial deposit grows to approximately:

11,268.25 birr

The regular deposits accumulate to approximately:

19,023.75 birr

Therefore:

**A₁₂ ≈ 30,292.00 birr**

### Solution 3

Given:

P = 4,000

i = 0.01

N = 60

Formula:

A₀ = P[1 − (1 + i)⁻ᴺ]/i

Substitute:

A₀ = 4,000[1 − (1.01)⁻⁶⁰]/0.01

**A₀ ≈ 179,695.55 birr**

### Solution 4

Given:

A₀ = 800,000

r = 0.12

i = 0.12/12 = 0.01

N = 15 × 12 = 180

Formula:

P = A₀i/[1 − (1 + i)⁻ᴺ]

Substitute:

P = 800,000 × 0.01/[1 − (1.01)⁻¹⁸⁰]

**P ≈ 9,601.26 birr per month**

### Solution 5

Given:

Outstanding balance = 100,000 birr

Monthly interest rate = 0.01

Monthly payment = 3,000 birr

**1. Interest portion**

Iₙ = iAₙ₋₁

Iₙ = 0.01 × 100,000

**Iₙ = 1,000 birr**

**2. Principal portion**

Pₙ = P − Iₙ

Pₙ = 3,000 − 1,000

**Pₙ = 2,000 birr**

**3. Remaining balance**

Aₙ = Previous balance − Principal repayment

Aₙ = 100,000 − 2,000

**Aₙ = 98,000 birr**

### Solution 6

The first deposit grows for n − 1 periods, the second for n − 2 periods, and the last deposit earns no interest before the balance is evaluated.

Therefore:

Aₙ = P[(1 + i)ⁿ⁻¹ + (1 + i)ⁿ⁻² + ... + 1]

Apply the geometric-series formula:

1 + q + ... + qⁿ⁻¹ = (qⁿ − 1)/(q − 1)

Set:

q = 1 + i

Then:

Aₙ = P[(1 + i)ⁿ − 1]/i

### Solution 7

The interest charged each period is calculated on the outstanding loan balance.

As the borrower repays principal, the outstanding balance decreases.

Therefore, the interest charged in later periods generally decreases.

Since the total scheduled payment remains fixed, a smaller interest portion means that a larger portion of the payment goes toward repaying principal.

### Solution 8

Given:

Q = 10,000 birr

i = 0.01

N = 15 × 12 = 180 months

Use the present value formula:

A₀ = Q[1 − (1 + i)⁻ᴺ]/i

Substitute:

A₀ = 10,000[1 − (1.01)⁻¹⁸⁰]/0.01

**A₀ ≈ 837,569.76 birr**

Therefore, approximately 837,569.76 birr is required immediately before the first withdrawal.

---

## 25. Conclusion

Annuities connect the principles of interest with real financial decisions.

In this topic, we studied how regular deposits accumulate into a future amount, how regular withdrawals reduce an account balance, how to calculate the initial capital required to support future withdrawals, and how to determine fixed loan payments.

We also applied annuity mathematics to retirement planning and loan amortization.

### Most Important Formulas

**Future value of regular deposits:**

Aₙ = P[(1 + i)ⁿ − 1]/i

**Present value of regular withdrawals:**

A₀ = P[1 − (1 + i)⁻ᴺ]/i

**Fixed loan payment:**

P = A₀i/[1 − (1 + i)⁻ᴺ]

**Interest portion of a loan payment:**

Iₙ = iAₙ₋₁

**Principal portion of a loan payment:**

Pₙ = P − Iₙ

### Final Takeaway

> **An annuity is a sequence of equal periodic payments. Its value depends not only on how much money is paid, but also on when each payment occurs and how interest accumulates over time.**

Understanding annuities provides the mathematical foundation for studying savings plans, retirement accounts, pensions, and loans.

---

**End of Topic 3: Annuities**

**Next Topic:** Bonds — understanding bond characteristics, coupon payments, maturity, and bond valuation.
