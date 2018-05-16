#!/usr/bin/env python3
"""Mail Room Functional Programming Module

This module contains all of the functions for the functional programming
Mail Room module.
"""

import datetime
from collections import defaultdict

SELECT_PROMPT = ('\nPlease select from the following options:\n'
                 '\t1. Send a Thank You\n'
                 '\t2. Create a Report\n'
                 '\t3. Send letters to all donors\n'
                 '\t4. Create contribution projection\n'
                 '\t5. quit\n'
                 ' --> ')
PROMPT_OPTS = (1, 2, 3, 4, 5)


class Donor:
    """Contains all information for a single donor"""
    def __init__(self, name, donations=None):
        if not donations:
            donations = []

        self.name = str(name)
        self._donations = list(donations)
        self._total = sum(self._donations)
        self._ave = self._total / len(self._donations) if donations else 0

    @property
    def donations(self):
        """Get list of donations for this donor"""
        return self._donations

    @property
    def num_donations(self):
        """Get number of donations given by this donor"""
        return len(self._donations)

    @property
    def total_donations(self):
        """Get total amount of donations given by this donor"""
        return self._total

    @property
    def average_donations(self):
        """Get average donation amount for this donor"""
        return self._ave

    def add_donation(self, amount):
        """Add donation to this donor's donation history

        Args:
            donation (int): donation amount
        """
        self._donations.append(amount)
        self._total += amount
        self._ave = self._total / self.num_donations


class DonorDatabase(defaultdict):
    """A database of Donors"""
    def __init__(self, *donors):
        if not donors:
            donors = []

        super().__init__(Donor, {d.name: d for d in donors})
        self.min_col_width = 12
        self.def_pad = 7
        self.col_sep = ' | '
        self.cols = ['Donor Name', 'Total Given', 'Num Gifts', 'Average Gift']
        self.thank_you_fmt = ('\nDear {:s},\n'
                              'Thank you for your generous donation of ${:,.2f}.\n'
                              '\t\tSincerely,\n'
                              '\t\t  -Your conscience')

    def __missing__(self, key):
        if self.default_factory is None:
            raise KeyError(key)
        else:
            ret = self[key] = self.default_factory(key)
            return ret

    def create_report(self):
        """Generate report of all donors and donations in database."""
        sorted_dnr_keys = sorted(self,
                                 key=lambda d: self[d].total_donations,
                                 reverse=True)

        max_name = len(max([dnr for dnr in self], key=len)) + self.def_pad
        max_total = len(max([str(d.total_donations)
                             for d in self.values()], key=len)) + self.def_pad
        max_gifts = len(max([str(d.num_donations)
                             for d in self.values()], key=len)) + self.def_pad
        max_ave = max_total

        if max_name < self.min_col_width:
            max_name = self.min_col_width
        if max_total < self.min_col_width:
            max_total = max_ave = self.min_col_width
        if max_gifts < self.min_col_width:
            max_gifts = self.min_col_width

        hdr_fmt = (f'\n{{:^{max_name}s}}{self.col_sep}{{:^{max_total}s}}'
                   f'{self.col_sep}{{:^{max_gifts}s}}{self.col_sep}'
                   f'{{:^{max_ave}s}}\n' +
                   '-' * (max_name + max_total + max_gifts + max_ave +
                          len(self.col_sep) * 3) +
                   '\n')

        row_fmt = (f'{{:<{max_name}s}}{self.col_sep}${{:>{max_total - 1},.2f}}'
                   f'{self.col_sep}{{:>{max_gifts}d}}{self.col_sep}'
                   f'${{:>{max_ave - 1},.2f}}')

        header = hdr_fmt.format(*self.cols)

        rows = [row_fmt.format(dnr, self[dnr].total_donations,
                               self[dnr].num_donations,
                               self[dnr].average_donations)
                for dnr in sorted_dnr_keys]

        return header + '\n'.join(rows)

    def send_letters(self):
        """Create a letter for each donor and write to disk as a text file"""
        now = datetime.datetime.today().strftime('%m-%d-%Y')

        for donor, data in self.items():
            f_name = f'{donor.replace(" ", "_")}_{now}.txt'
            with open(f_name, 'w') as f:
                f.write(self.thank_you_fmt.format(donor, data.total_donations))

    def challenge(self, factor, min_don=None, max_don=None):
        """Return a new database with all donations multiplied by the factor
           value if within the specified min and max donation range.

        Args:
            factor (float): Factor value
            min_don (float, optional): Defaults to None. Min donation value
            max_don (float, optional): Defaults to None. Max donation value

        Returns:
            DonorDatabase: New DonorDatabase with factor value applied
        """
        new_donors = []
        for donor in self.values():
            new_donors.append(Donor(donor.name,
                                    self.filter_and_factor(factor,
                                                           donor.donations,
                                                           min_don=min_don,
                                                           max_don=max_don)))
        return DonorDatabase(*new_donors)

    def projection(self, factor, min_don=None, max_don=None):
        """Return projection for a contribution that multiplies all current
        donations by 'factor' that are within the specified min and max
        donation range, if specified.

        Args:
            factor (float): Factor value
            min_don (float, optional): Defaults to None. Min donation value
            max_don (float, optional): Defaults to None. Max donation value

        Returns:
            float: Projected contribution value
        """
        projection = 0
        for donor in self.values():
            projection += sum(self.filter_and_factor(factor,
                                                     donor.donations,
                                                     min_don=min_don,
                                                     max_don=max_don))
        return projection

    @staticmethod
    def filter_and_factor(factor, donations, min_don=None, max_don=None):
        """For each donation, multiply by the factor value if the donation is
           within the min and max donation range, if set.

        Args:
            factor (float): Factor value
            donations (list): List of donations to filter and factor
            min_don (float, optional): Defaults to None. Min donation value
            max_don (float, optional): Defaults to None. Max donation value

        Raises:
            ValueError: Min donation value is greater than max value

        Returns:
            list: New list of filtered and factored donations
        """
        if min_don and max_don:
            if min_don > max_don:
                raise ValueError('Min donation value is greater than max')

            return list(map(lambda x: x * factor,
                            filter(lambda d: min_don <= d <= max_don, donations)))
        elif min_don:
            return list(map(lambda x: x * factor,
                            filter(lambda d: d >= min_don, donations)))
        elif max_don:
            return list(map(lambda x: x * factor,
                            filter(lambda d: d <= max_don, donations)))
        else:
            return list(map(lambda x: x * factor, donations))


def get_usr_input():
    """Get input from user.

    Prompt user to select one of three choices. If the user selects one of
    these three, that value is returned. If not, the user is prompted again to
    select.

    Returns:
        int: Value corresponding to user choice
    """
    usr_in = None
    while usr_in not in PROMPT_OPTS:
        try:
            usr_in = int(input(SELECT_PROMPT))
        except ValueError:
            print(f'\nPlease try again. Valid options are: {PROMPT_OPTS}')
        else:
            if usr_in not in PROMPT_OPTS:
                print(f'\nPlease select a number between {PROMPT_OPTS[0]}'
                      f' and {PROMPT_OPTS[-1]}')

    return usr_in


def prompt_for_donor(prompt, donor_db):
    """Prompt user to enter a donor name.

    Allows user the additional options of:
     - 'quit': quit donor prompt
     - 'list': list all current donors

    Args:
        prompt (str): String to prompt user with.
        donor_db (DonorDatabase): Database instance containing all donors

    Returns:
        str: Donor name.
    """
    donor = None

    while not donor:
        usr_in = input(prompt).strip().lower()

        if usr_in.startswith('q'):
            break
        elif usr_in == 'list':
            print()
            for name in donor_db:
                print(name.title())
        else:
            donor = " ".join([name.title() for name in usr_in.split()])

    return donor


def prompt_for_float(prompt, error_prompt):
    """Prompt for user contribution factor

    Args:
        prompt (str): String to prompt user with.
        error_prompt (str): Error response to invalid user input.

    Returns:
        float: Factor value
    """
    val = None

    while not val and val != 0.0:
        usr_in = input(prompt).strip().lower()

        if usr_in.startswith('q'):
            break
        else:
            try:
                val = float(usr_in)
            except ValueError:
                print(error_prompt)

    return val


def send_thank_you(donor_db):
    """Send a thank you.

    Prompt for a Full Name.
    If the user types ‘list’, show them a list of the donor names and re-prompt
    If the user types a name not in the list, add that name to the data
    structure and use it.
    If the user types a name in the list, use it.
    Once a name has been selected, prompt for a donation amount.
    Turn the amount into a number – it is OK at this point for the program to
    crash if someone types a bogus amount.
    Once an amount has been given, add that amount to the donation history of
    the selected user.
    Finally, use string formatting to compose an email thanking the donor for
    their generous donation. Print the email to the terminal and return to the
    original prompt.

    Args:
        donor_db (DonorDatabase): Database instance containing all donors
    """
    name_prompt = ('\nPlease enter name of "Thank You" recipient:\n'
                   '(Enter "list" to see all donors)\n'
                   '(Enter "quit" to return to main menu)\n'
                   ' --> ')
    amount_prompt = ('\nPlease enter the donation amount:\n'
                     '(Enter "quit" to return to main menu)\n'
                     ' --> ')
    error_prompt = '\nDonation amount must be a number'

    donor = prompt_for_donor(name_prompt, donor_db)
    if not donor:
        return

    donation = prompt_for_float(amount_prompt, error_prompt)
    if not donation:
        return

    donor_db[donor].add_donation(donation)
    print(donor_db.thank_you_fmt.format(donor, donation))


def create_report(donor_db):
    """Generate and print a report of donors in the database

    Prints a list of donors, sorted by total historical donation amount.
    Includes Donor Name, total donated, number of donations and average
    donation

    Args:
        donor_db (DonorDatabase): Database instance containing all donors
    """
    print(donor_db.create_report())


def send_letters(donor_db):
    """Create a letter for each donor and write to disk as a text file"""
    donor_db.send_letters()


def create_projection(donor_db):
    """Create contribution projection based on user constraints"""
    factor_prompt = ('\nPlease enter the contribution multiplicative factor:\n'
                     '(Enter "quit" to return to main menu)\n'
                     ' --> ')
    min_prompt = ('\nPlease enter the minimum donation limit:\n'
                  '(Optional, press "0" to continue)\n'
                  ' --> ')
    max_prompt = ('\nPlease enter the maximum donation limit:\n'
                  '(Optional, press "0" to continue)\n'
                  ' --> ')
    error_prompt = ('\nValue must be a float')

    factor = prompt_for_float(factor_prompt, error_prompt)
    if not factor:
        return

    min_don = prompt_for_float(min_prompt, error_prompt)
    max_don = prompt_for_float(max_prompt, error_prompt)
    projection = donor_db.projection(factor, min_don=min_don, max_don=max_don)

    print(f'\nProjected contribution value: ${projection:,.2f}')


def quit_mailroom(donor_db):
    """Exit operations when quitting mail room"""
    print('Quitting mailroom...')


def main():
    """Main function"""
    donors = [Donor('Toni Morrison', [1000, 5000, 100]),
              Donor('Mike McHargue', [12000, 5000, 2500]),
              Donor("Flannery O'Connor", [38734, 6273, 67520]),
              Donor('Angelina Davis', [74846, 38470, 7570, 50]),
              Donor('Bell Hooks', [634547, 47498, 474729, 4567])]

    donor_db = DonorDatabase(*donors)

    opt_dict = dict(zip(PROMPT_OPTS, (send_thank_you,
                                      create_report,
                                      send_letters,
                                      create_projection,
                                      quit_mailroom)))
    choice = ''
    while choice != PROMPT_OPTS[-1]:
        choice = get_usr_input()
        opt_dict.get(choice)(donor_db)


if __name__ == '__main__':
    main()
