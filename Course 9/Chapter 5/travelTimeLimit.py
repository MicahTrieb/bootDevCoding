#Lesson Link: https://www.boot.dev/lessons/ebb8cb27-e304-4799-b0b6-8d2137bceef4


def num_countries_in_days(max_days, factor):
    time_left = max_days
    count = 0
    time_in_country = 1
    if factor < 1:
        return 1
        

    while time_left > 0:
        if time_in_country > time_left:
            break
        count += 1
        time_in_country += 1
        time_in_country = time_in_country * factor
    return count

