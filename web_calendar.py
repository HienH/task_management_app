import calendar
# Create a plain text calendar

def make_calendar():
    c = calendar.TextCalendar(calendar.MONDAY)
    dynamic_calendar = c.formatmonth(2019,2)
    return dynamic_calendar
