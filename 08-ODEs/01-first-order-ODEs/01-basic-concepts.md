# 1. 🔑Basic Concepts and Definitions of Differential Equations

## 📋Table of Contents

1. [Learning Objectives](#learning-objectives)
2. [Motivation](#1-motivation)
3. [Prerequisites](#2-prerequisites)
4. [Introduction to Differential Equations](#3-introduction-to-differential-equations)

   * Ordinary Differential Equations (ODEs)
   * Partial Differential Equations (PDEs)
5. [Order and Degree of Differential Equations](#4-order-and-degree-of-differential-equations)

   * Order
   * Degree
   * Difference Between Order and Degree
6. [Classification of Differential Equations](#5-classification-of-differential-equations)

   * Classification by Type
   * Classification by Order
   * Linear and Nonlinear Equations
   * Homogeneous and Nonhomogeneous Equations
7. [Solutions of Differential Equations](#6-solutions-of-differential-equations)

   * General Solution
   * Particular Solution
   * Verification of Solutions
8. [Solution Curves](#7-solution-curves)
9. [Initial Value Problems](#8-initial-value-problems)
10. [Important Differences to Remember](#9-important-differences-to-remember)
11. [Common Mistakes](#10-common-mistakes)
12. [Formula and Concept Summary](#11-formula-and-concept-summary)
13. [Practice Questions](#12-practice-questions)
14. [Answers to Practice Questions](#13-answers-to-practice-questions)
15. [Conclusion](#14-conclusion)
16. [References](#references)

---

## 🎯Learning Objectives

After studying this topic, you should be able to:

1. Define differential equations and explain their importance.
2. Distinguish between ordinary and partial differential equations.
3. Determine the order and degree of a differential equation.
4. Classify differential equations according to their type, order, and linearity.
5. Distinguish between homogeneous and nonhomogeneous linear equations.
6. Recognize homogeneous nonlinear first-order differential equations.
7. Explain the meaning of a solution of a differential equation.
8. Distinguish between general and particular solutions.
9. Interpret solutions geometrically using solution curves.
10. Formulate and solve simple initial value problems.

---

## 1. Motivation

Many quantities in real life do not remain constant. They change with time, position, or other independent variables.

Examples include:

* Population growth over time.
* Changes in temperature.
* The motion and velocity of objects.
* The spread of infectious diseases.
* Changes in the concentration of substances.

Mathematics provides tools for describing and analyzing these changes.

One important mathematical tool is the **differential equation**.

Unlike ordinary algebraic equations, which often describe relationships between unknown quantities, differential equations describe relationships involving unknown functions and their rates of change.

Understanding these basic concepts provides the foundation for studying methods of solving differential equations.

## 2. Prerequisites

Before studying this topic, you should understand:

* Functions and their notation.
* Independent and dependent variables.
* Differentiation.
* Basic integration.
* Algebraic manipulation.
* Basic mathematical notation.

For example, if y is a function of x, we write:

`y = y(x)`

Its first derivative is:

`dy/dx`

Its second derivative is:

`d²y/dx²`

These derivatives describe how the function changes with respect to x.

---

## 3. Introduction to Differential Equations

### 3.1 Definition of a Differential Equation

A **differential equation** is an equation that involves an unknown function and one or more of its derivatives.

For example:

`dy/dx = 2x`

This is a differential equation because it contains the derivative of the unknown function y.

The objective is to find a function y(x) whose derivative satisfies the given equation.

For example, one function satisfying this equation is:

`y = x²`

because:

`dy/dx = 2x`

### 3.2 Ordinary Differential Equations (ODEs)

An **ordinary differential equation (ODE)** involves ordinary derivatives of an unknown function that depends on only one independent variable.

Example:

`dy/dx + y = x`

Here:

* x is the independent variable.
* y is the dependent variable.
* y is a function of x, written as `y = y(x)`.

### 3.3 Partial Differential Equations (PDEs)

A **partial differential equation (PDE)** involves partial derivatives of an unknown function that depends on two or more independent variables.

Example:

`∂u/∂t = ∂²u/∂x²`

Here:

* u is the unknown function.
* x represents position.
* t represents time.
* u depends on both x and t, written as `u = u(x, t)`.

### 3.4 Difference Between ODEs and PDEs

| Feature               | Ordinary Differential Equation (ODE) | Partial Differential Equation (PDE)            |
| --------------------- | ------------------------------------ | ---------------------------------------------- |
| Independent variables | One                                  | Two or more                                    |
| Derivatives           | Ordinary derivatives                 | Partial derivatives                            |
| Unknown function      | Usually depends on one variable      | Depends on several variables                   |
| Example               | `dy/dx = x + y`                      | `∂u/∂t = ∂²u/∂x²`                              |
| Applications          | Population growth, cooling, motion   | Heat distribution, wave propagation, diffusion |

**Important:** Our main focus in this course section is ordinary differential equations, particularly first-order ODEs.

---

## 4. Order and Degree of Differential Equations

Order and degree are two important characteristics used to describe differential equations.

Although they are related, they have different meanings.

### 4.1 Order of a Differential Equation

**Definition:**

The order of a differential equation is the order of the highest derivative appearing in the equation.

In simple terms, identify the derivative with the largest differentiation order. That order determines the order of the equation.

#### Worked Examples

**Example 1**

`dy/dx + y = x`

The highest derivative is:

`dy/dx`

It is a first-order derivative.

Therefore:

**Order = 1**

**Example 2**

`d²y/dx² + 3(dy/dx) + 2y = 0`

The highest derivative is:

`d²y/dx²`

Therefore:

**Order = 2**

**Example 3**

`d³y/dx³ + 2(d²y/dx²) + dy/dx + y = 0`

The highest derivative is the third derivative.

Therefore:

**Order = 3**

**Example 4**

`(dy/dx)^5 + d⁴y/dx⁴ = 0`

The highest derivative is:

`d⁴y/dx⁴`

Therefore:

**Order = 4**

**Important observation:**

The order depends on the highest derivative, not on the exponent applied to a derivative.

For example, `(dy/dx)^5` is still a power of the first derivative. It does not make the equation fifth-order.

#### Procedure for Determining Order

1. Identify all derivatives in the equation.
2. Determine the differentiation order of each derivative.
3. Identify the derivative with the highest order.
4. State its order.

### 4.2 Degree of a Differential Equation

**Definition:**

The degree of a differential equation is the exponent of its highest-order derivative after the equation has been expressed as a polynomial in its derivatives, provided the degree is defined.

In simple terms, after identifying the highest derivative, determine its exponent.

#### Worked Examples

**Example 1**

`dy/dx + y = 0`

The highest derivative is the first derivative.

Its exponent is 1.

Therefore:

* Order = 1
* Degree = 1

**Example 2**

`(d²y/dx²)^2 + dy/dx + y = 0`

The highest derivative is the second derivative.

Its exponent is 2.

Therefore:

* Order = 2
* Degree = 2

**Example 3**

`(d³y/dx³)^3 + d²y/dx² + y = 0`

The highest derivative is the third derivative.

Its exponent is 3.

Therefore:

* Order = 3
* Degree = 3

**Example 4**

`(d⁴y/dx⁴)^2 + 5(dy/dx) + y = 0`

The highest derivative is the fourth derivative.

Its exponent is 2.

Therefore:

* Order = 4
* Degree = 2

### 4.3 When Is the Degree Undefined?

The degree is not always defined.

Consider:

`sin(dy/dx) + y = 0`

Here, the derivative appears inside a trigonometric function.

The equation is not polynomial in its derivatives.

Therefore:

* Order = 1
* Degree = Undefined under the standard elementary definition.

**Important:** The degree is defined only when the equation can be expressed as a polynomial in its derivatives, after appropriate algebraic transformations where possible.

### 4.4 Difference Between Order and Degree

| Order                                             | Degree                                                      |
| ------------------------------------------------- | ----------------------------------------------------------- |
| Determined by the highest derivative.             | Determined by the exponent of the highest-order derivative. |
| Always identifiable from the derivatives present. | May be undefined.                                           |
| Does not depend on the exponent of a derivative.  | Depends on the exponent of the highest-order derivative.    |

### 4.5 Procedure for Determining Degree

1. Determine the order of the equation.
2. Check whether the equation is polynomial in its derivatives.
3. If necessary, remove radicals or fractional powers algebraically where appropriate.
4. Identify the highest-order derivative.
5. Determine its exponent.

---

## 5. Classification of Differential Equations

Differential equations can be classified according to different mathematical properties.

The main classifications considered here are:

1. Classification by type.
2. Classification by order.
3. Classification by linearity.
4. Classification by homogeneity.

### 5.1 Classification by Type

According to the type of derivative involved, differential equations are classified into:

* Ordinary differential equations (ODEs).
* Partial differential equations (PDEs).

Example of an ODE:

`dy/dx + y = x`

Example of a PDE:

`∂u/∂t = ∂²u/∂x²`

### 5.2 Classification by Order

According to the highest derivative, differential equations can be classified as:

* First-order differential equations.
* Second-order differential equations.
* Third-order differential equations.
* Higher-order differential equations.

Examples:

**First-order:**

`dy/dx + y = 0`

**Second-order:**

`d²y/dx² + y = 0`

**Third-order:**

`d³y/dx³ + y = 0`

### 5.3 Classification by Linearity

Differential equations can also be classified as linear or nonlinear.

#### 5.3.1 Linear Differential Equations

A first-order ODE is **linear** if it can be expressed in the standard form:

`dy/dx + P(x)y = Q(x)`

Where:

* P(x) is a function of x alone.
* Q(x) is a function of x alone.
* y is the unknown function.

In a linear equation:

1. The unknown function appears only to the first power.
2. Its derivatives appear only to the first power.
3. The unknown function is not multiplied by its derivatives.
4. Coefficients depend only on the independent variable.

**Examples:**

`dy/dx + 3y = x²`

`dy/dx + xy = sin(x)`

Both are linear first-order ODEs.

#### 5.3.2 Nonlinear Differential Equations

A differential equation is **nonlinear** if it cannot be expressed in the required linear form.

Nonlinear equations may contain:

* Powers of the dependent variable greater than one.
* Products of the dependent variable and its derivatives.
* Nonlinear functions of the dependent variable.

**Examples:**

`dy/dx + y² = 0`

`y(dy/dx) = x`

`dy/dx + sin(y) = x`

These equations are nonlinear.

#### 5.3.3 Important Comparison

Consider:

`dy/dx + xy = 0`

This equation is linear because x is a coefficient depending only on the independent variable.

However:

`dy/dx + y² = 0`

This equation is nonlinear because the dependent variable is squared.

**Remember:** The presence of a product involving x and y does not automatically make a differential equation nonlinear.

### 5.4 Homogeneous and Nonhomogeneous Differential Equations

The terminology of homogeneous and nonhomogeneous differential equations requires special attention because it has different meanings in different contexts.

There are two important meanings of homogeneity in first-order ODEs.

#### 5.4.1 Homogeneous and Nonhomogeneous Linear ODEs

A first-order linear ODE has the standard form:

`dy/dx + P(x)y = Q(x)`

**Homogeneous Linear ODE**

A linear differential equation is homogeneous if:

`Q(x) = 0`

Its standard form becomes:

`dy/dx + P(x)y = 0`

Example:

`dy/dx + 3y = 0`

This equation is linear and homogeneous.

**Nonhomogeneous Linear ODE**

A linear differential equation is nonhomogeneous if:

`Q(x) ≠ 0`

Its standard form is:

`dy/dx + P(x)y = Q(x)`

Example:

`dy/dx + 3y = x`

This equation is linear and nonhomogeneous.

**Important distinction:**

In this context, homogeneity refers to whether the right-hand side of the standard linear equation is zero. It does not mean that the equation is nonlinear or that all its terms have the same degree.

#### 5.4.2 Homogeneous Nonlinear First-Order ODEs

The term homogeneous can also describe a class of nonlinear first-order differential equations.

A common form is:

`dy/dx = F(y/x)`

Here, the right-hand side depends only on the ratio y/x.

In other words, it can be expressed as a function of y/x rather than depending independently on x and y.

**Example 1: Homogeneous Nonlinear ODE**

`dy/dx = 1 + (y/x)^2`

The right-hand side depends only on y/x.

Therefore, this is a homogeneous first-order ODE.

It is also nonlinear because of the squared ratio.

**Example 2: Nonlinear but Not Homogeneous in This Sense**

`dy/dx = x + y²`

The right-hand side cannot be expressed as a function of y/x alone.

Therefore, it is not homogeneous under this common first-order definition.

It is nonlinear because of the y² term.

#### 5.4.3 Homogeneity in Differential Form

A first-order ODE may also be expressed as:

`M(x,y)dx + N(x,y)dy = 0`

One common test for homogeneity is to determine whether M(x,y) and N(x,y) are homogeneous functions of the same degree.

A function G(x,y) is homogeneous of degree n if:

`G(tx,ty) = t^n G(x,y)`

for an appropriate range of t.

**Example:**

Consider:

`M(x,y) = x² + y²`

Replace x with tx and y with ty:

`M(tx,ty) = (tx)² + (ty)²`

Simplifying:

`M(tx,ty) = t²x² + t²y²`

Taking t² as a common factor:

`M(tx,ty) = t²(x² + y²)`

Therefore:

`M(tx,ty) = t²M(x,y)`

Hence, M(x,y) is homogeneous of degree 2.

This test is useful when recognizing homogeneous equations written in differential form.

#### 5.4.4 Comparison of Different Meanings of Homogeneity

| Equation              | Linearity | Homogeneity                         | Reason                                                          |
| --------------------- | --------- | ----------------------------------- | --------------------------------------------------------------- |
| `dy/dx + 3y = 0`      | Linear    | Homogeneous linear                  | Right-hand side is zero.                                        |
| `dy/dx + 3y = x`      | Linear    | Nonhomogeneous linear               | Right-hand side is not identically zero.                        |
| `dy/dx = 1 + (y/x)^2` | Nonlinear | Homogeneous first-order             | Right-hand side depends only on y/x.                            |
| `dy/dx = x + y²`      | Nonlinear | Not homogeneous in the stated sense | Right-hand side cannot be expressed as a function of y/x alone. |

**Important conclusion:**

A nonlinear ODE can be homogeneous.

Linearity and homogeneity describe different mathematical properties, and the meaning of homogeneity depends on the context.

**Common misconception:** Do not assume that every homogeneous ODE is linear or that every nonlinear ODE is nonhomogeneous.

---

## 6. Solutions of Differential Equations

### 6.1 Definition of a Solution

A **solution of a differential equation** is a function that satisfies the equation when the function and its required derivatives are substituted into it.

Consider:

`dy/dx = 2x`

Integrating both sides:

`y = ∫2x dx`

Therefore:

`y = x² + C`

where C is an arbitrary constant.

To verify this result, differentiate:

`dy/dx = 2x`

This satisfies the original differential equation.

Therefore:

`y = x² + C`

is a solution.

### 6.2 General Solution

A **general solution** represents a family of solutions, usually containing arbitrary constants.

For:

`dy/dx = 2x`

The general solution is:

`y = x² + C`

Different values of C produce different solutions.

Examples:

* `y = x²`, when C = 0.
* `y = x² + 2`, when C = 2.
* `y = x² - 3`, when C = -3.

All these functions satisfy the original differential equation.

### 6.3 Particular Solution

A **particular solution** is a specific solution obtained by assigning particular values to the arbitrary constants, often using an initial condition.

Consider:

`dy/dx = 2x`

Suppose the condition is:

`y(0) = 3`

From the general solution:

`y = x² + C`

Substitute x = 0 and y = 3:

`3 = 0² + C`

Therefore:

`C = 3`

The particular solution is:

`y = x² + 3`

### 6.4 Verification of a Solution

To verify a proposed solution:

1. Differentiate the proposed function as required.
2. Substitute the function and its derivatives into the original equation.
3. Check whether the equation is satisfied.
4. If an initial condition is given, verify that condition as well.

**Key idea:** A proposed solution is correct only if it satisfies the original differential equation and any prescribed initial condition.

---

## 7. Solution Curves

### 7.1 Definition

A **solution curve** is the graph of a particular solution of a differential equation.

Consider the general solution:

`y = x² + C`

Different values of C produce different parabolas.

For example:

* `y = x² - 2`
* `y = x²`
* `y = x² + 2`

All these curves satisfy:

`dy/dx = 2x`

This is because differentiating any member of the family gives:

`dy/dx = 2x`

### 7.2 Geometric Interpretation of an Initial Condition

Suppose we require:

`y(0) = 2`

This means that the solution curve must pass through the point:

`(0, 2)`

Using the general solution:

`y = x² + C`

Substitute x = 0 and y = 2:

`2 = 0² + C`

Therefore:

`C = 2`

The required solution curve is:

`y = x² + 2`

Thus, an initial condition selects a particular curve from a family of solution curves.

**Geometric interpretation:**

* A general solution represents a family of curves.
* A particular solution represents one specific curve.
* An initial condition identifies the required curve by specifying a point through which it must pass.

---

## 8. Initial Value Problems

### 8.1 Definition

An **initial value problem (IVP)** consists of a differential equation together with a condition specifying the value of the unknown function at a particular point.

For a first-order ODE, an IVP can be written as:

`dy/dx = f(x,y)`

Subject to:

`y(x₀) = y₀`

Where:

| Symbol | Meaning                                   |
| ------ | ----------------------------------------- |
| x      | Independent variable                      |
| y      | Unknown function                          |
| f(x,y) | Function determining the derivative       |
| x₀     | Initial value of the independent variable |
| y₀     | Prescribed value of the function at x₀    |

### 8.2 Worked Example

Solve:

`dy/dx = 2x`

Subject to:

`y(1) = 5`

**Step 1: Find the general solution.**

Integrating:

`y = ∫2x dx`

Therefore:

`y = x² + C`

**Step 2: Apply the initial condition.**

Given:

`y(1) = 5`

Substitute x = 1 and y = 5:

`5 = 1² + C`

Therefore:

`C = 4`

**Step 3: State the particular solution.**

Substitute C = 4:

`y = x² + 4`

**Step 4: Verify the differential equation.**

Differentiate:

`dy/dx = 2x`

This satisfies the original equation.

**Step 5: Verify the initial condition.**

Substitute x = 1:

`y(1) = 1² + 4`

`y(1) = 5`

The initial condition is satisfied.

Therefore, the solution is:

`y = x² + 4`

---

## 9. Important Differences to Remember

The following table summarizes the major concepts introduced in this topic.

| Concept                        | Meaning                                                           |
| ------------------------------ | ----------------------------------------------------------------- |
| Differential equation          | An equation involving an unknown function and its derivatives.    |
| ODE                            | A differential equation involving ordinary derivatives.           |
| PDE                            | A differential equation involving partial derivatives.            |
| Order                          | The order of the highest derivative.                              |
| Degree                         | The exponent of the highest-order derivative, when defined.       |
| Linear equation                | An equation that can be expressed in the required linear form.    |
| Nonlinear equation             | An equation that cannot be expressed in the required linear form. |
| Homogeneous linear equation    | A linear equation whose right-hand side is zero in standard form. |
| Nonhomogeneous linear equation | A linear equation whose right-hand side is not identically zero.  |
| General solution               | A family of solutions, usually containing arbitrary constants.    |
| Particular solution            | A specific solution.                                              |
| Solution curve                 | The graph of a particular solution.                               |
| Initial value problem          | A differential equation together with an initial condition.       |

---

## 10. Common Mistakes

Understanding common mistakes helps prevent errors when studying and solving differential equations.

### 1. Confusing Order and Degree

Order depends on the highest derivative, while degree depends on the exponent of that derivative when defined.

### 2. Assuming Every Equation Has a Defined Degree

The degree may be undefined if the equation is not polynomial in its derivatives under the standard definition.

### 3. Thinking That Every Equation Containing y² Is Linear

A term such as y² makes a first-order equation nonlinear.

### 4. Thinking That xy Makes an Equation Nonlinear

The equation:

`dy/dx + xy = 0`

is linear because x is a coefficient depending only on the independent variable.

### 5. Forgetting the Integration Constant

Indefinite integration introduces an arbitrary constant.

Always include C when finding the general solution.

### 6. Confusing General and Particular Solutions

A general solution represents a family of solutions, while a particular solution identifies one specific member.

### 7. Forgetting to Apply the Initial Condition

An initial value problem requires the given condition to determine the arbitrary constant, when appropriate.

### 8. Failing to Verify the Final Answer

Always check whether the proposed solution satisfies the original differential equation and any given initial condition.

### 9. Confusing the Different Meanings of Homogeneity

Homogeneous linear equations and homogeneous nonlinear first-order equations use different definitions.

Always identify the context before classifying an equation.

---

## 11. Formula and Concept Summary

### A. Differential Equation

An equation involving an unknown function and its derivatives.

### B. Order

`Order = Highest order of derivative appearing in the equation`

### C. Degree

`Degree = Exponent of the highest-order derivative`

This applies when the equation is appropriately expressed as a polynomial in its derivatives.

### D. First-Order Linear ODE

Standard form:

`dy/dx + P(x)y = Q(x)`

### E. Homogeneous Linear ODE

`dy/dx + P(x)y = 0`

### F. Nonhomogeneous Linear ODE

`dy/dx + P(x)y = Q(x)`, where Q(x) is not identically zero.

### G. Homogeneous Nonlinear First-Order ODE

Common form:

`dy/dx = F(y/x)`

### H. General Solution

A family of solutions, usually containing arbitrary constants.

Example:

`y = x² + C`

### I. Particular Solution

A specific solution obtained by determining the arbitrary constant.

Example:

`y = x² + 3`

### J. Initial Value Problem

`dy/dx = f(x,y)`

Subject to:

`y(x₀) = y₀`

---

## 12. Practice Questions

Try to solve the following questions before checking the answers.

### Part A: Order and Degree

Determine the order and degree of each differential equation, where defined.

**1.**

`dy/dx + 5y = x`

**2.**

`(dy/dx)^4 + y = 0`

**3.**

`d²y/dx² + 7(dy/dx) + 12y = 0`

**4.**

`(d³y/dx³)^2 + d²y/dx² + y = 0`

**5.**

`sin(dy/dx) + y = 0`

### Part B: Classification

Classify each equation as linear or nonlinear.

For linear equations, also determine whether the equation is homogeneous or nonhomogeneous.

**6.**

`dy/dx + 4y = 0`

**7.**

`dy/dx + xy = x²`

**8.**

`dy/dx + y² = 0`

**9.**

`y(dy/dx) = x`

### Part C: Solutions and Solution Curves

**10.** Verify that `y = x² + 7` is a solution of:

`dy/dx = 2x`

**11.** Find the general solution of:

`dy/dx = 4x³`

**12.** Find the particular solution of:

`dy/dx = 4x³`

Given:

`y(1) = 6`

**13.** For the family:

`y = x² + C`

Determine the value of C that gives the solution curve passing through (0, 5).

**14.** Explain the difference between a general solution and a particular solution in your own words.

---

## 13. Answers to Practice Questions

Try the questions independently before checking these answers.

| Question | Answer                                                                                                             |
| -------- | ------------------------------------------------------------------------------------------------------------------ |
| 1        | Order = 1, Degree = 1                                                                                              |
| 2        | Order = 1, Degree = 4                                                                                              |
| 3        | Order = 2, Degree = 1                                                                                              |
| 4        | Order = 3, Degree = 2                                                                                              |
| 5        | Order = 1, Degree is undefined under the standard definition.                                                      |
| 6        | Linear and homogeneous.                                                                                            |
| 7        | Linear and nonhomogeneous.                                                                                         |
| 8        | Nonlinear.                                                                                                         |
| 9        | Nonlinear.                                                                                                         |
| 10       | Differentiating gives dy/dx = 2x, so it satisfies the equation.                                                    |
| 11       | y = x⁴ + C                                                                                                         |
| 12       | y = x⁴ + 5                                                                                                         |
| 13       | C = 5                                                                                                              |
| 14       | A general solution represents a family of solutions, while a particular solution identifies one specific solution. |

### Detailed Solution to Question 12

Given:

`dy/dx = 4x³`

**Step 1: Integrate both sides.**

`y = ∫4x³ dx`

Therefore:

`y = x⁴ + C`

**Step 2: Apply the initial condition.**

Given:

`y(1) = 6`

Substitute:

`6 = 1⁴ + C`

Therefore:

`6 = 1 + C`

`C = 5`

**Step 3: State the particular solution.**

`y = x⁴ + 5`

---

## 14. Conclusion

In this topic, we introduced the fundamental concepts and definitions of differential equations.

The most important ideas are:

1. A differential equation involves an unknown function and its derivatives.
2. An ODE involves ordinary derivatives, while a PDE involves partial derivatives.
3. The order is determined by the highest derivative appearing in the equation.
4. The degree is the exponent of the highest-order derivative when the equation is appropriately expressed as a polynomial in its derivatives.
5. A first-order linear ODE can be written in the standard form `dy/dx + P(x)y = Q(x)`.
6. Differential equations can be classified as linear or nonlinear.
7. Homogeneity has different meanings depending on the type of differential equation.
8. A solution is a function that satisfies the differential equation.
9. A general solution represents a family of solutions, while a particular solution identifies a specific solution.
10. A solution curve is the graph of a particular solution.
11. An initial value problem combines a differential equation with an initial condition.
12. Proposed solutions should be verified by substitution and by checking any initial conditions.

These concepts form the foundation for studying methods of solving first-order differential equations, including separable equations, linear equations, exact equations, integrating factors, and other techniques.

---

## References

Kreyszig, E., Kreyszig, H., & Norminton, E. J. (2011). *Advanced Engineering Mathematics* (10th ed.). John Wiley & Sons. Chapter 1: First-Order ODEs.
