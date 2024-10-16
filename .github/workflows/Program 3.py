def generate_unique_odd_numbers(a):
    # Create a list to hold the unique odd numbers
    unique_odd_numbers = []
    
    # Generate unique odd numbers up to the a-th odd number
    i = 1
    while len(unique_odd_numbers) < a:
        odd_number = 2 * i - 1  # Formula for the i-th odd number
        if odd_number not in unique_odd_numbers:
            unique_odd_numbers.append(odd_number)
        i += 1
    
    return unique_odd_numbers

# Example usage
if __name__ == "__main__":
    a = int(input("Enter a positive integer (a): "))
    
    if a < 1:
        print("Please enter a positive integer greater than 0.")
    else:
        result = generate_unique_odd_numbers(a)
        print(f"Output: {', '.join(map(str, result))}")
