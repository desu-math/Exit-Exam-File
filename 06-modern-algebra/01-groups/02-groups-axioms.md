# Definition of a Group

A group (G, *) is a set G, closed under a binary operation *, such that the following axioms hold.

The three axioms are:

G1: Associativity

For all a, b, c ∈ G,

a * (b * c) = (a * b) * c

G2: Identity element

There is an element e ∈ G such that, for all x ∈ G,

e * x = x * e = x

G3: Inverse element

For each a ∈ G, there is an element a′ ∈ G such that

a * a′ = a′ * a = e

Here, a′ represents the inverse of a. It is also commonly written as a⁻¹.

---
Let's understand these ideas one by one.

 # What Is a Group?

A group is a set equipped with a binary operation that satisfies four conditions:

Closure under the operation.
Associativity.
Existence of an identity element.
Existence of an inverse for every element.

Think of a group as a mathematical system in which an operation behaves according to these four rules.

---

Let's use the integers under addition to understand them.

Let:

G = Z = {..., -2, -1, 0, 1, 2, ...}

and let * represent ordinary addition.

We will check each condition.

---

Condition 1: Closure

Meaning: Combining any two elements of G using the operation must produce another element of G.

For example:

3 + 5 = 8

-4 + 2 = -2

-3 + (-6) = -9

Every result is an integer.

Therefore, Z is closed under addition.

---

Condition 2: Associativity

a * (b * c) = (a * b) * c

Meaning: When combining three elements, changing the grouping does not change the result.

For ordinary addition:

2 + (3 + 4) = 2 + 7 = 9

On the other hand:

(2 + 3) + 4 = 5 + 4 = 9

Both results are equal.

Therefore, addition is associative.

Important distinction: Associativity concerns grouping, not changing the order of the elements.

---

Condition 3: Identity Element

e * x = x * e = x

Meaning: An identity element is an element that leaves every element unchanged when used with the operation.

For addition, the identity is zero because:

5 + 0 = 5

0 + 5 = 5

Similarly:

-7 + 0 = -7

0 + (-7) = -7

Therefore, 0 is the identity element for addition on Z.

Notice that the identity depends on the operation. For ordinary multiplication, the identity is 1 because multiplying a number by 1 leaves it unchanged.

---
Condition 4: Inverse Element

For each a ∈ G, there is an element a′ ∈ G such that:

a * a′ = a′ * a = e

Meaning: Every element must have another element that combines with it to produce the identity.

For addition on Z, the identity is 0.

Consider the element 5. Its additive inverse is -5 because:

5 + (-5) = 0

(-5) + 5 = 0

Similarly:

The inverse of 3 is -3.
The inverse of -8 is 8.
The inverse of 0 is 0.

Every integer has an additive inverse that also belongs to Z.

Therefore, every element satisfies the inverse requirement.

---

Conclusion

We have checked all four conditions:

Condition	Addition on Z
Closure	Satisfied
Associativity	Satisfied
Identity element	0
Inverse of every element	The inverse of a is -a

Hence, (Z, +) is a group.

---

## Is Every Group Commutative?

A group G is called abelian if its binary operation is commutative.

In other words, a group is abelian when:

a * b = b * a

for every a and b in G.

For example, addition on Z is commutative because:

3 + 5 = 5 + 3 = 8

Therefore, (Z, +) is an abelian group.

---

However, not every group is abelian. Some groups satisfy all four group conditions but do not satisfy commutativity.

We will study examples of both types as we continue through the chapter.

Remember:

Every abelian group is a group.
A group does not have to be abelian.
Commutativity is not one of the four requirements in the general definition of a group.

---

Example, Positive Integers Under Addition

(Z+, +) is not a group because it has no identity element.

Let's verify this carefully.

Here, Z+ represents the positive integers:

Z+ = {1, 2, 3, 4, ...}

The operation is ordinary addition.

Closure is satisfied because the sum of two positive integers is positive.

Associativity is also satisfied because ordinary addition is associative.

But what would the identity element be?

For addition, the identity must be 0, since:

a + 0 = 0 + a = a

However, 0 does not belong to Z+.

Therefore, there is no identity element in this set under ordinary addition.

That single failure is enough to conclude:

(Z+, +) is not a group.

---

This example teaches an important lesson: even when an operation satisfies closure and associativity, the set may still fail to be a group.

---

Check Your Understanding

Answer these three questions.

1. For the set of integers Z under ordinary multiplication, the identity element is 1. Is (Z, ×) a group? Explain which condition it satisfies or fails.

2. Consider (Z≥0, +), where Z≥0 = {0, 1, 2, 3, ...}. Your PDF says this is not a group because its elements do not all have inverses. Explain why.

3. Suppose a set with a binary operation satisfies closure, associativity, and has an identity element. However, one element has no inverse in the set. Is the structure a group? Why?

---
