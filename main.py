from dataclasses import dataclass
from datetime import datetime
from typing import Optional


def main():
    """
    main logic
    :return:
    """
    accounting = init_accounts()
    add_entries(accounting)
    show_balance(accounting)


def init_accounts():
    """
    initializes the dictionary for the accounting
    :return:
    """
    accounts = dict()
    for person in ['Marco', 'Bernd', 'Adam']:
        accounts[person] = list()
    return accounts


def add_entries(accounts):
    """
    adds the charging entries to the dictionary
    :param accounts: dict with customers and entries
    :return:
    """
    name = input('Kundenname > ')
    more_entries = True
    while more_entries:
        entry = Entry()
        accounts[name].append(entry)
        read_entry(entry)

        more_entries = input('Weitere Bezüge (y/N) > ') == 'y'


def read_entry(entry):
    """
    prompts the user to enter the data for an entry
    :return:
    """
    entry.start_time = read_datetime('Start des Ladevorgangs')
    entry.end_time = read_datetime('Ende des Ladevorgangs')
    entry.release_time = read_datetime('Freigabe der Säule')
    entry.energy_amount = read_float('Strommenge in KWh >')


def show_balance(accounting):
    """
    shows the balance for each customer
    :param accounting: dict with customers and entries
    :return:
    """
    for name, person in accounting.items():
        if len(person) > 0:
            total_cost = 0
            print(f'Abrechnung für {name}')
            for charge in person:
                print(f'  + {charge.start_time.strftime("%d.%m.%Y %H:%M")}: CHF {charge.cost:.2f}')
                total_cost += charge.cost
            print(f'Total: CHF {total_cost:.2f}')


def read_float(prompt):
    """
    prompts the user to enter a decimal number
    :param prompt:
    :return: the decimal number
    """
    number = None
    while number is None:
        try:
            number = float(input(prompt + ' > '))
            if number <= 0:
                print('Geben Sie eine positive Zahl ein')
                number = None
        except ValueError:
            print('Geben Sie eine positive Zahl ein')
    return number


def read_datetime(prompt):
    """
    prompts the user to enter a date/time
    :param prompt:
    :return: the datetime
    """
    timestamp = None
    while timestamp is None:
        user_input = input(prompt + '(dd.mm.jjjj hh:mm) > ')
        try:
            timestamp = datetime.strptime(user_input, '%d.%m.%Y %H:%M')
        except ValueError:
            print('Geben Sie ein gültiges Datum/Uhrzeit ein')
    return timestamp


@dataclass
class Entry:
    """
    an accounting entry for the charging
    """
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None
    release_time: Optional[datetime] = None
    energy_amount: Optional[float] = None

    @property
    def cost(self):
        """
        gets the total cost for the charging
        :return:
        """
        energy_cost = self.energy_amount * 0.35
        time_delta = self.release_time - self.end_time
        duration = time_delta.total_seconds() / 60
        if duration > 15:
            energy_cost += (duration - 15) * 0.05
        return round(energy_cost, 2)


if __name__ == '__main__':
    main()
