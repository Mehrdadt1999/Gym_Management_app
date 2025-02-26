from khayyam import JalaliDate
from window import war_window

def is_valid_date(year, month, day):
    try:
        jalali_date = JalaliDate(year=year, month=month, day=day)
        if jalali_date.month <= 6:
            return 1 <= jalali_date.day <= 31
        elif jalali_date.month > 6:
            return 1 <= jalali_date.day <= 30
        else:
            war_window(".تاریخ وارد شده اشتباه است")
    except:
        war_window(".تاریخ وارد شده اشتباه است")
        return 0
    