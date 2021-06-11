#  Overlapping Subproblems
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

# Memoization (Top Down)


def fib_m(n, lookup):
    if n == 0 or n == 1:
        lookup[n] = n

    if lookup[n] is None:
        lookup[n] = fib_m(n-1, lookup) + fib_m(n-2, lookup)

    return lookup[n]

#  Tabulation (Bottom Up)



def fibonacci(n):
    f = [0] * (n+1)
    f[0] = 0
    f[1] = 1

    for i in range(2, n+1):
        f[i] = f[i-1] + f[i-2]

    return f[n]

# Driver program to test the above function


def main():
    n = int(input("Enter number : "))
    lookup = [None] * 101
    print("Fibonacci Number using Overlapping Subproblems:  ", fib(n))
    print("Fibonacci Number using Memoization (Top Down): ", fib_m(n, lookup))
    print("Fibonacci Number using Tabulation (Bottom Up): ", fibonacci(n))


if __name__ == "__main__":
    main()
