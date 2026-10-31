# 📘 Inflation — Financial Mathematics

> **Course:** Financial Mathematics (Math4313)
> **Topic:** Inflation and Inflation-Adjusted Rate of Return
> **Purpose:** Understand how inflation changes prices, purchasing power, and the real return on an investment.

---

## 📑 Table of Contents

1. [Learning Objectives](#1-learning-objectives)
2. [What Is Inflation?](#2-what-is-inflation)
3. [Mathematical Model of Inflation](#3-mathematical-model-of-inflation)
4. [Derivation of the Inflation Formula](#4-derivation-of-the-inflation-formula)
5. [Worked Example: Future Price](#5-worked-example-future-price)
6. [Purchasing Power](#6-purchasing-power)
7. [Nominal and Real Rates of Return](#7-nominal-and-real-rates-of-return)
8. [Derivation of the Exact Real Rate Formula](#8-derivation-of-the-exact-real-rate-formula)
9. [Worked Examples: Real Rate of Return](#9-worked-examples-real-rate-of-return)
10. [Approximation of the Real Rate](#10-approximation-of-the-real-rate)
11. [Practical Applications](#11-practical-applications)
12. [Common Mistakes](#12-common-mistakes)
13. [Formula Summary](#13-formula-summary)
14. [Practice Questions](#14-practice-questions)
15. [Solutions to Practice Questions](#15-solutions-to-practice-questions)
16. [Conclusion](#16-conclusion)

---

## 1. Learning Objectives

After studying this topic, you should be able to:

* Define inflation and explain its effect on purchasing power.
* Calculate future prices using a constant inflation rate.
* Derive the mathematical formula for inflation.
* Calculate the purchasing power of future money in today's terms.
* Distinguish between nominal and real rates of return.
* Derive the exact formula for the inflation-adjusted rate of return.
* Apply inflation formulas to practical financial problems.

---

## 2. What Is Inflation?

### Definition

**Inflation** is a general increase in the prices of goods and services over time.

When inflation occurs, the purchasing power of money decreases. This means that the same amount of money generally buys fewer goods and services than before.

### Example

Suppose a notebook costs 100 birr today.

If the annual inflation rate is 25%, the notebook's price after one year will be:

100 + 25% of 100 = 125 birr

You now need 125 birr to buy the same notebook, assuming its price increases at the stated inflation rate.

### Important distinction

Inflation does not necessarily mean that every individual price increases at exactly the same rate. The mathematical models in this note assume a constant inflation rate for the purpose of calculation.

---

## 3. Mathematical Model of Inflation

Suppose:

* A₀ = initial price or amount of money
* A(t) = price after t years
* r_f = annual inflation rate, expressed as a decimal
* t = number of years

If the annual inflation rate is constant and prices increase by the same percentage each year, then:

**Future price = Initial price × (1 + Inflation rate)^Time**

Therefore,

**A(t) = A₀(1 + r_f)^t**

### Meaning of the formula

* A₀ represents the initial price.
* r_f represents the annual inflation rate.
* 1 + r_f represents the annual price-growth factor.
* t represents the number of years.
* A(t) represents the price after t years.

### Example

If inflation is 10% annually:

r_f = 10/100 = 0.10

The annual price-growth factor is:

1 + r_f = 1 + 0.10 = 1.10

This means that the price is multiplied by 1.10 each year.

---

## 4. Derivation of the Inflation Formula

We can derive the formula step by step.

### Step 1: Initial price

Let the initial price of a product be A₀.

At the beginning, its price is simply:

A(0) = A₀

### Step 2: Price after one year

If the annual inflation rate is r_f, the price increases by r_f times the initial price.

The increase in price is:

Increase = A₀ × r_f

Therefore, the price after one year is:

A(1) = A₀ + A₀r_f

Factor out A₀:

A(1) = A₀(1 + r_f)

### Step 3: Price after two years

During the second year, the inflation rate applies to the price at the end of the first year, not just to the original price.

Therefore,

A(2) = A(1)(1 + r_f)

Substitute A(1) = A₀(1 + r_f):

A(2) = A₀(1 + r_f)(1 + r_f)

Hence,

A(2) = A₀(1 + r_f)²

### Step 4: Price after three years

Similarly,

A(3) = A(2)(1 + r_f)

Substituting the expression for A(2):

A(3) = A₀(1 + r_f)²(1 + r_f)

Therefore,

A(3) = A₀(1 + r_f)³

### Step 5: Generalize the pattern

We obtain the following pattern:

* After 1 year: A(1) = A₀(1 + r_f)
* After 2 years: A(2) = A₀(1 + r_f)²
* After 3 years: A(3) = A₀(1 + r_f)³
* After t years: A(t) = A₀(1 + r_f)^t

Thus, the general formula is:

**A(t) = A₀(1 + r_f)^t**

### Key idea

Inflation compounds because each year's percentage increase is calculated using the previous year's price.

---

<!-- PAGE BREAK -->

## 5. Worked Example: Future Price

### Problem

A product costs 100 birr today. If the annual inflation rate is 25%, calculate its expected price after two years.

### Given

A₀ = 100 birr

r_f = 25% = 0.25

t = 2 years

### Formula

A(t) = A₀(1 + r_f)^t

### Calculation

Substitute the given values:

A(2) = 100(1 + 0.25)²

A(2) = 100(1.25)²

A(2) = 100 × 1.5625

**A(2) = 156.25 birr**

### Interpretation

The product's price is expected to increase from 100 birr to 156.25 birr after two years, assuming a constant annual inflation rate of 25%.

Notice that the total increase is 56.25 birr, not 50 birr. This is because inflation compounds.

---

## 6. Purchasing Power

### Definition

**Purchasing power** refers to the quantity of goods and services that a given amount of money can buy.

When prices increase, the purchasing power of a fixed amount of money decreases.

### Example

Suppose a person has 1,000 birr today.

If prices increase by 25%, a product that costs 1,000 birr today will cost 1,250 birr after one year.

Therefore, 1,000 birr will no longer buy the same product.

### Converting future money into today's purchasing power

Suppose you will have A(t) birr after t years, and the annual inflation rate is r_f.

To express that future amount in today's purchasing-power terms, divide it by the inflation growth factor:

**Today's purchasing-power value = Future amount / (1 + r_f)^t**

In symbols:

**Real value in today's money = A(t) / (1 + r_f)^t**

Since:

A(t) = A₀(1 + r_f)^t

We obtain:

A(t) / (1 + r_f)^t = A₀

This shows that if your money grows at exactly the same rate as inflation, its purchasing power remains unchanged under this model.

### Example

Suppose you will receive 1,500 birr after two years, and annual inflation is 10%.

Today's purchasing-power value is:

Real value = 1,500 / (1.10)²

Real value = 1,500 / 1.21

**Real value ≈ 1,239.67 birr**

Although the future amount is 1,500 birr, its purchasing power is equivalent to approximately 1,239.67 birr today.

---

## 7. Nominal and Real Rates of Return

These two concepts are essential for understanding the effect of inflation on investments.

### 7.1 Nominal Rate of Return

The **nominal rate of return** is the percentage increase in the money value of an investment before adjusting for inflation.

It tells us how much the investment balance grows in monetary terms.

For example, if 10,000 birr grows to 11,200 birr in one year, the nominal rate of return is:

Nominal return = (11,200 − 10,000) / 10,000

Nominal return = 0.12 = **12%**

### 7.2 Real Rate of Return

The **real rate of return** measures the growth in an investment's purchasing power after accounting for inflation.

It tells us whether an investment has genuinely increased the amount of goods and services the money can buy.

### Three possible situations

| Nominal return         | Inflation rate     | Effect on purchasing power         |
| ---------------------- | ------------------ | ---------------------------------- |
| Greater than inflation | Lower than return  | Purchasing power increases         |
| Equal to inflation     | Equal to return    | Purchasing power remains unchanged |
| Less than inflation    | Higher than return | Purchasing power decreases         |

**Important:** The comparison above assumes the nominal return and inflation rate refer to the same period.

---

## 8. Derivation of the Exact Real Rate Formula

The exact inflation-adjusted rate of return is:

**r_a = (r − r_f) / (1 + r_f)**

Where:

* r_a = real or inflation-adjusted rate of return
* r = nominal rate of return
* r_f = inflation rate

Let's derive this formula rather than memorize it.

### Step 1: Start with an initial investment

Suppose the initial investment is A₀.

If the nominal rate of return is r, then the investment's value after one year is:

**Future investment value = A₀(1 + r)**

For example, if you invest 1,000 birr at a nominal rate of 20%:

Future value = 1,000(1 + 0.20)

Future value = 1,200 birr

### Step 2: Remove the effect of inflation

If the inflation rate is r_f, the price level increases by a factor of:

1 + r_f

To express the future investment value in today's purchasing-power terms, divide by this factor.

Therefore,

Real value = A₀(1 + r) / (1 + r_f)

This gives the investment's value in today's money.

### Step 3: Express the real value as a growth factor

By definition, if the real rate of return is r_a, the investment's real value after one year can also be expressed as:

Real value = A₀(1 + r_a)

Both expressions represent the same real value. Therefore,

A₀(1 + r_a) = A₀(1 + r) / (1 + r_f)

Divide both sides by A₀:

1 + r_a = (1 + r) / (1 + r_f)

### Step 4: Isolate the real rate

Subtract 1 from both sides:

r_a = (1 + r) / (1 + r_f) − 1

Write 1 as a fraction with denominator (1 + r_f):

r_a = (1 + r) / (1 + r_f) − (1 + r_f) / (1 + r_f)

Combine the fractions:

r_a = [(1 + r) − (1 + r_f)] / (1 + r_f)

Simplify the numerator:

(1 + r) − (1 + r_f) = 1 + r − 1 − r_f

= r − r_f

Therefore, we obtain:

# **r_a = (r − r_f) / (1 + r_f)**

This is the **exact formula for the real rate of return**, assuming the nominal return and inflation rate apply over the same period.

### Understanding the denominator

The formula has two parts:

* **Numerator: r − r_f** — the difference between the nominal return and inflation rate.
* **Denominator: 1 + r_f** — the factor used to adjust for the increase in prices.

Why not simply subtract inflation from the nominal return?

Because the difference r − r_f is not generally the exact real rate. It is only an approximation. Dividing by 1 + r_f accounts for the compounded increase in prices.

---

<!-- PAGE BREAK -->

## 9. Worked Examples: Real Rate of Return

### Example 1: Nominal return of 20%, inflation of 10%

Suppose you invest 1,000 birr at a nominal rate of 20%, while annual inflation is 10%.

Find the exact real rate of return.

#### Given

r = 20% = 0.20

r_f = 10% = 0.10

#### Formula

r_a = (r − r_f) / (1 + r_f)

#### Calculation

r_a = (0.20 − 0.10) / (1 + 0.10)

r_a = 0.10 / 1.10

r_a = 0.090909...

Therefore,

**r_a ≈ 9.09%**

#### Verify using money

Initial investment = 1,000 birr

Investment after one year:

1,000(1.20) = 1,200 birr

Purchasing-power value in today's money:

1,200 / 1.10 = 1,090.91 birr

Real gain:

1,090.91 − 1,000 = 90.91 birr

Real rate:

90.91 / 1,000 = 0.09091

**Real rate ≈ 9.09%**

Both methods give the same answer.

#### Interpretation

Although the investment balance increases by 20%, its purchasing power increases by only about 9.09%.

---

### Example 2: Nominal return equals inflation

Suppose:

r = 10% = 0.10

r_f = 10% = 0.10

Using the exact formula:

r_a = (0.10 − 0.10) / (1 + 0.10)

r_a = 0 / 1.10

**r_a = 0%**

#### Interpretation

The investment grows at the same rate as prices. The money balance increases, but its purchasing power remains unchanged.

For example, 10,000 birr grows to 11,000 birr, while a basket of goods that costs 10,000 birr also increases in price to 11,000 birr.

---

### Example 3: Nominal return is lower than inflation

Suppose:

r = 6% = 0.06

r_f = 10% = 0.10

Then:

r_a = (0.06 − 0.10) / (1 + 0.10)

r_a = −0.04 / 1.10

r_a = −0.03636...

**r_a ≈ −3.64%**

#### Interpretation

The investment balance grows in nominal terms, but its purchasing power decreases by approximately 3.64%.

A positive nominal return does not guarantee a positive real return.

---

### Example 4: Calculate the real return on a larger investment

Suppose you invest 20,000 birr at a nominal annual return of 12%. The annual inflation rate is 8%.

Find the exact real rate of return.

#### Given

r = 0.12

r_f = 0.08

#### Calculation

r_a = (0.12 − 0.08) / (1 + 0.08)

r_a = 0.04 / 1.08

r_a = 0.037037...

**r_a ≈ 3.70%**

#### Interpretation

The investment's purchasing power grows by approximately 3.70%, even though the money balance grows by 12%.

---

## 10. Approximation of the Real Rate

When the nominal rate and inflation rate are relatively small, the real rate is sometimes approximated by:

**r_a ≈ r − r_f**

This is called the approximate real rate formula.

### Why is it an approximation?

The exact formula is:

r_a = (r − r_f) / (1 + r_f)

If the inflation rate is small, then 1 + r_f is close to 1.

Consequently,

(r − r_f) / (1 + r_f) ≈ r − r_f

However, the approximation becomes less accurate as the rates increase.

### Example

Suppose:

r = 20%

r_f = 10%

**Approximate calculation:**

r_a ≈ 20% − 10%

r_a ≈ 10%

**Exact calculation:**

r_a = (0.20 − 0.10) / 1.10

r_a ≈ 9.09%

| Method              |              Real rate |
| ------------------- | ---------------------: |
| Approximate formula |                 10.00% |
| Exact formula       |                  9.09% |
| Difference          | 0.91 percentage points |

### Exam reminder

If the question asks for the **exact real rate**, use:

r_a = (r − r_f) / (1 + r_f)

If the question explicitly asks for an approximation, use:

r_a ≈ r − r_f

---

## 11. Practical Applications

Understanding inflation is useful in several areas of finance and economics.

### 11.1 Personal savings

A savings account may pay interest, but if inflation is higher than the interest rate, the purchasing power of the savings decreases.

### 11.2 Investment evaluation

Investors compare nominal returns with inflation to determine whether their investments have increased their purchasing power.

### 11.3 Financial planning

When planning future expenses, inflation helps estimate how much money may be required to purchase goods and services.

### 11.4 Salary evaluation

A salary increase does not necessarily mean an increase in purchasing power. If salary grows more slowly than prices, the worker's real income decreases.

### 11.5 Long-term budgeting

Inflation assumptions help estimate future education costs, housing expenses, and other long-term financial needs.

---

## 12. Common Mistakes

### Mistake 1: Treating inflation as simple addition every year

Incorrect:

A(t) = A₀(1 + tr_f)

This expression does not model annual compounding.

Correct:

A(t) = A₀(1 + r_f)^t

### Mistake 2: Using percentages without converting them to decimals

For example:

10% = 0.10, not 10.

Always convert percentages to decimals before substituting them into these formulas.

### Mistake 3: Confusing nominal return with real return

The nominal rate measures growth in the money balance.

The real rate measures growth in purchasing power.

They are not generally equal.

### Mistake 4: Assuming the exact real rate equals nominal return minus inflation

The expression r − r_f is an approximation, not the exact formula.

The exact formula is:

r_a = (r − r_f) / (1 + r_f)

### Mistake 5: Ignoring the time period

The nominal return and inflation rate must refer to the same period when applying the real-rate formula.

For example, do not directly compare a monthly investment return with an annual inflation rate without converting them to compatible periods.

### Mistake 6: Thinking that a positive nominal return always means an investment is profitable in real terms

If inflation exceeds the nominal return, the investment loses purchasing power.

---

## 13. Formula Summary

| Concept                               | Formula                     |
| ------------------------------------- | --------------------------- |
| Future price under constant inflation | A(t) = A₀(1 + r_f)^t        |
| Price after one year                  | A(1) = A₀(1 + r_f)          |
| Purchasing power in today's money     | A(t) / (1 + r_f)^t          |
| Future investment value               | A₀(1 + r)                   |
| Exact real rate of return             | r_a = (r − r_f) / (1 + r_f) |
| Approximate real rate of return       | r_a ≈ r − r_f               |

### Symbols

| Symbol | Meaning                             |
| ------ | ----------------------------------- |
| A₀     | Initial price or initial investment |
| A(t)   | Price or amount after t years       |
| r_f    | Inflation rate                      |
| r      | Nominal rate of return              |
| r_a    | Real rate of return                 |
| t      | Time in years                       |

---

## 14. Practice Questions

Try to solve these questions before checking the solutions.

### Question 1: Future price

A product costs 500 birr today. If annual inflation is 8%, calculate its expected price after three years.

### Question 2: Future price

The price of a product is 2,000 birr today. Find its expected price after four years if annual inflation is 12%.

### Question 3: Purchasing power

You will receive 5,000 birr after two years. If annual inflation is 10%, calculate its value in today's purchasing-power terms.

### Question 4: Exact real rate

An investment earns a nominal annual return of 15%, while inflation is 9%. Calculate the exact real rate of return.

### Question 5: Approximate versus exact real rate

An investment earns 18% annually, while inflation is 12%.

1. Calculate the approximate real rate.
2. Calculate the exact real rate.
3. Find the difference between the two answers.

### Question 6: Interpretation

An investment earns a nominal return of 7%, while inflation is 10%.

1. Calculate the exact real rate.
2. Explain what the result means.

### Question 7: Derivation

Starting from:

A(t) = A₀(1 + r_f)^t

Explain how the formula is obtained by considering the price after one year, two years, and three years.

### Question 8: Derivation

Starting from:

1 + r_a = (1 + r) / (1 + r_f)

Derive the exact real rate formula:

r_a = (r − r_f) / (1 + r_f)

---

## 15. Solutions to Practice Questions

### Solution 1

Given:

A₀ = 500, r_f = 0.08, t = 3

A(3) = 500(1.08)³

**A(3) ≈ 629.86 birr**

### Solution 2

Given:

A₀ = 2,000, r_f = 0.12, t = 4

A(4) = 2,000(1.12)⁴

**A(4) ≈ 3,147.04 birr**

### Solution 3

Given:

Future amount = 5,000 birr, r_f = 0.10, t = 2

Real value = 5,000 / (1.10)²

Real value = 5,000 / 1.21

**Real value ≈ 4,132.23 birr**

### Solution 4

Given:

r = 0.15, r_f = 0.09

r_a = (0.15 − 0.09) / (1 + 0.09)

r_a = 0.06 / 1.09

**r_a ≈ 5.50%**

### Solution 5

Given:

r = 0.18, r_f = 0.12

**1. Approximate rate**

r_a ≈ 0.18 − 0.12

**Approximate rate = 6%**

**2. Exact rate**

r_a = (0.18 − 0.12) / 1.12

r_a = 0.06 / 1.12

**Exact rate ≈ 5.36%**

**3. Difference**

Difference ≈ 6.00% − 5.36%

**Difference ≈ 0.64 percentage points**

### Solution 6

Given:

r = 0.07, r_f = 0.10

r_a = (0.07 − 0.10) / 1.10

r_a = −0.03 / 1.10

**r_a ≈ −2.73%**

The investment loses purchasing power by approximately 2.73%, even though its nominal balance increases.

### Solution 7

After one year:

A(1) = A₀(1 + r_f)

After two years:

A(2) = A₀(1 + r_f)²

After three years:

A(3) = A₀(1 + r_f)³

Therefore, after t years:

**A(t) = A₀(1 + r_f)^t**

### Solution 8

Start with:

1 + r_a = (1 + r) / (1 + r_f)

Subtract 1 from both sides:

r_a = (1 + r) / (1 + r_f) − 1

Use a common denominator:

r_a = [(1 + r) − (1 + r_f)] / (1 + r_f)

Simplify the numerator:

(1 + r) − (1 + r_f) = r − r_f

Therefore:

**r_a = (r − r_f) / (1 + r_f)**

---

## 16. Conclusion

Inflation is a central concept in financial mathematics because it changes the purchasing power of money over time.

The formula:

**A(t) = A₀(1 + r_f)^t**

allows us to estimate future prices under a constant inflation rate.

However, an increase in the money balance does not necessarily mean an increase in purchasing power. To evaluate the real performance of an investment, we use the exact inflation-adjusted rate:

**r_a = (r − r_f) / (1 + r_f)**

The approximate formula, r_a ≈ r − r_f, is convenient, but the exact formula is more accurate.

### Final takeaway

> **Nominal return tells us how much the money grows. Real return tells us how much purchasing power grows.**

Understanding this distinction is essential for evaluating investments, savings, salaries, and future financial needs.

---

**End of Topic 2: Inflation**

**Next topic:** Annuities — periodic payments, accumulated value, and present value.
