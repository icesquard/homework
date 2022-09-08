price = 0
while True:
    try:
        number_of_tickets = input("Введите количество билетов которое хотите приобрести:")
        number_of_tickets = int(number_of_tickets)
        if type(number_of_tickets) == int:
            break
    except ValueError:
        print("Введите целое число")
for i in range(number_of_tickets):
    i += 1
    while True:
        try:
            visitor_age = input(f"Возраст посетителя №{i}?")
            visitor_age = int(visitor_age)
            if visitor_age < 18:
                print("Билет бесплатный")
            elif 18 <= visitor_age < 25:
                price += 990
                print("Стоимость билета: 990 руб.")
            else:
                price += 1390
                print("Стоимость билета: 1390 руб.")
            if type(visitor_age) == int:
                break
        except ValueError:
            print("Введите целое число")
if number_of_tickets > 3:
    price = price - ((price / 100) * 10)
    print(f"Сумма к оплате {price} руб. с учетом 10% скидки за регистрацию больше 3-ех человек")
else:
    print(f"Сумма к оплате {price} руб.")
