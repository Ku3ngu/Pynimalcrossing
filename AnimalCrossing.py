import csv

def create(item_type):
    with open(item_type + ".csv", "a+", newline="") as csvfile:
        fieldnames = [item_type, "price"]
        writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
        writer.writeheader()

create("fish")
create("shell")
create("bug")
create("resource")
create("misc")

run  = True

def program():
    global run
    species = input("What type of item? ('f' for fish, 's' for shell, 'b' for bug, 'r' for resource, 'm' for misc, 'q' for quit) \n")

    def newentry(itemy):
        with open(itemy + ".csv", "a+", newline="") as csvfile:
            fieldnames = [itemy, "price"]
            name = input(f"what type of {itemy}?")
            price = input("how much?")

            writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
            writer.writerow({itemy : name, "price" : price})

##############################################

    if species == "f":
        newentry("fish")

    elif species == "s":
        newentry("shell")

    elif species == "b":
        newentry("bug")

    elif species == "r":
        newentry("resource")

    elif species == "m":
        newentry("misc")

    elif species == "q":
        run = False

    else:
        print("invalid type.")

while run:
    program()