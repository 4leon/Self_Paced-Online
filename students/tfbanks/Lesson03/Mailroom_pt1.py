# mailroom_pt1.py Exercise by tfbanks

# !/usr/bin/env python3

# Donor Database containing names and donations
donor_db = [
    ['Tim Cooker', 1500.50, 25050.50, 15680.75],
    ['Elon Musket', 5250.25, 26500],
    ['Frank Petersmankempt', 550.60],
    ['Megan Morgan', 650.40, 1600, 20625.40],
    ['Marlene Wheeler', 820, 1222.80]
]

donor = []
for dname in donor_db:
    d = dname[0]
    donor.append(d)


def thank_you():  # Coded out to focus on the report part
    ty_donor = input('Enter the Full Name of a donor (for list of previous donors type list): ')

    if ty_donor.title() == 'List':
        print(donor)
        thank_you()
    elif ty_donor.title() in donor:
        d_name = donor.index(ty_donor.title())
        amount = float(input('Please enter the donation amount: '))
        donor_db[d_name].append(amount)
        print('\n\nDear {},\n'
              '\nThank you for your additional generous donation of ${}, your generosity is so greatly appreciated.\n'
              'We are pleased to have you continue to help in our effort to teach Python to the next generation.\n'
              '\nSincerely,\n'
              '\nJoesef Edword Bringingham\n\n'.format(ty_donor, amount))

        what_to_do_2()
    elif ty_donor.title() not in donor:
        donor.append(ty_donor.title())
        new_donor = []
        amount = float(input('Please enter the donation amount: '))
        new_donor.append(ty_donor.title())
        new_donor.append(amount)
        donor_db.append(new_donor)
        print('\n\nDear {},\n'
              '\nThank you for your generous donation of ${}, your generosity is greatly appreciated.\n'
              'These funds will help insure that our efforts to teach Python to the next generation.\n'
              '\nSincerely,\n'
              '\nJoesef Edword Bringingham\n\n'.format(ty_donor, amount))
        what_to_do_2()


def report():
    print('Donor Name            |  Total Given | Num Gifts |  Average Gift')
    print('------------------------------------------------------------------\n')
    donor_names = []
    total_given = []
    num_gifts = []
    average_gift = []
    for donor in donor_db:
        name = donor[0]
        count_gifts = len(donor) - 1
        sum_total = sum(donor[1:])
        avg_gift = sum_total / count_gifts
        donor_names.append(name)
        total_given.append('{:.2f}'.format(sum_total))
        num_gifts.append(count_gifts)
        average_gift.append('{:.2f}'.format(avg_gift))
    for p in range(len(donor_names)):
        print(f'{donor_names[p]:<22s}  ${total_given[p]:>13}   {num_gifts[p]:^8}    ${average_gift[p]:>12}')
    print('\n')
    what_to_do_3()


def what_to_do():
    answer = input('What would you like to do? Send an Thank You note? (n), Create a report (r), or Quit (q): ')
    while answer.title() not in ['N', 'R', 'Q']:
        answer = input('What would you like to do? Send an Thank You note? (n), Create a report (r) or Quit (q): ')
    if answer.title() == 'N':
        print('\n')
        thank_you()
    if answer.title() == 'R':
        print('\n')
        report()
    if answer.title() == 'Q':
        print('Have a nice day')
        quit()


def what_to_do_2():
    answer = input(
        'Anything else you would like to do? Send another Thank You note? (n), Create a report (r), or Quit (q): ')
    while answer.title() not in ['N', 'R', 'Q']:
        answer = input(
            'Anything else you would like to do? Send another Thank You note? (n), Create a report (r), or Quit (q): ')
    if answer.title() == 'N':
        thank_you()
    if answer.title() == 'R':
        report()
    if answer.title() == 'Q':
        print('Have a nice day')
        quit()


def what_to_do_3():
    answer = input(
        'Anything else you would like to do? Send an Thank You note? (n), Create another report (r), or Quit (q): ')
    while answer.title() not in ['N', 'R', 'Q']:
        answer = input(
            'Anything else you would like to do? Send an Thank You note? (n), Create another report (r), or Quit (q): ')
    if answer.title() == 'N':
        thank_you()
    if answer.title() == 'R':
        report()
    if answer.title() == 'Q':
        print('Have a nice day')
        quit()


if __name__ == '__main__':
    what_to_do()
