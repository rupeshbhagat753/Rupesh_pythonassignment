# Code by Rupesh bhagat

def classify_number():
    
   # Function to classify a number as positive, negative, or zero.
   # It allows repeated input until the user types 'exit'.
    
    while True:
        user_input = input("Enter a number to classify or 'exit' to quit: ")
        
        # For Exit condition
        if user_input.lower() == "exit":
            print("Exiting program.")
            break
        
        # To check if input is positive, negative or zero
        try:
            number = float(user_input)      #changing input to float
            if number > 0:
                print(f"{number} is a positive number.")
            elif number < 0:
                print(f"{number} is a negative number.")
            else:
                print(f"{number} is zero.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            
            
# To Call the function
classify_number()