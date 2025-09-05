# Function 1: Calculate the height of the ball after time t
# This function should take the initial height h0 and time t as inputs, and return the height at time t.
# Round up to one decimal point
def calculate_height(h0, t):
    # TODO: Implement this function
 # State the formula
print("The formula for the height of the ball at time t is: h(t) = h_0 - 0.5 * g * t^2")

# Define each variable
print("\nVariable definitions:")
print("h(t): height of the ball at time t (meters)")
print("h_0: initial height from which the ball is dropped (meters)")
print("g: acceleration due to gravity (approximately 9.8 m/s^2)")
print("t: time elapsed since the ball was dropped (seconds)")

# Outline the calculation steps
print("\nSteps to calculate h(t):")
print("1. Identify the values for the initial height (h_0), acceleration due to gravity (g), and the time elapsed (t).")
print("2. Substitute these values into the formula: h(t) = h_0 - 0.5 * g * t^2.")
print("3. Calculate the term 0.5 * g * t^2.")
print("4. Subtract the result from h_0 to get the height at time t (h(t)).")

g= 9.8
h_0= float(input("Enter initial height:"))
t= float(input("Enter time: "))
h = h_0 - 0.5 * g * (t ** 2)
calculated_height = round(h, 1)
print("Height of the ball at time",t, "seconds =",calculated_height,"meters") 

# Function 2: Calculate the distance traveled by the car
# This function should take the time t as input and return the distance traveled by the car.
def calculate_car_distance(t):
    # TODO: Implement this function
    pass  # Replace with your code
