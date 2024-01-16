from datetime import datetime as dt
from os import system as sys
from os import name


#region CONSTANTS
WIDTH_FULL = 65
WIDTH_INPUT = (WIDTH_FULL * 2) / 3

APP_TITLE = 'PyBANK ALGEBRA\n'
PAGE_TITLE_EXIT = 'IZLAZAK IZ PROGRAMA'
PAGE_TITLE_MAIN = 'GLAVNI IZBORNIK'
PAGE_TITLE_CREATE = 'KREIRANJE RACUNA'
PAGE_TITLE_UPDATE = 'AZURIRANJE RACUNA'
PAGE_TITLE_NEW_TRANSACTION = 'NOVA TRANSAKCIJA'
PAGE_TITLE_TRANSACTIONS = 'TRANSAKCIJE PO RACUNU'
PAGE_TITLE_BALANCE = 'PRIKAZ STANJA RACUNA'
PAGE_TITLE_WITHDRAW = 'ISPLATA NOVCA S RACUNA'
PAGE_TITLE_DEPO = 'UPLATA NOVCA NA RACUN'
#endregion


bank_accounts = {
    f'BA-{dt.now().strftime("%Y-%m")}-{str(1).zfill(5)}': {
        'company': {
            'name': 'Algebra d.o.o.',
            'hq_address': {
                'street': "Ilica 123",
                'postal_code': '10000',
                'city': 'Zagreb'
            },
            'oib': '12345678901',
            'manager': 'Pero Peric'
        },
        'currency': ' €',
        'transactions': [
            {
                'date': dt.now().strftime('%d.%m.%Y %H:%M:%S'),
                'amount': 2000.00,
                'description': 'Uplata prilikom otvaranja racuna',
                'transaction_type': 'depo'
            }
        ],
        'balance': 2000.00
    }
}


#region DISPLAY
def display_bank_account_numbers():
    for index, number in enumerate(bank_accounts.keys()):
        print(f'{index + 1}. {number}')


def display_main_menu(first_time: bool = True, message: str = '') -> None:
    display_header()

    if first_time:
        print('1. Kreiranje racuna')
    else:
        print('1. Azuriranje racuna')
    print('2. Prikaz stanja racuna')
    print('3. Prikaz prometa po racunu')
    print('4. Polog novca na racun')
    print('5. Podizanje novca s racuna')
    print('0. Izlaz')

    print('_' * WIDTH_FULL)
    print(message)
    print('-' * WIDTH_FULL)


def display_header(page_title: str = PAGE_TITLE_MAIN, message: str = '') -> None:
    sys('cls' if name == 'nt' else 'clear')

    print('*' * WIDTH_FULL)
    print(APP_TITLE.center(WIDTH_FULL), '\n')
    print(f'{page_title}\n'.center(WIDTH_FULL))

    if message != '':
        print(message.center(WIDTH_FULL))
        print()


def display_bank_account_balance(bank_account_number: str = '',
                                 short_display: bool = True) -> None:
    if short_display:
        if bank_account_number != '':
            if bank_account_number in bank_accounts.keys():
                balance = bank_accounts[bank_account_number]['balance']
                print(f'Trenutno stanje racuna:\t{balance:.2f} {bank_accounts[bank_account_number]["currency"]}\n')
    else:
        if bank_account_number != '':
            if bank_account_number in bank_accounts.keys():
                balance = bank_accounts[bank_account_number]['balance']
                print(f'Broj racuna:\t{bank_account_number}')
                print(f'Datum i vrijeme:\t{dt.now().strftime("%d.%m.%Y %H:%M:%S")}\n')

                print(f'Trenutno stanje racuna:\t{balance:.2f} {bank_accounts[bank_account_number]["currency"]}\n')
                print('-' * WIDTH_FULL)
                input('Za Povratak u Glavni izbornik pritisnite bilo koju tipku\t')


def display_bank_account_transactions(bank_account_number: str = '') -> None:
    if bank_account_number != '':
        if bank_account_number in bank_accounts.keys():
            print(f'\n{"ID":<5}{"TIP":<15}{"Datum":<25}{"IZNOS":<20}{"OPIS":<50}')
            print('-' * WIDTH_FULL)
            for index, transaction in enumerate(bank_accounts[bank_account_number]['transactions']):
                print(f'{str(index + 1):<5}', end='')
                if transaction["transaction_type"] == 'depo':
                    print(f'{"Uplata":<15}', end='')
                else:
                    print(f'{"Isplata":<15}', end='')

                print(f'{transaction["date"]:<25}', end='')
                amount = f'{transaction["amount"]:.2f} {bank_accounts[bank_account_number]["currency"]}'
                print(f'{str(amount):<20}', end='')
                print(f'{transaction["description"]:<50}', end='')
                print()
            print('\n')
            print('-' * WIDTH_FULL)
            input('Za Povratak u Glavni izbornik pritisnite bilo koju tipku\t')


def display_account_properties(bank_account_number: str = ''):
    if bank_account_number != '':
        if bank_account_number in bank_accounts.keys():
            print()
            print(f'{"1. Naziv Tvrtke":<45}{str(bank_accounts[bank_account_number]["company"]["name"]):>25}')
            print(f'{"2. Ulica i broj sjedista Tvrtke":<45}{str(bank_accounts[bank_account_number]["company"]["hq_address"]["street"]):>25}')
            print(f'{"3. Postanski broj sjedista Tvrtke":<45}{str(bank_accounts[bank_account_number]["company"]["hq_address"]["postal_code"]):>25}')
            print(f'{"4. Grad sjedista Tvrtke":<45}{str(bank_accounts[bank_account_number]["company"]["hq_address"]["city"]):>25}')
            print(f'{"5. OIB Tvrtke":<45}{str(bank_accounts[bank_account_number]["company"]["oib"]):>25}')
            print(f'{"6. Ime i prezime odgovorne osobe Tvrtke":<45}{str(bank_accounts[bank_account_number]["company"]["manager"]):>25}')
            print(f'{"7. Konverzija u drugu valutu":<45}{str(bank_accounts[bank_account_number]["currency"]):>25}')
            print()


#endregion


#region BANK ACCOUNTS CRUD (Create, Read/Retrive, Update, Delete)
def create_bank_account_number(last_bank_account_number: int = 0,
                               number_lenght: int = 5) -> str:
    return f'BA-{dt.now().strftime("%Y-%m")}-{str(last_bank_account_number + 1).zfill(number_lenght)}'


def get_last_bank_accounts_number() -> int:
    if len(bank_accounts.keys()) > 0:
        return int(str(bank_accounts.keys()[-1]).split('-')[-1])
    else:
        return 0


def get_bank_accounts() -> dict:
    return bank_accounts


def get_bank_account(bank_account_number: str = '') -> dict:
    if bank_account_number != '':
        return bank_accounts[bank_account_number]
    else:
        return {}


def create_bank_account():
    global bank_accounts

    display_header(page_title=PAGE_TITLE_CREATE, message='Podaci o vlasniku racuna\n')

    bank_account_number = create_bank_account_number(get_last_bank_accounts_number())

    company_name = input(f'{"Naziv Tvrtke:":<{WIDTH_INPUT}}')
    company_street_and_number = input(f'{"Ulica i broj sjedista Tvrtke:":<{WIDTH_INPUT}}')
    company_postal_code = input(f'{"Postanski broj sjedista Tvrtke:":<{WIDTH_INPUT}}')
    company_city = input(f'{"Grad sjedista Tvrtke:":<{WIDTH_INPUT}}')
    while True:
        company_tax_id = input(f'{"OIB Tvrtke:":<{WIDTH_INPUT}}')
        if len(company_tax_id) != 11 and company_tax_id.isdigit():
            print('OIB mora imati tocno 11 znamenki i moraju biti samo brojke.')
            print('Molimo Vas ponovite unos\n')
        else:
            break
    company_manager = input(f'{"Ime i prezime odgovorne osobe Tvrtke:":<{WIDTH_INPUT}}')

    print()
    currency = input(f'{"Upisite naziv valute racuna (EUR ili HRK):":<{WIDTH_INPUT}}')
    if currency.upper() == 'HRK':
        currency = ' hr'
    else:
        currency = ' €'

    bank_accounts[bank_account_number] = {
        'company': {
            'name': company_name,
            'hq_address': {
                'street': company_street_and_number,
                'postal_code': company_postal_code,
                'city': company_city
            },
            'oib': company_tax_id,
            'manager': company_manager
        },
        'currency': currency,
        'transactions': [],
        'balance': 0.00
    }

    input('\nSPREMI? (Pritisnite bilo koju tipku) ')

    display_header(page_title=PAGE_TITLE_CREATE,
                   message=f'Racun broj {bank_account_number}, tvrtke {company_name}, je uspjesno kreiran.')

    input(f'{"Za nastavak pritisnite bilo koju tipku":<{WIDTH_INPUT}}')

    insert_transaction_to_bank_account(bank_account_number=bank_account_number)


def update_bank_account(bank_account_number: str = ''):
    global bank_accounts

    if bank_account_number != '':
        if bank_account_number in bank_accounts.keys():

            display_header(page_title=PAGE_TITLE_UPDATE, message='Podaci o vlasniku racuna\n')
            display_account_properties(bank_account_number)

            while True:
                choice = int(input(f'{"Birajte broj ispred podatka:":<{WIDTH_INPUT}}'))
                if choice >= 1 and choice <= 7:
                    break
                else:
                    print('Pograsan unos. Birajte brojeve izmedu 1 i 7.')

            match choice:
                case 1:
                    print(f'{"Sadasnji naziv Tvrtke":<45}{str(bank_accounts[bank_account_number]["company"]["name"]):>25}')
                    new_value = int(input(f'{"Unesite novi naziv Tvrtke:":<{WIDTH_INPUT}}'))
                    bank_accounts[bank_account_number]["company"]["name"] = new_value
                case 2:
                    print(f'{"Sadasnja ulica i broj sjedista Tvrtke":<45}{str(bank_accounts[bank_account_number]["company"]["hq_address"]["street"]):>25}')
                    new_value = int(input(f'{"Unesite novu ulicu sjedista Tvrtke:":<{WIDTH_INPUT}}'))
                    bank_accounts[bank_account_number]["company"]["hq_address"]["street"] = new_value
                case 3:
                    print(f'{"Sadasnji postanski broj sjedista Tvrtke":<45}{str(bank_accounts[bank_account_number]["company"]["hq_address"]["postal_code"]):>25}')
                    new_value = int(input(f'{"Unesite novi postanski broj sjedista Tvrtke:":<{WIDTH_INPUT}}'))
                    bank_accounts[bank_account_number]["company"]["hq_address"]["postal_code"] = new_value
                case 4:
                    print(f'{"Sadasnji grad sjedista Tvrtke":<45}{str(bank_accounts[bank_account_number]["company"]["hq_address"]["city"]):>25}')
                    new_value = int(input(f'{"Unesite novi grad sjedista Tvrtke:":<{WIDTH_INPUT}}'))
                    bank_accounts[bank_account_number]["company"]["hq_address"]["city"] = new_value
                case 5:
                    print(f'{"Sadasnji OIB Tvrtke":<45}{str(bank_accounts[bank_account_number]["company"]["oib"]):>25}')
                    new_value = int(input(f'{"Unesite novi OIB Tvrtke:":<{WIDTH_INPUT}}'))
                    # TODO provjera OIBa
                    bank_accounts[bank_account_number]["company"]["oib"] = new_value
                case 6:
                    print(f'{"Sadasnje ime i prezime odgovorne osobe Tvrtke":<45}{str(bank_accounts[bank_account_number]["company"]["manager"]):>25}')
                    new_value = int(input(f'{"Unesite novo ime i prezime odgovorne osobe Tvrtke:":<{WIDTH_INPUT}}'))
                case 7:
                    # TODO Ispis dostupnih valuta
                    print(f'{"Sadasnja valuta racuna":<45}{str(bank_accounts[bank_account_number]["currency"]):>25}')
                    new_value = int(input(f'{"Birajte broj ispred zeljene valute racuna Tvrtke:":<{WIDTH_INPUT}}'))
                    # TODO Provjera unosa i konverzija stanja u novu valutu
                    bank_accounts[bank_account_number]["currency"] = new_value



            input(f'{"Za nastavak pritisnite bilo koju tipku":<{WIDTH_INPUT}}')
            return f'Racun {bank_account_number} je uspjesno azuriran'
        else:
            return f'Broj racuna "{bank_account_number}" NIJE ispravan ili ga nema u bazi'
    else:
        return f'Potrebno je unijeti broj racuna koji zelite azurirati!'


def get_bank_account_balance(bank_account_number: str = '') -> float:
    if bank_account_number != '':
        if bank_account_number in bank_accounts.keys():
            return bank_accounts[bank_account_number]['balance']
        else:
            return 0.00
    else:
        return -1.00

#endregion


#region TRANSACTIONS CRUD (Create)
def insert_transaction_to_bank_account(bank_account_number: str = '',
                                       transaction_type: str = 'depo'):
    global bank_accounts

    display_header(page_title=PAGE_TITLE_NEW_TRANSACTION,
                           message=f'Stanje racuna broj: {bank_account_number}')
    bank_account_balance = get_bank_account_balance(bank_account_number)
    if bank_account_balance != -1:
        display_bank_account_balance(bank_account_number)

    if transaction_type == 'depo':
        print('Molimo Vas upisite iznos koji zelite poloziti na racun.')
        print('NAPOMENA Molimo Vas koristite decimalnu tocku, a ne zarez.\n')
    else:
        print('Molimo Vas upisite iznos koji zelite podici s racuna.')
        print('NAPOMENA Molimo Vas koristite decimalnu tocku, a ne zarez.\n')

    while True:
        amount = float(input(f'{"Iznos:":<{WIDTH_INPUT}}'))
        if amount != 0:
            break
        else:
            print(f'Vrijednost {amount} mora biti razlicita od nule.')
            print('Molimo ponovite unos!\n')

    description = input(f'{"Upisite opis transakcije":<{WIDTH_INPUT}}')

    transaction = {
        'date': dt.now().strftime('%d.%m.%Y %H:%M:%S'),
        'amount': amount,
        'description': description,
        'transaction_type': transaction_type
    }
    if transaction_type == 'depo':
        bank_accounts[bank_account_number]['balance'] += amount
    else:
        bank_accounts[bank_account_number]['balance'] -= amount

    bank_accounts[bank_account_number]['transactions'].append(transaction)

    input('\nSPREMI? (Pritisnite bilo koju tipku) ')
    display_header(page_title=PAGE_TITLE_NEW_TRANSACTION,
                   message=f'Uspjesno ste uplatili {amount:.2f} {bank_accounts[bank_account_number]["currency"]} na racun: {bank_account_number}')
    input(f'{"Za nastavak pritisnite bilo koju tipku":<{WIDTH_INPUT}}')

#endregion


def main_menu(first_time: bool = True) -> int:
    choice = -1

    if first_time:
        display_main_menu(message='Jos niste otvorili racun. Kreirat cemo jedan.')
        input('Za nastavak pritisnite bilo koju tipku\t')
    else:
        while choice not in [0, 1, 2, 3, 4, 5]:
            display_main_menu(first_time=False,
                              message='Molimo Vas upisite samo broj ispred opcije koju zelite odabrati')
            choice = int(input(f'{"Vas izbor:":<{WIDTH_INPUT}}'))

    return choice


def select_bank_account_number(page_title: str) -> list:
    display_header(page_title=page_title)
    display_bank_account_numbers()
    account_number_index = int(input(f'{"Birajte broj ispred broja racuna":<{WIDTH_INPUT}}'))
    return list(get_bank_accounts().keys())[account_number_index - 1]


def main():
    while True:
        if len(get_bank_accounts().keys()) == 0:
            choice = main_menu()
        else:
            choice = main_menu(False)

        match choice:
            case -1:
                create_bank_account()
            case 1:
                selected_bank_account_number = select_bank_account_number(page_title=PAGE_TITLE_UPDATE)
                update_bank_account(selected_bank_account_number)
            case 2:
                selected_bank_account_number = select_bank_account_number(page_title=PAGE_TITLE_BALANCE)
                display_bank_account_balance(bank_account_number=selected_bank_account_number, short_display=False)
            case 3:
                selected_bank_account_number = select_bank_account_number(page_title=PAGE_TITLE_TRANSACTIONS)
                display_bank_account_transactions(bank_account_number=selected_bank_account_number)
            case 4:
                selected_bank_account_number = select_bank_account_number(page_title=PAGE_TITLE_DEPO)
                insert_transaction_to_bank_account(selected_bank_account_number)
            case 5:
                selected_bank_account_number = select_bank_account_number(page_title=PAGE_TITLE_WITHDRAW)
                insert_transaction_to_bank_account(selected_bank_account_number, 'withdraw')
            case 0:
                display_header(page_title=PAGE_TITLE_EXIT,
                            message='Hvala sto ste koristili Py Bank\n')
                input(f'{"Za izlaz pritisnite bilo koju tipku":<{WIDTH_INPUT}}')
                return


if __name__ == "__main__":
    main()
