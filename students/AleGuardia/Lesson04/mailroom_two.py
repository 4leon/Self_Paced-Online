#!/usr/bin/env python3
"""Takes donor and donation information and sends thank you notes. Adds donors and donations and reports it"""

# Lesson 3 Mailroom Assignment by Alejandro Guardia

donations = {'William Gates, III': [1000000, 585000, 5750000],
             'Mark Zuckerberg': [15000, 5000],
             'Jeff Bezos': [3000000],
             'Paul Allen': [25000,1000],
             'Elon Musk': [30000,3499]}


main_responses = {1:"1 - Send a Thank You\n", 2:"2 - Create a Report\n", 3:"3 - quit\n"}
main_prompt = f"Please choose one of the following:\n" \
              f"{main_responses[1]}{main_responses[2]}{main_responses[3]}"
thank_you_note = "Dear {}:\nWe want to thank you for your generous donation of ${:.2f}"


def return_average(seq):
    """Takes a sequence and returns the average"""
    return sum(seq)/len(seq)


def return_label():
    """Builds and returns a table row label"""
    label ="{:18} | {:>12} | {:>9} | {:>12}\n".format('Donor Name','Total Given','Num Gifts','Average Gift')
    label += "-"*len(label)
    return label


def return_report(data):
    """Creates and prints a report of donors and donations"""
    report = f"{return_label()}\n"
    for item in data:
        row = "{:18} $ {:>12.2f}  {:>9d}  $ {:>12.2f}\n".format(item,sum(data[item]),len(data[item]),return_average(data[item]))
        report += row
    return report


def return_donors():
    """Returns the names of all donors"""
    donors = ""
    for item in donations:
        donors += item + "\n"
    return donors


def prompt_donors():
    """Prompt donor name and adds donor and donations"""
    name = input("Please enter a donor name: ")
    if name == 'quit':
        return None
    if name == 'list':
        print(return_donors())
        return prompt_donors()
    if name in return_donors():
        send_note(name,add_donation(name),thank_you_note)
    if name not in return_donors():
        add_donor(name)
        send_note(name,add_donation(name),thank_you_note)


def add_donor(name):
    """Adds a donor name"""
    donations[name] = []
    return donations


def add_donation(name):
    """Takes the name of a donor and adds a donation on his behalf"""
    amount = float(input("Please enter a donation amount for {}:".format(name)))
    donations[name].append(float(amount))
    return amount


def send_note(name,donation,note):
    """Takes a donor name,donation amount and a note and sends the note to the donor"""
    print()
    print(note.format(name,donation))
    print()


def menu_selection(prompt, dispatch_dict, key_def=None):
    while True:
        response = input(prompt)
        try:
            if dispatch_dict[response]() == "quit":
                break
        except KeyError:
            if not callable(key_def):
                pass
            else:
                key_def()


def print_report():
    print()
    print(return_report(donations))


def quit_sys():
    return "quit"


main_dispatch = {"1": prompt_donors, "2": print_report, "3": quit_sys}


if __name__ == '__main__':
    menu_selection(main_prompt,main_dispatch)


