# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 13:06:38 2018

@author: Laura.Fiorentino
"""
donor_list = {
    'Frank Reynolds': [10, 20, 50],
    'Dee Reynolds': [25, 100],
    'Dennis Reynolds': [10, 50],
    'Mac McDonald': [25, 35, 20],
    'Charlie Kelly': [0.25]
    }


def write_email(name, donation):
    print('Email Creation:')
    print('Dear {}, \n'
          'Thank you so much for your generous donation of ${:.2f} \n'
          'Sincerely, \n'
          'Laura F'.format(name, donation))


def create_email():
    while True:
        name = input("Type full donor name, or ''list'' for choices?>")
        if name.lower() == 'list':
            print(donor_list.keys())
        elif name not in donor_list:
            donor_list[name] = []
            donation = input("Donation Amount?>")
            donation = float(donation)
            donor_list[name] = [donation]
            write_email(name, donation)
            break
        else:
            donation = input("Donation Amount?>")
            donation = float(donation)
            donor_list[name].append(donation)
            write_email(name, donation)
            break


def create_report():
    print('-------List of Donors-------')
    print('{:<20}{:<20}{:<20}{:<20}'.format('Donor Name', 'Total Donated',
                                            '# of donations',
                                            'Average donation'))
    print('-----------------   '*4)
    for it in range(0, len(donor_list), 2):
        print('{:<20}${:<20.2f}{:<20d}${:<20.2f}'.format(donor_list[it],
                                                         sum(donor_list[it+1]),
                                                         len(donor_list[it+1]),
                                                         sum(donor_list[it+1])
                                                         / len(donor_list[it+1]
                                                               )))


def main():
    print('----------Mailroom------------')
    while True:
        task = input("Choose an action: [1] Send a Thank You; [2] Create a \
Report; [3] Quit>")
        arg_dict = {'1': create_email, '2': create_report}
        if task in arg_dict.keys():
            arg_dict.get(task)()
        elif task == '3':
            break
        else:
            continue


if __name__ == '__main__':
    main()
