# Code By Rupesh bhagat


# For Creating variables of each primitive data types
int_value = 15
float_value = 24.5
str_value = "Rupesh"

# For Performing Arithmetic Operations
sum_value = int_value + float_value         # Adding int and float
difference_value = float_value - int_value  # Subtracting int from float
product_value = int_value * float_value     # Multiplying int and float 
division_value = float_value / int_value    # Dividing float by int


# For String concatenation
concatenated_str = str_value + " Bhagat. "


# For Creating a dictionary to store and display these variables by their types as keys
datatypes_dict = {
    "int": [int_value],
    "float": [float_value],
    "str": [concatenated_str],
}


# For Displaying the results
print(datatypes_dict)
for data_type, values in datatypes_dict.items():
    print(f"{data_type}: {values}")


    