from datetime import datetime
def sec_difference():
    date_str1=input("Enter the first date in format DD.MM.YYYY HH:MM:SS: ")
    date_str2=input("Enter the second date in format DD.MM.YYYY HH:MM:SS: ")

    date_format = "%d.%m.%Y %H:%M:%S"

    try:
        date1 = datetime.strptime(date_str1, date_format)
        date2 = datetime.strptime(date_str2, date_format)
    except:
        print("You entered the wrong date format")

    dates_diff=abs(date2 - date1)
    seconds_difference = dates_diff.total_seconds()
    print(seconds_difference)
sec_difference()
