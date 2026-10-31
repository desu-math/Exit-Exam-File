# 📘 Bonds — Financial Mathematics (Math4313)

**Course:** Financial Mathematics (Math4313)
**Topic:** Bonds
**Department:** Applied Mathematics
**Institution:** Adama Science and Technology University (ASTU)
**Primary Reference:** Lecture 1 — Tamirat T. Dufera (PhD)
**Supplementary References:** An Introduction to Mathematical Finance with Applications; An Introduction to Financial Mathematics: Option Valuation.

---

## 📑 Table of Contents

1. [Learning Objectives](#1-learning-objectives)
2. [Introduction and Motivation](#2-introduction-and-motivation)
3. [What Is a Bond?](#3-what-is-a-bond)
4. [Important Bond Terminology](#4-important-bond-terminology)
5. [Zero-Coupon Bonds](#5-zero-coupon-bonds)
6. [Mathematical Valuation of Zero-Coupon Bonds](#6-mathematical-valuation-of-zero-coupon-bonds)
7. [Value of a Bond at Any Time](#7-value-of-a-bond-at-any-time)
8. [Coupon Bonds](#8-coupon-bonds)
9. [Mathematical Valuation of Coupon Bonds](#9-mathematical-valuation-of-coupon-bonds)
10. [Worked Example: Coupon Bond Valuation](#10-worked-example-coupon-bond-valuation)
11. [Relationship Between Bond Prices and Interest Rates](#11-relationship-between-bond-prices-and-interest-rates)
12. [Additional Bond Concepts](#12-additional-bond-concepts)
13. [Bond Price Classification](#13-bond-price-classification)
14. [Practical Applications of Bonds](#14-practical-applications-of-bonds)
15. [Common Mistakes](#15-common-mistakes)
16. [Formula Summary](#16-formula-summary)
17. [How to Approach Bond Valuation Problems](#17-how-to-approach-bond-valuation-problems)
18. [Practice Questions](#18-practice-questions)
19. [Solutions to Practice Questions](#19-solutions-to-practice-questions)
20. [Final Summary](#20-final-summary)

---

# 1. Learning Objectives

After studying this topic, you should be able to:

* Define a bond and explain its financial purpose.
* Distinguish between zero-coupon bonds and coupon bonds.
* Understand face value, maturity date, and coupon payments.
* Calculate the present value of a zero-coupon bond.
* Calculate the value of a bond at any given time before maturity.
* Derive and apply the coupon bond valuation formula.
* Explain the relationship between market interest rates and bond prices.
* Understand coupon rate, current yield, and yield to maturity.
* Classify bonds as par, discount, or premium bonds.
* Apply present value concepts to practical bond valuation problems.

---

# 2. Introduction and Motivation

Governments, corporations, and other institutions sometimes need large amounts of money to finance their activities.

For example:

* A government may need money to construct roads, schools, and hospitals.
* A company may need money to expand its business.
* An institution may need money to purchase equipment or finance a project.

One way to obtain this money is by issuing bonds.

When an investor purchases a bond, the investor is essentially lending money to the issuing institution. In return, the issuer promises to make specified future payments.

The mathematical problem is:

**How much should an investor pay today for a bond that promises to make payments in the future?**

This is where the time value of money becomes important.

Money received in the future is not generally worth the same amount as money received today. Therefore, we use present value and discounting to calculate the current price of a bond.

---

# 3. What Is a Bond?

A bond is a financial contract issued by governments, corporations, or other institutions.

It requires that the holder be reimbursed a specific amount at a prescribed time in the future.

In simple terms, a bond is a financial instrument through which an institution borrows money from investors and promises future payments.

### Example

Suppose the government issues a bond.

You purchase the bond for 900 ETB, and the government promises to pay you 1,000 ETB after a specified period.

In this situation:

* The government is the bond issuer.
* You are the bondholder.
* 900 ETB is the initial purchase price.
* 1,000 ETB is the promised payment at maturity.

The difference between the purchase price and the maturity payment represents your investment gain, assuming the issuer fulfills its obligation.

### Important idea

A bond represents a borrowing relationship:

**Issuer borrows money → Investor provides money → Issuer makes future payments.**

---

# 4. Important Bond Terminology

Before studying the mathematical formulas, we need to understand the important terminology.

| Term                    | Meaning                                                                                        |
| ----------------------- | ---------------------------------------------------------------------------------------------- |
| Bond issuer             | Government, corporation, or institution that issues the bond                                   |
| Bondholder              | Investor who purchases and holds the bond                                                      |
| Face value (F)          | Amount promised to be repaid at maturity                                                       |
| Par value               | Another name for face value                                                                    |
| Maturity date           | Date when the bond reaches the end of its life                                                 |
| Maturity period (T)     | Time remaining until maturity                                                                  |
| Coupon payment (C)      | Periodic interest payment made to the bondholder                                               |
| Coupon rate             | Annual coupon payment divided by face value                                                    |
| Bond price (B₀)         | Current market price of the bond                                                               |
| Current yield           | Annual coupon payment divided by current market price                                          |
| Yield to maturity (YTM) | Discount rate that equates the present value of future bond payments to the current bond price |

### Important distinction

The face value and current market price are not necessarily equal.

For example, a bond may have:

* Face value = 10,000 ETB
* Current market price = 9,500 ETB

The issuer still promises to repay 10,000 ETB at maturity, even though the investor pays only 9,500 ETB to purchase the bond.

---

# 5. Zero-Coupon Bonds

A zero-coupon bond is a bond that does not make periodic coupon payments.

Instead, the investor purchases the bond at a price below its face value and receives the full face value at maturity.

### Example

Suppose you purchase a zero-coupon bond for 800 ETB today.

It promises to pay 1,000 ETB after two years.

You receive no payments during those two years.

At maturity:

Amount received = 1,000 ETB

Initial investment = 800 ETB

Investment gain = 1,000 − 800

**Investment gain = 200 ETB**

The investor earns a return from the difference between the purchase price and the amount received at maturity.

### Key characteristics

* No periodic coupon payments.
* Purchased below face value in the usual case.
* Face value is paid at maturity.
* Its value is calculated using the present value of the future payment.

---

# 6. Mathematical Valuation of Zero-Coupon Bonds

Your instructor's lecture note gives the following formula:

**B₀ = Fe^(-rT)**

Where:

| Symbol | Meaning                                      |
| ------ | -------------------------------------------- |
| B₀     | Current price of the bond                    |
| F      | Face value                                   |
| r      | Continuously compounded interest rate        |
| T      | Time until maturity                          |
| e      | Mathematical constant, approximately 2.71828 |

This formula calculates the present value of the face value.

## 6.1 Derivation of the Formula

Recall the continuous compound interest formula:

A(t) = A₀e^(rt)

For a zero-coupon bond:

* A₀ represents the initial bond price B₀.
* A(t) represents the future face value F.
* t represents the maturity period T.

Therefore:

F = B₀e^(rT)

Divide both sides by e^(rT):

B₀ = F/e^(rT)

Using the property 1/e^(rT) = e^(-rT):

**B₀ = Fe^(-rT)**

This is the zero-coupon bond valuation formula.

### Interpretation

The formula discounts the future face value back to the present using a continuously compounded interest rate.

## 6.2 Worked Example

Suppose a zero-coupon bond has:

* Face value = 10,000 ETB
* Interest rate = 8% per year
* Maturity = 3 years
* Continuous compounding

Find its current price.

**Step 1: Identify the given values.**

F = 10,000

r = 0.08

T = 3

**Step 2: Apply the formula.**

B₀ = Fe^(-rT)

B₀ = 10,000e^(-0.08 × 3)

B₀ = 10,000e^(-0.24)

**Step 3: Calculate.**

B₀ ≈ 10,000 × 0.7866

**B₀ ≈ 7,866.28 ETB**

Therefore, the current price of the bond is approximately 7,866.28 ETB.

### Interpretation

An investor should pay approximately 7,866.28 ETB today to receive 10,000 ETB after three years, assuming an 8% continuously compounded discount rate.

---

# 7. Value of a Bond at Any Time

Your instructor also gives the value of a zero-coupon bond at any time t:

**Bₜ = Fe^(-r(T−t)) = B₀e^(rt)**

This formula calculates the bond's value at any time before maturity.

Where:

* Bₜ = Bond value at time t.
* F = Face value.
* r = Continuously compounded interest rate.
* T = Maturity time.
* t = Current time.

## 7.1 Understanding the First Expression

Bₜ = Fe^(-r(T−t))

The expression T − t represents the remaining time until maturity.

For example:

If a bond matures in five years and we are currently at year two:

Remaining time = 5 − 2 = 3 years.

Therefore, we discount the face value over three years.

## 7.2 Understanding the Second Expression

Bₜ = B₀e^(rt)

This expression shows that the bond's value grows continuously from its initial price.

It follows directly from the continuous compound interest formula.

## 7.3 Worked Example

Suppose:

* Face value = 10,000 ETB
* Continuous interest rate = 8%
* Maturity = 5 years

Find the bond's value after two years.

**Step 1: Identify the remaining time.**

T − t = 5 − 2 = 3 years.

**Step 2: Apply the formula.**

Bₜ = Fe^(-r(T−t))

B₂ = 10,000e^(-0.08 × 3)

**B₂ ≈ 7,866.28 ETB**

### Important observation at maturity

At maturity, t = T.

Therefore:

Bₜ = Fe^(-r(T−T))

Bₜ = Fe⁰

**Bₜ = F**

This confirms that the bond's value equals its face value at maturity.

---

# 8. Coupon Bonds

A coupon bond makes periodic payments to the bondholder during its lifetime and returns the face value at maturity.

Unlike a zero-coupon bond, a coupon bond provides two types of cash flows:

1. Periodic coupon payments.
2. Face value repayment at maturity.

### Example

Suppose a bond has:

* Face value = 10,000 ETB
* Annual coupon payment = 800 ETB
* Maturity = 3 years

The payment schedule is:

| Year   |    Payment |
| ------ | ---------: |
| Year 1 |    800 ETB |
| Year 2 |    800 ETB |
| Year 3 | 10,800 ETB |

Why is the final payment 10,800 ETB?

Because the investor receives both the final coupon and the face value:

Final payment = 800 + 10,000

Final payment = 10,800 ETB.

### Difference between zero-coupon and coupon bonds

| Feature              | Zero-Coupon Bond                                 | Coupon Bond                             |
| -------------------- | ------------------------------------------------ | --------------------------------------- |
| Periodic payments    | No                                               | Yes                                     |
| Face value repayment | At maturity                                      | At maturity                             |
| Source of return     | Difference between purchase price and face value | Coupons and possible price gain or loss |
| Cash flows           | One payment                                      | Multiple payments                       |

---

# 9. Mathematical Valuation of Coupon Bonds

Your instructor gives the following formula:

**B₀ = Σ(n=1 to N) Cₙe^(-rtₙ) + Fe^(-rT)**

This is the central formula for coupon bond valuation in the lecture.

Where:

| Symbol | Meaning                                |
| ------ | -------------------------------------- |
| B₀     | Current price of the coupon bond       |
| Cₙ     | Coupon payment at time tₙ              |
| tₙ     | Time when coupon payment n is received |
| N      | Total number of coupon payments        |
| F      | Face value                             |
| T      | Maturity time                          |
| r      | Continuously compounded interest rate  |

The formula states:

**Current bond price = Present value of all coupon payments + Present value of face value.**

## 9.1 Derivation of the Coupon Bond Formula

Suppose a bond makes three coupon payments:

* C₁ at time t₁.
* C₂ at time t₂.
* C₃ at time t₃.

At maturity T, the investor also receives face value F.

The cash flows are:

| Time | Cash flow |
| ---- | --------: |
| t₁   |        C₁ |
| t₂   |        C₂ |
| t₃   |        C₃ |
| T    |         F |

From continuous compounding, the present value of a future amount A received at time t is:

PV = Ae^(-rt)

Therefore, the present value of each coupon is:

PV₁ = C₁e^(-rt₁)

PV₂ = C₂e^(-rt₂)

PV₃ = C₃e^(-rt₃)

The present value of the face value is:

PV(F) = Fe^(-rT)

The total current price is the sum of all these present values:

B₀ = C₁e^(-rt₁) + C₂e^(-rt₂) + C₃e^(-rt₃) + Fe^(-rT)

For N coupon payments, we generalize the expression:

**B₀ = Σ(n=1 to N) Cₙe^(-rtₙ) + Fe^(-rT)**

This is the coupon bond valuation formula in your lecture note.

### Important idea

Every future payment must be discounted according to the time at which it is received.

We do not simply add all future payments together because money received at different times has different present values.

---

# 10. Worked Example: Coupon Bond Valuation

Suppose a bond has:

* Face value = 10,000 ETB
* Annual coupon = 800 ETB
* Maturity = 3 years
* Continuous discount rate = 10%
* Coupons are paid annually.

Find the current price of the bond.

### Step 1: List the future cash flows.

| Time   |  Cash flow |
| ------ | ---------: |
| Year 1 |    800 ETB |
| Year 2 |    800 ETB |
| Year 3 | 10,800 ETB |

The final payment includes the last coupon and the face value.

### Step 2: Write the valuation formula.

B₀ = C₁e^(-rt₁) + C₂e^(-rt₂) + C₃e^(-rt₃) + Fe^(-rT)

### Step 3: Substitute the values.

B₀ = 800e^(-0.10 × 1) + 800e^(-0.10 × 2) + 800e^(-0.10 × 3) + 10,000e^(-0.10 × 3)

### Step 4: Calculate each present value.

First coupon:

800e^(-0.10) ≈ 723.87

Second coupon:

800e^(-0.20) ≈ 654.98

Third coupon:

800e^(-0.30) ≈ 592.65

Face value:

10,000e^(-0.30) ≈ 7,408.18

### Step 5: Add everything.

B₀ = 723.87 + 654.98 + 592.65 + 7,408.18

**B₀ ≈ 9,379.69 ETB**

Therefore, the current price of the coupon bond is approximately 9,379.69 ETB.

---

# 11. Relationship Between Bond Prices and Interest Rates

One of the most important principles in bond valuation is the inverse relationship between market interest rates and existing fixed-coupon bond prices.

**When market interest rates increase, existing bond prices generally decrease.**

**When market interest rates decrease, existing bond prices generally increase.**

## 11.1 Why Does This Happen?

Suppose you own a bond that promises to pay 1,000 ETB after one year.

If the market interest rate is 5%, its present value under continuous discounting is:

B₀ = 1,000e^(-0.05)

B₀ ≈ 951.23 ETB

Now suppose the market interest rate increases to 10%.

B₀ = 1,000e^(-0.10)

B₀ ≈ 904.84 ETB

The bond price decreases.

Why?

Because investors can now earn higher returns from other investments. Therefore, they are less willing to pay the previous price for an existing bond with the same future payment.

### Summary

| Market interest rate | Existing fixed-coupon bond price |
| -------------------- | -------------------------------- |
| Increases            | Decreases                        |
| Decreases            | Increases                        |

This relationship is fundamental to understanding bond markets.

---

# 12. Additional Bond Concepts

The following concepts supplement your instructor's lecture and help develop a broader understanding of bond markets.

## 12.1 Coupon Rate

The coupon rate is the annual coupon payment expressed as a percentage of the bond's face value.

Formula:

**Coupon rate = Annual coupon payment / Face value**

Example:

Face value = 10,000 ETB

Annual coupon = 800 ETB

Coupon rate = 800/10,000

**Coupon rate = 8%**

The coupon rate is based on face value, not the current market price.

## 12.2 Current Yield

Current yield measures the annual coupon income relative to the current market price.

Formula:

**Current yield = Annual coupon payment / Current market price**

Example:

Annual coupon = 800 ETB

Current market price = 9,000 ETB

Current yield = 800/9,000

**Current yield ≈ 8.89%**

Notice:

* Coupon rate = 8%.
* Current yield ≈ 8.89%.

They are different because the bond is currently selling below its face value.

## 12.3 Yield to Maturity (YTM)

Yield to maturity is the rate of return an investor expects to earn by purchasing a bond at its current price and holding it until maturity, under the standard assumption that coupon payments are reinvested at the same rate.

Mathematically, YTM is the discount rate that makes:

**Current bond price = Present value of all future bond payments.**

For a bond with equal annual coupon payments, annual yield y, N remaining annual payments, coupon C, and face value F:

B₀ = C/(1+y) + C/(1+y)² + ... + (C+F)/(1+y)^N

Using the present value of an annuity, this becomes:

**B₀ = C[1 − (1+y)^(-N)]/y + F(1+y)^(-N)**

Notice the connection with annuities:

* Coupon payments form an annuity.
* Face value is a single future payment.

YTM is generally calculated using numerical methods or financial software because the unknown rate y cannot usually be isolated through simple algebra.

**Important distinction:** The YTM formula above uses discrete annual compounding. Your instructor's main bond valuation formula uses continuous discounting. Do not mix these two conventions without converting the rates appropriately.

---

# 13. Bond Price Classification

Bonds can be classified according to the relationship between their current market price and face value.

| Bond type     | Price relationship        |
| ------------- | ------------------------- |
| Par bond      | Market price = Face value |
| Discount bond | Market price < Face value |
| Premium bond  | Market price > Face value |

For a standard fixed-coupon bond:

* If the coupon rate equals the required market yield, the bond sells at par.
* If the coupon rate is below the required market yield, the bond sells at a discount.
* If the coupon rate is above the required market yield, the bond sells at a premium.

### Example

Suppose a bond has a face value of 10,000 ETB.

| Market price | Classification |
| -----------: | -------------- |
|   10,000 ETB | Par bond       |
|    9,500 ETB | Discount bond  |
|   10,500 ETB | Premium bond   |

---

# 14. Practical Applications of Bonds

Bonds are important in several areas of finance and economics.

### 1. Government Financing

Governments issue bonds to raise money for infrastructure, public services, and development projects.

### 2. Corporate Financing

Companies issue bonds to finance expansion, purchase equipment, or support business operations.

### 3. Investment

Investors purchase bonds to receive future coupon payments and repayment of principal.

### 4. Financial Valuation

Financial analysts use present value methods to determine the fair price of bonds.

### 5. Interest-Rate Risk Management

Investors study how bond prices respond to changes in market interest rates.

---

# 15. Common Mistakes

1. Confusing face value with current market price.
2. Forgetting to include the face value in the final coupon payment.
3. Discounting all coupon payments using the same time when they occur at different dates.
4. Confusing coupon rate with current yield.
5. Assuming that a zero-coupon bond pays periodic interest.
6. Forgetting that higher market interest rates generally decrease the prices of existing fixed-coupon bonds.
7. Using an annual interest rate without checking whether the formula requires continuous or discrete compounding.
8. Treating YTM as the same thing as coupon rate.
9. Adding future cash flows directly instead of discounting them to the present.

---

# 16. Formula Summary

| Concept                         | Formula                                |
| ------------------------------- | -------------------------------------- |
| Zero-coupon bond price          | B₀ = Fe^(-rT)                          |
| Bond value at time t            | Bₜ = Fe^(-r(T−t))                      |
| Bond value using initial price  | Bₜ = B₀e^(rt)                          |
| Coupon bond price               | B₀ = Σ Cₙe^(-rtₙ) + Fe^(-rT)           |
| Coupon rate                     | Annual coupon / Face value             |
| Current yield                   | Annual coupon / Current market price   |
| YTM valuation (annual discrete) | B₀ = C[1 − (1+y)^(-N)]/y + F(1+y)^(-N) |

### Essential relationships

* Zero-coupon bond: One payment at maturity.
* Coupon bond: Periodic coupon payments plus face value at maturity.
* Higher market interest rate: Lower existing fixed-coupon bond price.
* Lower market interest rate: Higher existing fixed-coupon bond price.
* At maturity: A zero-coupon bond's value equals its face value.

---

# 17. How to Approach Bond Valuation Problems

When solving bond valuation problems, follow these steps:

**Step 1: Identify the type of bond.**

Determine whether it is a zero-coupon bond or a coupon bond.

**Step 2: Identify the given information.**

Write down:

* Face value (F).
* Interest rate (r).
* Maturity (T).
* Coupon payments (Cₙ), if applicable.
* Coupon payment times (tₙ).

**Step 3: Check the compounding convention.**

Determine whether the problem uses continuous or discrete compounding.

**Step 4: Choose the correct formula.**

For a zero-coupon bond:

B₀ = Fe^(-rT)

For a coupon bond:

B₀ = Σ Cₙe^(-rtₙ) + Fe^(-rT)

**Step 5: Substitute the values.**

Pay particular attention to the timing of each payment.

**Step 6: Calculate and interpret.**

Present the answer with the correct currency and explain what the calculated price represents.

---

# 18. Practice Questions

Try solving these questions before checking the solutions.

## Question 1: Zero-Coupon Bond

A zero-coupon bond has:

* Face value = 20,000 ETB.
* Continuous interest rate = 6%.
* Maturity = 4 years.

Find its current price.

## Question 2: Bond Value at a Given Time

A zero-coupon bond has:

* Face value = 15,000 ETB.
* Continuous interest rate = 5%.
* Maturity = 6 years.

Find its value after 2 years.

## Question 3: Coupon Bond

A bond has:

* Face value = 5,000 ETB.
* Annual coupon = 400 ETB.
* Maturity = 2 years.
* Continuous discount rate = 8%.

Coupons are paid annually.

Calculate the current price of the bond.

## Question 4: Conceptual Understanding

Explain why the price of an existing fixed-coupon bond decreases when market interest rates increase.

## Question 5: Coupon Rate and Current Yield

A bond has:

* Face value = 10,000 ETB.
* Annual coupon payment = 900 ETB.
* Current market price = 9,500 ETB.

Calculate:

a) The coupon rate.

b) The current yield.

---

# 19. Solutions to Practice Questions

## Solution 1: Zero-Coupon Bond

Given:

F = 20,000

r = 0.06

T = 4

Formula:

B₀ = Fe^(-rT)

Substitute:

B₀ = 20,000e^(-0.06 × 4)

B₀ = 20,000e^(-0.24)

**B₀ ≈ 15,732.56 ETB**

## Solution 2: Bond Value at a Given Time

Given:

F = 15,000

r = 0.05

T = 6

t = 2

Remaining time:

T − t = 6 − 2 = 4 years.

Formula:

Bₜ = Fe^(-r(T−t))

Substitute:

B₂ = 15,000e^(-0.05 × 4)

B₂ = 15,000e^(-0.20)

**B₂ ≈ 12,280.96 ETB**

## Solution 3: Coupon Bond

Given:

F = 5,000

C = 400

r = 0.08

T = 2

Formula:

B₀ = 400e^(-0.08 × 1) + 400e^(-0.08 × 2) + 5,000e^(-0.08 × 2)

The final coupon and face value are both received at year 2.

Calculate:

B₀ = 400e^(-0.08) + 5,400e^(-0.16)

**B₀ ≈ 4,970.82 ETB**

## Solution 4: Conceptual Understanding

When market interest rates increase, newly issued bonds offer higher returns.

Existing fixed-coupon bonds become less attractive because their coupon payments remain unchanged.

Therefore, their market prices must decrease to make their returns competitive with the new market interest rates.

## Solution 5: Coupon Rate and Current Yield

Given:

F = 10,000

Annual coupon = 900

Market price = 9,500

### a) Coupon Rate

Coupon rate = Annual coupon / Face value

Coupon rate = 900/10,000

Coupon rate = 0.09

**Coupon rate = 9%**

### b) Current Yield

Current yield = Annual coupon / Current market price

Current yield = 900/9,500

Current yield ≈ 0.09474

**Current yield ≈ 9.47%**

---

# 20. Final Summary

A bond is a financial contract through which an institution borrows money from investors and promises future payments.

There are two important types of bonds:

**Zero-coupon bonds:** These bonds do not make periodic coupon payments. Instead, they pay the face value at maturity.

**Coupon bonds:** These bonds make periodic coupon payments and return the face value at maturity.

The mathematical foundation of bond valuation is the time value of money.

We calculate the current price of a bond by discounting all future payments to the present.

For zero-coupon bonds:

**B₀ = Fe^(-rT)**

For coupon bonds:

**B₀ = Σ Cₙe^(-rtₙ) + Fe^(-rT)**

The most important market relationship is:

**Interest rates increase → Existing bond prices decrease.**

**Interest rates decrease → Existing bond prices increase.**

Understanding bonds also prepares us for more advanced financial concepts, especially investment evaluation and the internal rate of return.

---

## 🎯 Next Topic: Internal Rate of Return (IRR)

In the next lesson, we will study how to evaluate an investment by finding the interest rate that makes the present value of future returns equal to the initial investment.

We will also examine the mathematical existence and uniqueness of IRR.
