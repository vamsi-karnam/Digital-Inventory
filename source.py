import time
import csv
import os

# intro function here
def intro(name):
    print(""" Hi {} Welcome to Digital Inventory by Vamsi,
    I know, I know, you and me both! We keep forgetting where stuff is or wait too late and the snacks expire,
    Yeah all that sort, I know right! It's the worst! 
    Let's see if we can do something about that, 
    Assuming you are in your usual seating position infront of your work desk.""". format(name))

    for i in range(5):
        print(".", end="", flush=True)
        time.sleep(0.5)
    print("")    
    print("Lets get started with the number of storage areas and their locations you have around you")


def confirmation(section):
    conf = input("Do you confirm? Y/N \n")
    if conf=="Y" or conf=="y":
        print("Let's move to the next storage section")
        print("!! Warning: Selecting the same section again will overwrite previous values !!")
        for i in range(5):
            print(".", end="", flush=True)
            time.sleep(0.5)
        main()
    else:
        section()


def storage(sections):
        section_dict = {}
        for i in range(1,sections):
            section_dict["Section {0}".format(i)] = input("""What kind of items do you like to keep in section {0}?
            1. Stationery
            2. Books
            3. Food
            4. Medicines
            5. Electronic accessories
            6. Hardware tools .... 
            or type whatever you keep in as much detail as you'd like to remember \n""".format(i))

            outfile = open("out.csv", "a")
            
            writer = csv.writer(outfile)
            writer.writerow(section_dict.keys())
            writer.writerow(section_dict.values())


        print(section_dict) #Try adding the outputs to a Database and remove dicts.



def overhead_choice():
    try:
        overhead_sections = int(input("How many sections are present in the overhead storage? Enter numerical: \n"))
        overhead_sections+=1
        if overhead_sections >= 1:
                print("Lets go left to right \n")
                for i in range(5):
                    print(".", end="", flush=True)
                    time.sleep(0.5)
                print("This is your overhead storage area (left to right)")
                storage(overhead_sections)
                print("..............................")
                confirmation(overhead_choice)
    except:
        cont = input("You have entered a wrong input, Do you want to continue? Y/N \n")
        if cont=="Y" or cont=="y":
            print("Enter numerical and try again: \n")
            overhead_choice()
        else:
            quit()


def underdesk_choice():
    try:
        underdesk_sections = int(input("How many sections are present in the underdesk storage? Enter numerical: \n"))
        underdesk_sections+=1
        if underdesk_sections >= 1:
                print("Lets go left to right \n")
                for i in range(5):
                    print(".", end="", flush=True)
                    time.sleep(0.5)
                print("This is your underdesk storage area (left to right)")
                storage(underdesk_sections)
                print("..............................")
                confirmation(underdesk_choice)
    except:
        cont = input("You have entered a wrong input, Do you want to continue? Y/N \n")
        if cont=="Y" or cont=="y":
            print("Enter numerical and try again: \n")
            underdesk_choice()
        else:
            quit()


def ondesk_choice():
    try:
        ondesk_sections = int(input("How many sections do you want to divide your work desk into? Enter numerical: \n"))
        ondesk_sections+=1
        if ondesk_sections >= 1:
                print("Lets go left to right \n")
                for i in range(5):
                    print(".", end="", flush=True)
                    time.sleep(0.5)
                print("These are the items on your desk (left to right)")
                storage(ondesk_sections)
                print("..............................")
                confirmation(ondesk_choice)
    except:
        cont = input("You have entered a wrong input, Do you want to continue? Y/N \n")
        if cont=="Y" or cont=="y":
            print("Enter numerical and try again: \n")
            ondesk_choice()
        else:
            quit()


def main():
    print(".......................................")
    print("""Pick the corresponding number:
    1. Over head
    2. Under desk
    3. on the desk
    4. Done saving""")
    storage_type = input("Choose storage type you want to enter: \n")
    print("........................................")

    if (storage_type == "1"):
        print("You chose overhead")
        print("....................")
        overhead_choice()
    elif (storage_type == "2"):
        print("You chose under desk")
        print("....................")
        underdesk_choice()  
    elif (storage_type == "3"):
        print("You chose your work desk")
        print("....................")
        ondesk_choice()
    elif (storage_type == "4"):
        print("Nice work! Out.csv has your storage areas divided into sections with your items in it.....")
        os.startfile("out.csv")
        print("Let's see what other features are going to be added soon......")
        print("Making this program into an application, Database sytem to store your items in real-time, Machine learning features (Experimental), Expiry date for food etc....")
        quit()



# Code runs from here
csvfile = open("out.csv", "w")
csvfile.truncate(0)
name = input("Hey whats your name? \n")
intro(name)
main() # Main starts here