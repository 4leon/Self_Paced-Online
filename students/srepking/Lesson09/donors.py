

class Group:

    def __init__(self, *args):

        self._donor_raw = {d.name: d for d in args}

    def search(self, donor):
        return self._donor_raw.get(donor)

    def add(self, donor, donation):
        if self._donor_raw.get(donor):
            self._donor_raw[donor].add_donation(donation)
        else:
            self._donor_raw[donor] = Individual(donor, [donation])

    def print_donors(self):
        # This prints the list of donors
        for x in self._donor_raw:
            print(x)

    def summary(self):
        """Create a new dictionary with Total, number of donations,
        and average donation amount"""

        donors_f = {some_name: [sum(donor_obj.donations),
                                int(len(donor_obj.donations)),
                                sum(donor_obj.donations) /
                                int(len(donor_obj.donations))]
                    for some_name, donor_obj in self._donor_raw.items()}
        return donors_f

    @staticmethod
    def column_name_width(donor_summary):
        name_list = list(donor_summary.keys())  # creates a list of keys
        name_wi = 11  # Establish minimum column width
        for i in name_list:
            if len(i) > name_wi:
                name_wi = (len(i))  # width of name column
        return name_wi

    @staticmethod
    def column_total_width(donor_summary):
        tot_wi = 12
        for name, summary in donor_summary.items():
            if len(str(summary[0])) > tot_wi:
                # width of total column
                tot_wi = (len(str(summary[0]))) + 3
                # width of number of donations column
        return tot_wi

    @staticmethod
    def column_average_width(donor_summary):
        ave_wi = 12
        for name, summary in donor_summary.items():
            if len(str(summary[2])) > ave_wi:
                # width of total column
                ave_wi = (len(str(summary[2]))) + 3
                # width of number of donations column
        return ave_wi

    @staticmethod
    def column_number_width(donor_summary):
        num_wi = 12
        for name, summary in donor_summary.items():
            if len(str(summary[1])) > num_wi:
                # width of total column
                num_wi = (len(str(summary[1]))) + 3
                # width of number of donations column
        return num_wi

    @staticmethod
    def sort_list(donor_summary):
        list_sorted = sorted(donor_summary,
                             key=donor_summary.__getitem__, reverse=True)
        return list_sorted

    @property
    def report(self):
        """Return a report on all the donors"""
        donor_summary = self.summary()
        name_wi = Group.column_name_width(donor_summary)
        tot_wi = Group.column_total_width(donor_summary)
        num_wi = Group.column_number_width(donor_summary)
        ave_wi = Group.column_average_width(donor_summary)

        list_sorted = Group.sort_list(donor_summary)

        rows = ['\n''A summary of your donors donations:',
                f"{'Donor Name':{name_wi}}| {'Total Given':^{tot_wi}}| "
                f"{'Num Gifts':^{num_wi}}| {'Average Gift':^{ave_wi}}",
                f"{'-':-^{(name_wi+tot_wi+ave_wi+num_wi+8)}}"]

        for key in list_sorted:
            temp = donor_summary[key]
            rows.append(f"{key:{name_wi}}${temp[0]:{tot_wi}.2f}"
                        f"{temp[1]:^{num_wi}}   "
                        f"${temp[2]:>{ave_wi}.2f}")

        return '\n'.join(rows)

    def letters(self):
        donors_f = self.summary()

        for donor, donor_obj in self._donor_raw.items():
            donation_summary = donors_f[donor]
            letter = f'Dear {donor}, thank you so much for your ' \
                     f'last contribution of ${donor_obj.donations[-1]:.2f}! ' \
                     f'You have contributed a total of $' \
                     f'{donation_summary[0]:.2f}, ' \
                     f'and we appreciate your support!'
            # Write the letter to a destination
            with open(donor + '.txt', 'w') as to_file:
                to_file.write(letter)


class Individual:
    def __init__(self, name, donations):
        self.name = name
        self.donations = donations

    def add_donation(self, donation):
        self.donations.append(donation)

    @property
    def thank_you(self):
        """Add a donation to a donors records and print a report."""
        return ('Thank you so much for the generous gift of ${0:.2f}, {1}!'
                .format(self.donations[-1], self.name))
