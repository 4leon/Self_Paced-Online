#!/usr/bin/env python3

from datetime import date

donors = {'William Gates, III': [653784.49, 2, 326892.24],
    'Mark ZuckerBerg': [16396.10, 3, 5465.37],
    'Jeff Bezos': [877.33, 1, 877.33],
    'Paul Allen': [708.42, 3, 236.14] }

options = { 1: 'Send Thank You', 2: 'Create a Report', 3:'Send letters to everyone', 4:'Quit'}

def get_key(items):
    """return total donation amount"""
    return items[1]

def write_letter(name, amount):
    msg = []
    msg.append('Dear {},'.format(name))
    msg.append('\n\n\tThank you for your very kind donation of ${:.2f}.'.format(amount))
    msg.append('\n\n\tIt will be put to very good use.')
    msg.append('\n\n\t\t\t\tSincerely,')
    msg.append('\n\t\t\t\t-The Team\n')
    return "".join(msg)

def send_thank_you():
    """This function asks user to enter name and donation amount"""
    full_name = 'Enter a full name (enter Q to main menu): '
    donation_amount = 'Enter donation amount(enter Q to main menu):'
    response = input(full_name)
    # display all donors' names if input is 'list'
    while response == 'list':
        display_donors()
        response = input(full_name)
    # if input is not 'Q' to quit
    if response.upper() != 'Q':
        amount_input = input(donation_amount)
        if amount_input.upper() != 'Q':
            try:
                amount = float(amount_input)
                # go through each donor record
                for name, donation in donors.items():
                    # existing donor
                    if response == name:
                        donation[0] = donation[0] + amount
                        donation[1] = donation[1] + 1
                        donation[2] = donation[2]/donation[1]
                        break
                else:
                    # new donor
                    donors[response] =[amount, 1, amount]
                # thank you email
                print(write_letter(response, amount))
            except ValueError:
                print('Input must be a float.  try again')


def send_letters():
    """Send letters to all donors"""
    for k, v in donors.items():
        letter = write_letter(k, v[0])
       # strip ','
        filename = k.replace(',','')
       # replace space with '_'
        filename = filename.replace(' ', '_')
        # open file to write
        with open('{}-{}{}'.format(filename, str(date.today()),'.txt'), 'w') as thefile:
            thefile.write(letter)

def create_report():
    """Generate report"""
    print("--------------------------------------------------------------")
    print("{:20} | {:10} | {:5} | {:10}".format('Donor Name', 'Total Given', 'Num Gifts', 'Average Gift'))
    print("--------------------------------------------------------------")
    for k, v in sorted(donors.items(), key=get_key, reverse=True):
        a_row = '{:20}  $ {:>10.2f}  {:>10d}  $ {:>11.2f}'.format(k, v[0],v[1],v[2])
        print(a_row)

def display_donors():
    """
    Display donor names
    """
    new_list = [ donor for donor in donors.keys()]
    print(*new_list, sep = "\n")


def quit():
    return 'exit menu'

def display_main_menu():
    """Display main menu"""
    print('Choose an action:')
    options = ['1. Send Thank You', '2. Create a Report', '3. Send letters to everyone', '4. Quit']
    option_str = '\n'.join(['\t'+item for item in options])
    print(option_str)


if __name__ == '__main__':
    choice = ''
    selection = 'Select an option (1, 2, 3, or 4) ===>'
    switch_function_dict = {'1': send_thank_you, '2': create_report, '3': send_letters, '4': quit}
    while True:
        # Display main menu
        display_main_menu()
        try:
            choice = input(selection)
            if switch_function_dict[choice]() == 'exit menu':
                break
        except KeyError:
            print("Please enter 1, 2, 3, or 4")
