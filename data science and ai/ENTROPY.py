import math

def calculate_entropy(probabilities):
    
    # Calculates the entropy of a possible event based on its probabilities
    entropy = 0
    for p in probabilities:
        if p <= 0 or p >= 1:
            raise ValueError("Invalid probability value: probabilities must be greater than 0 and less than 1.")
        entropy += -p * math.log2(p)
    return entropy

def get_probabilities():

    # Asks the user to enter the probabilities of the event and returns them as a list
    probabilities = []
    while True:
        try:
            num_probabilities = int(input("Enter the number of probabilities you want to enter: "))
            if num_probabilities <= 0:
                raise ValueError("Number of probabilities must be greater than 0.")
            break
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

    for i in range(num_probabilities):
        while True:
            try:
                p = float(input(f"Enter probability {i+1}: "))
                if p < 0 or p > 1:
                    raise ValueError("Probability must be between 0 and 1.")
                probabilities.append(p)
                break
            except ValueError:
                print("Invalid input. Please enter a probability between 0 and 1.")

    return probabilities

while True:
    probabilities = get_probabilities()
    try:
        entropy = calculate_entropy(probabilities)
        print(f"The entropy of the event is {entropy:.2f}.")
    except ValueError as e:
        print(e)
        continue

    answer = input("Do you want to calculate entropy again? (y/n) ").lower()
    if answer != "y":
        break
