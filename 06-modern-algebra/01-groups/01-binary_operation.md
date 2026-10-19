# BINARY OPERATION

A binary operation * on a set S is a function that maps S × S into S.

In mathematical notation:
* : S × S → S
This means that the operation takes two elements from S and produces an element that also belongs to S.

---

To make the above definition of binary operation easier and understandable, let us treat the statement word by word:

## What is a set?
A set is simply a collection of distinct objects.

For example:

S = {1, 2, 3, 4, 5}
A = {a, b, c}
Z = the set of all integers: {..., -3, -2, -1, 0, 1, 2, 3, ...}
R = the set of all real numbers.

We use capital letters such as S, A, Z, and R to represent sets.

---

## What is an operation?

An operation is a rule that tells us how to combine or use mathematical objects.

For example, addition is an operation:

2 + 3 = 5

Multiplication is another operation:

2 × 3 = 6

Subtraction is also an operation:

5 - 2 = 3

However, an operation is not automatically a binary operation on every set. We must check whether it satisfies the requirements of a binary operation on the particular set we are considering.

---

## Why is it called a binary operation?

The word binary means involving two things.

For example, in

3 + 4 = 7

the two inputs are 3 and 4, and the output is 7.

We can represent this as:

3, 4 → addition → 7

Similarly:

2, 5 → multiplication → 10

A binary operation takes two inputs and produces one output.

---

## What does S × S mean?

This is called the Cartesian product of S with itself.

It is the set of all ordered pairs whose first and second elements both belong to S.

Suppose:

S = {1, 2, 3}

Then:

S × S = {(1,1), (1,2), (1,3), (2,1), (2,2), (2,3), (3,1), (3,2), (3,3)}

Notice that each pair contains two elements from S.

For example:

(1, 2) belongs to S × S.
(3, 1) belongs to S × S.
(2, 2) belongs to S × S.

But (1, 4) does not belong to S × S because 4 does not belong to S.

---

## Why do we need S × S?

Because a binary operation takes two elements from S as its inputs. S × S represents all possible pairs of inputs.

---

## What does S × S → S mean?

This is the most important part of the definition.

The notation

* : S × S → S

means that the operation accepts any ordered pair from S × S and assigns it an output belonging to S.

In simpler language:

Choose any two elements from S.
Apply the operation to them.
The result must also belong to S.

Example 1: Addition on S = {1, 2, 3}

Suppose we define the operation as ordinary addition.

Consider:

1 + 2 = 3

The result, 3, belongs to S.

But now consider:

2 + 3 = 5

The result, 5, does not belong to S.

Therefore, ordinary addition is not a binary operation on S = {1, 2, 3}.

Why?

Because the operation must produce a result in S for every possible pair of elements from S, and this condition fails for the pair (2, 3).

One failure is enough to show that an operation is not a binary operation on the set.

---

H. Example 2: Addition on S = Z

Now let:

S = Z

Here, Z represents all integers, including negative numbers, zero, and positive numbers.

Consider some examples:

2 + 3 = 5

-4 + 2 = -2

-3 + (-5) = -8

All the results are integers.

In fact, the sum of any two integers is always an integer.

Therefore, ordinary addition is a binary operation on Z.

Similarly, ordinary multiplication is a binary operation on Z because the product of any two integers is always an integer.

I. Example 3: Subtraction on S = Z+

Suppose Z+ represents the positive integers:

Z+ = {1, 2, 3, 4, 5, ...}

Consider ordinary subtraction:

5 - 2 = 3

The result belongs to Z+.

However:

2 - 5 = -3

The result does not belong to Z+.

Therefore, ordinary subtraction is not a binary operation on the positive integers.

Notice the important lesson: an operation can be a binary operation on one set but fail to be a binary operation on another set.

Subtraction is a binary operation on the integers, Z, but not on the positive integers, Z+.

1.2. The Two Essential Requirements

From the definition in your PDF, we can identify two important requirements.

Requirement 1: The operation must be well-defined.

For every pair of inputs, the rule must determine one unambiguous output.

For example, ordinary addition is well-defined: 2 + 3 always equals 5.

Requirement 2: The set must be closed under the operation.

For every a and b in S, the result a * b must also belong to S.

In symbols:

If a, b ∈ S, then a * b ∈ S.

Here, ∈ means "belongs to."

These requirements are related but distinct. A rule might determine a unique result for every pair yet fail to produce a result inside the chosen set.

For example, subtraction is well-defined on the positive integers, but it does not always produce a positive integer.

Important: Closure is the main test you will repeatedly use when deciding whether a rule is a binary operation on a given set.

1.3. A General Example Using a New Operation

A binary operation does not have to be ordinary addition, subtraction, or multiplication.

Suppose S = Z+, and define:

a * b = a + b + 1

Let's test it.

If a = 2 and b = 3:

2 * 3 = 2 + 3 + 1 = 6

If a = 4 and b = 5:

4 * 5 = 4 + 5 + 1 = 10

Both results belong to Z+.

More generally, if a and b are positive integers, then a + b + 1 is also a positive integer.

Therefore, this rule is a binary operation on Z+.

The symbol * here does not mean ordinary multiplication. It represents the particular rule we have defined.

This is a key idea in abstract algebra: mathematicians can define new operations and then investigate their properties.

1.4. Quick Summary

Remember these points:

A set is a collection of objects.
A binary operation takes two inputs and produces one output.
S × S represents all ordered pairs of elements from S.
* : S × S → S means that the operation takes pairs from S and produces outputs in S.
To qualify as a binary operation on S, the rule must be well-defined and closed on S.
A rule may be a binary operation on one set but not on another.
Check Your Understanding

Before we continue to the next definition in your PDF, try these three questions.

Question 1: Is ordinary multiplication a binary operation on S = {1, 2, 3}?

Question 2: Is ordinary subtraction a binary operation on Z, the set of all integers?

Question 3: Let S = Z+ and define a * b = a + b. Is * a binary operation on S? Explain why.

---
