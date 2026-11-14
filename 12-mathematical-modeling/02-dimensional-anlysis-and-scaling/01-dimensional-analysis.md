# Chapter 2: Dimensional Analysis and Scaling
## Part 1: Physical Quantities and Dimensional Analysis

## Table of Contents

1. [Introduction](#1-introduction)
2. [Learning Objectives](#2-learning-objectives)
3. [Physical Quantities](#3-physical-quantities)
4. [Dimensions](#4-dimensions)
5. [Units of Physical Quantities](#5-units-of-physical-quantities)
6. [Fundamental and Derived Physical Quantities](#6-fundamental-and-derived-physical-quantities)
7. [Dimensionless Quantities](#7-dimensionless-quantities)
8. [Dimensional Analysis](#8-dimensional-analysis)
9. [Dimensional Consistency of Equations](#9-dimensional-consistency-of-equations)
10. [Techniques for Checking Dimensional Consistency](#10-techniques-for-checking-dimensional-consistency)
11. [Limitations of Dimensional Analysis](#11-limitations-of-dimensional-analysis)
12. [Summary](#12-summary)
13. [Practice Questions and Solutions](#13-practice-questions-and-solutions)
14. [Conclusion](#14-conclusion)

---

## 1. Introduction

In mathematical modeling, we often describe real-world systems using mathematical equations. These equations may represent physical phenomena such as motion, population growth, fluid flow, temperature changes, and energy consumption.

However, before using a mathematical equation to describe a physical system, we should ask an important question:

**Does the equation make physical sense?**

One way to investigate this is through dimensional analysis.

Dimensional analysis helps us understand the physical nature of quantities and check whether mathematical equations are dimensionally consistent.

Before studying dimensional analysis, we need to understand physical quantities, dimensions, and units.

## 2. Learning Objectives

After studying this section, you should be able to:

- Define physical quantities, dimensions, and units.
- Distinguish between dimensions and units.
- Identify fundamental and derived physical quantities.
- Express derived quantities in terms of fundamental dimensions.
- Identify dimensionless quantities.
- Explain dimensional analysis.
- Check the dimensional consistency of mathematical equations.
- Recognize the limitations of dimensional analysis.

---

## 3. Physical Quantities

### 3.1 Definition

A **physical quantity** is a measurable property of an object, substance, or physical phenomenon.

In simple terms, if something can be measured and expressed numerically with an appropriate unit, it is a physical quantity.

Examples include:

- Length
- Mass
- Time
- Temperature
- Speed
- Acceleration
- Force
- Energy

A physical quantity is generally expressed as:

**Physical quantity = Numerical value × Unit**

For example:

If the length of a table is 2 meters:

- Numerical value = 2
- Unit = meter (m)
- Physical quantity = 2 m

The numerical value tells us how much of the quantity we have, while the unit tells us the measurement standard being used.

### 3.2 Examples

| Physical Quantity | Numerical Value | Unit |
|---|---:|---|
| Length | 5 | meter (m) |
| Mass | 10 | kilogram (kg) |
| Time | 20 | second (s) |
| Temperature | 30 | kelvin (K) |
| Speed | 15 | meter per second (m/s) |

---

## 4. Dimensions

### 4.1 What Is a Dimension?

A **dimension** describes the physical nature of a quantity in terms of fundamental physical quantities.

It tells us what kind of physical quantity we are dealing with, independently of the units used to measure it.

For example:

- Length has dimension L.
- Mass has dimension M.
- Time has dimension T.

Some quantities are combinations of these fundamental quantities.

For example, speed is defined as:

Speed = Distance / Time

Therefore, its dimension is:

Dimension of speed = L / T

Or:

**[Speed] = LT⁻¹**

Here, the square brackets indicate the dimension of a physical quantity.

### 4.2 Common Dimension Symbols

| Fundamental Quantity | Dimension Symbol |
|---|---|
| Length | L |
| Mass | M |
| Time | T |
| Electric current | I |
| Thermodynamic temperature | Θ |
| Amount of substance | N |
| Luminous intensity | J |

These symbols are used to express the dimensions of physical quantities.

### 4.3 Examples of Dimensions

| Physical Quantity | Definition | Dimension |
|---|---|---|
| Length | — | L |
| Area | Length × Length | L² |
| Volume | Length × Length × Length | L³ |
| Speed | Distance / Time | LT⁻¹ |
| Acceleration | Speed / Time | LT⁻² |
| Density | Mass / Volume | ML⁻³ |
| Momentum | Mass × Speed | MLT⁻¹ |
| Force | Mass × Acceleration | MLT⁻² |

### 4.4 Deriving Dimensions: Step by Step

We can obtain the dimension of a derived physical quantity by expressing its definition in terms of fundamental quantities.

**Example 1: Density**

Density is defined as:

Density = Mass / Volume

We know:

- Dimension of mass = M
- Dimension of volume = L³

Therefore:

[Density] = M / L³

**[Density] = ML⁻³**

**Example 2: Force**

According to Newton's second law:

Force = Mass × Acceleration

We know:

- Dimension of mass = M
- Dimension of acceleration = LT⁻²

Therefore:

[Force] = M × LT⁻²

**[Force] = MLT⁻²**

**Example 3: Pressure**

Pressure is defined as:

Pressure = Force / Area

We know:

- Dimension of force = MLT⁻²
- Dimension of area = L²

Therefore:

[Pressure] = MLT⁻² / L²

**[Pressure] = ML⁻¹T⁻²**

**Example 4: Work or Energy**

Work is defined as:

Work = Force × Distance

We know:

- Dimension of force = MLT⁻²
- Dimension of distance = L

Therefore:

[Work] = MLT⁻² × L

**[Work] = ML²T⁻²**

**Example 5: Power**

Power is defined as:

Power = Work / Time

We know:

- Dimension of work = ML²T⁻²
- Dimension of time = T

Therefore:

[Power] = ML²T⁻² / T

**[Power] = ML²T⁻³**

The important idea is that we do not need to memorize every derived dimension. We can calculate it from the definition of the physical quantity.

---

## 5. Units of Physical Quantities

### 5.1 What Is a Unit?

A **unit** is a standard reference used to measure a physical quantity.

For example:

- Meter is a unit of length.
- Kilogram is a unit of mass.
- Second is a unit of time.

Units allow different people to measure and communicate physical quantities using a common standard.

### 5.2 The SI System

The International System of Units (SI) is the internationally accepted system of measurement.

It provides standard units for physical quantities.

For example:

| Physical Quantity | SI Unit | Symbol |
|---|---|---|
| Length | Meter | m |
| Mass | Kilogram | kg |
| Time | Second | s |
| Temperature | Kelvin | K |
| Electric current | Ampere | A |

### 5.3 Difference Between Dimension and Unit

Dimension and unit are related, but they are not the same.

Consider length:

- Its dimension is L.
- Its SI unit is meter (m).

The dimension describes the physical nature of the quantity, while the unit provides a standard for measuring it.

For example, length can be measured in meters, centimeters, or kilometers, but its dimension remains L.

| Quantity | Dimension | SI Unit |
|---|---|---|
| Length | L | m |
| Mass | M | kg |
| Time | T | s |
| Speed | LT⁻¹ | m/s |
| Force | MLT⁻² | kg·m/s² |

**Remember:** Changing the unit does not change the dimension of a physical quantity.

---

## 6. Fundamental and Derived Physical Quantities

Physical quantities can be classified into two major groups:

1. Fundamental physical quantities.
2. Derived physical quantities.

### 6.1 Fundamental Physical Quantities

Fundamental physical quantities are independent quantities that are not defined in terms of other physical quantities within a chosen system of measurement.

In the SI system, there are seven fundamental physical quantities.

| No. | Fundamental Quantity | Dimension Symbol | SI Unit | Unit Symbol |
|---:|---|---|---|---|
| 1 | Length | L | Meter | m |
| 2 | Mass | M | Kilogram | kg |
| 3 | Time | T | Second | s |
| 4 | Electric current | I | Ampere | A |
| 5 | Thermodynamic temperature | Θ | Kelvin | K |
| 6 | Amount of substance | N | Mole | mol |
| 7 | Luminous intensity | J | Candela | cd |

These seven quantities form the foundation for expressing other physical quantities.

### 6.2 Derived Physical Quantities

Derived physical quantities are quantities that can be expressed in terms of fundamental physical quantities.

For example:

Speed = Distance / Time

Since distance and time are fundamental quantities, speed is a derived quantity.

Similarly, force is derived from mass and acceleration.

### 6.3 Common Derived Quantities, Dimensions, and SI Units

| Derived Quantity | Dimension | SI Unit | Unit Symbol |
|---|---|---|---|
| Area | L² | Square meter | m² |
| Volume | L³ | Cubic meter | m³ |
| Density | ML⁻³ | Kilogram per cubic meter | kg/m³ |
| Speed | LT⁻¹ | Meter per second | m/s |
| Acceleration | LT⁻² | Meter per second squared | m/s² |
| Momentum | MLT⁻¹ | Kilogram meter per second | kg·m/s |
| Force | MLT⁻² | Newton | N |
| Pressure | ML⁻¹T⁻² | Pascal | Pa |
| Work/Energy | ML²T⁻² | Joule | J |
| Power | ML²T⁻³ | Watt | W |
| Frequency | T⁻¹ | Hertz | Hz |
| Electric charge | IT | Coulomb | C |
| Electric potential | ML²T⁻³I⁻¹ | Volt | V |
| Electrical resistance | ML²T⁻³I⁻² | Ohm | Ω |

**Important:** A derived quantity is not necessarily expressed using a special named unit. For example, speed has the SI unit m/s, while force has the special SI unit newton (N).

---

## 7. Dimensionless Quantities

### 7.1 What Is a Dimensionless Quantity?

A **dimensionless quantity** is a physical quantity whose dimensions cancel out completely.

Its dimensional formula is equal to 1.

In other words, all the exponents of the fundamental dimensions are zero.

For example, consider strain:

Strain = Change in length / Original length

Both the numerator and denominator have dimension L.

Therefore:

[Strain] = L / L = 1

Strain is dimensionless.

### 7.2 Examples of Dimensionless Quantities

| Quantity | Definition | Dimension |
|---|---|---|
| Strain | Change in length / Original length | 1 |
| Refractive index | Speed of light in vacuum / Speed in medium | 1 |
| Relative density | Density of substance / Density of reference | 1 |
| Coefficient of friction | Frictional force / Normal force | 1 |
| Probability | — | 1 |
| Ratio of two lengths | Length / Length | 1 |

### 7.3 Why Are Dimensionless Quantities Important?

Dimensionless quantities are useful because they allow us to compare physical systems without depending on their measurement units.

For example, consider two objects:

- Object A has a length of 2 meters.
- Object B has a length of 4 meters.

The ratio of their lengths is:

Ratio = 4 / 2 = 2

The result is dimensionless because the units cancel.

Dimensionless quantities are particularly important in mathematical modeling, where they help simplify relationships between physical variables.

### 7.4 Important Note: Dimensionless Does Not Mean Zero

A dimensionless quantity is not necessarily equal to zero.

For example:

- Strain can be 0.05.
- A probability can be 0.7.
- A refractive index can be 1.5.

These quantities have no dimensions, but they can have nonzero numerical values.

**Another important example: Plane Angle**

A plane angle is defined as:

Angle = Arc length / Radius

Both arc length and radius have dimension L.

Therefore:

[Angle] = L / L = 1

Thus, a plane angle is dimensionless, even though its SI unit is the radian (rad).

---

## 8. Dimensional Analysis

### 8.1 Definition

**Dimensional analysis** is a mathematical technique that uses the dimensions of physical quantities to study relationships between them and check the consistency of physical equations.

It helps us determine whether an equation is physically meaningful from the perspective of dimensions.

### 8.2 Why Do We Need Dimensional Analysis?

Suppose someone gives us the following equation:

Distance = Speed × Time

We know that:

- Distance has dimension L.
- Speed has dimension LT⁻¹.
- Time has dimension T.

Therefore:

[Speed × Time] = LT⁻¹ × T

= L

The dimensions on both sides are equal.

This tells us that the equation is dimensionally consistent.

Now suppose someone gives us:

Distance = Speed + Time

The dimensions on the right side are:

LT⁻¹ + T

These quantities have different dimensions.

Adding them is physically meaningless.

Therefore, dimensional analysis helps us identify equations that cannot be correct because of dimensional inconsistencies.

---

## 9. Dimensional Consistency of Equations

### 9.1 Principle of Dimensional Homogeneity

A physical equation is dimensionally consistent if every term being added or subtracted has the same dimensions, and the dimensions of the left-hand side equal the dimensions of the right-hand side.

This principle is known as **dimensional homogeneity**.

In simple terms:

**All terms in a physically meaningful equation must have compatible dimensions.**

For example, consider:

s = ut + ½at²

Where:

- s = displacement
- u = initial velocity
- a = acceleration
- t = time

We know:

- [s] = L
- [u] = LT⁻¹
- [a] = LT⁻²
- [t] = T

Now examine each term on the right-hand side.

First term:

[ut] = LT⁻¹ × T = L

Second term:

[at²] = LT⁻² × T² = L

The numerical constant ½ has no dimensions.

Therefore:

[s] = [ut] = [at²] = L

The equation is dimensionally consistent.

### 9.2 Addition and Subtraction Rules

Physical quantities can only be added or subtracted if they have the same dimensions.

For example:

- Length + Length: Allowed.
- Speed + Speed: Allowed.
- Length + Time: Not allowed.
- Mass + Acceleration: Not allowed.

Consider:

5 meters + 3 seconds

This expression has no meaningful physical interpretation because length and time are different types of physical quantities.

However:

5 meters + 3 meters = 8 meters

This is meaningful.

### 9.3 Another Example

Consider the equation:

s = ut + at

Check whether it is dimensionally consistent.

Left-hand side:

[s] = L

First term on the right:

[ut] = LT⁻¹ × T = L

Second term on the right:

[at] = LT⁻² × T = LT⁻¹

The dimensions of the two terms on the right are different:

- [ut] = L
- [at] = LT⁻¹

Therefore, the terms cannot be added.

**Conclusion:** The equation is dimensionally inconsistent.

---

## 10. Techniques for Checking Dimensional Consistency

There are two convenient ways to check the dimensional consistency of physical equations:

1. Using fundamental dimensions.
2. Using SI base units.

Both methods follow the same principle. The difference is simply how we represent the quantities.

### 10.1 Method 1: Using Fundamental Dimensions

In this method, we express each physical quantity using fundamental dimensions such as M, L, and T.

**Example: Check the equation**

v = u + at

Where:

- v = final velocity
- u = initial velocity
- a = acceleration
- t = time

Step 1: Identify the dimensions.

[v] = LT⁻¹

[u] = LT⁻¹

[a] = LT⁻²

[t] = T

Step 2: Calculate the dimensions of each term.

[at] = LT⁻² × T

= LT⁻¹

Step 3: Compare the dimensions.

Left-hand side:

[v] = LT⁻¹

Right-hand side:

[u] + [at]

Both terms have dimension LT⁻¹.

Therefore, the equation is dimensionally consistent.

### 10.2 Method 2: Using SI Base Units

In this method, we express each physical quantity in terms of SI base units such as kg, m, and s.

**Example: Check the equation**

F = ma

Where:

- F = force
- m = mass
- a = acceleration

Step 1: Write the SI units.

Force = kg·m/s²

Mass = kg

Acceleration = m/s²

Step 2: Calculate the units on the right-hand side.

ma = kg × m/s²

= kg·m/s²

Step 3: Compare both sides.

Left-hand side:

F = kg·m/s²

Right-hand side:

ma = kg·m/s²

Both sides have the same SI base units.

Therefore, the equation is dimensionally consistent.

### 10.3 Another Example Using SI Base Units

Check the equation:

KE = ½mv²

Where:

- KE = kinetic energy
- m = mass
- v = velocity

Step 1: Write the SI units.

Kinetic energy = kg·m²/s²

Mass = kg

Velocity = m/s

Step 2: Calculate the units on the right-hand side.

½mv² = ½ × kg × (m/s)²

= kg·m²/s²

Step 3: Compare both sides.

Both sides have the same SI base units.

Therefore, the equation is dimensionally consistent.

### 10.4 Comparing the Two Methods

| Method | What We Use | Example |
|---|---|---|
| Fundamental dimensions | M, L, T, I, etc. | [F] = MLT⁻² |
| SI base units | kg, m, s, A, etc. | F = kg·m/s² |

Both methods are valid.

**Recommendation:** Use fundamental dimensions when studying the theoretical structure of equations. Use SI base units when you want to verify the units directly.

---

## 11. Limitations of Dimensional Analysis

Dimensional analysis is useful, but it does not prove that an equation is completely correct.

It has several limitations.

### 11.1 It Cannot Determine Numerical Constants

Consider the two equations:

s = ut + ½at²

s = ut + 7at²

Both equations are dimensionally consistent because numerical constants such as ½ and 7 have no dimensions.

Dimensional analysis alone cannot determine which numerical constant is correct.

### 11.2 Dimensional Consistency Does Not Guarantee Correctness

An equation may be dimensionally consistent but still describe the physical system incorrectly.

For example, dimensional analysis cannot determine whether the assumptions behind a model are reasonable.

### 11.3 Different Quantities Can Have the Same Dimensions

Some different physical quantities share the same dimensions.

For example:

- Work has dimension ML²T⁻².
- Torque also has dimension ML²T⁻².

Although their dimensions are identical, they represent different physical concepts.

Therefore, dimensional analysis cannot always distinguish between different physical quantities.

### 11.4 It Cannot Determine Every Mathematical Relationship

Dimensional analysis can help investigate relationships between physical quantities, but it cannot always determine the exact mathematical form of an equation.

Additional physical knowledge, experiments, and mathematical reasoning may be necessary.

**Main lesson:** Dimensional consistency is a necessary check for a physically meaningful equation, but it is not sufficient to establish that the equation is correct.

---

## 12. Summary

### 12.1 Important Definitions

| Concept | Meaning |
|---|---|
| Physical quantity | A measurable property of an object or phenomenon |
| Dimension | The physical nature of a quantity expressed using fundamental quantities |
| Unit | A standard used to measure a physical quantity |
| Fundamental quantity | An independent physical quantity |
| Derived quantity | A quantity expressed in terms of fundamental quantities |
| Dimensionless quantity | A quantity whose dimensions cancel completely |
| Dimensional analysis | A technique that uses dimensions to study physical relationships and check equations |
| Dimensional homogeneity | The principle that all terms in a physical equation must have compatible dimensions |

### 12.2 Fundamental Dimensions

| Quantity | Dimension |
|---|---|
| Length | L |
| Mass | M |
| Time | T |
| Electric current | I |
| Temperature | Θ |
| Amount of substance | N |
| Luminous intensity | J |

### 12.3 Important Derived Dimensions

| Quantity | Dimension |
|---|---|
| Area | L² |
| Volume | L³ |
| Density | ML⁻³ |
| Speed | LT⁻¹ |
| Acceleration | LT⁻² |
| Momentum | MLT⁻¹ |
| Force | MLT⁻² |
| Pressure | ML⁻¹T⁻² |
| Work/Energy | ML²T⁻² |
| Power | ML²T⁻³ |
| Frequency | T⁻¹ |

### 12.4 Key Rules to Remember

1. A physical quantity consists of a numerical value and a unit.
2. Dimensions describe the physical nature of quantities.
3. Units provide standards for measurement.
4. Derived quantities can be expressed using fundamental quantities.
5. Dimensionless quantities have no fundamental dimensions.
6. Terms being added or subtracted must have the same dimensions.
7. The dimensions of both sides of a dimensionally consistent equation must be equal.
8. Dimensional consistency does not guarantee that an equation is physically correct.

---

## 13. Practice Questions and Solutions

### Question 1: Basic Concepts

Explain the difference between a physical quantity, dimension, and unit.

**Solution:**

- A physical quantity is a measurable property.
- A dimension describes its physical nature.
- A unit is the standard used to measure it.

For example, for length:

- Physical quantity: Length
- Dimension: L
- SI unit: Meter (m)

### Question 2: Deriving Dimensions

Find the dimensions of gravitational constant G using Newton's law of gravitation:

F = Gm₁m₂/r²

**Solution:**

Rearrange the equation:

G = Fr²/(m₁m₂)

Now express the dimensions:

[G] = [F][r]²/([m₁][m₂])

We know:

[F] = MLT⁻²

[r] = L

[m₁] = M

[m₂] = M

Substitute:

[G] = (MLT⁻² × L²)/(M × M)

[G] = ML³T⁻²/M²

**[G] = M⁻¹L³T⁻²**

### Question 3: Checking Dimensional Consistency

Check whether the following equation is dimensionally consistent:

v² = u² + 2as

**Solution:**

We know:

[v] = LT⁻¹

[u] = LT⁻¹

[a] = LT⁻²

[s] = L

Left-hand side:

[v²] = (LT⁻¹)²

= L²T⁻²

Right-hand side:

[u²] = L²T⁻²

[as] = LT⁻² × L

= L²T⁻²

Both terms on the right have dimension L²T⁻².

Therefore:

**The equation is dimensionally consistent.**

### Question 4: Identify the Incorrect Equation

Which of the following equations is dimensionally inconsistent?

A. v = u + at

B. F = ma

C. s = ut + ½at³

**Solution:**

Check each equation.

**A. v = u + at**

- [v] = LT⁻¹
- [u] = LT⁻¹
- [at] = LT⁻² × T = LT⁻¹

Consistent.

**B. F = ma**

- [F] = MLT⁻²
- [ma] = M × LT⁻² = MLT⁻²

Consistent.

**C. s = ut + ½at³**

- [s] = L
- [ut] = L
- [at³] = LT⁻² × T³ = LT

The terms on the right do not have the same dimensions as each other or the left-hand side.

**Answer: C is dimensionally inconsistent.**

### Question 5: Conceptual Understanding

Can two different physical quantities have the same dimensions? Explain with an example.

**Solution:**

Yes.

For example, work and torque have the same dimensions:

ML²T⁻²

However, they represent different physical concepts.

This shows that dimensional analysis cannot always distinguish between different physical quantities.

---

## 14. Conclusion

In this part of Chapter 2, we studied the foundations of dimensional analysis.

We began with physical quantities, dimensions, and units, then explored fundamental and derived quantities. We also learned about dimensionless quantities and how dimensional analysis helps us check the consistency of physical equations.

The most important idea is that mathematical equations used to represent physical systems must respect the dimensions of the quantities involved.

Dimensional analysis provides a simple but powerful way to check this requirement.

In the next part of this chapter, we will study **Scaling**, which helps us understand how physical systems and their mathematical models behave when their characteristic sizes or quantities change.

---

### References

Course material: Chapter 2 — Dimensional Analysis and Scaling.
