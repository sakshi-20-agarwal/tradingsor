# Fibonacci Series Generator

# Method 1: Using a loop
def fibonacci_loop(n):
    """Generate Fibonacci series up to n terms using a loop"""
    a, b = 0, 1
    fib_series = []
    for _ in range(n):
        fib_series.append(a)
        a, b = b, a + b
    return fib_series


# Method 2: Using recursion
def fibonacci_recursive(n):
    """Generate Fibonacci series up to n terms using recursion"""
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    fib_series = fibonacci_recursive(n - 1)
    if len(fib_series) == 1:
        fib_series.append(1)
    else:
        fib_series.append(fib_series[-1] + fib_series[-2])
    return fib_series


# Method 3: Direct Fibonacci number calculation
def fibonacci_number(n):
    """Calculate the nth Fibonacci number (0-indexed)"""
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


# Main program
if __name__ == "__main__":
    # Generate first 10 Fibonacci numbers
    num_terms = 10
    
    print("Fibonacci Series using Loop:")
    print(fibonacci_loop(num_terms))
    
    print("\nFibonacci Series using Recursion:")
    print(fibonacci_recursive(num_terms))
    
    print("\nFibonacci Numbers:")
    for i in range(num_terms):
        print(f"F({i}) = {fibonacci_number(i)}")
