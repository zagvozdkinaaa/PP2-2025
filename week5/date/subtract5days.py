import datetime

current_date = datetime.datetime.now()

new_date = current_date - datetime.timedelta(days=5)

print(f"current date: {current_date}")
print(f"after subtraction: {new_date}")