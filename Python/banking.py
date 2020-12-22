import sqlite3
import random

conn = sqlite3.connect('card.s3db')
cursor = conn.cursor()
cursor.execute(
            '''CREATE TABLE IF NOT EXISTS card (
                id INTEGER PRIMARY KEY,
                number TEXT NOT NULL,
                pin TEXT NOT NULL,
                balance INTEGER NOT NULL
            );''')
conn.commit()


choice = ''


class BankAccount:
    # card number
    # PIN
    def __init__(self):
        card_number = '400000'
        pin_number = ''
        for i in range(9):
            card_number += str(random.randint(0, 9))
        card_number += luhn_algorithm(card_number)
        for i in range(4):
            pin_number += str(random.randint(0, 9))

        cursor.execute('SELECT id FROM card')
        id_counter = cursor.fetchall()

        self.id = len(id_counter) + 1
        self.cardnumber = card_number
        self.pin = pin_number
        self.balance = 0

        cursor.execute(
                    'INSERT INTO card (id, number, pin, balance) VALUES (' +
                    str(self.id) + ', ' + self.cardnumber + ', ' + self.pin +
                    ', ' + str(self.balance) + ')')
        conn.commit()

        print('Your card has been created')
        print('Your card number:')
        print(self.cardnumber)
        print('Your card PIN:')
        print(self.pin)


def luhn_algorithm(number):
    temp_list = list(number)
    # print(temp_list)
    for n in range(len(temp_list)):
        if (n + 1) % 2 != 0:
            temp_list[n] = 2 * int(temp_list[n])
        else:
            temp_list[n] = int(temp_list[n])

    for n in range(len(temp_list)):
        if temp_list[n] > 9:
            temp_list[n] = temp_list[n] - 9
        else:
            temp_list[n] = int(temp_list[n])
    # print(temp_list)

    sum_num = sum(temp_list)
    if sum_num % 10 == 0:
        chk_digit = 0
    else:
        chk_digit = 10 - (sum_num % 10)
    return str(chk_digit)


def main_menu():
    print('1. Create an account\n2. Log into account\n0. Exit')


def account_menu():
    print()
    print('1. Balance\n2. Add income\n3. Do transfer\n4. Close account\n' +
          '5. Log out\n0. Exit')


def check_balance(card):
    cursor.execute('''SELECT
                            balance
                      FROM
                            card
                      WHERE
                            number = {}
                      ;'''.format(card))
    detail = cursor.fetchall()
    return detail


def update_balance(amount, card):
    cursor.execute('UPDATE card SET balance = balance + ' + amount +
                   ' WHERE number = {}'.format(card))
    conn.commit()


def check_account(trans_account):
    cursor.execute('SELECT number FROM card WHERE ' +
                   'number = {}'.format(trans_account))
    account_info = cursor.fetchall()
    if trans_account != trans_account[:-1] + luhn_algorithm(trans_account[:-1]):
        print("Probably you made a mistake in the card number. " +
              "Please try again!")
        return False
    elif len(account_info) == 0:
        print("Such a card does not exist.")
        return False
    else:
        return True


while choice != 0:
    main_menu()
    choice = int(input())
    print()
    if choice == 1:
        account = BankAccount()
        print()
    elif choice == 2:
        card_number = input('Enter your card number:\n')
        pin_number = input('Enter your PIN:\n')
        print()

        cursor.execute('''SELECT
                                *
                          FROM
                                card
                          WHERE
                                number = {}
                                AND pin = {}
                          ;'''.format(card_number, pin_number))
        acc_info = cursor.fetchall()

        if len(acc_info) == 0:
            print('Wrong card number or PIN!')
        else:
            choice = ''
            print('You have successfully logged in!')
            while choice not in [0, 5]:
                account_menu()
                choice = int(input())
                print()
                if choice == 1:
                    acc_balance = check_balance(card_number)
                    print('Balance:', str(acc_balance[0]).strip('[(,)]'))
                elif choice == 2:
                    add_income = input('Enter income:\n')
                    update_balance(add_income, card_number)
                    print('Income was added!')
                elif choice == 3:
                    not_valid = True
                    print('Transfer')
                    while not_valid:
                        trans_acc = input('Enter card number:\n')
                        if trans_acc == acc_info[0][1]:
                            print("You can't transfer money to the same account!")
                            continue
                        else:
                            if check_account(trans_acc):
                                print('Enter how much money you want to transfer:')
                                trans_amount = input()
                                acc_balance = str(check_balance(card_number))
                                acc_balance = acc_balance.strip('[(,)]')
                                if int(trans_amount) <= int(acc_balance):
                                    update_balance('-' + trans_amount, card_number)
                                    update_balance(trans_amount, trans_acc)
                                    print('Success!')
                                else:
                                    print('Not enough money!')
                                not_valid = False
                            else:
                                break
                elif choice == 4:
                    cursor.execute('SELECT id FROM card ' +
                                   'WHERE number = {}'.format(card_number))
                    c_id = cursor.fetchall()
                    c_id = str(c_id[0]).strip('(,)')
                    cursor.execute('DELETE FROM card ' +
                                   'WHERE number = {}'.format(card_number))
                    conn.commit()
                    cursor.execute('UPDATE card SET id = id - 1 ' +
                                   'WHERE id > {}'.format(c_id))
                    conn.commit()
                    print('\nThe account has been closed!')
                    break
            if choice == 5:
                print('You have successfully logged out!')
print('Bye!')
