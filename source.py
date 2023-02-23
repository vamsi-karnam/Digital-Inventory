import time

print("""Welcome to Digital Inventory by Vamsi,
I know, I know, you and me both! We keep forgetting where stuff is or wait too late and the snacks expire,
Yeah all that sort, I know right! It's the worst! 
Let's see if we can do something about that, Assuming you are in your usual seating position infront of your work desk.""")

for i in range(5):
    print(".", end="", flush=True)
    time.sleep(0.5)
print("")    

print("Lets get started with the number of storage areas and their locations you have around you")


def confirmation(section):
    conf = input("Do you confirm? Y/N \n")
    if conf=="Y" or conf=="y":
        print("Let's move to the next storage section")
        for i in range(5):
            print(".", end="", flush=True)
            time.sleep(0.5)
    else:
        section()
        
def overhead(sections):
        overhead_dict = {}
        for i in range(1,sections):
            overhead_dict["Section {0}".format(i)] = input("""What kind of items do you like to keep in section {0}?
            1. Stationery
            2. Books
            3. Food
            4. Medicines
            5. Electronic accessories
            6. Hardware tools .... 
            or type whatever you keep in as much detail as you'd like to remember \n""".format(i))
        print(overhead_dict)


def overhead_choice():
    try:
        overhead_sections = int(input("How many sections are present in the overhead storage? Enter numerical: \n"))
        overhead_sections+=1
        if overhead_sections >= 1:
                print("Lets go left to right \n")
                for i in range(5):
                    print(".", end="", flush=True)
                    time.sleep(0.5)
                overhead(overhead_sections)
                print("..............................")
                ("This is your overhead storage area (left to right)")
                confirmation(overhead_choice)
    except:
        cont = input("You have entered a wrong input, Do you want to continue? Y/N \n")
        if cont=="Y" or cont=="y":
            print("Enter numerical and try again: \n")
            overhead_choice()
        else:
            quit()


over_head = input("Is there any storage overhead? Y/N \n")
if (over_head=="Y" or over_head=="y"):
    overhead_choice()