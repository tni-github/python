def check_weekend():
    while True:
        try:
            day_week = int(input('Day: '))
            return (day_week)
        except ValueError:
            print('Error')


num = check_weekend()

if num <= 5:
    print('Work')
elif num == 6 or num == 7:
    print('Rest')
else:
    print('Big number')
