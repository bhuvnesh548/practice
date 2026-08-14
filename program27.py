from datetime import datetime, timedelta
now = datetime.now()
print("Now:", now.strftime("%Y-%m-%d %H:%M:%S"))
next_week = now + timedelta(days=7)
print("Next week:", next_week.strftime("%Y-%m-%d"))