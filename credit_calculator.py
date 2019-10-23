#!/usr/bin/python

DNB_YEARLY_PERCENTAGE = 2.10 / 100
DNB_MONTHLY_PERCENTAGE = DNB_YEARLY_PERCENTAGE / 12
DNB_FEE = 50
DNB_INITIAL_PAYMENT = 10000

NORDEA_YEARLY_PERCENTAGE = 2.15 / 100
NORDEA_MONTHLY_PERCENTAGE = NORDEA_YEARLY_PERCENTAGE / 12
NORDEA_FEE = 65
NORDEA_INITIAL_PAYMENT = 0

def months_until_paid_out(credit_sum, monthly_payment, initial_payment, monthly_percentage, monthly_fee):
    MAX_YEARS = 30
    MAX_MONTHS = MAX_YEARS * 12
    for month in range(1, MAX_MONTHS):
        if month == 1:
            credit_sum = credit_sum * (1 + monthly_percentage) - (monthly_payment - monthly_fee - initial_payment)
        else:
            credit_sum = credit_sum * (1 + monthly_percentage) - (monthly_payment - monthly_fee)
        if credit_sum < 0:
            print("You will pay out credit in approximately {} months. Sum left {}".format(month, credit_sum))
            return
    print("You have to pay way much bigger monthly payment than {}".format(monthly_payment))
    return


if __name__ == "__main__":
    while True:
        credit_sum = input("Enter the credit sum value:")
        try:
            credit_sum = float(credit_sum)
        except ValueError:
            print("This is not a valid number. Please try again!")
        else:
            break
    
    while True:
        monthly_payment = input("Enter the monthly payment amount:")
        try:
            monthly_payment = float(monthly_payment)
        except ValueError:
            print("This is not a valid number. Please try again!")
        else:
            break

    print("DNB: ")
    months_until_paid_out(credit_sum, monthly_payment, DNB_INITIAL_PAYMENT, DNB_MONTHLY_PERCENTAGE, DNB_FEE)

    print("NORDEA: ")
    months_until_paid_out(credit_sum, monthly_payment, NORDEA_INITIAL_PAYMENT, NORDEA_MONTHLY_PERCENTAGE, NORDEA_FEE)

