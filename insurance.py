def calculate_compound_interest(years_until_pension, year_revenue, starting_monthly_capital):
    total_value = 0.0

    for i in range(0, years_until_pension):
        total_value = total_value + (starting_monthly_capital * 12)
        total_value = total_value + (total_value * (year_revenue / 100))

    return total_value


print(calculate_compound_interest(30, 6, 365))


def percentage_decrease_of_initial_investment_price_6(remain_years, revenue, initial_amount_per_month):
    if remain_years == 40 and revenue == 6:
        return initial_amount_per_month - (initial_amount_per_month * 0.75409)
    elif remain_years == 39 and revenue == 6:
        return initial_amount_per_month - (initial_amount_per_month * 0.74545)
    elif remain_years == 38 and revenue == 6:
        return initial_amount_per_month - (initial_amount_per_month * 0.73544)
    elif remain_years == 37 and revenue == 6:
        return initial_amount_per_month - (initial_amount_per_month * 0.72429)
    elif remain_years == 36 and revenue == 6:
        return initial_amount_per_month - (initial_amount_per_month * 0.715)
    elif remain_years == 35 and revenue == 6:
        return initial_amount_per_month - (initial_amount_per_month * 0.70434)
    elif remain_years == 34 and revenue == 6:
        return initial_amount_per_month - (initial_amount_per_month * 0.69201)
    elif remain_years == 33 and revenue == 6:
        return initial_amount_per_month - (initial_amount_per_month * 0.67892)
    elif remain_years == 32 and revenue == 6:
        return initial_amount_per_month - (initial_amount_per_month * 0.66863)
    elif remain_years == 31 and revenue == 6:
        return initial_amount_per_month - (initial_amount_per_month * 0.65526)
    elif remain_years == 30 and revenue == 6:
        return initial_amount_per_month - (initial_amount_per_month * 0.64235)
    elif remain_years == 29 and revenue == 6:
        return initial_amount_per_month - (initial_amount_per_month * 0.62947)
    elif remain_years == 28 and revenue == 6:
        return initial_amount_per_month - (initial_amount_per_month * 0.61436)
    elif remain_years == 27 and revenue == 6:
        return initial_amount_per_month - (initial_amount_per_month * 0.60068)
    elif remain_years == 26 and revenue == 6:
        return initial_amount_per_month - (initial_amount_per_month * 0.58615)
    elif remain_years == 25 and revenue == 6:
        return initial_amount_per_month - (initial_amount_per_month * 0.57023)
    elif remain_years == 24 and revenue == 6:
        return initial_amount_per_month - (initial_amount_per_month * 0.55485)
    elif remain_years == 23 and revenue == 6:
        return initial_amount_per_month - (initial_amount_per_month * 0.53828)
    elif remain_years == 22 and revenue == 6:
        return initial_amount_per_month - (initial_amount_per_month * 0.52227)
    elif remain_years == 21 and revenue == 6:
        return initial_amount_per_month - (initial_amount_per_month * 0.50424)
    elif remain_years == 20 and revenue == 6:
        return initial_amount_per_month - (initial_amount_per_month * 0.48759)
    elif remain_years == 19 and revenue == 6:
        return initial_amount_per_month - (initial_amount_per_month * 0.46935)
    elif remain_years == 18 and revenue == 6:
        return initial_amount_per_month - (initial_amount_per_month * 0.45077)
    elif remain_years == 17 and revenue == 6:
        return initial_amount_per_month - (initial_amount_per_month * 0.43129)
    elif remain_years == 16 and revenue == 6:
        return initial_amount_per_month - (initial_amount_per_month * 0.41216)
    elif remain_years == 15 and revenue == 6:
        return initial_amount_per_month - (initial_amount_per_month * 0.39224)
    elif remain_years == 14 and revenue == 6:
        return initial_amount_per_month - (initial_amount_per_month * 0.37173)
    elif remain_years == 13 and revenue == 6:
        return initial_amount_per_month - (initial_amount_per_month * 0.35064)
    elif remain_years == 12 and revenue == 6:
        return initial_amount_per_month - (initial_amount_per_month * 0.32904)
    elif remain_years == 11 and revenue == 6:
        return initial_amount_per_month - (initial_amount_per_month * 0.30670)
    elif remain_years == 10 and revenue == 6:
        return initial_amount_per_month - (initial_amount_per_month * 0.28411)
    elif remain_years == 9 and revenue == 6:
        return initial_amount_per_month - (initial_amount_per_month * 0.26122)
    elif remain_years == 8 and revenue == 6:
        return initial_amount_per_month - (initial_amount_per_month * 0.23747)
    elif remain_years == 7 and revenue == 6:
        return initial_amount_per_month - (initial_amount_per_month * 0.21337)
    elif remain_years == 6 and revenue == 6:
        return initial_amount_per_month - (initial_amount_per_month * 0.17789)
    elif remain_years == 5 and revenue == 6:
        return initial_amount_per_month - (initial_amount_per_month * 0.15785)
    elif remain_years == 4 and revenue == 6:
        return initial_amount_per_month - (initial_amount_per_month * 0.13)
    elif remain_years == 3 and revenue == 6:
        return initial_amount_per_month - (initial_amount_per_month * 0.11567)
    elif remain_years == 2 and revenue == 6:
        return initial_amount_per_month - (initial_amount_per_month * 0.07543)
    elif remain_years == 1 and revenue == 6:
        return initial_amount_per_month - (initial_amount_per_month * 0.05661)

print(percentage_decrease_of_initial_investment_price_6(37,6,351))