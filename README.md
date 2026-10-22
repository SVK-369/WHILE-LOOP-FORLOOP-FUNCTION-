# WHILE-LOOP-FORLOOP-FUNCTION-
WHILE LOOP,FOR LOOP,&amp; FUNCTION 

1.Number Guessing Game (while loop & control statements)
Step-by-Step Explanation
​import random and random.randint(1, 10): Generates an integer secret number between 1 and 10 inclusive.  
​attempts = 3: Keeps track of how many turns the user has left.  
​while attempts > 0:: Runs the guessing cycle as long as the user has attempts remaining.  
​continue statement: If the user inputs a number outside 1–10, we display an error message and use continue to jump directly to the next loop iteration.  
​break statement: When guess == secret_number, we display congratulations and use break to stop the loop immediately.  
​while ... else:: The else block connected to a while loop runs only if the loop finishes normally (i.e., attempts run out) without being terminated early by a break.

2.Multiplication Table Generator (for loop)

Step-by-Step Explanation
​int(input(...)): Converts the user's input into an integer so arithmetic can be performed.  
​range(1, 11): Generates a sequence of integers starting at 1 up to 10 (the upper limit 11 is exclusive).  
​for i in range(1, 11):: Iterates through numbers 1 to 10 one by one.  
​Formatted output: f"{num} x {i} = {result}" prints each step matching the requested format number x i = result.



3.BMI Calculator (function)

Step-by-Step Explanation
​def calculate_bmi(weight, height):: Declares a reusable function accepting two parameters.  
​Formula: \text{BMI} = \frac{\text{weight}}{\text{height}^2}. In Python, exponentiation is written using **.  
​float(input(...)): Converts user inputs to floating-point numbers so decimal values (like height 1.62\text{ m}) are supported.  
​:.2f formatting: Formats the floating-point result to 2 decimal places to match the sample output eg:22.10


