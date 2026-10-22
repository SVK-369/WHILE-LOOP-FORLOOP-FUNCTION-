import random

# 1. Generate a random secret number between 1 and 10
secret_number = random.randint(1, 10)

# Set max allowed attempts
attempts = 3

# 2 & 3. Implement the guessing logic using a while loop
while attempts > 0:
    guess = int(input("Guess the number (between 1 and 10): "))

    # Check if guess is out of valid range (1 to 10)
    if guess < 1 or guess > 10:
        print(
            "Your guess is out of range. Please guess a number between 1 and 10."
        )
        continue  # Skip the rest of the loop logic without deducting attempts/or directly next iteration

    # Check guess against the secret number
    if guess > secret_number:
        print("Too high. Try again.")
    elif guess < secret_number:
        print("Too low. Try again.")
    else:
        print("Congratulations! You guessed the correct number.")
        break  # Exit the loop on correct guess

    attempts -= 1  # Decrement remaining attempts
else:
    # Executes only if the loop finishes naturally without breaking
    print("Better luck next time!")



    # 1. Prompt the user for input
num = int(
    input("Enter the number for which you want the multiplication table: ")
)

# 2 & 3. Generate and display the multiplication table from 1 to 10
for i in range(1, 11):
    result = num * i
    print(f"{num} x {i} = {result}")


    # 1. Define the function to calculate BMI
def calculate_bmi(weight, height):
    """Calculates Body Mass Index using formula: weight / (height^2)"""
    bmi = weight / (height**2)
    return bmi


# 2. Prompt the user for weight (kg) and height (m)
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

# 3. Call the function and display the output formatted to 2 decimal places
bmi_result = calculate_bmi(weight, height)
print(f"Your BMI is: {bmi_result:.2f}")