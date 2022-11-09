import re

print('This is a calculator that determines the Riemann Sum\n\tfor a finite number of rectangles.\n\nYou can quit the program at any time by entering "end".\n')

# Function to escape the program
def escape():
    print('Thanks for using the Riemann Sum Calculator! Goodbye!')
    quit()

# Calculations for the area under the curve
def right_riemann_sum():
    total_area = 0
    for k in range(rectangles):
        x = left_bound + (k + 1) * delta_x
        total_area += delta_x * eval(function.replace("x", str(x)))
    print('The area under the curve is %s' % total_area)

def left_riemann_sum():
    total_area = 0
    for k in range(rectangles):
        x = left_bound + k * delta_x
        total_area += delta_x * eval(function.replace("x", str(x)))
    print('The area under the curve is %s' % total_area)

def midpoint_riemann_sum():
    total_area = 0
    for k in range(rectangles):
        x = left_bound + ((k + 1) - (delta_x / 2))
        total_area += delta_x * eval(function.replace("x", str(x)))
    print('The area under the curve is %s' % total_area)

while True:
    total_area = 0

    function = input("What is the function? (must be entered in python math syntax for now... sorry! \n\nf(x) = " )
    if function.upper() == "END":
        escape()

    left_bound = input("What is the left bound? ")
    if left_bound.upper() == "END":
        escape()
    #Regex number check
    while re.match(r'(\A\-?\d*\.?\d+$)', left_bound) == None:
        if left_bound.upper() == "END":
            escape()
        print("Please enter only numbers.")
        left_bound = input("What is the left bound? ")
    left_bound = float(left_bound)

    right_bound = input("What is the right bound? ")
    if right_bound.upper() == "END":
        escape()
    while re.match(r'(\A\-?\d*\.?\d+$)', right_bound) == None:
        if right_bound.upper() == "END":
            escape()
        print("Please enter only numbers.")
        right_bound = input("What is the right bound? ")
    right_bound = float(right_bound)

    rectangles = input("How many rectangles do you need? ")
    if rectangles.upper() == "END":
        escape()
    while rectangles == "0":
        if rectangles.upper() == "END":
            escape()
        print('The number of rectangles cannot be 0.')
        rectangles = input("How many rectangles do you need? ")
    while re.match(r'(\A\d+$)', rectangles) == None:
        if rectangles.upper() == "END":
            escape()
        print("Please enter only whole numbers.")
        rectangles = input("How many rectangles do you need? ")
    rectangles = int(rectangles)

    delta_x = (right_bound - left_bound) / rectangles

    # Loop if user wants to use same function
    while 1 == 1:
        total_area = 0
        sum_type = input("Do you need the right, left, or midpoint Riemann sum? ")

        # Forcing user to use desired inputs
        while re.match(r'(LEFT|RIGHT|MIDPOINT|END)', sum_type.upper()) == None:
            print("Just use one of the words, man.")
            sum_type = input("Left, right, or midpoint? ")
        sum_type = sum_type.upper()

        if sum_type == "END":
            escape()
        if sum_type == "RIGHT":
            right_riemann_sum()
        if sum_type == "LEFT":
            left_riemann_sum()
        if sum_type == "MIDPOINT":
            midpoint_riemann_sum()

        another = input("Should we do another? ")
        if another.upper() == "END":
            escape()

        while re.match(r'(YES|NO)', another.upper()) == None:
            if another.upper() == "END":
                escape()
            print('Please enter only "yes" or "no"')
            another = input("Should we do another? ")

        # If user doesn't want to do another, the program closes
        if 'YES'.find(another.upper()) == -1:
            escape()

        same = input("Is it the same function? ")
        if same.upper() == "END":
            escape()

        while re.match(r'(YES|NO)', same.upper()) == None:
            if same.upper() == "END":
                escape()
            print('Please enter only "yes" or "no"')
            same = input("Is it the same function? ")

        if 'YES'.find(same.upper()) == -1:
            break # Breaks loop on line 79, loops to line 33