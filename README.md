# python_questions
Structured collection of Python problems focused on strengthening core fundamentals, problem-solving, and clean coding practices. Covers control flow, functions, data structures, number logic, and string manipulation, with emphasis on clarity, simplicity, and disciplined implementation.


Prime Number Check – Optimized Approach (O√n)
<br>
This implementation checks whether a number is prime using an optimized approach.
<br>
Core Logic
for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
        return False
Explanation

n**0.5 → calculates √n (square root of n)

We check divisibility only up to √n

If n % i == 0 → number is divisible → Not Prime

Return immediately (early termination) for efficiency

Why Check Till √n?

If a number has a factor greater than √n,
it must also have a corresponding factor smaller than √n.

Example:
36 → (1×36), (2×18), (3×12), (6×6)
After √36 = 6, factors repeat in reverse.

So checking beyond √n is unnecessary.

Why +1?

range() excludes the last value.

Example:

range(2, 6) → 2, 3, 4, 5

So to include √n, we use:

range(2, int(n**0.5) + 1)
Time Complexity

O(√n)

Efficient and interview-ready solution.
