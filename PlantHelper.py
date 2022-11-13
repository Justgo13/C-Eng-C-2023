import random

def will_plant_die_next_year(age, lifespan):
    if(age+1 >= lifespan):
        return False
    else:
        return True


def can_produce_seeds(age, seed_production_year):
    if(age >= seed_production_year):
        return False
    else:
        return True


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


def get_overall_factor(factor_prep, factor_temp, factor_shade):
    return factor_prep * factor_temp * factor_shade


def does_plant_die(percent_from_prep, percent_from_temp, percent_from_shade):
    percent_living = (1-percent_from_prep) * (1-percent_from_temp), (1-percent_from_shade)
    rolled_dice = random.random()

    if percent_living < rolled_dice:
        return True
    else:
        return False

