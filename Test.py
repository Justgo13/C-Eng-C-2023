
upper_temp =15
lower_temp=-10

temp_today=-13
temp_tomorrow=16


def get_quadric_difference(upper_temp, lower_temp, temp_today):
    difference = upper_temp - lower_temp
    
    normRight = upper_temp + difference

    if temp_today <= upper_temp and temp_today >= lower_temp:
        return 1
    elif temp_today < lower_temp:
        normLeft = lower_temp - difference
        if temp_today <= normLeft:
            temp_today = normLeft
        normal_value =  (temp_today - normLeft) / (lower_temp - normLeft)
        normal_value = normal_value
        return normal_value**2
    else:
        normRight = upper_temp + difference
        if temp_today >= normRight:
            temp_today = normRight
        normal_value =  (temp_today - upper_temp) / (normRight - upper_temp)
        return (1-normal_value)**2


def get_factor_for_temp(upper_temp, lower_temp, temp_today, growth_rate):
    quadratic_difference = get_quadric_difference(upper_temp, lower_temp, temp_today)

    return quadratic_difference * growth_rate

def get_factor_for_precipitation(upper_prep, lower_prep, prep_today, growth_rate):
    quadratic_difference = get_quadric_difference(upper_prep, lower_prep, prep_today)

    return quadratic_difference * growth_rate


def get_percent_chance_die_by_temp(upper_temp, lower_temp, temp_today, growth_rate):
    return (1- get_factor_for_temp(upper_temp, lower_temp, temp_today, growth_rate)) * 0.3

def get_percent_chance_die_by_prep(upper_prep, lower_prep, prep_today, growth_rate):
    return (1- get_factor_for_precipitation(upper_prep, lower_prep, prep_today, growth_rate)) * 0.3


if __name__ == "__main__":
   print(get_temp_effect(upper_temp, lower_temp, -11))

   print(get_temp_effect(15, -5, 10))
   print(get_temp_effect(15, -5, -7))
   print(get_temp_effect(15, -5, -19))
   print(get_temp_effect(15, -5, -25))
   print(get_temp_effect(15, -5, -45))
   print("\n")
   print(get_temp_effect(15, -5, 10))
   print(get_temp_effect(15, -5, 20))
   print(get_temp_effect(15, -5, 35))
   print(get_temp_effect(15, -5, 39))
   print(get_temp_effect(15, -5, 45))

        