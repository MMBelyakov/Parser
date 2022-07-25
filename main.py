import re
from datetime import timedelta, datetime

"""35/42  """
"""MESSAGE={'STATUS': 'SUCCESS', 'DATE': {'year': 2021, 'month': 12, 'day': 13, 'hour': 16, 'minute': 15},
 'TEXT': 'Подписать служебку у начальника'}"""

global find_delayed_minute, find_delayed_hour, find_delayed_year, find_delayed_month, find_delayed_day, n, Remind, mes, \
    rem, index, match, time1, minute, hour, hour_text, minute_text, out, day_week, my_list, string_year


def main():
    global index, minute, find_delayed_hour, out, hour, Day, Month, Year, string_year, str_month
    Status = 'Success'
    # global find_delayed_minute, find_delayed_hour, find_delayed_year, find_delayed_month, find_delayed_day, n, Remind, mes, rem, index, match, time1, minute, hour, hour_text, minute_text, out, index
    print("О чём Вам напомнить ?")
    text = input()
    my_list = text.split()

    current_date = datetime.now()  # текущие: month day year hour minute
    current_date_string = current_date.strftime('%m/%d/%y %H:%M:%S')  # hour и minute далее

    month_current = current_date_string[1]
    day_current = current_date_string[3:5]
    year_current = current_date_string[6:8]

    try:
        match = re.search(r'\d{2}.\d{2}.\d{4}', text)  # находим день месяц год из сообщения  в формате даты
        date = datetime.strptime(match.group(), '%d.%m.%Y').date()

    except (AttributeError, ValueError):
        year = year_current
        month = month_current
        day = day_current

    else:
        day_month_year = str(date)
        year = day_month_year[:4]
        month = day_month_year[5:7]
        day = day_month_year[-2:]

    Year = int(year)
    Month = int(month)
    Day = int(day)

    hour_current = int(current_date_string[9:11])
    minute_current = int(current_date_string[12:14])
    try:
        Time = re.findall(r'[0-2]\d:[0-5]\d+', text)  # поиск времени в формате hh:mm
        time1 = str(Time)
        hour_text = int(time1[2:4])  # время в тексте
        minute_text = int(time1[5:7])
        if hour_text > 24 or minute_text > 60:
            raise ValueError

    except ValueError:
        hour = int(current_date_string[9:11])  # текущее время#
        minute = int(current_date_string[12:14])

    else:
        if Time:
            if hour_text < hour_current:
                Day += 1
                hour = hour_text
                minute = minute_text

            elif hour_text >= hour_current:
                hour = hour_text

                if minute_text < minute_current:
                    Day += 1
                    minute = minute_text

                elif minute_text >= minute_current:
                    minute = minute_text

            else:
                hour = hour_text
                minute = minute_text
        else:
            hour = int(current_date_string[9:11])
            minute = int(current_date_string[12:14])

    for i in range(len(my_list)):
        if my_list[i] == 'утром':
            hour = 6
            minute = 0
        elif my_list[i] == 'днем':
            hour = 12
            minute = 0
        elif my_list[i] == 'вечером':
            hour = 18
            minute = 0
        elif my_list[i] == 'ночью':
            hour = 0
            minute = 0

    mes = re.sub('\w [0-2]\d:[0-5]\d', '', text)
    rem = re.sub('\d{2}.\d{2}.\d{4}', '', mes)
    Remind = str(rem)

    match_find_delay_minute = re.findall('минут', text)
    minute_mass = ['минут', 'минуту', 'минуты']
    match_find_delay_hour = re.findall('час', text)
    hour_mass = ['час', 'часа', 'часов']
    match_find_delay_day = ['день', 'дней', 'дня']
    match_find_delay_month = ['месяц', 'месяцев', 'месяца']
    match_find_delay_year = ['год', 'лет', 'года']

    through = ['через', 'Через']
    every = ['каждый', 'Каждый', 'каждые', 'Каждые', 'каждую', 'Каждую']

    Mondays = ['понедельник', 'понедельникам', 'Понедельник', 'Понедельникам']
    Tuesdays = ['вторник', 'вторникам', 'Вторник', 'Вторникам']
    Wendsdays = ['среду', 'средам', 'Среду', 'Средам']
    Thursdays = ['четверг', 'четвергам', 'Четверг', 'Четвергам']
    Fridays = ['пятницу', 'пятницам', 'Пятницу', 'Пятницам']
    Saturdays = ['субботу', 'субботам', 'Субботу', 'Субботам']
    Sundays = ['воскресенье', 'воскресеньям', 'Воскресенье', 'Воскресеньям']
    Week = [Mondays, Tuesdays, Wendsdays, Thursdays, Fridays, Saturdays, Sundays]

    Septembers = ['сентябрь', 'сентября']
    Octobers = ['октябрь', 'октября']
    Novembers = ['ноябрь', 'ноября']
    Decembers = ['декабрь', 'декабря']
    Januarys = ['январь', 'января']
    Februarys = ['февраль', 'февраля']
    Marchs = ['март', 'марта']
    Aprils = ['апрель', 'апреля']
    Mays = ['май', 'мая']
    Junes = ['июнь', 'июня']
    Julys = ['июль', 'июля']
    Augusts = ['август', 'августа']
    MONTHS = [Septembers, Octobers, Novembers, Decembers, Januarys, Februarys, Marchs, Aprils, Mays, Junes, Julys,
              Augusts]

    str_day = ''
    str_month = ''
    string_year = ''
    try:
        for i in range(len(my_list)):
            if (my_list[i].isdigit() and int(my_list[i]) > 0) and my_list[i + 1].isalpha():
                str_day = my_list[i]

                try:
                    if (my_list[i + 2].isdigit() and int(my_list[i + 2]) > 2000) and my_list[i + 3] == 'года':
                        string_year = int(my_list[i + 2])

                except IndexError:
                    pass
                for j in range(len(MONTHS)):
                    if my_list[i + 1] in MONTHS[j]:
                         # поиск месяца
                        if MONTHS[j] == Januarys and int(my_list[i]) < 32:
                            str_month = '01'
                            Month = 1

                        elif  MONTHS[j] == Januarys and int(my_list[i]) > 32:
                            print('Неверный ввод.Попробуйте еще раз')
                            text = input()
                            main()

                        elif MONTHS[j] == Februarys and int(my_list[i]) < 29:
                            str_month = '02'
                            Month = 2

                        elif  MONTHS[j] == Februarys and int(my_list[i]) > 29:
                            print('Неверный ввод.Попробуйте еще раз')
                            text = input()
                            main()

                        elif MONTHS[j] == Marchs and int(my_list[i]) < 32:
                            str_month = '03'
                            Month = 3

                        elif MONTHS[j] == Marchs and int(my_list[i]) > 32:
                            print('Неверный ввод.Попробуйте еще раз')
                            text = input()
                            main()

                        elif MONTHS[j] == Aprils and int(my_list[i]) < 31:
                            str_month = '04'
                            Month = 4

                        elif MONTHS[j] == Aprils and int(my_list[i]) > 31:
                            print('Неверный ввод.Попробуйте еще раз')
                            text = input()
                            main()

                        elif MONTHS[j] == Mays  and int(my_list[i]) < 32:
                            str_month = '05'
                            Month = 5

                        elif MONTHS[j] ==Mays and int(my_list[i]) > 32:
                            print('Неверный ввод.Попробуйте еще раз')
                            text = input()
                            main()

                        elif MONTHS[j] == Junes and int(my_list[i]) < 31:
                            str_month = '06'
                            Month = 6

                        elif MONTHS[j] == Junes and int(my_list[i]) > 31:
                            print('Неверный ввод.Попробуйте еще раз')
                            text = input()
                            main()

                        elif MONTHS[j] == Julys and int(my_list[i]) < 32:
                            str_month = '07'
                            Month = 7
                        elif MONTHS[j] == Julys and int(my_list[i]) > 32:
                            print('Неверный ввод.Попробуйте еще раз')
                            text = input()
                            main()

                        elif MONTHS[j] == Augusts and int(my_list[i]) < 32 :
                            str_month = '08'
                            Month = 8

                        elif MONTHS[j] == Augusts and int(my_list[i]) > 32:
                            print('Неверный ввод.Попробуйте еще раз')
                            text = input()
                            main()


                        elif MONTHS[j] == Septembers and int(my_list[i]) < 31:
                            str_month = '09'
                            Month = 9

                        elif MONTHS[j] == Septembers and int(my_list[i]) > 31:
                            print('Неверный ввод.Попробуйте еще раз')
                            text = input()
                            main()

                        elif MONTHS[j] == Octobers and int(my_list[i]) < 32 :
                            str_month = '10'
                            Month = 10

                        elif MONTHS[j] == Octobers and int(my_list[i]) > 32:
                            print('Неверный ввод.Попробуйте еще раз')
                            main()
                            text = input()
                            main()


                        elif MONTHS[j] == Novembers  and int(my_list[i]) < 31 :
                            str_month = '11'
                            Month = 11

                        elif MONTHS[j] == Novembers and int(my_list[i]) > 31:
                            print('Неверный ввод.Попробуйте еще раз')
                            main()
                            text = input()
                            main()


                        elif MONTHS[j] == Decembers and int(my_list[i]) < 32:
                            str_month = '12'
                            Month = 12

                        elif MONTHS[j] == Decembers and int(my_list[i]) > 32:
                                print('Неверный ввод.Попробуйте еще раз')
                                main()
                                text = input()
                                main()

                    else:
                            month = ''
    except IndexError:
        pass

    try:

        if str_month and str_day:
            Day = str_day
            Month = str_month
            txt = mes.split()
            g = txt.index(str_day)
            for _ in range(2):
                txt.pop(g)
            out = str(' '.join(txt))

            if string_year:
                Day = str_day
                Month = str_month
                txt = mes.split()
                g = txt.index(str_day)
                Year = string_year
                for _ in range(2):
                    txt.pop(g)
                out = str(' '.join(txt))
            else:
                pass
            print("Message:{", "'STATUS':", Status, ",", "'DATE':{'year':", Year, ",", "'month':", Month, ",", "'day':",
                  Day,
                  ",", "'hour':", hour, ",", "'minute':", minute, "}", ",", "'TEXT':", out, "}", sep='')
            exit()

        else:
            Day = int(day)
            Month = int(month)

        print("Message:{", "'STATUS':", Status, ",", "'DATE':{'year':", Year, ",", "'month':", Month, ",", "'day':",
              Day,
              ",", "'hour':", hour, ",", "'minute':", minute, "}", ",", "'TEXT':", out, "}", sep='')

        exit()
    except (ValueError,NameError,IndexError):
        pass

    try:
        for i in range (len(my_list)):
            if my_list[i]=='следующей' or my_list[i]=='следующем' :
                if my_list[i]=='следующей' :
                    del my_list[i]
                elif my_list[i]=='следующем' :
                    del my_list[i]
                for j in range (len(my_list)):
                        if my_list[j] =='неделе' :
                            Day+=6
                            if Day>30:
                                Day-=30
                                Month+=1
                            del  my_list [j]

                        elif my_list[j]=='месяце' :
                            Month+=1
                            del my_list[j]

                        elif my_list[j]=='году' :
                            Year+=1
                            del my_list[j]

                        out=' '.join(my_list)
            else:
                pass
    except IndexError:
        pass

    for u in range (len(my_list)):
        if my_list[u]=='сегодня' :
            del my_list[u]
            out = ' '.join(my_list)
        elif my_list[u]== 'завтра' :
            Day+=1
            del my_list[u]
            out = " ".join(my_list)
        elif my_list[u]=='послезавтра' :
            Day+=2
            del my_list[j]
            out = " ".join(my_list)


    day_week = ''
    day_week_current = datetime.isoweekday(datetime.now())
    day_week_compare = 0

    def each():
        global index, hour, minute, out, Day, find_delayed_hour, Month, Year, a, b

        if 'каждый' in my_list:
            index = my_list.index('каждый')
        elif 'Каждый' in my_list:
            index = my_list.index('Каждый')
        elif 'каждые' in my_list:
            index = my_list.index('каждые')
        elif 'Каждые' in my_list:
            index = my_list.index('Каждые')
        elif 'каждую' in my_list:
            index = my_list.index('каждую')
        elif 'Каждую' in my_list:
            index = my_list.index('Каждую')
        elif 'каждое' in my_list:
            index = my_list.index('каждое')
        elif 'Каждое' in my_list:
            index = my_list.index('Каждое')

        try:
            if my_list[index + 1].isdigit() and my_list[index + 2] == 'число' and ('каждое' or 'Каждое' in my_list):
                Day = int(my_list[index + 1])
                if Day > 32:
                    print(Day, 'is out of range')
                else:

                    a = my_list[index + 1]
                    b = my_list[index + 2]
                    for i in range(3):
                        del my_list[index]

                    out = ' '.join(my_list)
                    print("Message:{", "'STATUS':", Status, "'TEXT':", out, ",",
                          "'PARAMS': {'repeat_always':", a, ' ', b,
                          "},'DATE':{" "'hour':", hour, ",", "'minute':", minute, "}", sep='')
                exit()
        except (IndexError, NameError):
            pass

        try:
            if Mondays and ('каждый' or 'Каждый' in my_list):
                if my_list[index] in every and my_list[index + 1] in Mondays:
                    for j in range(len(my_list)):
                        if my_list[j] in Mondays:
                            day_week = 'Monday'
                            day_week_compare = 1
                            for i in range(2):
                                del my_list[index]

                            out = ' '.join(my_list)
                            print("Message:{", "'STATUS':", Status, "'TEXT':", out, ",",
                                  "'PARAMS': {'repeat_always':", "каждый понедельник",
                                  "},'DATE':{" "'hour':", hour, ",", "'minute':", minute, "}", sep='')
                            exit()

        except (IndexError, NameError):
            pass

        try:
            if Tuesdays and ('каждый' or 'Каждый' in my_list):
                if my_list[index] in every and my_list[index + 1] in Tuesdays:
                    for j in range(len(my_list)):
                        if my_list[j] in Tuesdays:
                            day_week = 'Tuesday'
                            day_week_compare = 2
                            for i in range(2):
                                del my_list[index]

                            out = ' '.join(my_list)
                            print("Message:{", "'STATUS':", Status, "'TEXT':", out, ",",
                                  "'PARAMS': {'repeat_always':", "каждый вторник",
                                  "},'DATE':{" "'hour':", hour, ",", "'minute':", minute, "}", sep='')
                            exit()

        except (IndexError, NameError):
            pass

        try:
            if Wendsdays and ('каждую' or 'Каждую' in my_list):
                if my_list[index] in every and my_list[index + 1] in Wendsdays:
                    for j in range(len(my_list)):
                        if my_list[j] in Wendsdays:
                            day_week = 'Wendsday'
                            day_week_compare = 3
                            for i in range(2):
                                del my_list[index]

                            out = ' '.join(my_list)
                            print("Message:{", "'STATUS':", Status, "'TEXT':", out, ",",
                                  "'PARAMS': {'repeat_always':", "каждую среду",
                                  "},'DATE':{" "'hour':", hour, ",", "'minute':", minute, "}", sep='')
                            exit()

        except (IndexError, NameError):
            pass

        try:
            if Thursdays and ('каждый' or 'Каждый' in my_list):
                if my_list[index] in every and my_list[index + 1] in Thursdays:
                    for j in range(len(my_list)):
                        if my_list[j] in Thursdays:
                            day_week = 'Thursday'
                            day_week_compare = 4
                            for i in range(2):
                                del my_list[index]

                            out = ' '.join(my_list)
                            print("Message:{", "'STATUS':", Status, "'TEXT':", out, ",",
                                  "'PARAMS': {'repeat_always':", "каждый четверг",
                                  "},'DATE':{" "'hour':", hour, ",", "'minute':", minute, "}", sep='')
                            exit()

        except (IndexError, NameError):
            pass

        try:
            if Fridays and ('каждую' or 'Каждую' in my_list):
                if my_list[index] in every and my_list[index + 1] in Fridays:
                    for j in range(len(my_list)):
                        if my_list[j] in Fridays:
                            day_week = 'Friday'
                            day_week_compare = 5
                            for _ in range(2):
                                del my_list[index]
                            out = ' '.join(my_list)
                            print("Message:{", "'STATUS':", Status, "'TEXT':", out, ",",
                                  "'PARAMS': {'repeat_always':", 'каждую пятницу',
                                  "},'DATE':{" "'hour':", hour, ",", "'minute':", minute, "}", sep='')
                            exit()

        except (IndexError, NameError):
            pass

        try:
            if Saturdays and ('каждую' or 'Каждую' in my_list):
                if my_list[index] in every and my_list[index + 1] in Saturdays:
                    for j in range(len(my_list)):
                        if my_list[j] in Saturdays:
                            day_week = 'Saturday'
                            day_week_compare = 6
                            for _ in range(2):
                                del my_list[index]
                            out = ' '.join(my_list)
                            print("Message:{", "'STATUS':", Status, "'TEXT':", out, ",",
                                  "'PARAMS': {'repeat_always':", 'каждую субботу',
                                  "},'DATE':{" "'hour':", hour, ",", "'minute':", minute, "}", sep='')
                            exit()

        except (IndexError, NameError):
            pass

        try:
            if Sundays and ('каждое' or 'Каждое' in my_list):
                if my_list[index] in every and my_list[index + 1] in Sundays:
                    for j in range(len(my_list)):
                        if my_list[j] in Sundays:
                            day_week = 'Sunday'
                            day_week_compare = 7
                            for i in range(2):
                                del my_list[index]

                            out = ' '.join(my_list)
                            print("Message:{", "'STATUS':", Status, "'TEXT':", out, ",",
                                  "'PARAMS': {'repeat_always':", 'каждое воскресенье',
                                  "},'DATE':{" "'hour':", hour, ",", "'minute':", minute, "}", sep='')
                            exit()

        except (IndexError, NameError):
            pass

        if (match_find_delay_minute or match_find_delay_hour) and (
                'каждый' or 'Каждый' or 'каждые' or 'Каждые' or 'каждую' or 'Каждую' in my_list):
            try:
                if my_list[index + 1].isdigit() and (my_list[index + 2] in minute_mass):
                    find_delayed_hour = 0
                    find_delayed_minute = my_list[index + 1]
                    minute += int(find_delayed_minute)
                    a = my_list[index + 1]
                    b = my_list[index + 2]
                    while minute > 60:
                        minute -= 60
                        hour += 1

                    for i in range(3):
                        del my_list[index]

                    out = ' '.join(my_list)
                    print("Message:{", "'STATUS':", Status, "'TEXT':", out, ",",
                          "'PARAMS': {'repeat_always':", a, ' ', b,
                          "},'DATE':{" "'hour':", hour, ",", "'minute':", minute, "}", sep='')
                    exit()

                elif (my_list[index + 1] in minute_mass):
                    find_delayed_minute = '1'
                    find_delayed_hour = 0
                    a = my_list[index + 1]
                    b = my_list[index + 2]
                    while hour > 23:
                        hour -= 24
                        Day += 1

                    for i in range(2):
                        del my_list[index]

                    out = ' '.join(my_list)
                    print("Message:{", "'STATUS':", Status, "'TEXT':", out, ",",
                          "'PARAMS': {'repeat_always':", a, ' ', b,
                          "},'DATE':{" "'hour':", hour, ",", "'minute':", minute, "}", sep='')
                    exit()

                if my_list[index + 1].isdigit() and (my_list[index + 2] in hour_mass):
                    find_delayed_minute = 0
                    find_delayed_hour = my_list[index + 1]
                    hour += int(find_delayed_hour)
                    a = my_list[index + 1]
                    b = my_list[index + 2]
                    while hour > 23:
                        hour -= 24
                        Day += 1

                    for i in range(3):
                        del my_list[index]

                    out = ' '.join(my_list)
                    print("Message:{", "'STATUS':", Status, "'TEXT':", out, ",",
                          "'PARAMS': {'repeat_always':", a, ' ', b,
                          "},'DATE':{" "'hour':", hour, ",", "'minute':", minute, "}", sep='')
                    exit()

                elif (my_list[index + 1] in hour_mass):
                    find_delayed_minute = 0
                    find_delayed_hour = 1
                    hour += find_delayed_hour
                    while hour > 23:
                        hour -= 24
                        Day += 1
                    for i in range(2):
                        del my_list[index]

                    out = ' '.join(my_list)
                    print("Message:{", "'STATUS':", Status, "'TEXT':", out, ",",
                          "'PARAMS': {'repeat_always':", "каждый час",
                          "},'DATE':{" "'hour':", hour, ",", "'minute':", minute, "}", sep='')
                    exit()

                for c in match_find_delay_hour:
                    if my_list[index + 2] == c:
                        for d in match_find_delay_minute:
                            if my_list[index + 4] == d:
                                find_delayed_hour = my_list[index + 1]
                                find_delayed_minute = my_list[index + 3]
                                minute += int(find_delayed_minute)
                                hour += int(find_delayed_hour)
                                while minute > 59:
                                    minute -= 60
                                    hour += 1

                                while hour > 23:
                                    hour -= 24
                                    Day += 1

                                for i in range(5):
                                    del my_list[index]

                                out = ' '.join(my_list)

                                print('Каждые', find_delayed_hour, 'час', 'каждые', find_delayed_minute,
                                      'минут')
                                print("Message:{", "'STATUS':", Status, "'TEXT':", Remind, ",",
                                      "'PARAMS': {'repeat_always':", my_list[index + 1], ' ',
                                      my_list[index + 2], ' ', my_list[index + 4], ' ', my_list[index + 5],
                                      '  ', "},'DATE':{" "'hour':", hour, ",", "'minute':", minute, "}", sep='')
                                exit()
            except IndexError:
                pass

        elif (match_find_delay_day or match_find_delay_month or match_find_delay_year) and (
                'каждый' or 'Каждый' or 'каждые' or 'Каждые' or 'каждую' or 'Каждую' in my_list):
            try:
                if my_list[index + 1].isdigit() and (my_list[index + 2] in match_find_delay_day):
                    find_delayed_year = 0
                    find_delayed_month = 0
                    find_delayed_day = my_list[index + 1]
                    Day += int(find_delayed_day)
                    a = my_list[index + 1]
                    b = my_list[index + 2]
                    for i in range(3):
                        del my_list[index]

                    out = ' '.join(my_list)
                    print("Message:{", "'STATUS':", Status, "'TEXT':", out, ",",
                          "'PARAMS': {'repeat_always':", a, ' ', b,
                          "},'DATE':{" "'hour':", hour, ",", "'minute':", minute, "}", sep='')
                    exit()

                elif my_list[index + 1] in match_find_delay_day:
                    find_delayed_year = 0
                    find_delayed_month = 0
                    find_delayed_day = '1'
                    Day += int(find_delayed_day)

                    for i in range(2):
                        del my_list[index]

                    out = ' '.join(my_list)
                    print("Message:{", "'STATUS':", Status, "'TEXT':", out, ",",
                          "'PARAMS': {'repeat_always':", "каждый день",
                          "},'DATE':{" "'hour':", hour, ",", "'minute':", minute, "}", sep='')
                    exit()

                if my_list[index + 1].isdigit() and (my_list[index + 2] in match_find_delay_month):
                    find_delayed_year = 0
                    find_delayed_day = 0
                    find_delayed_month = my_list[index + 1]
                    Month += int(find_delayed_month)
                    a = my_list[index + 1]
                    b = my_list[index + 2]
                    for i in range(3):
                        del my_list[index]

                    out = ' '.join(my_list)
                    print("Message:{", "'STATUS':", Status, "'TEXT':", out, ",",
                          "'PARAMS': {'repeat_always':", a, ' ', b,
                          "},'DATE':{" "'hour':", hour, ",", "'minute':", minute, "}", sep='')
                    exit()

                elif my_list[index + 1] in match_find_delay_month:
                    find_delayed_year = 0
                    find_delayed_day = 0
                    find_delayed_month = '1'
                    Month += int(find_delayed_month)
                    for i in range(2):
                        del my_list[index]
                    out = ' '.join(my_list)
                    print("Message:{", "'STATUS':", Status, "'TEXT':", out, ",",
                          "'PARAMS': {'repeat_always':", "каждый месяц",
                          "},'DATE':{" "'hour':", hour, ",", "'minute':", minute, "}", sep='')
                    exit()

                if my_list[index + 1].isdigit() and (my_list[index + 2] in match_find_delay_year):
                    find_delayed_year = my_list[index + 1]
                    find_delayed_month = 0
                    find_delayed_day = 0
                    a = my_list[index + 1]
                    b = my_list[index + 2]
                    Year += int(find_delayed_year)
                    for i in range(3):
                        del my_list[index]

                    out = ' '.join(my_list)
                    print("Message:{", "'STATUS':", Status, "'TEXT':", out, ",",
                          "'PARAMS': {'repeat_always':", a, ' ', b,
                          "},'DATE':{" "'hour':", hour, ",", "'minute':", minute, "}", sep='')
                    exit()

                elif my_list[index + 1] in match_find_delay_year:
                    find_delayed_year = '1'
                    find_delayed_month = 0
                    find_delayed_day = 0
                    Year += int(find_delayed_year)
                    for i in range(2):
                        del my_list[index]

                    out = ' '.join(my_list)
                    print("Message:{", "'STATUS':", Status, "'TEXT':", out, ",",
                          "'PARAMS': {'repeat_always':", "каждый год",
                          "},'DATE':{" "'hour':", hour, ",", "'minute':", minute, "}", sep='')
                    exit()

                for j in match_find_delay_year:
                    if my_list[index + 2] == j:
                        for k in match_find_delay_month:
                            if my_list[index + 4] == k:
                                for l in match_find_delay_day:
                                    if my_list[index + 6] == l:
                                        find_delayed_year = my_list[index + 1]
                                        find_delayed_month = my_list[index + 3]
                                        find_delayed_day = my_list[index + 5]
                                        Day += int(find_delayed_day)
                                        Month += int(find_delayed_month)
                                        Year += int(find_delayed_year)

                                        for i in range(7):
                                            del my_list[index]

                                        out = ' '.join(my_list)
                                        print('Каждые', find_delayed_year, 'лет', 'каждые', find_delayed_month,
                                              'месяцев', 'каждые', find_delayed_day, 'дней')
                                        exit()

            except (IndexError, NameError):
                pass

    for j in range(len(my_list)):
        if my_list[j] in Mondays:
            day_week = 'Monday'
            day_week_compare = 1

        elif my_list[j] in Tuesdays:
            day_week = 'Tuesday'
            day_week_compare = 2
        elif my_list[j] in Wendsdays:
            day_week = 'Wendsday'
            day_week_compare = 3
        elif my_list[j] in Thursdays:
            day_week = 'Thursday'
            day_week_compare = 4
        elif my_list[j] in Fridays:
            day_week = 'Friday'
            day_week_compare = 5
        elif my_list[j] in Saturdays:
            day_week = 'Saturday'
            day_week_compare = 6
        elif my_list[j] in Sundays:
            day_week = 'Sunday'
            day_week_compare = 7

    if day_week:
        if 'каждый' in my_list:
            each()
        elif 'Каждый' in my_list:
            each()
        elif 'каждую' in my_list:
            each()
        elif 'каждый' in my_list:
            each()
        elif 'каждое' in my_list:
            each()
        elif 'Каждое' in my_list:
            each()

        else:
            if len(my_list) > 3:
                for i in range(4):
                    del my_list[-1]
                out = str(' '.join(my_list))
                print("Message:{", "'STATUS':", Status, "'TEXT':", out, ",", "'PARAMS': {'day_of_week':", day_week,
                      "},'DATE':{" "'hour':", hour, ",", "'minute':", minute, "}", sep='')
                exit()
            else:
                for i in range(2):
                    del my_list[0]
                out = str(' '.join(my_list))
                print("Message:{", "'STATUS':", Status, "'TEXT':", out, ",", "'PARAMS': {'day_of_week':", day_week,
                      "},'DATE':{" "'hour':", hour, ",", "'minute':", minute, "}", sep='')
                exit()

    if (match_find_delay_minute or match_find_delay_hour) and ('через' or 'Через' in my_list):
        try:
            if 'через' in my_list:
                index = my_list.index('через')

            elif 'Через' in my_list:
                index = my_list.index('Через')
            else:
                if 'каждый' or 'Каждый' or 'каждые' or 'Каждые' or 'каждую' or 'Каждую' or 'каждое' or 'Каждое' in my_list:
                    each()
                else:
                    pass

            if my_list[index + 1].isdigit() and my_list[index + 2] in minute_mass:
                find_delayed_hour = 0
                find_delayed_minute = my_list[index + 1]
                minute += int(find_delayed_minute)
                while minute > 60:
                    minute -= 60
                    hour += 1
                while hour > 23:
                    hour -= 24
                    Day += 1

                for i in range(3):
                    del my_list[index]

                out = ' '.join(my_list)

                print("Message:{", "'STATUS':", Status, ",", "'DATE':{'year':", Year, ",", "'month':",
                      Month, ",", "'day':", Day,
                      ",", "'hour':", hour, ",", "'minute':", minute, "}", ",", "'TEXT':", out, "}",
                      sep='')
                exit()

            if my_list[index + 1].isdigit() and my_list[index + 2] in hour_mass:
                find_delayed_minute = 0
                find_delayed_hour = my_list[index + 1]
                hour += int(find_delayed_hour)
                while hour > 23:
                    hour -= 24
                    Day += 1

                for i in range(3):
                    del my_list[index]

                out = ' '.join(my_list)
                print("Message:{", "'STATUS':", Status, ",", "'DATE':{'year':", Year, ",", "'month':",
                      Month, ",", "'day':", Day,
                      ",", "'hour':", hour, ",", "'minute':", minute, "}", ",", "'TEXT':", out, "}",
                      sep='')
                exit()

            elif my_list[index + 1] in match_find_delay_hour:
                find_delayed_minute = 0
                find_delayed_hour = '1'
                hour += int(find_delayed_hour)

                while hour > 23:
                    hour -= 24
                    Day += 1

                for i in range(2):
                    del my_list[index]

                out = ' '.join(my_list)

                print("Message:{", "'STATUS':", Status, ",", "'DATE':{'year':", Year, ",", "'month':",
                      Month, ",", "'day':", Day,
                      ",", "'hour':", hour, ",", "'minute':", minute, "}", ",", "'TEXT':", out, "}",
                      sep='')
                exit()

            if match_find_delay_minute and match_find_delay_hour:
                for c in match_find_delay_hour:
                    if my_list[index + 2] == c:
                        for d in match_find_delay_minute:
                            if my_list[index + 4] == d:
                                find_delayed_hour = my_list[index + 1]
                                find_delayed_minute = my_list[index + 3]
                                minute += int(find_delayed_minute)
                                hour += int(find_delayed_hour)
                                print(hour, minute)

                                while minute > 59:
                                    minute -= 60
                                    hour += 1

                                while hour > 23:
                                    hour -= 24
                                    Day += 1

                                for i in range(5):
                                    del my_list[index]

                                out = ' '.join(my_list)

                                print("Message:{", "'STATUS':", Status, ",", "'DATE':{'year':", Year, ",",
                                      "'month':",
                                      Month, ",", "'day':", Day, ",", "'hour':", hour, ",", "'minute':", minute,
                                      "}", ",", "'TEXT':", out,
                                      "}", sep='')
                                exit()

        except IndexError:
            pass

    if (match_find_delay_day or match_find_delay_month or match_find_delay_year) and ('через' or 'Через' in my_list):
        try:

            if 'через' in my_list:
                index = my_list.index('через')

            elif 'Через' in my_list:
                index = my_list.index('Через')
            else:
                if 'каждый' or 'Каждый' or 'каждые' or 'Каждые' or 'каждую' or 'Каждую' or 'каждое' or 'Каждое' in my_list:
                    each()
                else:
                    pass

            if my_list[index + 1].isdigit() and my_list[index + 2] in match_find_delay_day:
                find_delayed_year = 0
                find_delayed_month = 0
                find_delayed_day = my_list[index + 1]
                Day += int(find_delayed_day)

                for i in range(3):
                    del my_list[index]

                out = ' '.join(my_list)

                print("Message:{", "'STATUS':", Status, ",", "'DATE':{'year':", Year, ",", "'month':",
                      Month, ",", "'day':", Day,
                      ",", "'hour':", hour, ",", "'minute':", minute, "}", ",", "'TEXT':", out, "}", sep='')
                exit()

            elif my_list[index + 1] in match_find_delay_day:
                find_delayed_year = 0
                find_delayed_month = 0
                find_delayed_day = '1'
                Day += int(find_delayed_day)

                for i in range(2):
                    del my_list[index]

                out = ' '.join(my_list)

                print("Message:{", "'STATUS':", Status, ",", "'DATE':{'year':", Year, ",", "'month':",
                      Month, ",", "'day':", Day,
                      ",", "'hour':", hour, ",", "'minute':", minute, "}", ",", "'TEXT':", out, "}",
                      sep='')
                exit()

            if my_list[index + 1].isdigit() and my_list[index + 2] in match_find_delay_month:
                find_delayed_year = 0
                find_delayed_day = 0
                find_delayed_month = my_list[index + 1]
                Month += int(find_delayed_month)
                for i in range(3):
                    del my_list[index]

                out = ' '.join(my_list)
                print("Message:{", "'STATUS':", Status, ",", "'DATE':{'year':", Year, ",", "'month':",
                      Month, ",", "'day':", Day,
                      ",", "'hour':", hour, ",", "'minute':", minute, "}", ",", "'TEXT':", out, "}",
                      sep='')
                exit()

            elif my_list[index + 1] in match_find_delay_month:
                find_delayed_year = 0
                find_delayed_day = 0
                find_delayed_month = '1'
                Month += int(find_delayed_month)

                for i in range(2):
                    del my_list[index]

                out = ' '.join(my_list)

                print("Message:{", "'STATUS':", Status, ",", "'DATE':{'year':", Year, ",", "'month':",
                      Month, ",", "'day':", Day,
                      ",", "'hour':", hour, ",", "'minute':", minute, "}", ",", "'TEXT':", out, "}",
                      sep='')
                exit()

            if my_list[index + 1].isdigit() and my_list[index + 2] in match_find_delay_year:
                find_delayed_year = my_list[index + 1]
                find_delayed_month = 0
                find_delayed_day = 0
                Year += int(find_delayed_year)

                for i in range(3):
                    del my_list[index]

                out = ' '.join(my_list)
                print("Message:{", "'STATUS':", Status, ",", "'DATE':{'year':", Year, ",", "'month':",
                      Month, ",", "'day':", Day,
                      ",", "'hour':", hour, ",", "'minute':", minute, "}", ",", "'TEXT':", out, "}",
                      sep='')
                exit()

            elif my_list[index + 1] in match_find_delay_year:
                find_delayed_year = '1'
                find_delayed_month = 0
                find_delayed_day = 0
                Year += int(find_delayed_year)
                for i in range(2):
                    del my_list[index]

                out = ' '.join(my_list)

                print("Message:{", "'STATUS':", Status, ",", "'DATE':{'year':", Year, ",", "'month':",
                      Month, ",", "'day':", Day,
                      ",", "'hour':", hour, ",", "'minute':", minute, "}", ",", "'TEXT':", out, "}",
                      sep='')
                exit()

            for j in match_find_delay_year:
                if my_list[index + 2] == j:
                    for k in match_find_delay_month:
                        if my_list[index + 4] == k:
                            for l in match_find_delay_day:
                                if my_list[index + 6] == l:
                                    find_delayed_year = my_list[index + 1]
                                    find_delayed_month = my_list[index + 3]
                                    find_delayed_day = my_list[index + 5]
                                    Day += int(find_delayed_day)
                                    Month += int(find_delayed_month)
                                    Year += int(find_delayed_year)
                                    for i in range(7):
                                        del my_list[index]

                                    out = ' '.join(my_list)

                                    print("Message:{", "'STATUS':", Status, ",", "'DATE':{'year':", Year, ",",
                                          "'month':",
                                          Month, ",", "'day':", Day,
                                          ",", "'hour':", hour, ",", "'minute':", minute, "}", ",", "'TEXT':", out,
                                          "}", sep='')
                                    exit()

        except (IndexError, NameError):
            pass

    print("Message:{", "'STATUS':", Status, ",", "'DATE':{'year':", Year, ",", "'month':", Month, ",", "'day':", Day,
          ",", "'hour':", hour, ",", "'minute':", minute, "}", ",", "'TEXT':", Remind, "}", sep='')
    if 'каждый' or 'Каждый' or 'каждые' or 'Каждые' or 'каждую' or 'Каждую' or 'каждое' or 'Каждое' in my_list:
        each()


if __name__ == '__main__':
    main()
