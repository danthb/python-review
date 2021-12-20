# Calculate year, months, days between two dates
def calculate(year1, month1, day1, year2, month2, day2) -> str:
    # Calculate years
    years = year2 - year1
    # Calculate months
    months = month2 - month1
    # Calculate days
    days = day2 - day1
    # Calculate days in months
    if months < 0:
        months = months + 12
        years = years - 1
    # Calculate days in years
    if years < 0:
        years = years + 1
        months = months - 12
    # Calculate days in months
    if days < 0:
        days = days + 30
        months = months - 1
    # Calculate days in months
    if months < 0:
        months = months + 12
        years = years - 1
    # Return results
    return str(years) + " , " + str(months) + " , " + str(days)
