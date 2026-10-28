# 📘 Interest — Financial Mathematics

> **Course:** Financial Mathematics (Math4313)
> **Topic:** Interest and the Time Value of Money
> **Purpose:** Understand how money grows through interest, derive the main interest formulas, and compare different methods of compounding.

---

## 📑 Table of Contents

1. [Learning Objectives](#1-learning-objectives)
2. [What Is Interest?](#2-what-is-interest)
3. [Simple Interest](#3-simple-interest)
4. [Derivation of the Simple Interest Formula](#4-derivation-of-the-simple-interest-formula)
5. [Compound Interest](#5-compound-interest)
6. [Derivation of the Compound Interest Formula](#6-derivation-of-the-compound-interest-formula)
7. [Compound Interest with m Compounding Periods per Year](#7-compound-interest-with-m-compounding-periods-per-year)
8. [Continuous Compounding](#8-continuous-compounding)
9. [Derivation of the Continuous Compounding Formula](#9-derivation-of-the-continuous-compounding-formula)
10. [Effective Annual Interest Rate](#10-effective-annual-interest-rate)
11. [Comparison of Interest Methods](#11-comparison-of-interest-methods)
12. [Worked Examples](#12-worked-examples)
13. [Practical Applications](#13-practical-applications)
14. [Common Mistakes](#14-common-mistakes)
15. [Formula Summary](#15-formula-summary)
16. [Practice Questions](#16-practice-questions)
17. [Solutions to Practice Questions](#17-solutions-to-practice-questions)
18. [Conclusion](#18-conclusion)

---

## 1. Learning Objectives

After studying this topic, you should be able to:

* Define interest, principal, interest rate, and future value.
* Explain the difference between simple and compound interest.
* Derive the simple interest formula.
* Derive the compound interest formula for different compounding frequencies.
* Derive the continuous compounding formula using a mathematical limit.
* Calculate the effective annual interest rate.
* Compare different interest methods using numerical examples.
* Apply interest formulas to savings, loans, and investments.

---

## 2. What Is Interest?

### Definition

**Interest** is the amount of money paid or earned for the use of money over a period of time.

For example, when you deposit money into an interest-bearing bank account, the bank may pay you interest. When you borrow money, you may have to pay interest to the lender.

### Important terms

| Term          | Meaning                                                                 |
| ------------- | ----------------------------------------------------------------------- |
| Principal     | The initial amount of money invested or borrowed                        |
| Interest      | The additional amount earned or paid                                    |
| Interest rate | The rate at which interest is calculated                                |
| Time          | The period during which money earns or accumulates interest             |
| Present value | The value of money at the initial time                                  |
| Future value  | The value of money at a later time                                      |
| Compounding   | Adding earned interest to the balance so that it can also earn interest |

### Symbols used in this note

| Symbol | Meaning                                              |
| ------ | ---------------------------------------------------- |
| A₀     | Initial amount or principal                          |
| A(t)   | Amount after t years                                 |
| I      | Interest earned or paid                              |
| r      | Annual interest rate, expressed as a decimal         |
| t      | Time in years                                        |
| m      | Number of compounding periods per year               |
| e      | Base of the natural logarithm, approximately 2.71828 |

### Percentage reminder

Before substituting an interest rate into a formula, convert the percentage to a decimal.

For example:

* 5% = 0.05
* 8% = 0.08
* 12% = 0.12

---

## 3. Simple Interest

### Definition

**Simple interest** is interest calculated only on the original principal.

The interest earned in each year is the same when the principal, interest rate, and time period remain unchanged.

### Example

Suppose you deposit 10,000 birr at a simple annual interest rate of 8%.

The interest earned in one year is:

Interest = 10,000 × 0.08

Interest = 800 birr

After two years, the total interest is:

Total interest = 800 + 800 = 1,600 birr

Notice that the interest earned in the second year is still 800 birr. The interest from the first year is not added to the principal when calculating the second year's interest.

### Simple interest formulas

**Interest earned:**

I = A₀rt

**Future value:**

A(t) = A₀ + I

Substituting I = A₀rt:

**A(t) = A₀(1 + rt)**

These formulas assume a constant annual simple interest rate and time measured in years.

---

## 4. Derivation of the Simple Interest Formula

Let's derive the formula step by step.

### Step 1: Identify the principal

Suppose the initial amount is A₀.

The principal remains unchanged for the purpose of calculating simple interest.

### Step 2: Calculate interest for one year

If the annual interest rate is r, then the interest earned in one year is:

I₁ = A₀r

Therefore, the amount after one year is:

A(1) = A₀ + A₀r

Factor out A₀:

A(1) = A₀(1 + r)

### Step 3: Calculate interest for two years

Under simple interest, the interest earned during the second year is still A₀r.

Therefore, the total interest after two years is:

I₂ = A₀r + A₀r

I₂ = 2A₀r

The amount after two years is:

A(2) = A₀ + 2A₀r

Factor out A₀:

A(2) = A₀(1 + 2r)

### Step 4: Generalize to t years

After t years, the same amount of interest is earned each year.

Thus, the total interest is:

**I = A₀rt**

The future value equals the principal plus interest:

A(t) = A₀ + A₀rt

Factor out A₀:

# **A(t) = A₀(1 + rt)**

This is the simple interest formula.

### Key idea

Under simple interest, interest grows linearly with time because it is always calculated using the original principal.

---

<!-- PAGE BREAK -->

## 5. Compound Interest

### Definition

**Compound interest** is interest calculated on both the original principal and the interest accumulated in previous periods.

In other words, interest earns interest.

### Example

Suppose you deposit 10,000 birr at an annual interest rate of 8%, compounded annually.

**After one year:**

Interest = 10,000 × 0.08 = 800 birr

New balance = 10,000 + 800 = 10,800 birr

**After two years:**

The interest is now calculated on 10,800 birr:

Interest = 10,800 × 0.08 = 864 birr

New balance = 10,800 + 864 = 11,664 birr

Notice that the second year's interest is 864 birr, not 800 birr.

This happens because the interest earned in the first year is included in the balance.

### General compound interest formula

When interest is compounded annually:

**A(t) = A₀(1 + r)^t**

Where:

* A₀ is the initial principal.
* r is the annual interest rate as a decimal.
* t is the number of years.
* A(t) is the future value.

---

## 6. Derivation of the Compound Interest Formula

Let's derive the formula from the balance at the end of each year.

### Step 1: Amount after one year

The interest earned during the first year is:

I₁ = A₀r

The new balance is:

A(1) = A₀ + A₀r

Therefore,

A(1) = A₀(1 + r)

### Step 2: Amount after two years

During the second year, interest is calculated on the entire balance A(1).

Thus,

A(2) = A(1)(1 + r)

Substitute A(1) = A₀(1 + r):

A(2) = A₀(1 + r)(1 + r)

Therefore,

A(2) = A₀(1 + r)²

### Step 3: Amount after three years

Similarly,

A(3) = A(2)(1 + r)

Substitute the expression for A(2):

A(3) = A₀(1 + r)²(1 + r)

Therefore,

A(3) = A₀(1 + r)³

### Step 4: Generalize to t years

The pattern is:

* After 1 year: A(1) = A₀(1 + r)
* After 2 years: A(2) = A₀(1 + r)²
* After 3 years: A(3) = A₀(1 + r)³
* After t years: A(t) = A₀(1 + r)^t

Therefore,

# **A(t) = A₀(1 + r)^t**

This is the compound interest formula for annual compounding.

### Key idea

Simple interest adds the same amount of interest each year. Compound interest multiplies the balance by the same growth factor each year.

---

## 7. Compound Interest with m Compounding Periods per Year

In practice, interest is not always compounded annually. It may be compounded semiannually, quarterly, monthly, or daily.

### Common compounding frequencies

| Compounding method                | Periods per year (m) |
| --------------------------------- | -------------------: |
| Annually                          |                    1 |
| Semiannually                      |                    2 |
| Quarterly                         |                    4 |
| Monthly                           |                   12 |
| Daily, using a 365-day convention |                  365 |

### Deriving the general formula

Suppose:

* A₀ is the initial principal.
* r is the nominal annual interest rate.
* m is the number of compounding periods per year.
* t is the number of years.

**Step 1: Calculate the interest rate per period.**

If the nominal annual rate is r and there are m periods per year, the rate per period is:

Periodic rate = r/m

**Step 2: Calculate the number of periods.**

Over t years, the number of compounding periods is:

Number of periods = mt

**Step 3: Calculate the balance after each period.**

During each period, the balance is multiplied by:

1 + r/m

After the first period:

A₁ = A₀(1 + r/m)

After the second period:

A₂ = A₀(1 + r/m)²

After mt periods:

# **A(t) = A₀(1 + r/m)^(mt)**

This is the compound interest formula when interest is compounded m times per year.

### Important interpretation

Increasing the compounding frequency generally increases the future value when the nominal annual rate and investment period are held constant.

For example, monthly compounding generally produces a slightly larger balance than annual compounding at the same positive nominal annual rate.

---

## 8. Continuous Compounding

### Definition

**Continuous compounding** is the mathematical model obtained by allowing the compounding frequency to increase without bound.

Instead of adding interest at separate intervals, the model treats compounding as occurring continuously.

The continuous compounding formula is:

# **A(t) = A₀e^(rt)**

Where:

* A₀ is the initial principal.
* r is the continuously compounded annual rate.
* t is time in years.
* e is approximately 2.71828.

### Why is continuous compounding useful?

Continuous compounding provides a convenient mathematical model for continuously growing quantities. It is used in financial mathematics to study investments, interest-rate models, and other financial processes.

It also provides a limiting case for comparing discrete compounding methods.

---

## 9. Derivation of the Continuous Compounding Formula

We begin with the discrete compound interest formula:

A(t) = A₀(1 + r/m)^(mt)

As the compounding frequency m increases, the formula approaches continuous compounding.

### Step 1: Rewrite the formula

A(t) = A₀[(1 + r/m)^m]^t

This is the same formula because:

[(1 + r/m)^m]^t = (1 + r/m)^(mt)

### Step 2: Increase the compounding frequency

Consider what happens as:

m → ∞

The number of compounding periods per year becomes increasingly large, while the interest rate per period, r/m, becomes increasingly small.

The mathematical limit is:

lim (m→∞) (1 + r/m)^m = e^r

This is a standard exponential limit.

### Step 3: Apply the limit

Starting from:

A(t) = A₀[(1 + r/m)^m]^t

Taking the limit as m approaches infinity gives:

A(t) = A₀(e^r)^t

Using the exponent rule:

(e^r)^t = e^(rt)

Therefore,

# **A(t) = A₀e^(rt)**

This is the continuous compounding formula.

### Key idea

Continuous compounding is not an unrelated formula. It is the limiting case of discrete compound interest as the number of compounding periods per year approaches infinity.

---

<!-- PAGE BREAK -->

## 10. Effective Annual Interest Rate

### Definition

The **effective annual interest rate** is the actual percentage increase in an investment's value over one year after accounting for compounding.

It can differ from the quoted nominal annual rate.

### 10.1 Effective rate under discrete compounding

Suppose the nominal annual rate is r and interest is compounded m times per year.

From the compound interest formula, the balance after one year is:

A(1) = A₀(1 + r/m)^m

By definition, the effective annual rate r_eff is the rate that gives the same one-year growth:

A(1) = A₀(1 + r_eff)

Equate the expressions:

A₀(1 + r_eff) = A₀(1 + r/m)^m

Divide both sides by A₀:

1 + r_eff = (1 + r/m)^m

Subtract 1:

# **r_eff = (1 + r/m)^m − 1**

This is the effective annual rate under discrete compounding.

### Example

Suppose an account offers a nominal annual rate of 12%, compounded monthly.

Given:

r = 0.12

m = 12

The effective annual rate is:

r_eff = (1 + 0.12/12)^12 − 1

r_eff = (1.01)^12 − 1

r_eff ≈ 0.126825

Therefore,

**r_eff ≈ 12.68%**

Although the nominal annual rate is 12%, monthly compounding produces an effective annual rate of approximately 12.68%.

### 10.2 Effective rate under continuous compounding

Under continuous compounding, the balance after one year is:

A(1) = A₀e^r

By the definition of the effective annual rate:

A(1) = A₀(1 + r_eff)

Equate the two expressions:

A₀(1 + r_eff) = A₀e^r

Divide both sides by A₀:

1 + r_eff = e^r

Subtract 1:

# **r_eff = e^r − 1**

### Example

Suppose the continuously compounded annual rate is 8%.

Given:

r = 0.08

Then:

r_eff = e^0.08 − 1

r_eff ≈ 1.083287 − 1

**r_eff ≈ 8.33%**

### Important distinction

The quoted nominal rate and the effective annual rate are not always the same. Always check how often interest is compounded.

---

## 11. Comparison of Interest Methods

The different interest methods can produce different future values even when they start with the same principal and use the same nominal annual rate.

### Lecture example

Suppose:

* Initial deposit: A₀ = 1,000
* Annual interest rate: r = 3.5% = 0.035
* Investment period: t = 5.4 years

Compare simple interest, monthly compounding, daily compounding, and continuous compounding.

### Method 1: Simple interest

Formula:

A(t) = A₀(1 + rt)

Substitute:

A(5.4) = 1,000(1 + 0.035 × 5.4)

A(5.4) = 1,000(1.189)

**A(5.4) = 1,189.00**

### Method 2: Monthly compounding

Formula:

A(t) = A₀(1 + r/m)^(mt)

For monthly compounding, m = 12:

A(5.4) = 1,000(1 + 0.035/12)^(12 × 5.4)

**A(5.4) ≈ 1,207.71**

### Method 3: Daily compounding

Using a 365-day convention, m = 365:

A(5.4) = 1,000(1 + 0.035/365)^(365 × 5.4)

**A(5.4) ≈ 1,208.03**

### Method 4: Continuous compounding

Formula:

A(t) = A₀e^(rt)

Substitute:

A(5.4) = 1,000e^(0.035 × 5.4)

**A(5.4) ≈ 1,208.04**

### Comparison table

| Interest method        | Future value |
| ---------------------- | -----------: |
| Simple interest        |     1,189.00 |
| Monthly compounding    |     1,207.71 |
| Daily compounding      |     1,208.03 |
| Continuous compounding |     1,208.04 |

*Values are rounded to two decimal places.*

### Interpretation

Under these assumptions, continuous compounding gives the largest future value, while simple interest gives the smallest.

The difference between daily and continuous compounding is very small in this example. However, the difference between simple interest and compound interest is more noticeable.

---

## 12. Worked Examples

### Example 1: Simple interest

A student deposits 10,000 birr at a simple annual interest rate of 8% for three years. Find the interest earned and the final balance.

#### Given

A₀ = 10,000 birr

r = 0.08

t = 3 years

#### Step 1: Calculate interest

I = A₀rt

I = 10,000 × 0.08 × 3

**I = 2,400 birr**

#### Step 2: Calculate the future value

A(t) = A₀ + I

A(t) = 10,000 + 2,400

**A(t) = 12,400 birr**

#### Interpretation

The student earns 2,400 birr in interest and finishes with 12,400 birr.

---

### Example 2: Annual compound interest

Suppose 10,000 birr is invested at an annual compound interest rate of 8% for three years.

#### Given

A₀ = 10,000 birr

r = 0.08

t = 3 years

#### Formula

A(t) = A₀(1 + r)^t

#### Calculation

A(3) = 10,000(1.08)³

A(3) = 10,000 × 1.259712

**A(3) = 12,597.12 birr**

#### Interpretation

The investment grows to 12,597.12 birr. This is greater than the 12,400 birr obtained under simple interest because the interest earned is reinvested.

---

### Example 3: Continuous compounding

Suppose 10,000 birr is invested at a continuously compounded annual rate of 8% for three years.

#### Given

A₀ = 10,000 birr

r = 0.08

t = 3 years

#### Formula

A(t) = A₀e^(rt)

#### Calculation

A(3) = 10,000e^(0.08 × 3)

A(3) = 10,000e^0.24

**A(3) ≈ 12,712.49 birr**

#### Interpretation

Under continuous compounding, the future value is approximately 12,712.49 birr.

---

### Example 4: Monthly compound interest

A bank account contains 5,000 birr and pays a nominal annual interest rate of 12%, compounded monthly. Calculate the balance after one year.

#### Given

A₀ = 5,000 birr

r = 0.12

m = 12

t = 1 year

#### Formula

A(t) = A₀(1 + r/m)^(mt)

#### Calculation

A(1) = 5,000(1 + 0.12/12)^12

A(1) = 5,000(1.01)^12

A(1) ≈ 5,000 × 1.126825

**A(1) ≈ 5,634.13 birr**

The interest earned is approximately:

5,634.13 − 5,000 = **634.13 birr**

---

## 13. Practical Applications

### 13.1 Savings accounts

Interest formulas help estimate how much savings will grow over time.

### 13.2 Loans

Borrowers can use interest calculations to understand how interest accumulates on borrowed money.

### 13.3 Investment planning

Investors compare interest methods to understand how compounding frequency affects future wealth.

### 13.4 Comparing financial offers

Two accounts may advertise the same nominal annual rate but use different compounding frequencies. The effective annual rate helps compare their actual one-year growth.

### 13.5 Long-term financial decisions

Interest formulas provide a mathematical foundation for studying annuities, bonds, and internal rate of return.

These topics build on the same central principle: the value of money depends on time and the rate at which it grows.

---

## 14. Common Mistakes

### Mistake 1: Confusing simple interest with compound interest

Simple interest is calculated on the original principal.

Compound interest is calculated on the accumulated balance.

### Mistake 2: Forgetting to convert percentages to decimals

For example, 8% must be entered as 0.08, not 8.

### Mistake 3: Using the wrong number of compounding periods

For monthly compounding:

m = 12

Number of periods over t years = 12t

The exponent is mt, not simply t.

### Mistake 4: Confusing nominal and effective annual rates

A nominal rate of 12% compounded monthly produces an effective annual rate of approximately 12.68%, not 12%.

### Mistake 5: Confusing the future value with the interest earned

Future value includes both the principal and the accumulated interest.

Interest earned = Future value − Principal

### Mistake 6: Forgetting the assumptions behind the formula

The formulas in this note assume a constant stated rate and the compounding convention specified in the question. Real financial products may include fees, taxes, variable rates, or other conditions.

### Mistake 7: Rounding too early

Keep enough decimal places during calculations and round the final result as required by the question.

---

## 15. Formula Summary

| Concept                                       | Formula                 |
| --------------------------------------------- | ----------------------- |
| Simple interest                               | I = A₀rt                |
| Simple interest future value                  | A(t) = A₀(1 + rt)       |
| Annual compound interest                      | A(t) = A₀(1 + r)^t      |
| Periodic compound interest                    | A(t) = A₀(1 + r/m)^(mt) |
| Periodic interest rate                        | r/m                     |
| Number of periods                             | mt                      |
| Continuous compound interest                  | A(t) = A₀e^(rt)         |
| Effective annual rate, m compounding periods  | r_eff = (1 + r/m)^m − 1 |
| Effective annual rate, continuous compounding | r_eff = e^r − 1         |
| Interest earned from any future value         | I = A(t) − A₀           |

### Quick comparison

| Feature                 | Simple interest    | Compound interest                         |
| ----------------------- | ------------------ | ----------------------------------------- |
| Interest calculated on  | Original principal | Accumulated balance                       |
| Growth pattern          | Linear in time     | Exponential in time under a constant rate |
| Interest earns interest | No                 | Yes                                       |
| General future value    | A₀(1 + rt)         | A₀(1 + r/m)^(mt), for m periods per year  |

---

## 16. Practice Questions

Try these questions before checking the solutions.

### Question 1: Simple interest

A person invests 8,000 birr at a simple annual interest rate of 6% for four years.

1. Calculate the interest earned.
2. Find the final balance.

### Question 2: Compound interest

An amount of 15,000 birr is invested at an annual compound interest rate of 7% for three years.

Calculate the future value.

### Question 3: Monthly compounding

A bank account contains 10,000 birr and pays a nominal annual rate of 12%, compounded monthly.

Calculate the balance after two years.

### Question 4: Continuous compounding

An investment of 5,000 birr earns a continuously compounded annual rate of 9% for four years.

Calculate the future value.

### Question 5: Effective annual rate

A bank advertises a nominal annual interest rate of 10%, compounded quarterly.

Calculate the effective annual interest rate.

### Question 6: Compare simple and compound interest

An amount of 20,000 birr is invested at 8% per year for three years.

Calculate the future value under:

1. Simple interest
2. Annual compound interest

Which method produces the larger future value?

### Question 7: Derivation

Starting from the amount after one year, derive the compound interest formula:

A(t) = A₀(1 + r)^t

### Question 8: Continuous compounding

Explain how the continuous compounding formula is obtained from:

A(t) = A₀(1 + r/m)^(mt)

---

## 17. Solutions to Practice Questions

### Solution 1

Given:

A₀ = 8,000 birr

r = 0.06

t = 4 years

Interest:

I = A₀rt

I = 8,000 × 0.06 × 4

**I = 1,920 birr**

Final balance:

A(t) = A₀ + I

A(t) = 8,000 + 1,920

**A(t) = 9,920 birr**

### Solution 2

Given:

A₀ = 15,000 birr

r = 0.07

t = 3 years

A(3) = 15,000(1.07)³

A(3) = 15,000 × 1.225043

**A(3) ≈ 18,375.65 birr**

### Solution 3

Given:

A₀ = 10,000 birr

r = 0.12

m = 12

t = 2 years

A(2) = 10,000(1 + 0.12/12)^(12 × 2)

A(2) = 10,000(1.01)^24

**A(2) ≈ 12,697.35 birr**

### Solution 4

Given:

A₀ = 5,000 birr

r = 0.09

t = 4 years

A(4) = 5,000e^(0.09 × 4)

A(4) = 5,000e^0.36

**A(4) ≈ 7,167.42 birr**

### Solution 5

Given:

r = 0.10

m = 4

Effective annual rate:

r_eff = (1 + r/m)^m − 1

r_eff = (1 + 0.10/4)^4 − 1

r_eff = (1.025)^4 − 1

r_eff ≈ 0.103813

**r_eff ≈ 10.38%**

### Solution 6

Given:

A₀ = 20,000 birr

r = 0.08

t = 3 years

**1. Simple interest**

A(3) = 20,000(1 + 0.08 × 3)

A(3) = 20,000(1.24)

**A(3) = 24,800 birr**

**2. Annual compound interest**

A(3) = 20,000(1.08)³

A(3) = 20,000 × 1.259712

**A(3) = 25,194.24 birr**

Annual compound interest produces the larger future value in this example.

### Solution 7

After one year:

A(1) = A₀(1 + r)

After two years:

A(2) = A₀(1 + r)²

After three years:

A(3) = A₀(1 + r)³

Continuing the pattern, after t years:

**A(t) = A₀(1 + r)^t**

### Solution 8

Begin with the periodic compounding formula:

A(t) = A₀(1 + r/m)^(mt)

Rewrite it as:

A(t) = A₀[(1 + r/m)^m]^t

As m approaches infinity, the standard exponential limit gives:

lim (m→∞) (1 + r/m)^m = e^r

Therefore:

A(t) = A₀(e^r)^t

Using the exponent rule:

**A(t) = A₀e^(rt)**

This is the continuous compounding formula.

---

## 18. Conclusion

Interest is one of the fundamental concepts of financial mathematics. It explains how the value of money changes over time when money is invested or borrowed.

The simple interest formula is:

**A(t) = A₀(1 + rt)**

The compound interest formula is:

**A(t) = A₀(1 + r/m)^(mt)**

The continuous compounding formula is:

**A(t) = A₀e^(rt)**

The effective annual rate helps compare the actual one-year growth produced by different compounding methods.

### Final takeaway

> **Simple interest grows from the original principal, while compound interest grows from the accumulated balance. Continuous compounding is the limiting case of periodic compounding as the compounding frequency approaches infinity.**

Understanding these formulas provides the foundation for the next topics in Financial Mathematics.

---

**End of Topic 1: Interest**

**Next topic:** Inflation — how rising prices affect purchasing power and real returns.
