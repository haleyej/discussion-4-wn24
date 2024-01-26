import math

class Rectangle():
    # Create the constructor "__init__" method
    # Arguments: width (an ingeter), height (an integer)
    # 
    # It sets an instance variable, "width" to the passed argument, width
    # It sets an instance variable, "height" to the passed argument, height

    # YOUR CODE HERE



    # Create the "__str__" method
    #
    # It returns a string, 
    #       "A rectangle with width ____ and height ____"

    # YOUR CODE HERE



    # Create the "describe_shape" method 
    #
    # It returns a string 
    # If the width is greater than the height, return "width is greater than height"
    # If the height is greater than the width, return "height is greater than width"
    # If the width and height are the same, return "width and height are equal, it is a square"

    # YOUR CODE HERE

    # Create the "calculate_area" method
    #
    # Returns the area of the rectangle (float)

    # YOUR CODE HERE


    # Create the "calculate_diagonal_length" method
    # 
    # The length of the diagonal of a rectangle is sqrt(width ^ 2 + length ^ 2)
    # Returns the length of the diagonal 
    # HINT: use math.sqrt() to get the square root of a number / mathemtical expression

    


def main():
    r = Rectangle(10, 10)
    print(r)
    print("Shape Description", r.describe_shape())
    print("Area:", r.calculate_area())
    print("Diagonal Length:", r.calculate_diagonal_length())
    print()

    r = Rectangle(10, 15)
    print(r)
    print("Shape Description", r.describe_shape())
    print("Area:", r.calculate_area())
    print("Diagonal Length:", r.calculate_diagonal_length())
    print()

    # you can create additional rectangle objects to 
    # test your code or learn more about how the class behaves

if __name__ == "__main__":
    main()