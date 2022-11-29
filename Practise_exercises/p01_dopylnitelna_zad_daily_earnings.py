work_days = int(input())
earned_money_per_day = float(input())
usd_to_leva = float(input())

montly_salary = work_days * earned_money_per_day
bonus = montly_salary * 2.5
annual_earnings = (montly_salary * 12) + bonus
earnings_after_taxes = annual_earnings - annual_earnings * 0.25

annual_earnings_in_leva = earnings_after_taxes * usd_to_leva

daily_earnings_in_leva = annual_earnings_in_leva / 365

print(f"{daily_earnings_in_leva:.2f}")
