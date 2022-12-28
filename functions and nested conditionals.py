def time (month,year):
    if month in {"jan","mar","may","jul","aug","oct","dec"}:
        print ("31 days")
    elif month == "feb":
        if year%4 == 0:
            print ("29 days")
        else:
            print ("28 days")
    else:
        print ("30 days")
time("feb",2020)