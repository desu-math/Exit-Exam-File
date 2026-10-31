# 📘 Internal Rate of Return (IRR) — Financial Mathematics (Math4313)

**Course:** Financial Mathematics (Math4313)
**Topic:** Internal Rate of Return (IRR)
**Department:** Applied Mathematics
**Institution:** Adama Science and Technology University (ASTU)
**Primary Reference:** Lecture 1 — Tamirat T. Dufera (PhD)
**Supplementary Reference:** *An Introduction to Financial Mathematics: Option Valuation* (CRC Press, 2019).

---

## 📑 Table of Contents

1. [Learning Objectives](#1-learning-objectives)
2. [Introduction and Motivation](#2-introduction-and-motivation)
3. [What Is Internal Rate of Return?](#3-what-is-internal-rate-of-return)
4. [Mathematical Definition of IRR](#4-mathematical-definition-of-irr)
5. [Understanding the IRR Equation](#5-understanding-the-irr-equation)
6. [Worked Example: Calculating IRR](#6-worked-example-calculating-irr)
7. [Existence and Uniqueness of IRR](#7-existence-and-uniqueness-of-irr)
8. [Defining the Present Value Function R(i)](#8-defining-the-present-value-function-ri)
9. [Proof of Continuity](#9-proof-of-continuity)
10. [Limits of R(i)](#10-limits-of-ri)
11. [Existence of IRR: Intermediate Value Theorem](#11-existence-of-irr-intermediate-value-theorem)
12. [Uniqueness of IRR: Strict Monotonicity](#12-uniqueness-of-irr-strict-monotonicity)
13. [The Existence and Uniqueness Theorem](#13-the-existence-and-uniqueness-theorem)
14. [Remark: When Is IRR Positive, Zero, or Negative?](#14-remark-when-is-irr-positive-zero-or-negative)
15. [Numerical Methods for Finding IRR](#15-numerical-methods-for-finding-irr)
16. [Relationship Between IRR and NPV](#16-relationship-between-irr-and-npv)
17. [Practical Applications of IRR](#17-practical-applications-of-irr)
18. [Common Mistakes](#18-common-mistakes)
19. [Formula Summary](#19-formula-summary)
20. [How to Approach IRR Problems](#20-how-to-approach-irr-problems)
21. [Practice Questions](#21-practice-questions)
22. [Solutions to Practice Questions](#22-solutions-to-practice-questions)
23. [Final Summary](#23-final-summary)

---

# 1. Learning Objectives

After studying this topic, you should be able to:

* Define internal rate of return and explain its financial importance.
* Understand the relationship between initial investment and future returns.
* Formulate the mathematical IRR equation.
* Interpret the present value function R(i).
* Explain why the IRR must satisfy i > −1.
* Prove that the IRR exists using continuity and the Intermediate Value Theorem.
* Prove that the IRR is unique using strict monotonicity.
* Determine whether an investment has a positive, zero, or negative IRR without calculating its exact value.
* Understand the relationship between IRR and net present value (NPV).
* Recognize numerical methods used to calculate IRR.

---

# 2. Introduction and Motivation

Investors and businesses often need to evaluate investment opportunities before committing their money.

For example:

* A company may invest money in a new factory.
* An entrepreneur may invest money in a business.
* A government may finance a development project.
* An individual may invest money in an income-generating project.

In each situation, an important question arises:

**What rate of return does the investment generate?**

Consider an investment of 10,000 ETB today that produces the following future payments:

| Period | Future return |
| ------ | ------------: |
| Year 1 |     4,000 ETB |
| Year 2 |     5,000 ETB |
| Year 3 |     6,000 ETB |

The investor wants to determine the interest rate that makes the present value of these future returns equal to the initial investment.

This is the central idea of internal rate of return.

IRR brings together several concepts from previous topics:

* Compound interest.
* Present value and discounting.
* Future cash flows.
* Investment evaluation.

---

# 3. What Is Internal Rate of Return?

According to the lecture note:

> Internal rate of return is a measure used to evaluate a sequence of financial events.

It is also:

> Used to rank projects that involve future cash flows.

In simple terms:

**Internal Rate of Return (IRR) is the periodic interest rate that makes the present value of all future investment returns equal to the initial investment.**

### Understanding the definition

Suppose you invest 10,000 ETB today and receive payments in the future.

There are two important financial quantities:

1. Initial investment: The amount of money paid today.
2. Present value of future returns: The value today of all expected future payments.

IRR is the rate that makes these two quantities equal.

### Important idea

IRR accounts for both:

* The amount of money received.
* The time at which each payment is received.

Therefore, it is more informative than simply calculating total profit.

---

# 4. Mathematical Definition of IRR

Your instructor considers an investment with an initial payment P > 0 that produces future returns Aₙ ≥ 0 at the end of periods:

n = 1, 2, ..., N.

The notation is:

| Symbol | Meaning                                |
| ------ | -------------------------------------- |
| P      | Initial investment                     |
| Aₙ     | Amount received at the end of period n |
| n      | Period number                          |
| N      | Total number of periods                |
| i      | Internal rate of return                |

The IRR is defined as the periodic interest rate i for which the present value of the sequence of returns equals the initial investment.

Mathematically:

**P = Σ(n=1 to N) Aₙ(1+i)^(-n)**

Equivalently:

**P = A₁/(1+i) + A₂/(1+i)² + ... + Aₙ/(1+i)ⁿ**

This is the fundamental IRR equation.

---

# 5. Understanding the IRR Equation

Let's understand where this equation comes from.

Recall the compound interest formula:

Aₙ = P(1+i)ⁿ

Where:

* P is the present value.
* Aₙ is the future value.
* i is the periodic interest rate.
* n is the number of periods.

Rearranging:

P = Aₙ/(1+i)ⁿ

Therefore, the present value of a future payment Aₙ received after n periods is:

**PV(Aₙ) = Aₙ/(1+i)ⁿ**

Now consider an investment that produces multiple future payments:

A₁, A₂, ..., Aₙ.

Their present values are:

PV(A₁) = A₁/(1+i)

PV(A₂) = A₂/(1+i)²

PV(A₃) = A₃/(1+i)³

And so on.

The total present value is the sum of all individual present values:

PV = A₁/(1+i) + A₂/(1+i)² + ... + Aₙ/(1+i)ⁿ

By the definition of IRR, this total present value must equal the initial investment P.

Therefore:

**P = Σ(n=1 to N) Aₙ(1+i)^(-n)**

### Why does each payment have a different power?

Because each payment is received at a different time.

* A₁ is discounted for one period.
* A₂ is discounted for two periods.
* A₃ is discounted for three periods.
* Aₙ is discounted for n periods.

The timing of payments is therefore an essential part of IRR.

---

# 6. Worked Example: Calculating IRR

Suppose an investment requires 100 ETB today and produces the following returns:

| Period | Return |
| ------ | -----: |
| Year 1 | 18 ETB |
| Year 2 | 37 ETB |
| Year 3 | 39 ETB |
| Year 4 | 27 ETB |

Find the internal rate of return.

### Step 1: Identify the given information.

P = 100

A₁ = 18

A₂ = 37

A₃ = 39

A₄ = 27

N = 4

### Step 2: Write the IRR equation.

P = A₁/(1+i) + A₂/(1+i)² + A₃/(1+i)³ + A₄/(1+i)⁴

### Step 3: Substitute the values.

100 = 18/(1+i) + 37/(1+i)² + 39/(1+i)³ + 27/(1+i)⁴

### Step 4: Determine the IRR.

The equation is nonlinear, so its solution is generally obtained numerically.

For this investment:

**IRR ≈ 7.66%**

### Interpretation

The investment has an internal rate of return of approximately 7.66% per period.

At this rate, the present value of all future returns equals the initial investment of 100 ETB.

---

# 7. Existence and Uniqueness of IRR

One of the most important mathematical results in this topic is that the IRR equation has a unique solution under the assumptions of the lecture.

Your instructor states:

**The IRR equation has a unique solution i > −1.**

To understand this result, we need to prove two things:

1. At least one solution exists.
2. There cannot be more than one solution.

These are called existence and uniqueness.

The proof uses three important mathematical concepts:

* Continuity.
* The Intermediate Value Theorem.
* Strict monotonicity.

---

# 8. Defining the Present Value Function R(i)

Your instructor introduces the function:

**R(i) = Σ(n=1 to N) Aₙ(1+i)^(-n)**

Equivalently:

R(i) = A₁/(1+i) + A₂/(1+i)² + ... + Aₙ/(1+i)ⁿ

This function represents the total present value of all future investment returns at a discount rate i.

The IRR equation becomes:

**R(i) = P**

Our objective is to prove that this equation has exactly one solution.

### Why must i > −1?

Look at the denominator:

(1+i)ⁿ

For the expression to be defined as a real-valued financial discount factor, we require:

1+i > 0

Therefore:

**i > −1**

Our solution must belong to the interval:

**(−1, ∞)**

---

# 9. Proof of Continuity

Your instructor states:

> R is continuous on (−1, ∞).

Let's prove this.

We have:

R(i) = A₁/(1+i) + A₂/(1+i)² + ... + Aₙ/(1+i)ⁿ

Each term is a continuous function for i > −1 because its denominator is not zero.

A finite sum of continuous functions is also continuous.

Therefore:

**R(i) is continuous on (−1, ∞).**

### Why is continuity important?

Continuity means that the function does not jump over intermediate values.

This property allows us to use the Intermediate Value Theorem to establish the existence of an IRR.

---

# 10. Limits of R(i)

Your instructor gives two important limits:

**lim R(i) = 0 as i → ∞**

and

**lim R(i) = ∞ as i → −1⁺**

Let's understand both.

## 10.1 First Limit: As i Approaches Infinity

Recall:

R(i) = A₁/(1+i) + A₂/(1+i)² + ... + Aₙ/(1+i)ⁿ

As i becomes very large:

1+i becomes very large.

Therefore:

A₁/(1+i) → 0

A₂/(1+i)² → 0

A₃/(1+i)³ → 0

The same happens to every term.

Since R(i) is a finite sum:

**lim R(i) = 0 as i → ∞.**

### Interpretation

When the discount rate becomes extremely large, future payments become almost worthless in today's terms.

Therefore, their total present value approaches zero.

## 10.2 Second Limit: As i Approaches −1 From the Right

As i approaches −1 from the right:

1+i → 0⁺

Consider a positive future payment:

A₁/(1+i)

As the denominator approaches zero from the positive side:

A₁/(1+i) → ∞

Since all future returns are nonnegative, the terms cannot cancel one another.

Provided at least one future return is positive:

**lim R(i) = ∞ as i → −1⁺.**

### Interpretation

When the discount rate approaches −100%, the discount factor approaches zero.

Dividing a positive future payment by a number approaching zero from the positive side produces an extremely large present value.

---

# 11. Existence of IRR: Intermediate Value Theorem

We have established that:

1. R(i) is continuous on (−1, ∞).
2. R(i) → ∞ as i → −1⁺.
3. R(i) → 0 as i → ∞.

Also, the initial investment satisfies:

P > 0.

Now consider the equation:

R(i) = P

Near i = −1, R(i) is greater than P.

For sufficiently large i, R(i) is smaller than P.

Because R(i) is continuous, it must take the value P somewhere between these two regions.

By the **Intermediate Value Theorem**, there exists at least one value i > −1 satisfying:

**R(i) = P**

Therefore:

**The IRR exists.**

### Important conclusion

Continuity and the Intermediate Value Theorem establish the existence of at least one solution.

However, this does not yet prove that the solution is unique.

---

# 12. Uniqueness of IRR: Strict Monotonicity

Your instructor states:

> Since R is strictly decreasing, the solution is unique.

Let's prove that R(i) is strictly decreasing.

Recall:

R(i) = Σ(n=1 to N) Aₙ(1+i)^(-n)

Differentiate with respect to i.

Using the power rule:

d/di [(1+i)^(-n)] = −n(1+i)^(-n−1)

Therefore:

R'(i) = Σ(n=1 to N) [−nAₙ(1+i)^(-n−1)]

Equivalently:

**R'(i) = −Σ(n=1 to N) nAₙ/(1+i)^(n+1)**

Now examine the expression.

We know:

* n > 0.
* Aₙ ≥ 0.
* 1+i > 0.
* Therefore, every denominator is positive.

Each term in the summation is nonpositive.

Since at least one future return is positive, at least one term is strictly negative.

Thus:

**R'(i) < 0**

Therefore, R(i) is strictly decreasing on (−1, ∞).

### What does strictly decreasing mean?

It means that when i increases, R(i) decreases.

For example:

| Discount rate | Present value |
| ------------- | ------------- |
| 5%            | Higher        |
| 10%           | Lower         |
| 15%           | Even lower    |
| 20%           | Still lower   |

The exact values depend on the future payments, but the decreasing relationship follows from the mathematical properties of R(i).

### Why does this prove uniqueness?

Suppose two different interest rates, i₁ and i₂, both satisfy:

R(i₁) = P

R(i₂) = P

If i₁ and i₂ are different, one must be larger than the other.

But because R is strictly decreasing, different inputs must produce different outputs.

Therefore, both cannot produce the same value P.

This is a contradiction.

Hence:

**The IRR is unique.**

---

# 13. The Existence and Uniqueness Theorem

We can now combine the two parts of the proof.

### Existence

Because R(i) is continuous and:

* R(i) → ∞ as i → −1⁺.
* R(i) → 0 as i → ∞.

The Intermediate Value Theorem guarantees at least one solution to:

R(i) = P.

### Uniqueness

Because:

R'(i) < 0

R(i) is strictly decreasing.

Therefore, the equation cannot have two different solutions.

### Final Theorem

For an initial investment P > 0 and nonnegative future returns Aₙ ≥ 0, with at least one future return strictly positive, the IRR equation:

**P = Σ(n=1 to N) Aₙ(1+i)^(-n)**

has exactly one solution satisfying:

**i > −1.**

This is the central mathematical theorem of the IRR topic.

---

# 14. Remark: When Is IRR Positive, Zero, or Negative?

Your instructor's Remark 1 establishes a useful relationship between the initial investment and the total undiscounted future returns.

We know:

R(i) = Σ Aₙ(1+i)^(-n)

At i = 0:

R(0) = Σ Aₙ(1+0)^(-n)

Since:

(1+0)^(-n) = 1

We obtain:

**R(0) = Σ(n=1 to N) Aₙ**

At the IRR:

R(i) = P

Because R is strictly decreasing:

i > 0 if and only if R(i) < R(0).

Substituting:

P < Σ Aₙ

Therefore:

**i > 0 if and only if P < Σ Aₙ.**

Similarly:

| Condition | IRR      |
| --------- | -------- |
| P < Σ Aₙ  | Positive |
| P = Σ Aₙ  | Zero     |
| P > Σ Aₙ  | Negative |

### Worked Example

Suppose an investment requires:

P = 10,000 ETB

The future returns are:

| Period |    Return |
| ------ | --------: |
| Year 1 | 4,000 ETB |
| Year 2 | 3,000 ETB |
| Year 3 | 5,000 ETB |

Total future payments:

Σ Aₙ = 4,000 + 3,000 + 5,000

Σ Aₙ = 12,000 ETB

Compare:

10,000 < 12,000

Therefore:

**IRR > 0**

We can determine that the IRR is positive without calculating its exact value.

### Important Correction to the Lecture Slide

The final sentence of the lecture's Remark 1 appears to contain a reversed inequality.

The correct mathematical conclusion is:

* For a positive IRR, the sum of future payments is greater than the initial investment.
* For a zero IRR, the sum of future payments equals the initial investment.
* For a negative IRR, the sum of future payments is less than the initial investment.

This follows directly from the preceding mathematical statement and is also consistent with the supplementary reference.

---

# 15. Numerical Methods for Finding IRR

The IRR equation is generally nonlinear, so its exact solution cannot always be obtained easily using ordinary algebra.

There are several numerical methods used to approximate IRR, including:

* Trial and error.
* Bisection method (interval-halving method).
* Newton's method.
* Spreadsheet and financial software functions.

For example, the supplementary reference gives an investment of 100 with future returns of 18, 37, 39, and 27. Its IRR is approximately:

**IRR = 7.66%.**

The detailed procedures for these numerical methods are outside the scope of this note.

---

# 16. Relationship Between IRR and NPV

This is a useful supplementary concept that connects IRR with another important financial measure.

NPV stands for **Net Present Value**.

It measures the difference between the present value of future returns and the initial investment.

For a discount rate r:

**NPV(r) = R(r) − P**

Or:

NPV(r) = Σ Aₙ/(1+r)ⁿ − P

At the internal rate of return:

R(i) = P

Therefore:

NPV(i) = P − P

**NPV(i) = 0**

This gives us an important relationship:

**IRR is the discount rate at which NPV equals zero.**

### Investment Decision

Suppose an investor requires a minimum return of 10%.

| Condition             | General interpretation                |
| --------------------- | ------------------------------------- |
| IRR > Required return | Investment may be attractive          |
| IRR = Required return | Investment is at the break-even point |
| IRR < Required return | Investment may be unattractive        |

This is a common decision rule for conventional investments.

However, IRR should not always be used alone. For projects with unusual cash-flow patterns or mutually exclusive alternatives, NPV can provide a more reliable comparison.

---

# 17. Practical Applications of IRR

IRR is widely used in financial and economic decision-making.

### 1. Business Investment

Companies use IRR to evaluate investments in new equipment, factories, and business expansion.

### 2. Project Evaluation

Governments and development institutions use investment-return measures to compare infrastructure and development projects.

### 3. Investment Comparison

Investors use IRR to compare opportunities with different future payment patterns.

### 4. Financial Planning

IRR helps evaluate long-term investments and expected returns.

### 5. Real Estate Investment

Investors use IRR to evaluate property purchases, rental income, and future resale values.

---

# 18. Common Mistakes

1. Confusing IRR with ordinary profit.
2. Adding future payments without discounting them.
3. Forgetting that each payment must be discounted according to its period.
4. Treating the initial investment as a future return.
5. Forgetting the condition i > −1.
6. Confusing existence of a solution with uniqueness of a solution.
7. Forgetting that continuity and the Intermediate Value Theorem establish existence.
8. Forgetting that strict monotonicity establishes uniqueness.
9. Using the undiscounted sum of future payments to calculate the exact IRR.
10. Ignoring the timing of future cash flows when comparing investments.
11. Assuming the uniqueness theorem applies to every possible cash-flow pattern, including those with negative future payments.

---

# 19. Formula Summary

| Concept                    | Formula                    |
| -------------------------- | -------------------------- |
| IRR equation               | P = Σ Aₙ(1+i)^(-n)         |
| Present value function     | R(i) = Σ Aₙ(1+i)^(-n)      |
| First derivative           | R'(i) = −Σ nAₙ/(1+i)^(n+1) |
| IRR condition              | R(i) = P                   |
| NPV                        | NPV(r) = R(r) − P          |
| NPV at IRR                 | NPV(i) = 0                 |
| Present value at zero rate | R(0) = Σ Aₙ                |

### Important Mathematical Properties

Under the assumptions P > 0, Aₙ ≥ 0, and at least one positive future return:

1. R(i) is continuous on (−1, ∞).
2. R(i) → ∞ as i → −1⁺.
3. R(i) → 0 as i → ∞.
4. R'(i) < 0.
5. The IRR exists and is unique.
6. i > 0 if and only if P < Σ Aₙ.

---

# 20. How to Approach IRR Problems

When solving IRR problems, follow these steps:

**Step 1: Identify the initial investment.**

Write down P.

**Step 2: Identify all future returns.**

Write down A₁, A₂, ..., Aₙ and their corresponding periods.

**Step 3: Determine the total number of periods.**

Identify N.

**Step 4: Formulate the IRR equation.**

P = Σ Aₙ(1+i)^(-n)

**Step 5: Identify what the question asks.**

* If it asks for the IRR, determine the numerical solution.
* If it asks whether the IRR is positive, zero, or negative, compare P with Σ Aₙ.
* If it asks for existence and uniqueness, use continuity, limits, the Intermediate Value Theorem, and strict monotonicity.

**Step 6: Interpret the result.**

Explain what the calculated rate means for the investment.

---

# 21. Practice Questions

Try solving these questions before checking the solutions.

## Question 1: Basic IRR Equation

An investment requires 5,000 ETB today and returns:

* 3,000 ETB at the end of year 1.
* 3,000 ETB at the end of year 2.

Write the IRR equation.

## Question 2: Positive, Zero, or Negative IRR?

An investment requires 12,000 ETB and produces:

* Year 1: 4,000 ETB.
* Year 2: 5,000 ETB.
* Year 3: 6,000 ETB.

Without calculating the exact IRR, determine whether it is positive, zero, or negative.

Explain your answer.

## Question 3: Existence of IRR

Explain why the continuity of R(i), together with the limits:

* R(i) → ∞ as i → −1⁺.
* R(i) → 0 as i → ∞.

guarantees the existence of an IRR.

Name the mathematical theorem used.

## Question 4: Uniqueness of IRR

Given:

R(i) = Σ Aₙ(1+i)^(-n)

where Aₙ ≥ 0 and at least one Aₙ is positive.

Find R'(i) and explain why R(i) is strictly decreasing for i > −1.

## Question 5: Conceptual Understanding

Explain the difference between:

a) Existence of IRR.

b) Uniqueness of IRR.

## Question 6: Numerical Calculation

An investment of 100 ETB produces the following future returns:

| Period | Return |
| ------ | -----: |
| 1      | 18 ETB |
| 2      | 37 ETB |
| 3      | 39 ETB |
| 4      | 27 ETB |

Write the IRR equation and state the approximate IRR.

---

# 22. Solutions to Practice Questions

## Solution 1: Basic IRR Equation

Given:

P = 5,000

A₁ = 3,000

A₂ = 3,000

The IRR equation is:

P = A₁/(1+i) + A₂/(1+i)²

Substitute:

5,000 = 3,000/(1+i) + 3,000/(1+i)²

Solving gives:

i ≈ 0.0934

**IRR ≈ 9.34%.**

## Solution 2: Positive, Zero, or Negative IRR?

Initial investment:

P = 12,000

Total future payments:

Σ Aₙ = 4,000 + 5,000 + 6,000

Σ Aₙ = 15,000

Since:

12,000 < 15,000

The IRR is positive.

**Answer: IRR > 0.**

## Solution 3: Existence of IRR

We know that R(i) is continuous on (−1, ∞).

Also:

R(i) → ∞ as i → −1⁺.

R(i) → 0 as i → ∞.

Since P > 0, the function takes values both above and below P.

By the **Intermediate Value Theorem**, there must be at least one value i > −1 such that:

R(i) = P.

Therefore, an IRR exists.

## Solution 4: Uniqueness of IRR

Given:

R(i) = Σ Aₙ(1+i)^(-n)

Differentiate:

R'(i) = Σ [−nAₙ(1+i)^(-n−1)]

Therefore:

**R'(i) = −Σ nAₙ/(1+i)^(n+1)**

Since:

* n > 0.
* Aₙ ≥ 0.
* 1+i > 0.
* At least one Aₙ is positive.

We obtain:

R'(i) < 0.

Therefore, R(i) is strictly decreasing.

A strictly decreasing function can take a particular value only once.

Hence, the IRR is unique.

## Solution 5: Existence and Uniqueness

**a) Existence**

Existence means that at least one value of i satisfies the IRR equation:

R(i) = P.

**b) Uniqueness**

Uniqueness means that no other value of i satisfies the same equation.

In this topic:

* Continuity and the Intermediate Value Theorem establish existence.
* Strict monotonicity establishes uniqueness.

## Solution 6: Numerical Calculation

Given:

P = 100

A₁ = 18

A₂ = 37

A₃ = 39

A₄ = 27

The IRR equation is:

100 = 18/(1+i) + 37/(1+i)² + 39/(1+i)³ + 27/(1+i)⁴

The approximate solution is:

**IRR ≈ 7.66%.**

---

# 23. Final Summary

An investment requires an initial payment P and produces future returns A₁, A₂, ..., Aₙ.

The internal rate of return is the periodic interest rate that makes the present value of all future returns equal to the initial investment.

Its mathematical definition is:

**P = Σ(n=1 to N) Aₙ(1+i)^(-n)**

We define:

R(i) = Σ(n=1 to N) Aₙ(1+i)^(-n)

Then the IRR satisfies:

R(i) = P.

Under the assumptions of the lecture:

* R(i) is continuous.
* R(i) approaches infinity as i approaches −1 from the right.
* R(i) approaches zero as i approaches infinity.
* R(i) is strictly decreasing.

Therefore:

* The Intermediate Value Theorem guarantees existence.
* Strict monotonicity guarantees uniqueness.

We also established:

**i > 0 if and only if P < Σ Aₙ.**

Finally:

**IRR is the discount rate at which NPV equals zero.**

---

# 🎓 Chapter 1 Completed: Basic Finance Concepts

Congratulations! You have completed all five topics of Chapter 1.

| No. | Topic                   | Main idea                                         |
| --- | ----------------------- | ------------------------------------------------- |
| 1   | Interest                | How money grows over time                         |
| 2   | Inflation               | How rising prices affect purchasing power         |
| 3   | Annuities               | How regular payments accumulate or are valued     |
| 4   | Bonds                   | How future bond payments are valued today         |
| 5   | Internal Rate of Return | How to determine the return rate of an investment |

These five topics are connected through one central mathematical idea:

**The Time Value of Money.**

Interest explains how money grows. Inflation explains how purchasing power changes. Annuities describe sequences of payments. Bonds use present value to determine the price of future payments. IRR uses present value to determine the return rate of an investment.

Together, they form an important mathematical foundation for financial analysis.

**End of Chapter 1 — Basic Finance Concepts.**
