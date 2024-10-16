def count_multiples(numbers):
    multiple_counts = {}
    
    # Initialize counts for each digit from 1 to 9
    for i in range(1, 10):
        multiple_counts[i] = 0
    
    # Count multiples for each digit
    for num in numbers:
        for i in range(1, 10):
            if num % i == 0:
                multiple_counts[i] += 1
    
    return multiple_counts

# Example usage
if __name__ == "__main__":
    numbers = list(map(int, input("Enter a list of numbers (separated by spaces): ").split()))
    
    result = count_multiples(numbers)
    print("Output:")
    for key, value in result.items():
        print(f"{key}: {value}")
