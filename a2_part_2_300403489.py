def min_enclosing_rectangle(radius : float, x :float, y :float) -> tuple:
    """
    This function returns the coordinates of the top-left corner of the smallest rectangle
    containing a given circle with a given radius and center (x,y)

    Parameters:
    radius (float): the radius of the circle
    x (float): the x coordinate of the center
    y (float): the y coordinate of the center

    Returns:
    tuple: a tuple of two floats containing the x and y coordinates of the top-left corner
    """
    # calculate the x and y of the top-left corner of the rectangle
    # the x and y are the center coordinates minus the radius
    x_bl = x - radius
    y_bl = y - radius

    # return the coordinates
    return x_bl, y_bl

def calculate_vote_percentage(merged_bulletins: str) -> float:
    """Calculate the percentage of people that voted yes.

    Args:
        merged_bulletins (str): The merged bulletins containing a certain amount of yes or no and arbitrary useless values.

    Returns:
        float: The percentage of people that voted yes.
    """
    # Count the number of yes and no and calculate the percentage
    yes_count = merged_bulletins.count("yes")
    no_count = merged_bulletins.count("no")
    total = yes_count + no_count

    # Test for edge case in which there are no yes or no's (division by zero error)
    if total == 0:
        return 0.0
    else:
        return yes_count / total

def vote():
    """This function will calculate the percentage of people that voted yes using a  merged bulletin typed in by the user
    
    It will then print out whether the proposal passed or not, and with which majority.

    Returns:
    None: No value
    """
    # Ask the user for the merged bulletin
    merged_bulletins = input("Please enter the merged bulletin: (yes/no/abstained) ")
    # Calculate the vote percentage and print it
    yesVotes = calculate_vote_percentage(merged_bulletins)
    if yesVotes == 1:
        print("proposal passes unanimously")
    elif yesVotes >= (2/3):
        print("proposal passes with super majority")
    elif yesVotes >= 0.5:
        print("proposal passes with majority")
    else:
        print("proposal fails")
        
def l2lo(w : float):
    """
    This function takes a non-negative number w as input and returns a pair of numbers (l,o) such that w = l + o/16 and l is
    an integer and o is a non-negative number smaller than 16.

    Parameters:
    w : float: a non-negative number

    Returns:
    tuple: a tuple of two numbers (l,o) such that w = l + o/16 and l is an integer and o is a non-negative number smaller
    than 16

    """

    #We et l as the whole part and 0 as the decimal and add both (easy!)
    l = int(w)
    #In order to respect the / by 16 part, we do the mathematical opposite which is * 16
    o = 16 * (w - l)
    return l, o
#Testing the  min_enclosing_rectangle function

radius = float(input("Please enter the radius of the circle: "))
x = float(input("Please enter the x coordinate of the center: "))
y = float(input("Please enter the y coordinate of the center: "))

print(min_enclosing_rectangle(radius, x, y))
 