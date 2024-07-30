def car_cost_calculator():
    """
    Calculates and displays the monthly and annual costs of operating a car.

    Prompts the user for loan payment, insurance, gas, and maintenance costs.
    Returns a tuple with the calculated monthly and annual costs.
    """

    while True:
        try:
            # Prompt user for monthly expenses
            loan_payment = float(input("Enter your monthly loan payment: "))
            insurance = float(input("Enter your monthly insurance cost: "))
            gas = float(input("Enter your average monthly gas expenditure: "))
            maintenance = float(input("Enter your average monthly maintenance cost: "))

            # Validate inputs are non-negative
            if loan_payment < 0 or insurance < 0 or gas < 0 or maintenance < 0:
                raise ValueError("Inputs must be non-negative.")

            # Calculate total monthly cost
            total_monthly_cost = loan_payment + insurance + gas + maintenance

            # Calculate annual cost
            annual_cost = total_monthly_cost * 12

            # Display results
            print(f"\nTotal monthly cost: ${total_monthly_cost:.2f}")
            print(f"Total annual cost: ${annual_cost:.2f}")

            # Return values for further use (optional)
            return total_monthly_cost, annual_cost

        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a valid number.")

# Run the calculator
car_cost_calculator()

