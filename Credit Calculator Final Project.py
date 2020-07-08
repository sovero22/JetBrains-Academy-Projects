import sys
import math

def error_end():
    print('Incorrect parameters')
    sys.exit()

args = sys.argv
del args[0]

types_list = ['--type=annuity', '--type=diff']

if len(args) < 4:
    error_end()
elif args[0] not in types_list:
    error_end()

payment_type = args[0].strip('=-0123456789.')
del args[0]
argmnts = []
abc = 'abcdefghijklmnopqrstuvwxyz-'

credit_principal = 0
n_months = 0
interest = 0
month_pay = 0
extra_pay = 0
counter = 0

for i in args:
    argmnts.append(i.strip('=-0123456789.'))
    arg_val = i.lstrip(abc)
    arg_val = arg_val.lstrip('=')

    if argmnts[counter] == 'principal':
        if int(arg_val) < 0:
            error_end()
        credit_principal = int(arg_val)
    elif argmnts[counter] == 'interest':
        if '.' in i:
            if float(arg_val) < 0:
                error_end()
            interest = float(arg_val) / 100 / 12
        else:
            if int(arg_val) < 0:
                error_end()
            interest = int(arg_val) / 100 / 12
    elif argmnts[counter] == 'periods':
        if int(arg_val) < 0:
            error_end()
        n_months = int(arg_val)
    elif argmnts[counter] == 'payment':
        if (int(arg_val) < 0):
            error_end()
        elif payment_type == 'type=diff':
            error_end()
        month_pay = int(arg_val)

    counter += 1

if 'interest' not in argmnts:
    error_end()

def diff_payment():
    global month_pay, interest, credit_principal, n_months, extra_pay
    total_pay = 0
    for i in range(1, n_months + 1):
        month_pay = (credit_principal * (i - 1)) / n_months
        month_pay = interest * (credit_principal - month_pay)
        month_pay = credit_principal / n_months + month_pay

        if round(month_pay) < month_pay:
            month_pay = round(month_pay) + 1
        else:
            month_pay = round(month_pay)
        print('Month', i, ': paid out', month_pay)
        total_pay += month_pay
        extra_pay = total_pay - credit_principal
    print('Overpayment =', extra_pay)


def annuity_payment():
    global month_pay, interest, credit_principal, n_months, extra_pay
    total_pay = 0
    if 'periods' not in argmnts:
        n_months = month_pay - interest * credit_principal
        n_months = math.log(month_pay / (n_months), 1 + interest)

        if round(n_months) < n_months:
            n_months = round(n_months) + 1
        else:
            n_months = round(n_months)

        extra_pay = (month_pay * n_months) - credit_principal

        if n_months % 12 != 0:
            print('You need', n_months // 12, 'years and', n_months % 12, 'months to repay this credit!')
        else:
            print('You need', n_months // 12, 'years to repay this credit!')

    elif 'principal' not in argmnts:
        factor = math.pow(1 + interest, n_months)
        credit_principal = (interest * factor) / (factor - 1)
        credit_principal = month_pay / credit_principal
        if round(credit_principal) > credit_principal:
            credit_principal = round(credit_principal) - 1
        print('Your credit principal =', credit_principal, '!')
        extra_pay = (month_pay * n_months) - credit_principal

    elif 'payment' not in argmnts:
        factor = math.pow(1 + interest, n_months)
        month_pay = credit_principal * ((interest * factor))
        month_pay = month_pay / (factor - 1)
        if round(month_pay) < month_pay:
                month_pay = round(month_pay) + 1
        else:
                month_pay = round(month_pay)
        print('Your annuity payment =', month_pay, '!')
        extra_pay = (month_pay * n_months) - credit_principal

    print('Overpayment =', extra_pay)

if payment_type == 'type=annuity':
    annuity_payment()
elif payment_type == 'type=diff':
    diff_payment()
