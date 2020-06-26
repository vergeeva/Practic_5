import header


def main():
    pay_ = 10000
    h_pay = 400
    per = 5
    key = 1
    val = 1
    dict_ = {}
    while val != 0:
        print(f'базовый оклад = {pay_};\nпроцент = {per};\nчасовая ставка = {h_pay}')
        print("Хотите изменить данные?")
        val = int(input("Введите 0, если нет: "))
        if val == 0:  # Чтобы в случае отказа от изменения данных, цикл не предлагал их вводить
            break
        header.input_d()

    while key != 0:
        key = int(
            input("Выберите дальнейшее действие:\n1.Добавить сотрудника и выбрать вид оплаты\n0.Выйти\nВаш выбор: "))
        if key == 1:
            type_pay = int(
                input("Выберите: \n1-оклад\n2-по ставке и количеству часов\n3-по ставке и процентам\nВаш выбор: "))
            if type_pay == 1:
                pay = header.salary(pay_)
            elif type_pay == 2:
                hour = int(input("Количество часов: "))
                pay = header.on_hour(hour, h_pay)
            elif type_pay == 3:
                pay = header.on_per(per, h_pay)
            else:
                pay = 0
            name = input("Введите имя сотрудника: ")
            dict_[name] = pay
        else:
            break  # Чтобы избежать путанницы, когда пользователь вводит что-то другое кроме 0 или 1
    for key, value in dict_.items():
        print(f'Имя сотрудника: {key}; Зарплата: {value}')


main()
