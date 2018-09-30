
#VARIABLES
donor_list_with_donations = [["Carlos Santos", 25.00, 50.00, 100.00],["Esperanza Gomez", 10.00, 20.00, 30.00], ["Paul Jackson", 5.00, 10.00, 15.00], ["Karl Black", 100.00, 200.00, 3000.00], ["Charles Exx", 15.00, 30.00, 45.00] ]

"""
FUNCTIONS NEEDED FOR SCRIPT TO RUN
"""
def get_name():
    """get donor name from user"""
    name = input("Enter the full name of the donor.")
    return name

def show_donor_list():
    """Create list of donor names only. Display list of all donors"""
    donor_names = []
    for i in donor_list_with_donations:
        donor_names.append(i[0])
    print(donor_names)

def check_list(x):
    """takes users input name as arg. checks donor list to see if name is there. Returns true if it is. False if the name is not on the list"""
    for i in donor_list_with_donations:
        if x == i[0]: 
            return True
        else:
            return False
 
def get_amount():
    """Gets donation amount from user"""
    amount = input("Enter the donation amount:")
    amount = float(amount)
    return amount

def add_to_existing_donor(d, a):
    """adds donation amount to donor in list. d is donor name. a is amount of donation"""
    for i in donor_list_with_donations:
                if i[0] == d:
                    i.append(a)
    

def create_new_donor(d):
    """Creates a new donor list. adds new list to current donor list"""
    new_donor_list=[]
    new_donor_list.append(d)
    donor_list_with_donations.append(new_donor_list)

   
def print_email(d, a):
    """Prints an email using donor name and donation amount"""
    email = "\nDear {:s}, \n Thank you for your generous donation of ${:.2f}. We appreciate your support. \n Sincerely,\n Mailroom".format(d,a)
    print(email)

def tail(x):
    """Get the tail indexes- everything after 0"""
    return x[1:]

def print_row():
    
    for i in copy_donors:
        name = i[0]
        rest = tail(i)
        num_gifts =len(i)
        total = sum(rest)
        average = total / num_gifts
        average = round(average,2)
      

        row = "{:<25}   ${:^20}   {:10}   ${:>20}".format(name,total,num_gifts,average)
        print(row)
        



def menu():
    print("Welcome to mailroom program")
    response = input("Please enter a number \n (1) Send a thank you \n (2) Create Report \n (3) Quit")
    if response == "1":
        thankyou()
    elif response =="2":
        create_report()
    elif response == "3":
        print("Good-bye")
        SystemExit(0)
    else:
        print("Invalid entry")
        menu()


#thank you function gets a donors name and amount of donation. then prints out a thank you email
def thankyou():
    donorName = get_name()
    while donorName == "list":
        show_donor_list()
        donorName =get_name()

    if check_list(donorName)==True: 
        donation_amount = get_amount()
        add_to_existing_donor(donorName, donation_amount)
        print_email(donorName, donation_amount)

    elif check_list(donorName) == False:
        create_new_donor(donorName)
        donation_amount = get_amount()
        add_to_existing_donor(donorName, donation_amount)
        print_email(donorName, donation_amount)
        menu()
            

def create_report():
    
    heading = "{:<25s} | {:^20s} | {:^10s} | {:^20s} ".format("Donor Name", "Total Given", "Num Gifts", "Average Gift")
    print(heading)
    print("-" * len(heading))
    print_row()
 

if __name__ == '__main__':
    menu()

  
                




        
