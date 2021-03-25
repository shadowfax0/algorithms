from datetime import datetime, timedelta
import holidays

us_holidays = holidays.UnitedStates()

# return the last business day
def business_day(today):
  
  weekend = datetime.weekday(today - timedelta(days=1)) >= 5
  holiday = today - timedelta(days=1) in us_holidays
  
  if holiday or weekend:
    try_next = today - timedelta(days=1)
    return business_day(try_next)
  else:
    return business_day - timedelta(days=1)



today = datetime.today()
last_bizday = business_day(today)

