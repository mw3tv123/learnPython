"""Write a program to solve a classic ancient Chinese puzzle: We count 35 heads and 94 legs among the chickens and
rabbits in a farm. How many rabbits and how many chickens do we have? ET 30m """

head = int(input(">>>Enter number of head: "))
leg = int(input(">>>Enter number of leg: "))
for chicken in range(head+1):
    rabbit = head - chicken
    if (2 * chicken) + (4 * rabbit) == leg:
        print("With {} heads and {} legs we can have {} chicken and {} rabbits!".format(head, leg, chicken, rabbit))
        break
