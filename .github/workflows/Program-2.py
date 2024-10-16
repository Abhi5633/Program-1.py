def generate_odd_numbers(a):
    # Create a list to hold the odd numbers
    odd_numbers = []
    
    # Generate odd numbers from 1 up to the a-th odd number
    for i in range(a):
        odd_number = 2 * i + 1  # Formula for the i-th odd number
        odd_numbers.append(odd_number)
    
    return odd_numbers

# Example usage
if __name__ == "__main__":
    a = int(input("Enter a positive integer (a): "))
    
    if a < 1:
        print("Please enter a positive integer greater than 0.")
    else:
        result = generate_odd_numbers(a)
        print(f"Output: {', '.join(map(str, result))}")
