# 1. Interest

## 1.1 Definition

**Interest** is the amount of money earned by lending or investing money, or paid for borrowing money, over a specified period.

* **Principal (A₀):** The initial amount invested or borrowed.
* **Interest rate (r):** The rate at which interest is earned or charged, usually expressed annually.
* **Future value (A(t)):** The total amount after interest has accumulated.
* **Present value:** The value of a future amount at the starting time.

Unless otherwise stated, express interest rates as decimals and time in years.

## 1.2 Simple Interest

Under simple interest, interest is calculated only on the original principal.

**Total interest:**

I = A₀rt

**Future value:**

A(t) = A₀(1 + rt)

**Present value:**

A₀ = A(t)/(1 + rt)

Where:

* A₀ = initial principal
* r = annual interest rate
* t = time in years
* I = total interest earned or charged

**Example:** Invest 10,000 ETB at 8% simple interest for 3 years.

A(t) = 10,000(1 + 0.08 × 3)

A(t) = 12,400 ETB

Total interest = 12,400 − 10,000 = 2,400 ETB.

**Key idea:** Simple interest grows linearly with time because interest is always calculated on the original principal.

## 1.3 Compound Interest

Under compound interest, interest is calculated on the principal plus previously accumulated interest.

### A. Annual Compounding

Interest is compounded once per year.

**Formula:**

A(t) = A₀(1 + r)ᵗ

**Example:** Invest 10,000 ETB at 8% annually for 3 years.

A(3) = 10,000(1.08)³

A(3) = 12,597.12 ETB

Total interest = 2,597.12 ETB.

### B. Discrete Compounding

Interest is compounded a specified number of times per year.

**Formula:**

A(t) = A₀(1 + r/m)ᵐᵗ

Where:

* m = number of compounding periods per year
* r/m = interest rate per period
* mt = total number of compounding periods

Common values of m:

* Annually: m = 1
* Quarterly: m = 4
* Monthly: m = 12
* Daily: m = 365 (common convention)

**Example:** Invest 10,000 ETB at a nominal annual rate of 12%, compounded monthly, for 2 years.

A(2) = 10,000(1 + 0.12/12)²⁴

A(2) ≈ 12,697.35 ETB.

**Key idea:** Compound interest grows faster than simple interest over time because accumulated interest also earns interest.

## 1.4 Continuous Compounding

Continuous compounding models interest as being compounded continuously.

**Formula:**

A(t) = A₀eʳᵗ

Where e ≈ 2.71828.

**Example:** Invest 10,000 ETB at a continuously compounded annual rate of 8% for 3 years.

A(3) = 10,000e⁰·²⁴

A(3) ≈ 12,712.49 ETB.

The formula is obtained as the limit of discrete compounding when m approaches infinity:

lim (m → ∞) A₀(1 + r/m)ᵐᵗ = A₀eʳᵗ

## 1.5 Effective Annual Interest Rate

The **effective annual rate** is the actual percentage growth of an investment over one year after accounting for compounding.

For interest compounded m times per year:

**Formula:**

rₑ = (1 + r/m)ᵐ − 1

For continuous compounding:

rₑ = eʳ − 1

**Example:** A nominal annual rate of 12% compounded monthly gives:

rₑ = (1 + 0.12/12)¹² − 1

rₑ ≈ 0.126825 = 12.68%.

Therefore, the effective annual rate is approximately **12.68%**, not 12%.

**Key idea:** The effective annual rate allows fair comparisons between investments with different compounding frequencies, assuming comparable terms.

## 1.6 Comparison of Interest Methods

| Method                 | Formula              | Main characteristic                                    |
| ---------------------- | -------------------- | ------------------------------------------------------ |
| Simple interest        | A(t) = A₀(1 + rt)    | Interest is calculated only on the original principal. |
| Annual compounding     | A(t) = A₀(1 + r)ᵗ    | Interest is compounded once per year.                  |
| Discrete compounding   | A(t) = A₀(1 + r/m)ᵐᵗ | Interest is compounded m times per year.               |
| Continuous compounding | A(t) = A₀eʳᵗ         | Compounding frequency tends to infinity.               |

For the same positive nominal annual rate and investment period, more frequent compounding produces a larger future value. Continuous compounding gives the limiting maximum among these compound-interest methods.

## 1.7 Important Exam Reminders

1. Convert percentages to decimals before substituting into formulas.
2. In discrete compounding, calculate the periodic rate using r/m.
3. The total number of compounding periods is mt.
4. Do not confuse simple interest with compound interest.
5. The nominal annual rate is not necessarily equal to the effective annual rate.
6. Simple interest grows linearly; compound interest grows exponentially.
7. Always check that the time unit matches the interest-rate convention.

## 1.8 Practice Questions

1. Calculate the simple interest on 15,000 ETB at 6% per year for 4 years.
2. Find the future value of 20,000 ETB invested at 8% annual compound interest for 3 years.
3. Calculate the future value of 10,000 ETB invested at 12% nominal annual interest, compounded monthly, for 2 years.
4. Find the future value of 5,000 ETB invested at a continuously compounded annual rate of 7% for 4 years.
5. Calculate the effective annual rate for a nominal rate of 10% compounded quarterly.

---

**Summary:** Interest measures the cost or return associated with money over time. Simple interest applies only to the original principal, while compound interest applies to the growing balance. Continuous compounding is the limiting case of discrete compounding, and the effective annual rate measures the actual annual growth after compounding.
