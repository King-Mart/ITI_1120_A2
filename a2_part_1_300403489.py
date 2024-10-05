import math
import random


def elementary_school_quiz(flag, n):
    """
    Ask the elementary student if he wants to practice exponential or logarithms and give his n random equations of the corresponding time to solve.

    Parameters:
    flag :int: 0 for logarithm, 1 for exponential
    n :int: The number of questions to ask

    Preconditions: flag is 0 or 1, n is 1 or 2

    Returns:
    float: The score of the student
    """
    #Only execute the functions if conditions are met:
    score = 0
    if flag in [0,1] and n in [1,2]:
        #Ask n times
        for i in range(n):
            #Set up the power before hand
            power = random.randint(0,10)
            #If flag is 0 then logarithm will be asked
            if not bool(flag):
                if int(input(f"What is the power put on 2 to reach {2**power}\n : ").strip()) == power:
                    score += 1
            if flag == 1:
                if int(input(f" What is the result of 2 to the power of {power} \n : ").strip()) == 2**power:
                    score += 1
        print(f" You answered {score} questions right.")
    else:
        print("Use supported parameters only!")
    return score/n


def high_school_quiz(a, b, c):
    """
    An absurdly simple functions that outputs the result of the quadratic formula.

    It takes three parameters a, b and c which are the coefficients of the quadratic equation.
    It then prints out the solutions of the equation.

    Parameters:
    a :float: The coefficient of the x^2 term
    b :float: The coefficient of the x term
    c :float: The constant term

    Returns:
    None: No value is returned
    """
    # Calculate the discriminant
    discriminant = b**2 - 4*a*c

    # If the discriminant is less than zero, the equation has no solutions
    if discriminant < 0:
        print(f"The function ({a})x^2+({b})x+({c}) = 0 is satisfied for no value of x")
    # If the discriminant is zero, the equation has one solution
    elif discriminant == 0:
        if b != 0:
            print(f"The function ({a})x^2+({b})x+({c}) = 0 has has one solution at x = {(-b)/(2*a)}")
        else:
            print(f"The function ({a})x^2+({b})x+({c}) = 0 has real roots for all values of x")
    # If the discriminant is greater than zero, the equation has two solutions
    else:
        print(f'''The function ({a})x^2+({b})x+({c}) = 0 has real roots at :
        {(-b+((b**2)-(4*a*c)**0.5))/2} and at :
        {(-b-((b**2)-(4*a*c)**0.5))/2}
        ''')



# main

# your code for the welcome message goes here
greeting = "\n*   __Welcome to the extremely difficult high school quiz! attention decimals MATTER, you will never get a point!__   *"
"""Here is a breakdown of the string list manipulation : 
\n*   __Welcome to the extremely difficult high school quiz! attention decimals MATTER, you will never get a poin!__   * is the main message
now the full star (*) row is the header and the footer in between which we insert the subheader and the prefooter which are the same but with blank spaces i between the initial and the final star. 
In the footer and header we inserted the initial greeting.
In order to insert I used the useful str.join(iterable) function from python to make a brand new string. 
This can easily be implemented inside a lambda function
Thus I leveraged list operations to beautifully resolve this string concatenation problem"""
greeting = (greeting.join(["\n" + (" "*(len(greeting)-3)).join(["*"]*2)]*2)).join(["\n" + "*"*(len(greeting)-1)]*2)
print(greeting)

name=input("What is your name? ")

status=input("Hi "+name+". Are you in? Enter \n1 for elementary school\n2 for high school or\n3 or other character(s) for none of the above?\n")

if status=='1':
    # your code goes here
    grade = elementary_school_quiz(int(input("Do you want to practice logarithms or exponentials (0 for log and 1 for expo) : ")), int(input("One or two questions (You have to answer in numbers)? : "))) * 100
    if grade == 100:
        print(f"Congratulations {name}! You’ll probably get an A tomorrow. Good bye {name}!")
    elif grade == 50:
        print(f"You did ok {name}, but I know you can do better. Goodbye {name}!")
    else:
        print(f"You need some more practice {name} >;( . Goodbye {name}!")
    

elif status=='2':



    flag=True
    while flag:
        question=input(name+", would you like a quadratic equation solved? ").strip().lower()

        # your code to handle varous form of "yes" goes here

        if question!="yes":
            break
        else:
            print("Good choice!")
            # your code goes here (i.e ask for coefficients a,b and c and call)
            # then make a function call and pass to the fucntion
            high_school_quiz(int(input("Enter your a coefficient : ")), int(input("Enter your b coefficient : ")), int(input("Enter your c coefficient : ")))

            # the three coefficients the pupil entered
 
else:
    # your code goes here
    pass

print("Good bye "+name+"!")
