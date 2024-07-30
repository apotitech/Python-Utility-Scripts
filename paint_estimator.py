def paint_estimator(wall_area, paint_price):
    """
    Estimates the resources and cost for a painting job.

    Args:
        wall_area: Area of the walls in square feet (float)
        paint_price: Price of paint per gallon (float)

    Returns:
        A dictionary containing:
            gallons: Gallons of paint required (float)
            paint_cost: Cost of paint (float)
            labor_hours: Estimated labor hours (float)
            labor_cost: Estimated labor cost (float)
            total_cost: Total job cost (float)
    """
    # Validate input
    if wall_area <= 0:
        raise ValueError("Wall area must be a positive number.")
    if paint_price <= 0:
        raise ValueError("Paint price must be a positive number.")

    # Define constants
    PAINT_COVERAGE = 400  # Square feet covered per gallon of paint
    LABOR_RATE = 35  # Dollars per hour of labor

    # Calculate gallons of paint
    gallons = wall_area / PAINT_COVERAGE

    # Calculate paint cost
    paint_cost = gallons * paint_price

    # Estimate labor hours
    labor_hours = wall_area / 100  # Assuming 100 sq ft per hour of painting

    # Calculate labor cost
    labor_cost = labor_hours * LABOR_RATE

    # Calculate total cost
    total_cost = paint_cost + labor_cost

    # Return results as a dictionary
    return {
        "gallons": gallons,
        "paint_cost": paint_cost,
        "labor_hours": labor_hours,
        "labor_cost": labor_cost,
        "total_cost": total_cost
    }

# Example usage with error handling
try:
    wall_area = float(input("Enter the wall area in square feet: "))
    paint_price = float(input("Enter the price of paint per gallon: "))

    estimate = paint_estimator(wall_area, paint_price)

    print(f"Gallons of paint required: {estimate['gallons']:.2f}")
    print(f"Paint cost: ${estimate['paint_cost']:.2f}")
    print(f"Estimated labor hours: {estimate['labor_hours']:.2f}")
    print(f"Estimated labor cost: ${estimate['labor_cost']:.2f}")
    print(f"Total job cost: ${estimate['total_cost']:.2f}")
except ValueError as e:
    print(f"Invalid input: {e}")
