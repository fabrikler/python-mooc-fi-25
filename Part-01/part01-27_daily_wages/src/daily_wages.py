hourly_wage = float(input("Hourly wage:"))
hours_worked = float(input("Hours worked:"))
weekday = input("Day of the week:")

daily_wages = float(hourly_wage * hours_worked)

if weekday == "Sunday":
    daily_wages = 2 * daily_wages

print("Daily wages:", daily_wages, "euros")