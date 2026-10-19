# Subgroups

## Definition of a Subgroup

A subgroup is a subset of a group that is itself a group under the same operation.

---

Let’s unpack this definition.

Suppose we have a group (G, *), and H is a subset of G.

For H to be a subgroup of G:

H must be a subset of G. Every element of H must also belong to G.
H must use the same operation. If G uses *, then H must use * too.
H must itself satisfy the group axioms. The operation must be closed in H, associative, have an identity element in H, and every element of H must have an inverse in H.

We write H ≤ G to mean that H is a subgroup of G.

---

Example

Consider the groups:

G = (Z, +), the integers under addition.
H = (2Z, +), the even integers under addition.

Since every even integer is an integer, H is a subset of G.

Let’s check whether H is a subgroup:

Closure: The sum of two even integers is even. For example, 4 + 6 = 10.
Associativity: Integer addition is associative.
Identity: The additive identity 0 is even, so 0 belongs to H.
Inverse: The additive inverse of any even integer is even. For example, the inverse of 6 is −6.

Therefore, (2Z, +) is a subgroup of (Z, +).

---

Key idea

A subset is not automatically a subgroup just because it is contained in a group. It must also form a group under the same operation.

You need to check two main conditions:

Subset condition: H ⊆ G.
Group condition: H must itself be a group under the same operation, which means checking the four group axioms:
Closure
Associativity
Identity
Inverse

One useful shortcut: Since H inherits associativity from G, you usually don't need to prove associativity separately. If G is already a group and H ⊆ G, associativity automatically holds in H. You still need to establish the other requirements.

