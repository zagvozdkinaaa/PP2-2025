from datetime import datetime, timedelta

today=datetime.now()
yesterday=today-timedelta(days=1)
tomorrow=today+timedelta(days=1)
print(yesterday, '\n', today, '\n', tomorrow)