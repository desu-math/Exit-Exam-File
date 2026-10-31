# Bonds — Algorithms and Step-by-Step Procedures

## Table of Contents

1. [General Procedure](#1-general-procedure)
2. [Zero-Coupon Bond Valuation](#2-zero-coupon-bond-valuation)
3. [Value of a Zero-Coupon Bond at a Future Time](#3-value-of-a-zero-coupon-bond-at-a-future-time)
4. [Coupon Bond Valuation](#4-coupon-bond-valuation)
5. [Complete Worked Examples](#5-complete-worked-examples)
6. [Pseudocode](#6-pseudocode)
7. [Formula Selection Guide](#7-formula-selection-guide)
8. [Common Mistakes and Checks](#8-common-mistakes-and-checks)
9. [Summary](#9-summary)

---

## 1. General Procedure

A bond is a financial contract issued by governments, corporations, or other institutions. The issuer promises to pay the bondholder a specified amount at a prescribed future time.

Before solving a bond problem, identify the following quantities:

| Symbol | Meaning                                      |
| ------ | -------------------------------------------- |
| B₀     | Initial price of the bond                    |
| Bₜ     | Value of the bond at time t                  |
| F      | Face value or par value                      |
| r      | Continuously compounded annual interest rate |
| T      | Maturity time                                |
| t      | Current time                                 |
| Cₙ     | Coupon payment at time tₙ                    |
| N      | Number of coupon payments                    |

### General Steps

1. Read the problem carefully.
2. Identify whether the bond is a zero-coupon bond or a coupon bond.
3. Extract the given values.
4. Identify the required quantity.
5. Select the appropriate formula.
6. Substitute the values.
7. Calculate the result.
8. Check whether the answer is reasonable.

---

## 2. Zero-Coupon Bond Valuation

### Purpose

Calculate the present price of a bond that pays only its face value at maturity and makes no intermediate coupon payments.

### Formula

B₀ = F e^(-rT)

Where:

* B₀ = present bond price
* F = face value
* r = continuously compounded annual interest rate
* T = time to maturity in years
* e = exponential constant, approximately 2.71828

### Step-by-Step Algorithm

**Step 1:** Identify the face value F.

**Step 2:** Identify the annual interest rate r.

**Step 3:** Identify the maturity time T.

**Step 4:** Convert the interest rate into decimal form if it is given as a percentage.

For example:

6% = 0.06

**Step 5:** Substitute the values into:

B₀ = F e^(-rT)

**Step 6:** Evaluate the exponential expression.

**Step 7:** Report the present bond price.

### Worked Example

A zero-coupon bond has a face value of 1,000 ETB and matures after 3 years. If the continuously compounded annual interest rate is 6%, calculate its present price.

**Given:**

* F = 1,000 ETB
* r = 0.06
* T = 3 years

**Solution:**

Using:

B₀ = F e^(-rT)

Substitute:

B₀ = 1,000 e^(-0.06 × 3)

B₀ = 1,000 e^(-0.18)

B₀ ≈ 1,000 × 0.83527

**Final Answer:**

B₀ ≈ 835.27 ETB

Therefore, the bond should cost approximately 835.27 ETB today.

---

## 3. Value of a Zero-Coupon Bond at a Future Time

### Purpose

Calculate the value of a zero-coupon bond at a time before its maturity.

The lecture gives the following formula:

Bₜ = F e^(-r(T-t))

It also establishes the equivalent relationship:

Bₜ = B₀ e^(rt)

### Step-by-Step Algorithm

**Step 1:** Identify the face value F.

**Step 2:** Identify the annual interest rate r.

**Step 3:** Identify the maturity time T.

**Step 4:** Identify the time t at which the bond's value is required.

**Step 5:** Substitute the values into:

Bₜ = F e^(-r(T-t))

**Step 6:** Calculate the remaining time to maturity:

Remaining time = T - t

**Step 7:** Evaluate the exponential expression.

**Step 8:** Report the bond's value at time t.

### Worked Example

A zero-coupon bond has a face value of 1,000 ETB and matures after 3 years. The continuously compounded annual interest rate is 6%. Find its value after 1.5 years.

**Given:**

* F = 1,000 ETB
* r = 0.06
* T = 3 years
* t = 1.5 years

**Solution:**

Using:

Bₜ = F e^(-r(T-t))

Substitute:

B₁.₅ = 1,000 e^(-0.06(3-1.5))

B₁.₅ = 1,000 e^(-0.09)

B₁.₅ ≈ 913.93 ETB

**Final Answer:**

B₁.₅ ≈ 913.93 ETB

The bond is worth approximately 913.93 ETB after 1.5 years.

### Alternative Method

We can also calculate the value using:

Bₜ = B₀ e^(rt)

First calculate the initial price:

B₀ = 1,000 e^(-0.06 × 3)

B₀ ≈ 835.27 ETB

Then:

B₁.₅ = 835.27 e^(0.06 × 1.5)

B₁.₅ ≈ 913.93 ETB

Both methods give the same result.

---

## 4. Coupon Bond Valuation

### Purpose

Calculate the present price of a bond that pays periodic coupon payments during its lifetime and returns its face value at maturity.

Unlike a zero-coupon bond, a coupon bond provides several payments before maturity.

### Formula

B₀ = Σ(n=1 to N) Cₙ e^(-rtₙ) + F e^(-rT)

Where:

* B₀ = present price of the coupon bond
* Cₙ = coupon payment at time tₙ
* tₙ = time when coupon n is paid
* N = total number of coupon payments
* F = face value
* r = continuously compounded annual interest rate
* T = maturity time

### Understanding the Formula

The formula has two main parts:

**Part 1: Present value of coupon payments**

PV of coupons = Σ(n=1 to N) Cₙ e^(-rtₙ)

This calculates the present value of every coupon payment.

**Part 2: Present value of face value**

PV of face value = F e^(-rT)

This calculates the present value of the amount received at maturity.

Therefore:

Bond price = PV of all coupons + PV of face value

### Step-by-Step Algorithm

**Step 1:** Identify the face value F.

**Step 2:** Identify the continuously compounded annual interest rate r.

**Step 3:** Identify the maturity time T.

**Step 4:** Identify the number of coupon payments N.

**Step 5:** List every coupon payment Cₙ and its payment time tₙ.

**Step 6:** Calculate the present value of each coupon:

PV(Cₙ) = Cₙ e^(-rtₙ)

**Step 7:** Add all coupon present values:

Total coupon PV = PV(C₁) + PV(C₂) + ... + PV(Cₙ)

**Step 8:** Calculate the present value of the face value:

PV(F) = F e^(-rT)

**Step 9:** Add the two components:

B₀ = Total coupon PV + PV(F)

**Step 10:** Report the present price of the coupon bond.

---

## 5. Complete Worked Examples

### Example 1: Zero-Coupon Bond

A bond pays 5,000 ETB after 4 years. If the continuously compounded annual interest rate is 8%, calculate its present price.

**Given:**

* F = 5,000 ETB
* r = 0.08
* T = 4

**Solution:**

B₀ = F e^(-rT)

B₀ = 5,000 e^(-0.08 × 4)

B₀ = 5,000 e^(-0.32)

B₀ ≈ 5,000 × 0.72615

**Answer:**

B₀ ≈ 3,630.75 ETB

### Example 2: Coupon Bond

A coupon bond has the following characteristics:

* Face value = 1,000 ETB
* Annual interest rate = 5% (continuously compounded)
* Maturity = 3 years
* Annual coupon payments = 50 ETB
* Coupon payments occur at the end of years 1, 2, and 3.

Calculate the present price of the bond.

**Step 1: Identify the given values.**

F = 1,000

r = 0.05

T = 3

C₁ = C₂ = C₃ = 50

t₁ = 1, t₂ = 2, t₃ = 3

**Step 2: Write the formula.**

B₀ = Σ(n=1 to 3) Cₙ e^(-rtₙ) + F e^(-rT)

**Step 3: Substitute the values.**

B₀ = 50e^(-0.05×1) + 50e^(-0.05×2) + 50e^(-0.05×3) + 1,000e^(-0.05×3)

**Step 4: Calculate each present value.**

First coupon:

PV(C₁) = 50e^(-0.05) ≈ 47.56

Second coupon:

PV(C₂) = 50e^(-0.10) ≈ 45.24

Third coupon:

PV(C₃) = 50e^(-0.15) ≈ 43.04

Face value:

PV(F) = 1,000e^(-0.15) ≈ 860.71

**Step 5: Add all present values.**

B₀ = 47.56 + 45.24 + 43.04 + 860.71

**Answer:**

B₀ ≈ 996.55 ETB

The present price of the coupon bond is approximately 996.55 ETB.

---

## 6. Pseudocode

### Algorithm 1: Zero-Coupon Bond Price

```text
START

INPUT F, r, T

B0 = F * exp(-r * T)

DISPLAY B0

END
```

### Algorithm 2: Value at a Future Time

```text
START

INPUT F, r, T, t

IF t < 0 OR t > T:
    DISPLAY "Invalid time"
ELSE:
    Bt = F * exp(-r * (T - t))
    DISPLAY Bt

END
```

### Algorithm 3: Coupon Bond Price

```text
START

INPUT F, r, T, N

total_coupon_value = 0

FOR n = 1 TO N:

    INPUT Cn, tn

    coupon_value = Cn * exp(-r * tn)

    total_coupon_value =
        total_coupon_value + coupon_value

END FOR

face_value_present = F * exp(-r * T)

B0 = total_coupon_value + face_value_present

DISPLAY B0

END
```

---

## 7. Formula Selection Guide

| Problem asks you to find              | Formula                      |
| ------------------------------------- | ---------------------------- |
| Present price of a zero-coupon bond   | B₀ = F e^(-rT)               |
| Value at time t of a zero-coupon bond | Bₜ = F e^(-r(T-t))           |
| Value at time t using initial price   | Bₜ = B₀ e^(rt)               |
| Present price of a coupon bond        | B₀ = Σ Cₙe^(-rtₙ) + Fe^(-rT) |

### How to Choose

* If the bond pays only one amount at maturity, use the zero-coupon bond formula.
* If the bond pays coupons during its lifetime, use the coupon bond formula.
* If the question asks for the bond's value before maturity, use the future-time valuation formula.

---

## 8. Common Mistakes and Checks

1. **Forgetting the negative sign in the exponent**

   Correct: B₀ = F e^(-rT)

2. **Using a percentage instead of a decimal**

   Correct: 6% = 0.06.

3. **Confusing current time and maturity time**

   In Bₜ = F e^(-r(T-t)), T is maturity time and t is the time at which the value is required.

4. **Forgetting one or more coupon payments**

   Every coupon payment must be included in the summation.

5. **Forgetting the face value in a coupon bond**

   The face value is also paid at maturity, so its present value must be included.

6. **Using the wrong payment time**

   Each coupon must be discounted using its own payment time tₙ.

7. **Mixing compounding conventions**

   The formulas in this lesson use continuous compounding. Do not replace them with discrete-compounding formulas unless the problem specifies a different convention.

---

## 9. Summary

The bond calculations in this lesson are based on the present value of future payments.

**Zero-coupon bond:**

B₀ = F e^(-rT)

**Value at a future time:**

Bₜ = F e^(-r(T-t)) = B₀ e^(rt)

**Coupon bond:**

B₀ = Σ(n=1 to N) Cₙ e^(-rtₙ) + F e^(-rT)

The most important idea is:

**A bond's present price is the sum of the present values of all payments that the bondholder will receive in the future.**

<!-- PAGE BREAK -->

## Practice Questions

### Question 1

A zero-coupon bond has a face value of 10,000 ETB and matures after 5 years. If the continuously compounded annual interest rate is 7%, find its present price.

### Question 2

A zero-coupon bond has a face value of 2,000 ETB and matures after 4 years. If the continuously compounded annual interest rate is 5%, find its value after 2 years.

### Question 3

A coupon bond has a face value of 5,000 ETB, pays annual coupons of 400 ETB for 3 years, and has a continuously compounded annual interest rate of 6%.

Calculate its present price, assuming coupons are paid at the end of each year.

### Question 4

Explain the difference between a zero-coupon bond and a coupon bond in terms of their future payments.

### Question 5

Why must the face value be included separately when calculating the present price of a coupon bond?

---

## Final Learning Check

You should now be able to:

* Identify the important components of a bond.
* Calculate the present price of a zero-coupon bond.
* Calculate the value of a zero-coupon bond at a future time.
* Calculate the present price of a coupon bond.
* Apply continuous discounting to individual future payments.
* Select the correct formula for a bond valuation problem.
