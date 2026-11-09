# Chapter 2: Probability Spaces — Review
## Part 1: Foundations of Probability Spaces

---

## Table of Contents

1. [Learning Objectives](#1-learning-objectives)
2. [Introduction to Probability](#2-introduction-to-probability)
3. [Discrete Probability Spaces](#3-discrete-probability-spaces)
4. [Properties of Discrete Probability Measures](#4-properties-of-discrete-probability-measures)
5. [The Sigma-Field (Algebra) of Events](#5-the-sigma-field-algebra-of-events)
6. [Examples of Sigma-Algebras](#6-examples-of-sigma-algebras)
7. [General Probability Spaces](#7-general-probability-spaces)
8. [Properties of General Probability Measures](#8-properties-of-general-probability-measures)
9. [Conditional Probability](#9-conditional-probability)
10. [Multiplication Rule for Conditional Probabilities](#10-multiplication-rule-for-conditional-probabilities)
11. [Total Probability Law](#11-total-probability-law)
12. [Independence of Events](#12-independence-of-events)
13. [Practical Applications](#13-practical-applications)
14. [Common Mistakes and Important Observations](#14-common-mistakes-and-important-observations)
15. [Formula Summary](#15-formula-summary)
16. [Practice Questions with Solutions](#16-practice-questions-with-solutions)
17. [Conclusion](#17-conclusion)

---

# 1. Learning Objectives

After completing this section, you should be able to:

- Explain the concepts of experiments, outcomes, sample spaces, and events.
- Construct discrete probability spaces and calculate event probabilities.
- State and apply the fundamental properties of probability.
- Define a sigma-field and verify whether a collection of sets is a sigma-field.
- Explain the difference between discrete and general probability spaces.
- Define a probability measure and identify its fundamental properties.
- Apply the addition, difference, and complement rules.
- Calculate conditional probabilities.
- Apply the multiplication rule for conditional probabilities.
- Identify partitions and use the total probability law.
- Determine whether two events are independent.

---

# 2. Introduction to Probability

## 2.1 What Is Probability?

Probability is a mathematical concept used to measure the likelihood that an uncertain event will occur.

It provides a numerical description of uncertainty.

For example, consider tossing a fair coin. There are two possible outcomes:

- Heads (H)
- Tails (T)

Since the coin is fair, both outcomes are equally likely:

P(H) = 1/2

P(T) = 1/2

The probability of an event ranges from 0 to 1:

- 0 means the event is impossible.
- 1 means the event is certain.
- A value between 0 and 1 represents uncertainty.

## 2.2 Basic Terminologies

Before constructing probability spaces, we need to understand four fundamental concepts.

### A. Random Experiment

A random experiment is a process that produces an outcome whose exact result cannot be predicted with certainty before the experiment is performed.

Examples:

- Tossing a coin.
- Rolling a die.
- Selecting a customer randomly.
- Observing the daily return of a financial asset.

### B. Outcome

An outcome is a single possible result of a random experiment.

For example, when rolling a die, obtaining 4 is one possible outcome.

### C. Sample Space

The sample space is the set of all possible outcomes of a random experiment.

It is usually denoted by the Greek letter Omega (Ω).

Examples:

**One coin toss:**

Ω = {H, T}

**One die roll:**

Ω = {1, 2, 3, 4, 5, 6}

**Two coin tosses:**

Ω = {HH, HT, TH, TT}

### D. Event

An event is a subset of the sample space. It represents one or more outcomes of interest.

For example, when rolling a die:

Ω = {1, 2, 3, 4, 5, 6}

Let A be the event of obtaining an even number:

A = {2, 4, 6}

An event occurs if the experimental outcome belongs to that event.

Mathematically:

A ⊆ Ω

**Important distinction:**

- Sample space: All possible outcomes.
- Event: A particular outcome or collection of outcomes.

---

# 3. Discrete Probability Spaces

## 3.1 Definition

A discrete sample space is a sample space whose outcomes can be listed individually. It may contain finitely many or countably infinitely many outcomes.

For example:

Ω = {1, 2, 3, 4, 5, 6}

is a finite sample space.

Meanwhile:

Ω = {1, 2, 3, 4, ...}

is a countably infinite sample space.

## 3.2 Probability Distribution

Let the sample space be:

Ω = {ω₁, ω₂, ...}

Assign a probability pₙ to each outcome ωₙ.

The sequence:

(p₁, p₂, p₃, ...)

is called the probability vector or probability distribution of the experiment.

The probabilities must satisfy two conditions:

**Condition 1: Non-negativity and upper bound**

0 ≤ pₙ ≤ 1

**Condition 2: Total probability equals one**

Σ pₙ = 1, for all ωₙ ∈ Ω.

The first condition ensures that every outcome has a valid probability. The second ensures that the probabilities of all possible outcomes account for the entire experiment.

## 3.3 Probability of an Event

The probability of an event A is obtained by adding the probabilities of all outcomes belonging to A.

The formula is:

P(A) = Σ pₙ, for ωₙ ∈ A

If A is empty, the sum is defined to be zero:

P(∅) = 0

The function P is called a probability measure for the experiment.

The pair (Ω, P) is called a **discrete probability space**.

## 3.4 Worked Example: Rolling a Fair Die

Suppose a fair six-sided die is rolled once.

**Step 1: Identify the sample space.**

Ω = {1, 2, 3, 4, 5, 6}

**Step 2: Assign probabilities to outcomes.**

Since the die is fair, each outcome has probability:

pₙ = 1/6

Check the probability conditions:

0 ≤ 1/6 ≤ 1

Σ pₙ = 6 × (1/6) = 1

Therefore, the probability distribution is valid.

**Step 3: Define the event.**

Let A be the event of obtaining an even number:

A = {2, 4, 6}

**Step 4: Calculate its probability.**

P(A) = P(2) + P(4) + P(6)

P(A) = 1/6 + 1/6 + 1/6

**Answer:**

P(A) = 1/2

Therefore, the probability of obtaining an even number is 0.5 or 50%.

---

# 4. Properties of Discrete Probability Measures

A discrete probability measure satisfies three fundamental properties.

## Property 1: Probability Bounds

For every event A:

0 ≤ P(A) ≤ 1

The probability of an event cannot be negative or greater than one.

## Property 2: Empty Set and Sample Space

P(∅) = 0

P(Ω) = 1

The empty set represents an impossible event, while the sample space represents a certain event.

## Property 3: Additive Property of Probability

If A₁, A₂, ... is a finite or infinite sequence of pairwise disjoint events, then:

P(∪ Aₙ) = Σ P(Aₙ)

This property is called **countable additivity**.

### Understanding Disjoint Events

Two events are disjoint if they cannot occur simultaneously.

Mathematically:

A ∩ B = ∅

For example, when rolling one die:

A = {1, 3, 5}

B = {2, 4, 6}

Since the two events have no common outcomes, they are disjoint.

Therefore:

P(A ∪ B) = P(A) + P(B)

### Worked Example

For a fair die, calculate the probability of obtaining an odd or even number.

Let:

A = {1, 3, 5}

B = {2, 4, 6}

Then:

P(A) = 3/6 = 1/2

P(B) = 3/6 = 1/2

Since A and B are disjoint:

P(A ∪ B) = P(A) + P(B)

P(A ∪ B) = 1/2 + 1/2

**Answer:**

P(A ∪ B) = 1

This is expected because every possible die outcome is either odd or even.

---

# 5. The Sigma-Field (Algebra) of Events

## 5.1 Why Do We Need a Sigma-Field?

In probability theory, we need to specify which subsets of a sample space are considered measurable events.

For finite sample spaces, we can often use all subsets. However, for more general sample spaces, particularly uncountable ones, we need a carefully defined collection of events.

This collection is called a sigma-field.

## 5.2 Definition of a Sigma-Field

Let Ω be a sample space.

A collection F of subsets of Ω is called a **sigma-field (or sigma-algebra)** if it satisfies the following three properties:

### Property 1: Contains the Empty Set and Sample Space

∅, Ω ∈ F

The impossible event and the sure event must belong to every sigma-field.

### Property 2: Closed Under Complements

If A ∈ F, then A′ ∈ F.

Here, A′ represents the complement of A:

A′ = Ω − A

The complement contains all outcomes that do not belong to A.

For example:

Ω = {1, 2, 3, 4, 5, 6}

A = {2, 4, 6}

Then:

A′ = {1, 3, 5}

If A belongs to the sigma-field, its complement must also belong to it.

### Property 3: Closed Under Countable Unions

If A₁, A₂, ... belong to F, then:

∪ Aₙ ∈ F

This means that the union of any finite or countably infinite collection of events in F must also belong to F.

### Important Consequence: Closure Under Countable Intersections

A sigma-field is also closed under countable intersections.

By De Morgan's law:

∩ Aₙ = (∪ Aₙ′)′

Since a sigma-field is closed under complements and countable unions, it must also be closed under countable intersections.

## 5.3 Events in a Sigma-Field

The members of F are called events.

Therefore:

A is an event if and only if A ∈ F.

**Important:** In a general probability space, not every subset of Ω must necessarily be an event. Only the subsets belonging to F are considered events.

---

# 6. Examples of Sigma-Algebras

## Example 1: The Trivial Sigma-Field

The collection:

F = {∅, Ω}

is called the trivial sigma-field.

It contains only two events:

1. The impossible event.
2. The sure event.

It satisfies all three sigma-field conditions:

- It contains ∅ and Ω.
- The complement of each member is also included.
- The union of any collection of its members is either ∅ or Ω.

Therefore, it is a sigma-field.

## Example 2: Sigma-Field Generated by a Partition

### Understanding a Partition

A partition of a nonempty sample space Ω is a collection of nonempty, pairwise disjoint subsets whose union is the entire sample space.

Suppose:

Ω = {1, 2, 3, 4}

Consider the collection:

P = {{1, 2}, {3, 4}}

The two subsets:

- Do not overlap.
- Together contain every outcome in Ω.

Therefore, P is a partition of Ω.

### Constructing the Sigma-Field

The collection consisting of the empty set and all possible unions of members of P is a sigma-field.

Thus:

F = {∅, {1, 2}, {3, 4}, Ω}

This collection contains:

- The empty union: ∅
- The first partition member: {1, 2}
- The second partition member: {3, 4}
- The union of both members: Ω

Therefore, it forms a sigma-field.

**Key idea:** A partition divides the sample space into non-overlapping groups. The sigma-field generated by that partition contains all possible unions of those groups.

## Example 3: Sigma-Field Generated by a Collection

Let A be a collection of subsets of Ω.

In general, many sigma-fields may contain A. For example, the power set P(Ω), which contains every subset of Ω, is a sigma-field containing A.

The intersection of all sigma-fields containing A is itself a sigma-field containing A.

This is called the **sigma-field generated by A** and is denoted by:

σ(A)

It is the smallest sigma-field containing the original collection A.

### Borel Sigma-Field

If Ω is an interval of real numbers and A is the collection of all subintervals of Ω, then:

σ(A)

is called the **Borel sigma-field** of Ω.

Its members are called Borel sets.

For this chapter, the essential idea is that the Borel sigma-field provides a standard collection of measurable subsets of intervals in the real numbers.

---

# 7. General Probability Spaces

## 7.1 Motivation

A discrete probability space is useful when outcomes can be listed individually.

However, some experiments have uncountably many possible outcomes.

For example, consider measuring the exact waiting time of a customer at a bank.

The waiting time could be:

0.5 minutes, 1.25 minutes, 2.73 minutes, 4.816 minutes, and so on.

The possible values may form a continuous interval rather than a list of separate outcomes.

To handle such experiments, we use a more general mathematical framework.

## 7.2 Probability Measure

Let Ω be a sample space and F be a sigma-field of events.

A probability measure P is a function that assigns a number P(A) to every event A ∈ F.

It must satisfy the following three axioms:

### Axiom 1: Probability Bounds

0 ≤ P(A) ≤ 1

### Axiom 2: Probability of Impossible and Sure Events

P(∅) = 0

P(Ω) = 1

### Axiom 3: Countable Additivity

For any finite or countably infinite sequence of pairwise disjoint events A₁, A₂, ...:

P(∪ Aₙ) = Σ P(Aₙ)

These three conditions are the fundamental axioms of probability.

## 7.3 Definition of a General Probability Space

A general probability space consists of three mathematical objects:

(Ω, F, P)

Where:

- Ω = Sample space: The collection of all possible outcomes.
- F = Sigma-field: The collection of measurable events.
- P = Probability measure: The function assigning probabilities to events.

Therefore:

**A probability space is the mathematical structure (Ω, F, P).**

### Understanding the Relationship

Consider an experiment involving the return of a financial investment.

1. Ω describes all possible outcomes of the investment return.
2. F identifies the measurable events, such as the return being positive or exceeding a specified value.
3. P assigns probabilities to those events.

Together, these three components form a probability space.

## 7.4 Mutually Exclusive Events

A collection of events is called mutually exclusive if every pair of distinct events has an intersection of probability zero.

For two events A and B:

P(A ∩ B) = 0

For example, when tossing a coin:

A = {Heads}

B = {Tails}

The events cannot occur simultaneously.

Therefore:

P(A ∩ B) = 0

**Note:** In general probability spaces, mutually exclusive events may have an intersection that is nonempty but has probability zero. Thus, mutually exclusive is formally expressed using probability zero.

---

# 8. Properties of General Probability Measures

A probability measure has several useful properties that follow from its three fundamental axioms.

## Property 1: Addition Rule

For any two events A and B:

P(A ∪ B) = P(A) + P(B) − P(A ∩ B)

### Derivation

When adding P(A) and P(B), the outcomes belonging to both events are counted twice.

Therefore, subtract the intersection once:

P(A ∪ B) = P(A) + P(B) − P(A ∩ B)

### Worked Example

Suppose:

P(A) = 0.60

P(B) = 0.50

P(A ∩ B) = 0.30

Find P(A ∪ B).

Using the addition rule:

P(A ∪ B) = 0.60 + 0.50 − 0.30

**Answer:**

P(A ∪ B) = 0.80

Therefore, the probability that at least one of the events occurs is 80%.

### Special Case: Disjoint Events

If A and B are disjoint:

P(A ∩ B) = 0

Therefore:

P(A ∪ B) = P(A) + P(B)

## Property 2: Difference of Events

If B ⊆ A, then:

P(A − B) = P(A) − P(B)

### Explanation

Since B is contained in A, removing B from A leaves only the outcomes belonging to A but not B.

The probability of the remaining event is obtained by subtracting P(B) from P(A).

### Worked Example

Suppose:

P(A) = 0.80

P(B) = 0.30

and B ⊆ A.

Find P(A − B).

P(A − B) = P(A) − P(B)

P(A − B) = 0.80 − 0.30

**Answer:**

P(A − B) = 0.50

### Important Consequence

If B ⊆ A, then:

P(B) ≤ P(A)

A subset cannot have a greater probability than the set containing it.

## Property 3: Complement Rule

For any event A:

P(A′) = 1 − P(A)

### Derivation

An event and its complement are disjoint, and their union is the entire sample space:

A ∪ A′ = Ω

A ∩ A′ = ∅

Using the addition rule:

P(A ∪ A′) = P(A) + P(A′)

Since P(Ω) = 1:

1 = P(A) + P(A′)

Rearranging:

P(A′) = 1 − P(A)

### Worked Example

Suppose the probability that a customer repays a loan is 0.85.

Find the probability that the customer does not repay.

Let A represent the event that the customer repays the loan.

Then:

P(A′) = 1 − P(A)

P(A′) = 1 − 0.85

**Answer:**

P(A′) = 0.15

There is a 15% probability that the customer does not repay the loan.

---

# 9. Conditional Probability

## 9.1 Definition

Conditional probability is the probability of an event occurring when we already know that another event has occurred.

It is denoted by:

P(A | B)

Read this as:

"Probability of A given B."

If P(B) > 0, the conditional probability of A given B is:

P(A | B) = P(A ∩ B) / P(B)

Where:

- P(A | B) = Probability of A given B.
- P(A ∩ B) = Probability that both A and B occur.
- P(B) = Probability that B occurs.

### Intuition

Suppose a university has 100 students:

- 60 study Mathematics.
- 40 study Statistics.
- 25 study both subjects.

We randomly select one student.

Let:

A = Student studies Mathematics.

B = Student studies Statistics.

Suppose we are told that the selected student studies Statistics.

We no longer consider all 100 students. We only consider the 40 Statistics students.

Among those 40 students, 25 also study Mathematics.

Therefore:

P(A | B) = 25/40

**Answer:**

P(A | B) = 0.625

The probability that a student studies Mathematics, given that the student studies Statistics, is 62.5%.

### Important Observation

Ordinary probability considers the entire sample space, while conditional probability considers a restricted group.

In general:

P(A | B) ≠ P(A)

Additional information can change the probability of an event.

---

# 10. Multiplication Rule for Conditional Probabilities

## 10.1 Multiplication Rule for Two Events

Starting from the definition of conditional probability:

P(B | A) = P(A ∩ B) / P(A)

provided P(A) > 0.

Multiplying both sides by P(A):

P(A ∩ B) = P(A) × P(B | A)

Therefore:

**Multiplication Rule:**

P(A ∩ B) = P(A)P(B | A)

The probability that both events occur equals the probability of the first event multiplied by the conditional probability of the second event given the first.

## 10.2 Worked Example

Suppose:

P(A) = 0.40

P(B | A) = 0.70

Find the probability that both A and B occur.

Using the multiplication rule:

P(A ∩ B) = P(A)P(B | A)

P(A ∩ B) = 0.40 × 0.70

**Answer:**

P(A ∩ B) = 0.28

## 10.3 Multiplication Rule for Multiple Events

The multiplication rule can be extended to any finite number of events.

For events A₁, A₂, ..., Aₙ:

P(A₁ ∩ A₂ ∩ ... ∩ Aₙ)

= P(A₁)
× P(A₂ | A₁)
× P(A₃ | A₁ ∩ A₂)
× ...
× P(Aₙ | A₁ ∩ A₂ ∩ ... ∩ Aₙ₋₁)

### Worked Example: Three Events

Suppose:

P(A) = 0.50

P(B | A) = 0.60

P(C | A ∩ B) = 0.80

Find the probability that all three events occur.

Using the multiplication rule:

P(A ∩ B ∩ C)

= P(A) × P(B | A) × P(C | A ∩ B)

= 0.50 × 0.60 × 0.80

**Answer:**

P(A ∩ B ∩ C) = 0.24

---

# 11. Total Probability Law

## 11.1 Understanding a Partition

Before studying the total probability law, we need to understand the concept of a partition.

A collection of events B₁, B₂, ..., is a partition of Ω if:

**Condition 1: Pairwise disjointness**

Bᵢ ∩ Bⱼ = ∅, for i ≠ j

**Condition 2: Their union equals the sample space**

∪ Bₙ = Ω

In simple terms:

- The events do not overlap.
- Together, they cover the entire sample space.

### Example

Suppose a bank has three branches:

- Branch 1.
- Branch 2.
- Branch 3.

Every customer belongs to exactly one branch.

The three branches divide the entire customer population into separate groups.

Therefore, they form a partition.

## 11.2 Statement of the Total Probability Law

Let B₁, B₂, ... be a finite or infinite sequence of mutually exclusive events whose union is Ω.

If P(Bₙ) > 0 for every n, then for any event A:

P(A) = Σ P(A | Bₙ)P(Bₙ)

This is called the **Total Probability Law**.

## 11.3 Understanding the Formula

The formula calculates the overall probability of an event by considering all possible groups in which that event could occur.

For each group:

1. Find the probability of belonging to that group.
2. Find the probability of the event occurring within that group.
3. Multiply the two probabilities.
4. Add the results across all groups.

## 11.4 Worked Example: Loan Default Across Bank Branches

Suppose a bank has three branches with the following customer distribution:

| Branch | Proportion of Customers | Probability of Default |
|---|---:|---:|
| Branch 1 | 50% | 2% |
| Branch 2 | 30% | 5% |
| Branch 3 | 20% | 10% |

Find the probability that a randomly selected customer defaults.

### Step 1: Define the events

Let:

A = Customer defaults.

B₁ = Customer belongs to Branch 1.

B₂ = Customer belongs to Branch 2.

B₃ = Customer belongs to Branch 3.

### Step 2: Write the given probabilities

P(B₁) = 0.50

P(B₂) = 0.30

P(B₃) = 0.20

P(A | B₁) = 0.02

P(A | B₂) = 0.05

P(A | B₃) = 0.10

### Step 3: Apply the total probability law

P(A) = P(A | B₁)P(B₁)
     + P(A | B₂)P(B₂)
     + P(A | B₃)P(B₃)

### Step 4: Substitute

P(A) = (0.02)(0.50) + (0.05)(0.30) + (0.10)(0.20)

P(A) = 0.01 + 0.015 + 0.02

**Answer:**

P(A) = 0.045 = 4.5%

Therefore, the overall probability that a randomly selected customer defaults is 4.5%.

---

# 12. Independence of Events

## 12.1 Definition

Two events A and B are independent if the occurrence of one event does not change the probability of the other event.

Mathematically, A and B are independent if:

P(A ∩ B) = P(A)P(B)

This is the fundamental condition for independence.

## 12.2 Understanding Independence

Consider tossing a fair coin twice.

The result of the first toss does not affect the result of the second toss.

For example, obtaining Heads on the first toss does not increase or decrease the probability of obtaining Heads on the second toss.

Each toss is independent of the other.

## 12.3 Worked Example: Two Coin Tosses

Suppose a fair coin is tossed twice.

The sample space is:

Ω = {HH, HT, TH, TT}

Let:

A = Getting Heads on the first toss.

B = Getting Heads on the second toss.

Then:

A = {HH, HT}

B = {HH, TH}

### Step 1: Calculate P(A)

P(A) = 2/4 = 1/2

### Step 2: Calculate P(B)

P(B) = 2/4 = 1/2

### Step 3: Calculate P(A ∩ B)

A ∩ B = {HH}

Therefore:

P(A ∩ B) = 1/4

### Step 4: Check the independence condition

P(A)P(B) = (1/2)(1/2)

P(A)P(B) = 1/4

Since:

P(A ∩ B) = P(A)P(B)

**Answer:**

A and B are independent events.

## 12.4 Independence and Conditional Probability

Recall the conditional probability formula:

P(A | B) = P(A ∩ B) / P(B)

If A and B are independent:

P(A ∩ B) = P(A)P(B)

Substituting:

P(A | B) = P(A)P(B) / P(B)

Therefore:

P(A | B) = P(A)

provided P(B) > 0.

This means that knowing B has occurred does not change the probability of A.

Similarly:

P(B | A) = P(B)

provided P(A) > 0.

## 12.5 Independence Versus Mutually Exclusive Events

These two concepts are frequently confused, but they describe different relationships.

| Mutually Exclusive Events | Independent Events |
|---|---|
| Cannot occur together (up to probability zero). | Occurrence of one does not change the probability of the other. |
| P(A ∩ B) = 0 | P(A ∩ B) = P(A)P(B) |
| No overlap in probability. | May occur together. |

### Important Result

Two mutually exclusive events with positive probabilities cannot be independent.

**Proof:**

If A and B are mutually exclusive:

P(A ∩ B) = 0

If they are independent:

P(A ∩ B) = P(A)P(B)

Combining:

P(A)P(B) = 0

But if both events have positive probabilities:

P(A) > 0 and P(B) > 0

then:

P(A)P(B) > 0

This is a contradiction.

Therefore, two mutually exclusive events with positive probabilities are dependent.

---

# 13. Practical Applications

Probability spaces and their properties are fundamental tools in financial mathematics and other quantitative fields.

| Concept | Practical Application |
|---|---|
| Sample space and events | Identifying possible financial outcomes |
| Discrete probability | Modeling situations with countable outcomes |
| Probability measure | Assigning probabilities to financial events |
| Sigma-field | Defining measurable events in mathematical models |
| Addition rule | Calculating the probability of at least one risk occurring |
| Complement rule | Calculating the probability of loan default or investment loss |
| Conditional probability | Evaluating risk using additional customer information |
| Multiplication rule | Calculating the probability of several events occurring together |
| Total probability law | Combining risk estimates from different customer groups |
| Independence | Modeling events that do not influence one another |

These concepts provide the mathematical foundation for more advanced topics such as random variables, probability distributions, expected values, and financial risk analysis.

---

# 14. Common Mistakes and Important Observations

### 1. Confusing Sample Space and Event

The sample space contains every possible outcome, while an event contains only selected outcomes.

### 2. Adding Probabilities Without Checking Disjointness

The formula:

P(A ∪ B) = P(A) + P(B)

is valid only when A and B are disjoint.

For general events, use:

P(A ∪ B) = P(A) + P(B) − P(A ∩ B)

### 3. Confusing a Sigma-Field with a Sample Space

The sample space Ω contains outcomes, whereas the sigma-field F contains measurable subsets of Ω.

### 4. Forgetting the Condition for Conditional Probability

The conditional probability P(A | B) is defined only when:

P(B) > 0

### 5. Reversing Conditional Probability

In general:

P(A | B) ≠ P(B | A)

The event after the vertical bar is the condition being assumed.

### 6. Confusing Independence and Mutual Exclusivity

Mutually exclusive events cannot occur together, while independent events do not influence each other's probabilities.

### 7. Forgetting the Partition Conditions

Before applying the total probability law, check that the conditioning events:

- Are mutually exclusive.
- Cover the entire sample space.
- Have positive probabilities.

### 8. Confusing Discrete and General Probability Spaces

A discrete probability space uses individually listed outcomes and their probabilities.

A general probability space uses the structure:

(Ω, F, P)

to handle a broader range of experiments, including those with uncountable sample spaces.

---

# 15. Formula Summary

| No. | Concept | Formula |
|---:|---|---|
| 1 | Probability distribution | 0 ≤ pₙ ≤ 1 |
| 2 | Total probability of outcomes | Σ pₙ = 1 |
| 3 | Probability of a discrete event | P(A) = Σ pₙ, for ωₙ ∈ A |
| 4 | Empty event | P(∅) = 0 |
| 5 | Sure event | P(Ω) = 1 |
| 6 | Countable additivity | P(∪ Aₙ) = Σ P(Aₙ), for pairwise disjoint events |
| 7 | Addition rule | P(A ∪ B) = P(A) + P(B) − P(A ∩ B) |
| 8 | Difference rule | P(A − B) = P(A) − P(B), if B ⊆ A |
| 9 | Complement rule | P(A′) = 1 − P(A) |
| 10 | Conditional probability | P(A \| B) = P(A ∩ B) / P(B) |
| 11 | Multiplication rule | P(A ∩ B) = P(A)P(B \| A) |
| 12 | Multiple-event multiplication rule | P(A₁ ∩ ... ∩ Aₙ) = P(A₁)P(A₂ \| A₁)...P(Aₙ \| A₁ ∩ ... ∩ Aₙ₋₁) |
| 13 | Total probability law | P(A) = Σ P(A \| Bₙ)P(Bₙ) |
| 14 | Independence | P(A ∩ B) = P(A)P(B) |

---

# 16. Practice Questions with Solutions

## Question 1: Discrete Probability

A fair six-sided die is rolled once.

Find the probability of obtaining a number greater than 3.

### Solution

Sample space:

Ω = {1, 2, 3, 4, 5, 6}

Event:

A = {4, 5, 6}

Therefore:

P(A) = 3/6

**Answer:**

P(A) = 1/2

---

## Question 2: Probability Distribution

A random experiment has four possible outcomes with probabilities:

p₁ = 0.10

p₂ = 0.20

p₃ = 0.30

p₄ = 0.40

Determine whether these probabilities form a valid probability distribution.

### Solution

Check the first condition:

0 ≤ pₙ ≤ 1

All probabilities satisfy this condition.

Check the second condition:

Σ pₙ = 0.10 + 0.20 + 0.30 + 0.40

Σ pₙ = 1

**Answer:**

The probabilities form a valid probability distribution.

---

## Question 3: Addition Rule

Suppose:

P(A) = 0.60

P(B) = 0.50

P(A ∩ B) = 0.20

Find P(A ∪ B).

### Solution

Using:

P(A ∪ B) = P(A) + P(B) − P(A ∩ B)

Substitute:

P(A ∪ B) = 0.60 + 0.50 − 0.20

**Answer:**

P(A ∪ B) = 0.90

---

## Question 4: Complement Rule

The probability that a financial investment produces a positive return is 0.75.

Find the probability that it does not produce a positive return.

### Solution

Using:

P(A′) = 1 − P(A)

P(A′) = 1 − 0.75

**Answer:**

P(A′) = 0.25

---

## Question 5: Conditional Probability

Suppose:

P(A ∩ B) = 0.24

P(B) = 0.40

Calculate P(A | B).

### Solution

Using:

P(A | B) = P(A ∩ B) / P(B)

P(A | B) = 0.24 / 0.40

**Answer:**

P(A | B) = 0.60

---

## Question 6: Multiplication Rule

Suppose:

P(A) = 0.40

P(B | A) = 0.75

Find P(A ∩ B).

### Solution

Using:

P(A ∩ B) = P(A)P(B | A)

P(A ∩ B) = 0.40 × 0.75

**Answer:**

P(A ∩ B) = 0.30

---

## Question 7: Total Probability Law

A bank receives customers from two branches.

- 60% of customers come from Branch 1, where the default probability is 3%.
- 40% come from Branch 2, where the default probability is 8%.

Find the overall probability of default.

### Solution

Let A represent default.

Let B₁ and B₂ represent the two branches.

Given:

P(B₁) = 0.60

P(B₂) = 0.40

P(A | B₁) = 0.03

P(A | B₂) = 0.08

Using the total probability law:

P(A) = P(A | B₁)P(B₁) + P(A | B₂)P(B₂)

P(A) = (0.03)(0.60) + (0.08)(0.40)

P(A) = 0.018 + 0.032

**Answer:**

P(A) = 0.05 = 5%

---

## Question 8: Independence

Suppose:

P(A) = 0.40

P(B) = 0.50

P(A ∩ B) = 0.20

Determine whether A and B are independent.

### Solution

Two events are independent if:

P(A ∩ B) = P(A)P(B)

Calculate:

P(A)P(B) = 0.40 × 0.50 = 0.20

Since:

P(A ∩ B) = P(A)P(B)

**Answer:**

A and B are independent.

---

## Question 9: Mutually Exclusive and Independent Events

Suppose two events A and B are mutually exclusive, with:

P(A) = 0.30

P(B) = 0.40

Determine whether they are independent.

### Solution

Since A and B are mutually exclusive:

P(A ∩ B) = 0

For independence, we require:

P(A ∩ B) = P(A)P(B)

Calculate:

P(A)P(B) = 0.30 × 0.40 = 0.12

Since:

0 ≠ 0.12

**Answer:**

A and B are not independent.

They are mutually exclusive and dependent.

---

# 17. Conclusion

Probability spaces provide the mathematical foundation for studying uncertainty.

The main structure is:

(Ω, F, P)

where:

- Ω represents all possible outcomes.
- F specifies the measurable events.
- P assigns probabilities to those events.

Starting from discrete probability spaces, we developed the concept of sigma-fields and general probability measures. We then established important probability rules, including the addition rule, complement rule, conditional probability, multiplication rule, and total probability law.

Finally, we studied independence and learned how to determine whether two events influence each other's probabilities.

These concepts are essential for understanding the next part of the chapter, where we will study random variables and their properties.

**Next: Chapter 2 — Part 2: Random Variables and Probability Distributions.**
