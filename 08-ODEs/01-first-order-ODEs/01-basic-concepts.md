# 1. Basic Concepts and Definitions

## 1.1 Introduction to Differential Equations

A **differential equation** is an equation that involves an unknown function and one or more of its derivatives.

For example:

`dy/dx = 2x`

This is a differential equation because it contains the derivative of the unknown function y.

Differential equations are used to model quantities that change, such as population, temperature, velocity, and the spread of diseases.

### Ordinary Differential Equations (ODEs)

An **ordinary differential equation (ODE)** involves ordinary derivatives of an unknown function that depends on one independent variable.

Example:

`dy/dx + y = x`

Here, y is a function of x, written as `y = y(x)`.

### Partial Differential Equations (PDEs)

A **partial differential equation (PDE)** involves partial derivatives of an unknown function that depends on two or more independent variables.

Example:

`∂u/∂t = ∂²u/∂x²`

Here, u depends on both position x and time t, written as `u = u(x, t)`.

| Feature               | ODE                                | PDE                                            |
| --------------------- | ---------------------------------- | ---------------------------------------------- |
| Independent variables | Usually one                        | Two or more                                    |
| Derivatives           | Ordinary derivatives               | Partial derivatives                            |
| Example               | dy/dx = x + y                      | ∂u/∂t = ∂²u/∂x²                                |
| Applications          | Population growth, cooling, motion | Heat distribution, wave propagation, diffusion |

---

## 1.2 Order of a Differential Equation

The **order** of a differential equation is the order of the highest derivative appearing in the equation.

### Examples

**Example 1**

`dy/dx + y = x`

The highest derivative is the first derivative.

**Order = 1**

**Example 2**

`d²y/dx² + 3(dy/dx) + 2y = 0`

The highest derivative is the second derivative.

**Order = 2**

**Example 3**

`d³y/dx³ + 2(d²y/dx²) + dy/dx + y = 0`

The highest derivative is the third derivative.

**Order = 3**

**Example 4**

`(dy/dx)^5 + d⁴y/dx⁴ = 0`

The highest derivative is the fourth derivative.

**Order = 4**

**Important:** The order depends on the highest derivative, not on the exponent applied to a derivative.

### Procedure for determining order

1. Identify all derivatives in the equation.
2. Find the derivative of the highest order.
3. State its order.

---

## 1.3 Degree of a Differential Equation

The **degree** of a differential equation is the exponent of its highest-order derivative after the equation has been expressed as a polynomial in its derivatives, provided the degree is defined.

### Examples

**Example 1**

`dy/dx + y = 0`

The highest derivative is the first derivative, and its exponent is 1.

**Order = 1, Degree = 1**

**Example 2**

`(d²y/dx²)^2 + dy/dx + y = 0`

The highest derivative is the second derivative, and its exponent is 2.

**Order = 2, Degree = 2**

**Example 3**

`(d³y/dx³)^3 + d²y/dx² + y = 0`

The highest derivative is the third derivative, and its exponent is 3.

**Order = 3, Degree = 3**

**Example 4**

`(d⁴y/dx⁴)^2 + 5(dy/dx) + y = 0`

The highest derivative is the fourth derivative, and its exponent is 2.

**Order = 4, Degree = 2**

### When is the degree undefined?

Consider:

`sin(dy/dx) + y = 0`

The derivative appears inside a trigonometric function. The equation is not polynomial in its derivatives, so its degree is **undefined under the standard elementary definition**.

### Difference between order and degree

* **Order:** Determined by the highest derivative.
* **Degree:** Determined by the exponent of the highest-order derivative when the degree is defined.

### Procedure for determining degree

1. Determine the order of the equation.
2. Check whether the equation is polynomial in its derivatives, removing radicals or fractional powers algebraically where appropriate.
3. Identify the highest-order derivative.
4. Determine its exponent.

---

## 1.4 Classification of Differential Equations

Differential equations can be classified according to their type, order, linearity, and other properties.

### 1.4.1 Classification by type

Differential equations may be ordinary or partial.

Example of an ODE:

`dy/dx + y = x`

Example of a PDE:

`∂u/∂t = ∂²u/∂x²`

### 1.4.2 Classification by order

The order is determined by the highest derivative.

For example:

`dy/dx + y = 0`

is a first-order equation.

However:

`d²y/dx² + y = 0`

is a second-order equation.

### 1.4.3 Linear Differential Equations

A first-order ODE is **linear** if it can be written in the standard form:

`dy/dx + P(x)y = Q(x)`

Here, P(x) and Q(x) are functions of x alone.

Examples:

`dy/dx + 3y = x²`

and

`dy/dx + xy = sin(x)`

are linear first-order ODEs.

In a linear equation, the unknown function and its derivative appear only to the first power, and the unknown function is not multiplied by its derivative.

### 1.4.4 Nonlinear Differential Equations

A differential equation is **nonlinear** if it cannot be written in the required linear form.

Examples:

`dy/dx + y² = 0`

`y(dy/dx) = x`

`dy/dx + sin(y) = x`

These equations are nonlinear because they contain terms such as y², a product of y and its derivative, or sin(y).

**Important distinction:**

`dy/dx + xy = 0`

is linear because x is a coefficient depending only on the independent variable.

However:

`dy/dx + y² = 0`

is nonlinear because y is squared.

### 1.4.5 Homogeneous and Nonhomogeneous Linear Equations

A first-order linear ODE has the standard form:

`dy/dx + P(x)y = Q(x)`

* It is **homogeneous** if Q(x) = 0.
* It is **nonhomogeneous** if Q(x) ≠ 0.

Examples:

`dy/dx + 2y = 0`

is homogeneous.

`dy/dx + 2y = e^x`

is nonhomogeneous.

**Note:** The term homogeneous has other meanings in differential equations. Here, it refers specifically to homogeneous linear equations.

---

## Homogeneous and Nonhomogeneous Differential Equations

The terms *homogeneous* and *nonhomogeneous* can have different meanings depending on the type of differential equation being studied. In first-order differential equations, it is especially important to distinguish between homogeneous linear equations and homogeneous nonlinear equations.

### 1. Homogeneous and Nonhomogeneous Linear ODEs

A first-order linear ODE can be written in the standard form:

dy/dx + P(x)y = Q(x)

Here, P(x) and Q(x) are functions of x.

**Homogeneous linear ODE**

The equation is called homogeneous if Q(x) = 0. Therefore, its standard form is:

dy/dx + P(x)y = 0

Example:

dy/dx + 3y = 0

This equation is linear and homogeneous because the right-hand side of the standard form is zero.

**Nonhomogeneous linear ODE**

The equation is called nonhomogeneous if Q(x) is not identically zero. Its standard form is:

dy/dx + P(x)y = Q(x)

Example:

dy/dx + 3y = x

This equation is linear and nonhomogeneous because Q(x) = x, which is not identically zero.

Important: In this context, the word "homogeneous" refers to the right-hand side of the standard linear equation. It does not mean that the differential equation is nonlinear or that every term must have the same degree.

### 2. Homogeneous Nonlinear First-Order ODEs

A nonlinear first-order ODE can also be called homogeneous, but the term has a different meaning in this context.

A common form of a homogeneous first-order ODE is:

dy/dx = F(y/x)

Here, F is a function that depends on the ratio y/x.

In other words, the right-hand side can be expressed entirely in terms of y/x, rather than depending independently on x and y.

**Example 1: A homogeneous nonlinear ODE**

dy/dx = 1 + (y/x)^2

The right-hand side depends only on the ratio y/x. Therefore, this is a homogeneous first-order ODE.

It is also nonlinear because the equation contains (y/x)^2, so it cannot be expressed in the standard linear form:

dy/dx + P(x)y = Q(x)

**Example 2: A nonlinear ODE that is not homogeneous in this sense**

dy/dx = x + y^2

The right-hand side cannot be expressed as a function of y/x alone. Therefore, this equation is not homogeneous under the common first-order definition used here.

It is nonlinear because of the y^2 term.

### 3. Another Way to Identify a Homogeneous First-Order ODE

A first-order ODE may also be written in the differential form:

M(x,y)dx + N(x,y)dy = 0

One common test for homogeneity is to check whether M(x,y) and N(x,y) are homogeneous functions of the same degree.

A function G(x,y) is homogeneous of degree n if:

G(tx,ty) = t^n G(x,y)

for an appropriate range of t.

For example, consider:

M(x,y) = x^2 + y^2

Replace x with tx and y with ty:

M(tx,ty) = (tx)^2 + (ty)^2

M(tx,ty) = t^2(x^2 + y^2)

Therefore, M(x,y) is homogeneous of degree 2.

This test is useful when an ODE is written in differential form. It is another way to recognize homogeneous first-order equations.

### 4. Comparison of the Different Meanings

Consider the following equations:

**Equation A:**

dy/dx + 3y = 0

* Type: Linear
* Homogeneity: Homogeneous linear ODE
* Reason: The right-hand side is zero.

**Equation B:**

dy/dx + 3y = x

* Type: Linear
* Homogeneity: Nonhomogeneous linear ODE
* Reason: The right-hand side is not identically zero.

**Equation C:**

dy/dx = 1 + (y/x)^2

* Type: Nonlinear
* Homogeneity: Homogeneous first-order ODE
* Reason: The right-hand side depends only on y/x.

**Equation D:**

dy/dx = x + y^2

* Type: Nonlinear
* Homogeneity: Not homogeneous under the common first-order definition discussed above
* Reason: The right-hand side cannot be expressed as a function of y/x alone.

### 5. Important Conclusion

A nonlinear ODE can be homogeneous. However, we must identify which definition of homogeneity is being used.

* For a linear ODE, homogeneous means that Q(x) = 0 when the equation is written as dy/dx + P(x)y = Q(x).
* For a common class of nonlinear first-order ODEs, homogeneous means that the equation can be written as dy/dx = F(y/x).
* In differential form, another useful test is whether M(x,y) and N(x,y) are homogeneous functions of the same degree.

**Common misconception:** Do not assume that every homogeneous ODE is linear, or that every nonlinear ODE is nonhomogeneous. Linearity and homogeneity describe different properties, and the meaning of homogeneity depends on the context.

---

## 1.5 Solutions of Differential Equations

A **solution of a differential equation** is a function that satisfies the equation when the function and its required derivatives are substituted into it.

Consider:

`dy/dx = 2x`

Integrating both sides gives:

`y = ∫2x dx`

Therefore:

`y = x² + C`

where C is an arbitrary constant.

To verify the solution, differentiate:

`dy/dx = 2x`

This satisfies the original differential equation.

### General Solution

A **general solution** represents a family of solutions, usually containing arbitrary constants.

For the equation:

`dy/dx = 2x`

the general solution is:

`y = x² + C`

Different values of C give different solutions.

For example:

* `y = x²`, when C = 0.
* `y = x² + 2`, when C = 2.
* `y = x² - 3`, when C = -3.

### Particular Solution

A **particular solution** is a specific solution obtained by assigning a particular value to the arbitrary constant, often using an initial condition.

For example, suppose:

`dy/dx = 2x`

with the condition:

`y(0) = 3`

From the general solution:

`y = x² + C`

Substitute x = 0 and y = 3:

`3 = 0² + C`

Therefore:

`C = 3`

The particular solution is:

`y = x² + 3`

### Verifying a Solution

To verify a proposed solution:

1. Differentiate the function as required.
2. Substitute the function and its derivatives into the original equation.
3. Check whether the equation is satisfied.
4. If an initial condition is given, verify it as well.

---

## 1.6 Solution Curves

A **solution curve** is the graph of a particular solution of a differential equation.

Consider the family:

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

### Geometric Interpretation of an Initial Condition

Suppose we require:

`y(0) = 2`

The solution curve must pass through the point (0, 2).

Using:

`y = x² + C`

we obtain:

`2 = 0² + C`

Therefore:

`C = 2`

The required solution curve is:

`y = x² + 2`

Thus, an initial condition selects a particular curve from a family of solution curves.

---

## 1.7 Initial Value Problems

An **initial value problem (IVP)** consists of a differential equation together with a condition specifying the value of the unknown function at a particular point.

For a first-order ODE, an IVP can be written as:

`dy/dx = f(x, y)`

with the initial condition:

`y(x₀) = y₀`

Here:

* x is the independent variable.
* y is the unknown function.
* f(x, y) determines the derivative.
* x₀ is the initial value of the independent variable.
* y₀ is the prescribed value of the function at x₀.

### Example

Solve:

`dy/dx = 2x`

subject to:

`y(1) = 5`

**Step 1: Find the general solution.**

Integrating:

`y = x² + C`

**Step 2: Apply the initial condition.**

`5 = 1² + C`

Therefore:

`C = 4`

**Step 3: State the particular solution.**

`y = x² + 4`

**Step 4: Verify the solution.**

Differentiating:

`dy/dx = 2x`

Checking the initial condition:

`y(1) = 1² + 4 = 5`

Both the differential equation and the initial condition are satisfied.

Therefore, the solution is correct.

---

## 1.8 Important Differences to Remember

| Concept               | Meaning                                                          |
| --------------------- | ---------------------------------------------------------------- |
| Differential equation | An equation involving an unknown function and its derivatives    |
| ODE                   | A differential equation involving ordinary derivatives           |
| PDE                   | A differential equation involving partial derivatives            |
| Order                 | The order of the highest derivative                              |
| Degree                | The exponent of the highest-order derivative, when defined       |
| Linear equation       | An equation that can be expressed in the required linear form    |
| Nonlinear equation    | An equation that cannot be expressed in the required linear form |
| General solution      | A family of solutions, usually containing arbitrary constants    |
| Particular solution   | A specific solution                                              |
| Solution curve        | The graph of a particular solution                               |
| Initial value problem | A differential equation together with an initial condition       |

---

## 1.9 Common Mistakes

1. **Confusing order and degree.**
   Order depends on the highest derivative, while degree depends on its exponent when defined.

2. **Assuming every equation has a defined degree.**
   The degree may be undefined if the equation is not polynomial in its derivatives under the standard definition.

3. **Thinking that every equation containing y² is linear.**
   A term y² makes a first-order equation nonlinear.

4. **Thinking that xy makes an equation nonlinear.**
   The term xy is linear in y because x is a coefficient depending only on the independent variable.

5. **Forgetting the integration constant.**
   Indefinite integration introduces an arbitrary constant.

6. **Confusing general and particular solutions.**
   A general solution represents a family; a particular solution identifies a specific member.

7. **Failing to apply the initial condition.**
   An IVP requires the given condition to be used to determine the constant, when appropriate.

8. **Failing to verify the final answer.**
   A solution should satisfy the original differential equation and any given initial condition.

---

## 1.10 Practice Questions

### Part A: Order and Degree

Determine the order and degree, where defined.

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

Classify each equation as linear or nonlinear. For linear equations, also determine whether it is homogeneous or nonhomogeneous.

**6.**

`dy/dx + 4y = 0`

**7.**

`dy/dx + xy = x²`

**8.**

`dy/dx + y² = 0`

**9.**

`y(dy/dx) = x`

### Part C: Solutions and Solution Curves

**10.** Verify that `y = x² + 7` is a solution of `dy/dx = 2x`.

**11.** Find the general solution of `dy/dx = 4x³`.

**12.** Find the particular solution of `dy/dx = 4x³`, given that `y(1) = 6`.

**13.** For the family `y = x² + C`, determine the value of C that gives the solution curve passing through (0, 5).

**14.** Explain the difference between a general solution and a particular solution in your own words.

---

## 1.11 Answers to Practice Questions

Try the questions before checking these answers.

| Question | Answer                                                                                                             |
| -------- | ------------------------------------------------------------------------------------------------------------------ |
| 1        | Order = 1, Degree = 1                                                                                              |
| 2        | Order = 1, Degree = 4                                                                                              |
| 3        | Order = 2, Degree = 1                                                                                              |
| 4        | Order = 3, Degree = 2                                                                                              |
| 5        | Order = 1, Degree is undefined in the standard sense                                                               |
| 6        | Linear and homogeneous                                                                                             |
| 7        | Linear and nonhomogeneous                                                                                          |
| 8        | Nonlinear                                                                                                          |
| 9        | Nonlinear                                                                                                          |
| 10       | Differentiating gives dy/dx = 2x, so it satisfies the equation.                                                    |
| 11       | y = x⁴ + C                                                                                                         |
| 12       | y = x⁴ + 5                                                                                                         |
| 13       | C = 5                                                                                                              |
| 14       | A general solution represents a family of solutions, while a particular solution identifies one specific solution. |

### Solution to Question 12

Given:

`dy/dx = 4x³`

Integrating:

`y = x⁴ + C`

Using the initial condition `y(1) = 6`:

`6 = 1⁴ + C`

Therefore:

`C = 5`

The particular solution is:

`y = x⁴ + 5`

---

## 1.12 Summary

In this topic, we studied the basic concepts and definitions of differential equations.

The main ideas are:

1. A differential equation involves an unknown function and its derivatives.
2. An ODE involves ordinary derivatives, while a PDE involves partial derivatives.
3. The order is determined by the highest derivative appearing in the equation.
4. The degree is the exponent of the highest-order derivative when the equation is appropriately expressed as a polynomial in its derivatives.
5. A first-order linear ODE can be written as `dy/dx + P(x)y = Q(x)`.
6. A solution is a function that satisfies the differential equation.
7. A general solution represents a family of solutions, while a particular solution identifies a specific solution.
8. A solution curve is the graph of a particular solution.
9. An initial value problem combines a differential equation with an initial condition.
10. Proposed solutions should be verified by substitution and by checking any initial conditions.

These concepts form the foundation for solving first-order differential equations using separable methods, integrating factors, exact equations, and other techniques.

---

## References

Kreyszig, E., Kreyszig, H., & Norminton, E. J. (2011). *Advanced Engineering Mathematics* (10th ed.). John Wiley & Sons. Chapter 1: First-Order ODEs.
