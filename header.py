def salary(pay_):
    return pay_


def on_hour(hour, pay_):
    return hour * pay_


def on_per(per_, pay_):
    return pay_ + pay_ * per_ / 100


def input_d():
    pay_ = int(input("Базовый оклад = "))
    per_ = int(input("Процент = "))
    h_pay_ = int(input("Часовая ставка = "))
    return pay_, per_, h_pay_
