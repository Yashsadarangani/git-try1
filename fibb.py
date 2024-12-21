def fibonacci_series(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fib_series = [0, 1]
    for i in range(2, n):
        next_term = fib_series[-1] + fib_series[-2]
        fib_series.append(next_term)
    return fib_series
num_terms = int(input("Enter the number of terms: "))

print("Fibonacci Series:")
print(" ".join(map(str, fibonacci_series(num_terms))))
