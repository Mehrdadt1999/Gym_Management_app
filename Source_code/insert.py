from tkinter import *
import sqlite3
from khayyam import JalaliDate
from window import war_window
from date_check import is_valid_date

# Current date
current_persian_date = JalaliDate.today()

# function for insert data to database
def insert(f_name, l_name, phone_number, tuition, day, month, national_id, major, receipt, acc_type):
    if is_valid_date(current_persian_date.year, month.get(), day.get()):
        value = str(tuition.get()).replace(",", "")
        
        try:
            # Create a JalaliDate object
            jalali_date = JalaliDate(current_persian_date.year, int(month.get()), int(day.get()))
            # Format the JalaliDate object to the desired string format
            date = jalali_date.strftime('%Y-%m-%d')
        except ValueError:
            war_window('.لطفاً تمامی موارد را تکمیل نمایید')
             
        
        if national_id.get() != '' and phone_number.get() != '' and f_name.get() != '' and l_name.get() != '':
            try:
                int(value)
                int(national_id.get())
                int(phone_number.get())
                #connect to Database 
                gym = sqlite3.connect('gym_db.db')

                # Create cursor
                c = gym.cursor()

                c.execute("INSERT INTO members VALUES(:national_id, :date, :tuition, :phone_number, :l_name, :f_name, :major, :acc_type, :receipt)",
                        {
                            'f_name': f_name.get(),
                            'l_name': l_name.get(),
                            'phone_number': phone_number.get(),
                            'tuition': tuition.get(),
                            'date': date,
                            'national_id': national_id.get(),
                            'major': major.get(),
                            'acc_type': acc_type.get(),
                            'receipt': receipt.get()
                        })
                
                c.execute("INSERT INTO tuitions VALUES(:receipt, :date, :tuition, :major, :national_id, :acc_type)",
                        {
                            'receipt': receipt.get(),
                            'tuition': tuition.get(),
                            'date': date,
                            'major': major.get(),
                            'acc_type': acc_type.get(),
                            'national_id': national_id.get(),
                        })
                # # Commit chages
                gym.commit()

                f_name.delete(0, END)
                l_name.delete(0, END)
                phone_number.delete(0, END)
                tuition.delete(0, END)
                national_id.delete(0, END)
                day.delete(0, END)
                month.delete(0, END)
                receipt.delete(0, END)
            except sqlite3.IntegrityError:
                war_window('.کد ملی یا شماره فیش مشکل دارد')
            except:
                war_window(".لطفاً به ازای شماره تلفن، کد ملی و شهریه عدد وارد کنید")
        else:
            war_window('.لطفاً تمامی موارد را تکمیل نمایید')

        
