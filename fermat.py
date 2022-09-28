import time

# Defined calculation variable
def calculate():
    x1 = pow(x0, n)
    y1 = pow(y0, n)
    z1 = pow(z0, n)

    xy1 = x1 + y1
    
    if b == 1:
        print(f"{x1} + {y1} --> {xy1} = {z1}")
    
    if (xy1 == z1):
        print("True...? You just disproved Fermat's Theorem!!!\n")
        exit()
    else:
        print("False")
        print(u"\u2501" * 20)
    
    if b == 1:
        if t <= 10:
            time.sleep(1)
    
# Prints a brief explaination of Fermat's theorem
print("\nIn number theory, Fermat's Last Theorem (sometimes called Fermat's conjecture...) states that no three positive integers a, b, and c satisfy the equation a^n + b^n = c^n for any integer value of n greater than 2. The cases n = 1 and n = 2 have been known since antiquity to have infinitely many solutions (Credit: Wikipedia, 2021)\n")
time.sleep(12)

# Input-taking process begins
while True:
    print("Please enter a value for n (exponent):")
    n = input()
    n = int(n)
    if n > 2:
        break
    else:
        print("Nope.")
        time.sleep(1)

while True:
    print("Please enter a value for t (number of trials):")
    t = input()
    t = int(t)
    # This is an optional check (python will return an error when converting 't' to an integer if 't' equals a decimal)
    c = isinstance(t, int)
    if c == True and t > 0:
        break
    else:
        print("Nope.")
        time.sleep(1)

while True:
    print("Do you want to see basic working? (sum and final inequality - y/n)")
    w = input()
    yes = "y"
    no = "n"
    if w == yes:
        b = 1
        break
    elif w == no:
        b = 0
        break
    else:
        print("Nope.")
        time.sleep(1)

# Prints a horizontal line for organization
print(u"\u2501" * 20)

# Defining initial values for x, y, and, z
x0 = 1
y0 = 1
z0 = 1

# Manipulating variables and solving the theorem's equation
for i in range(t):
    
    # 1 + 1 = 1
    calculate()

    # 2 + 1 = 1
    x0 += 1
    calculate()

    # 2 + 2 = 1    
    y0 += 1
    calculate()

    # 2 + 2 = 2
    z0 += 1
    calculate()

    # 1 + 2 = 2
    x0 -= 1
    calculate()

    # 1 + 1 = 2
    y0 -= 1
    calculate()
    z0 -= 1

    # Prints another horizontal line after each set of solved equations of each increment in the values
    print(u"\u2501" * 20)

    # Incrementing all of the variables for the next iteration
    x0 += 1
    y0 += 1
    z0 += 1
