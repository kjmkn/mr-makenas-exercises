def days(month):
    if month in ["jan", "mar", "may", "jul", "aug", "oct", "dec"]:
        print("30 days")
    elif month == "feb":
        year = int(input("What year is it? "))
        if year % 4 == 0:
            print("29 days")
        else:
            print("28 days")

    else:
        print("30 days")


days("feb")
