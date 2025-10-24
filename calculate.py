def calculate_total_sales(filename):
    """
    Reads a CSV file (Name,Sales) and calculates the total sales amount.
    Returns 0 if the file is not found.
    """
    total_sales = 0.0

    try:
        # 'with open' ensures the file is automatically closed
        with open(filename, 'r') as file:
            for line in file:
                # Strip whitespace/newline characters and split by comma
                parts = line.strip().split(',')
                
                # Basic check to ensure the line has at least two parts
                if len(parts) == 2:
                    try:
                        # The sales amount is the second part (index 1)
                        sales_amount = float(parts[1])
                        total_sales += sales_amount
                    except ValueError:
                        # Handle cases where the sales amount is not a valid number
                        print(f"Warning: Skipping invalid sales amount in line: {line.strip()}")
                        continue
                        
    except FileNotFoundError:
        # Handle the specific error required by the prompt
        return 0
    
    return total_sales

# --- Setup and Test Cases ---

# 1. Create a dummy file for testing
import os
dummy_filename = "sales_data.csv"
csv_content = """Apples,150.50
Bananas,80
Oranges,210.75
Grapes,120
Invalid Product,NotANumber""" # Added an invalid line for robust testing

try:
    with open(dummy_filename, 'w') as f:
        f.write(csv_content)

    # Test Case 1: File Exists
    result_exists = calculate_total_sales(dummy_filename)
    # Expected sum: 150.50 + 80 + 210.75 + 120 = 561.25
    print(f"Total Sales (Existing File): {result_exists}") 

    # Test Case 2: File Missing
    result_missing = calculate_total_sales("missing_data.csv")
    # Expected result: 0 (due to FileNotFoundError)
    print(f"Total Sales (Missing File): {result_missing}") 

finally:
    # Clean up the dummy file
    if os.path.exists(dummy_filename):
        os.remove(dummy_filename)