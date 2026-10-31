# Internal Rate of Return (IRR) — Algorithms and Step-by-Step Procedures

## Table of Contents

1. [General Procedure](#1-general-procedure)
2. [Setting Up the IRR Equation](#2-setting-up-the-irr-equation)
3. [Finding the IRR](#3-finding-the-irr)
4. [Determining Whether IRR Is Positive, Zero, or Negative](#4-determining-whether-irr-is-positive-zero-or-negative)
5. [Understanding NPV at the IRR](#5-understanding-npv-at-the-irr)
6. [Existence and Uniqueness of IRR](#6-existence-and-uniqueness-of-irr)
7. [Complete Worked Example](#7-complete-worked-example)
8. [Pseudocode](#8-pseudocode)
9. [Formula Selection Guide](#9-formula-selection-guide)
10. [Common Mistakes and Checks](#10-common-mistakes-and-checks)
11. [Summary](#11-summary)

---

## 1. General Procedure

The Internal Rate of Return (IRR) is a measure used to evaluate an investment involving an initial payment and a sequence of future returns.

The IRR is the periodic interest rate that makes the present value of all future returns equal to the initial investment.

### Important Symbols

| Symbol | Meaning                                |
| ------ | -------------------------------------- |
| P      | Initial investment                     |
| Aₙ     | Return received at the end of period n |
| N      | Total number of periods                |
| i      | Internal rate of return                |
| R(i)   | Present value of all future returns    |
| NPV    | Net present value                      |

### General Steps

1. Identify the initial investment P.
2. Identify all future returns A₁, A₂, ..., Aₙ.
3. Identify the total number of periods N.
4. Write the present-value equation.
5. Set the present value of future returns equal to the initial investment.
6. Determine the interest rate i that satisfies the equation.
7. Interpret the resulting IRR.

---

## 2. Setting Up the IRR Equation

### Purpose

Construct the mathematical equation used to determine the internal rate of return.

### Formula

P = Σ(n=1 to N) Aₙ(1+i)^(-n)

Equivalently:

P = A₁/(1+i) + A₂/(1+i)² + ... + Aₙ/(1+i)ᴺ

Where:

* P = initial investment
* Aₙ = return at the end of period n
* i = internal rate of return
* N = total number of periods

### Step-by-Step Algorithm

**Step 1:** Identify the initial investment P.

**Step 2:** List all future returns in chronological order.

**Step 3:** Number the periods from 1 to N.

**Step 4:** Discount each future return using its corresponding period.

**Step 5:** Add all discounted returns.

**Step 6:** Set their sum equal to the initial investment.

**Step 7:** The resulting equation is the IRR equation.

### Worked Example

An investment requires an initial payment of 100 ETB and produces the following returns:

| Period | Return |
| ------ | -----: |
| 1      | 18 ETB |
| 2      | 37 ETB |
| 3      | 39 ETB |
| 4      | 27 ETB |

Find the equation used to determine its IRR.

**Step 1: Identify the values.**

P = 100

A₁ = 18

A₂ = 37

A₃ = 39

A₄ = 27

N = 4

**Step 2: Write the general formula.**

P = Σ(n=1 to N) Aₙ(1+i)^(-n)

**Step 3: Substitute the values.**

100 = 18/(1+i) + 37/(1+i)² + 39/(1+i)³ + 27/(1+i)⁴

**Final Equation:**

100 = 18/(1+i) + 37/(1+i)² + 39/(1+i)³ + 27/(1+i)⁴

The value of i that satisfies this equation is the investment's IRR.

---

## 3. Finding the IRR

### Purpose

Determine the periodic interest rate that makes the present value of future returns equal to the initial investment.

### Step-by-Step Algorithm

**Step 1:** Construct the IRR equation:

P = Σ(n=1 to N) Aₙ(1+i)^(-n)

**Step 2:** Identify the unknown interest rate i.

**Step 3:** Determine an appropriate numerical method for solving the equation.

Common methods include:

* Trial-and-error method
* Bisection method
* Newton's method

**Step 4:** Obtain the value of i that satisfies the equation.

**Step 5:** Express the result as a percentage:

IRR (%) = i × 100%

**Step 6:** Verify that substituting the calculated rate makes the present value approximately equal to the initial investment.

### Important Note

The IRR equation may be difficult to solve algebraically, especially when there are many periods.

Therefore, numerical methods are commonly used.

The calculation procedures for these numerical methods are outside the scope of this lesson.

---

## 4. Determining Whether IRR Is Positive, Zero, or Negative

### Purpose

Determine the sign of the IRR without calculating its exact value.

### Important Function

Define:

R(i) = Σ(n=1 to N) Aₙ(1+i)^(-n)

The IRR satisfies:

R(i) = P

At i = 0:

R(0) = A₁ + A₂ + ... + Aₙ

Therefore, compare the total future returns with the initial investment.

### Decision Algorithm

**Step 1:** Identify the initial investment P.

**Step 2:** Calculate the total future returns:

S = A₁ + A₂ + ... + Aₙ

**Step 3:** Compare S with P.

There are three possibilities:

| Condition | IRR      |
| --------- | -------- |
| S > P     | Positive |
| S = P     | Zero     |
| S < P     | Negative |

### Worked Example 1: Positive IRR

An investment requires 1,000 ETB and produces total future returns of 1,200 ETB.

Given:

P = 1,000

S = 1,200

Since:

S > P

Therefore:

**IRR > 0**

### Worked Example 2: Zero IRR

An investment requires 1,000 ETB and produces total future returns of 1,000 ETB.

Given:

P = 1,000

S = 1,000

Since:

S = P

Therefore:

**IRR = 0**

### Worked Example 3: Negative IRR

An investment requires 1,000 ETB and produces total future returns of 800 ETB.

Given:

P = 1,000

S = 800

Since:

S < P

Therefore:

**IRR < 0**

### Important Interpretation

This comparison determines only the sign of the IRR. It does not give the exact numerical value.

---

## 5. Understanding NPV at the IRR

### Purpose

Understand the relationship between Net Present Value (NPV) and Internal Rate of Return.

### Formula

NPV(i) = R(i) - P

Where:

R(i) = Σ(n=1 to N) Aₙ(1+i)^(-n)

Therefore:

NPV(i) = Σ(n=1 to N) Aₙ(1+i)^(-n) - P

At the IRR:

R(i) = P

Consequently:

NPV(i) = P - P

**NPV(i) = 0**

### Step-by-Step Algorithm

**Step 1:** Identify the initial investment P.

**Step 2:** Identify all future returns Aₙ.

**Step 3:** Calculate the present value of future returns using a given discount rate.

**Step 4:** Subtract the initial investment:

NPV = Present value of future returns - P

**Step 5:** If the discount rate is the IRR, the NPV must equal zero.

### Interpretation

* NPV > 0: Present value of returns exceeds the initial investment.
* NPV = 0: Present value of returns equals the initial investment.
* NPV < 0: Present value of returns is below the initial investment.

At the IRR, the investment is at its break-even point in present-value terms.

---

## 6. Existence and Uniqueness of IRR

### Purpose

Understand when an IRR exists and whether it is unique.

According to the lecture, consider:

R(i) = Σ(n=1 to N) Aₙ(1+i)^(-n)

Assume:

* P > 0
* Aₙ ≥ 0
* At least one future return is positive
* i > -1

The following properties hold:

1. R(i) is continuous on (-1, ∞).
2. As i approaches infinity, R(i) approaches zero.
3. As i approaches -1 from the right, R(i) approaches infinity.
4. R(i) is strictly decreasing.

### Step-by-Step Reasoning

**Step 1: Check the investment and returns.**

Confirm that P is positive, all returns are nonnegative, and at least one return is positive.

**Step 2: Consider the behavior of R(i).**

As i approaches infinity:

R(i) → 0

As i approaches -1 from the right:

R(i) → ∞

**Step 3: Apply continuity.**

Because R(i) is continuous and moves from infinity to zero, it must take the value P for some i > -1.

Therefore, at least one IRR exists.

**Step 4: Apply strict decrease.**

Since R(i) is strictly decreasing, it can equal P at only one value of i.

Therefore, the IRR is unique.

### Final Conclusion

For P > 0, nonnegative future returns, and at least one positive future return, there exists exactly one IRR satisfying:

P = Σ(n=1 to N) Aₙ(1+i)^(-n)

---

## 7. Complete Worked Example

### Problem

An investor pays 100 ETB today and receives the following future payments:

| Year | Return |
| ---- | -----: |
| 1    | 18 ETB |
| 2    | 37 ETB |
| 3    | 39 ETB |
| 4    | 27 ETB |

Determine:

1. The IRR equation.
2. Whether the IRR is positive, zero, or negative.
3. The approximate IRR.
4. The NPV at the IRR.

### Solution

**Step 1: Identify the given values.**

P = 100

A₁ = 18

A₂ = 37

A₃ = 39

A₄ = 27

N = 4

**Step 2: Construct the IRR equation.**

100 = 18/(1+i) + 37/(1+i)² + 39/(1+i)³ + 27/(1+i)⁴

**Step 3: Determine the sign of IRR.**

Calculate the total future returns:

S = 18 + 37 + 39 + 27

S = 121

Compare:

121 > 100

Therefore:

**IRR > 0**

**Step 4: Determine the approximate IRR.**

Solving the IRR equation numerically gives approximately:

i ≈ 0.0766

Convert to percentage:

IRR ≈ 0.0766 × 100%

**IRR ≈ 7.66%**

**Step 5: Determine NPV at the IRR.**

At the IRR:

NPV = R(i) - P

Since:

R(i) = P = 100

Therefore:

NPV = 100 - 100

**NPV = 0**

### Final Answers

| Required quantity    |                                             Result |
| -------------------- | -------------------------------------------------: |
| IRR equation         | 100 = 18/(1+i) + 37/(1+i)² + 39/(1+i)³ + 27/(1+i)⁴ |
| Total future returns |                                            121 ETB |
| Sign of IRR          |                                           Positive |
| Approximate IRR      |                                              7.66% |
| NPV at IRR           |                                              0 ETB |

---

## 8. Pseudocode

### Algorithm 1: Construct the IRR Equation

```text
START

INPUT P
INPUT N

FOR n = 1 TO N:
    INPUT A[n]
END FOR

DISPLAY:
    P = A[1]/(1+i)^1
      + A[2]/(1+i)^2
      + ...
      + A[N]/(1+i)^N

END
```

### Algorithm 2: Determine the Sign of IRR

```text
START

INPUT P
INPUT N

S = 0

FOR n = 1 TO N:
    INPUT A[n]
    S = S + A[n]
END FOR

IF S > P:
    DISPLAY "IRR is positive"

ELSE IF S == P:
    DISPLAY "IRR is zero"

ELSE:
    DISPLAY "IRR is negative"

END IF

END
```

### Algorithm 3: Calculate NPV

```text
START

INPUT P
INPUT N
INPUT i

R = 0

FOR n = 1 TO N:
    INPUT A[n]

    R = R + A[n]/(1+i)^n
END FOR

NPV = R - P

DISPLAY NPV

END
```

---

## 9. Formula Selection Guide

| Problem asks you to find | Formula or procedure                            |
| ------------------------ | ----------------------------------------------- |
| IRR equation             | P = Σ Aₙ(1+i)^(-n)                              |
| Exact numerical IRR      | Solve the IRR equation using a numerical method |
| Sign of IRR              | Compare ΣAₙ with P                              |
| Present value of returns | R(i) = Σ Aₙ(1+i)^(-n)                           |
| Net present value        | NPV(i) = R(i) - P                               |
| NPV at IRR               | NPV(i) = 0                                      |
| Existence and uniqueness | Use continuity, limits, and strict decrease     |

---

## 10. Common Mistakes and Checks

1. **Forgetting the initial investment**

   The initial investment P must be included separately from future returns.

2. **Using the wrong period**

   Each return must be discounted according to the period in which it is received.

3. **Confusing IRR with total returns**

   IRR is an interest rate, not the total amount of money received.

4. **Confusing IRR with NPV**

   IRR is the rate that makes NPV equal to zero.

5. **Misinterpreting the sign of IRR**

   * Total future returns greater than P means positive IRR.
   * Total future returns equal to P means zero IRR.
   * Total future returns less than P means negative IRR.

6. **Assuming every investment has a unique IRR**

   The uniqueness result in this lesson requires nonnegative future returns with at least one positive return. Cash flows with changing signs may have multiple IRRs or no IRR.

7. **Forgetting the periodic nature of IRR**

   The calculated IRR is expressed per period. If the periods are years, it is an annual rate; if the periods are months, it is a monthly rate.

---

## 11. Summary

The Internal Rate of Return measures the periodic rate of return of an investment.

**Main IRR equation:**

P = Σ(n=1 to N) Aₙ(1+i)^(-n)

**Present value of future returns:**

R(i) = Σ(n=1 to N) Aₙ(1+i)^(-n)

**Net present value:**

NPV(i) = R(i) - P

**At the IRR:**

NPV(i) = 0

**Sign of IRR:**

* ΣAₙ > P → Positive IRR
* ΣAₙ = P → Zero IRR
* ΣAₙ < P → Negative IRR

**Existence and uniqueness:**

For a positive initial investment and nonnegative future returns, with at least one positive return, exactly one IRR exists.

The most important idea is:

**IRR is the interest rate that makes the present value of all future returns equal to the initial investment.**

<!-- PAGE BREAK -->

## Practice Questions

### Question 1

An investment requires an initial payment of 5,000 ETB and produces the following returns:

* Year 1: 3,000 ETB
* Year 2: 3,000 ETB

Answer the following:

1. Construct the IRR equation.
2. Determine whether the IRR is positive, zero, or negative.
3. Find the approximate IRR.
4. What is the NPV at the IRR?

### Question 2

An investment requires 2,000 ETB and produces future returns of 500, 600, 700, and 800 ETB over four years.

Determine the sign of the IRR without calculating its exact value.

### Question 3

An investment requires 4,000 ETB and produces total future returns of 4,000 ETB.

What is its IRR?

### Question 4

Explain why the IRR is unique under the assumptions of the existence and uniqueness theorem.

### Question 5

An investment has an initial cost of 10,000 ETB and future returns of 2,000, 3,000, and 4,000 ETB.

Determine whether its IRR is positive, zero, or negative.

---

## Final Learning Check

You should now be able to:

* Construct an IRR equation from investment information.
* Understand the meaning of the internal rate of return.
* Identify the numerical methods used to find IRR.
* Determine whether IRR is positive, zero, or negative.
* Calculate and interpret NPV.
* Explain why NPV equals zero at IRR.
* Understand the existence and uniqueness of IRR.
* Recognize situations where the uniqueness result may not apply.
