def calculate_bmi(weight_kg, height_m):
    """Calculates the Body Mass Index (BMI)."""
    if height_m <= 0:
        return None  # Handle invalid height
    return weight_kg / (height_m ** 2)

def categorize_bmi(bmi):
    """Assigns a weight category based on the calculated BMI."""
    if bmi is None:
        return "Invalid input"
    elif bmi < 18.5:
        return "Underweight 📉"
    elif 18.5 <= bmi < 25.0:
        return "Normal weight (Healthy) ✅"
    elif 25.0 <= bmi < 30.0:
        return "Overweight ⚠️"
    else:
        return "Obesity 🛑"

# --- Main Program Execution ---

print("--- BMI Calculator ---")
try:
    # 1. Get user input for weight and height
    weight = float(input("Enter your weight in kilograms (kg): "))
    height = float(input("Enter your height in meters (m): "))

    # 2. Calculate BMI
    bmi_score = calculate_bmi(weight, height)

    # 3. Print the results
    if bmi_score is not None:
        category = categorize_bmi(bmi_score)
        print(f"\nYour BMI is: {bmi_score:.2f}")
        print(f"Category: {category}")
    else:
        print("\nError: Height must be greater than zero.")

except ValueError:
    print("\nInvalid input. Please enter valid numbers for weight and height.")
except Exception as e:
    print(f"\nAn unexpected error occurred: {e}")