def hot_dog_calculator(attendees, hot_dogs_per_person):
    """
    Calculates the number of hot dog and bun packages needed for a cookout with minimal leftovers.

    Args:
        attendees: Number of people attending the cookout (integer)
        hot_dogs_per_person: Number of hot dogs each person will receive (integer)

    Returns:
        A tuple containing:
            hot_dog_packages: Minimum number of hot dog packages required (integer)
            bun_packages: Minimum number of bun packages required (integer)
            hot_dog_leftovers: Number of hot dogs leftover after serving (integer)
            bun_leftovers: Number of buns leftover after serving (integer)
    """

    # First, let us validate the input parameters
    if attendees <= 0:
            raise ValueError("Number of attendees must be greater than 0.")
    if hot_dogs_per_person <= 0:
        raise ValueError("Number of hot dogs per person must be greater than 0.")

    # We have 2 contants in the question, let us define them
    HOT_DOGS_PER_PACKAGE = 8
    BUNS_PER_PACKAGE = 12

    # First, what is the otal number of hotdogs
    total_hot_dogs = attendees * hot_dogs_per_person

    # First, let us calculate hot dog packages and leftovers (using ceiling division)
    hot_dog_packages = -(-total_hot_dogs // HOT_DOGS_PER_PACKAGE)
    hot_dog_leftovers = hot_dog_packages * HOT_DOGS_PER_PACKAGE - total_hot_dogs


    # Now we calculate bun packages and leftovers (using ceiling division)
    bun_packages = -(-total_hot_dogs // BUNS_PER_PACKAGE)
    bun_leftovers = bun_packages * BUNS_PER_PACKAGE - total_hot_dogs

    # We are done with the function, return the results
    return (
        hot_dog_packages,
        bun_packages,
        hot_dog_leftovers,
        bun_leftovers
    )

# Example usage of the function with user input
attendees = int(input("Enter the number of people attending: "))
hot_dogs_per_person = int(input("Enter the number of hot dogs per person: "))

hot_dog_packages, bun_packages, hot_dog_leftovers, bun_leftovers = hot_dog_calculator(
    attendees, hot_dogs_per_person
)

print(f"Minimum hot dog packages: {hot_dog_packages}")
print(f"Minimum bun packages: {bun_packages}")
print(f"Hot dog leftovers: {hot_dog_leftovers}")
print(f"Bun leftovers: {bun_leftovers}")
