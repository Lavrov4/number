def generate_fibonacci(n):
    """
    Generate a Fibonacci sequence up to the nth term.
    """
    fibonacci_sequence = [0, 1]
    while fibonacci_sequence[-1] + fibonacci_sequence[-2] <= n:
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
    return fibonacci_sequence

def sum_even_numbers(sequence):
    """
    Calculate the sum of even numbers in a sequence.
    """
    even_sum = sum(num for num in sequence if num % 2 == 0)
    return even_sum

if __name__ == "__main__":
    try:
        n = int(input("Enter a number to generate Fibonacci sequence up to: "))
        if n <= 0:
            print("Please enter a positive integer.")
        else:
            fibonacci_sequence = generate_fibonacci(n)
            print("Fibonacci sequence up to {}:".format(n), fibonacci_sequence)
            even_sum = sum_even_numbers(fibonacci_sequence)
            print("Sum of even numbers in the sequence:", even_sum)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
