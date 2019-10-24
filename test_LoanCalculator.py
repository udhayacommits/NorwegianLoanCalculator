import credit_calculator

def test_1DNB_months_until_paid_out(capsys):
    # DNBTest1
    credit_calculator.months_until_paid_out(200000,12000,
                                            credit_calculator.DNB_INITIAL_PAYMENT,
                                            credit_calculator.DNB_MONTHLY_PERCENTAGE,
                                            credit_calculator.DNB_FEE)

    captured = capsys.readouterr()
    assert captured.out == "You will pay out credit in approximately 18 months. Sum left -1633.3779040913305\n"

def test_2DNB_months_until_paid_out(capsys):
    # DNBTest2
    credit_calculator.months_until_paid_out(200000,200,
                                            credit_calculator.DNB_INITIAL_PAYMENT,
                                            credit_calculator.DNB_MONTHLY_PERCENTAGE,
                                            credit_calculator.DNB_FEE)

    captured = capsys.readouterr()
    assert captured.out == "You have to pay way much bigger monthly payment than 200\n"

def test_1NORDEA_months_until_paid_out(capsys):
    value = credit_calculator.months_until_paid_out(200000,12000,
                                            credit_calculator.NORDEA_INITIAL_PAYMENT,
                                            credit_calculator.NORDEA_MONTHLY_PERCENTAGE,
                                            credit_calculator.NORDEA_FEE)

    captured = capsys.readouterr()
    assert captured.out == "You will pay out credit in approximately 18 months. Sum left -11583.9826298258\n"

def test_2NORDEA_months_until_paid_out(capsys):
    value = credit_calculator.months_until_paid_out(200000,200,
                                            credit_calculator.NORDEA_INITIAL_PAYMENT,
                                            credit_calculator.NORDEA_MONTHLY_PERCENTAGE,
                                            credit_calculator.NORDEA_FEE)

    captured = capsys.readouterr()
    assert captured.out == "You have to pay way much bigger monthly payment than 200\n"
