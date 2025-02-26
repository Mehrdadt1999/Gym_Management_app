from tkinter import *
from tkinter import ttk
from insert import insert
from format_entry import format_entry
from show_table import show_all_table, show_account, show_Tracking_table
from khayyam import JalaliDate
from search_update import search, renewal
import shutil
import os
# from Tracking import Tracking

# Current date
current_persian_date = JalaliDate.today()

# all type of majors
major_options = ["بدنسازی", "کاراته", "تکواندو", "مدرسه بسکتبال", "مدرسه والیبال", "مدرسه فوتبال", "باستانی", "کشتی", "چمن مصنوعی", "سالن توپی", "ژیمناستیک"]

# Define a Persian font
persian_font_b = ("B Nazanin", 12, "bold")
persian_font = ("B Nazanin", 13, "normal")

root=Tk()
root.title(" باشگاه عقاب")
root.iconbitmap('eagle.ico')

# Make Add record part

# make insert frame
insert_frame = LabelFrame(root, text="اضافه کردن افراد", padx=10, pady=10, labelanchor='ne', font=persian_font_b)
insert_frame.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

# Labels in insert frame 
f_name_label = Label(insert_frame, text=":نام", justify=RIGHT, font=persian_font)
f_name_label.grid(row=0, column=7)

l_name_label = Label(insert_frame, text=":نام‌خانوادگی", justify=RIGHT, font=persian_font)
l_name_label.grid(row=1, column=7)

phone_number_label = Label(insert_frame, text=":شماره تماس", justify=RIGHT, font=persian_font)
phone_number_label.grid(row=0, column=4)

tuition_label = Label(insert_frame, text=": شهریه _ تومان", justify=RIGHT, font=persian_font)
tuition_label.grid(row=1, column=4)

date_label = Label(insert_frame, text=":تاریخ", justify=RIGHT, font=persian_font)
date_label.grid(row=0, column=1)

national_id_label = Label(insert_frame, text=":کد ملی", justify=RIGHT, font=persian_font)
national_id_label.grid(row=1, column=1)

accType_label = Label(insert_frame, text=":نوع پذیرش", justify=RIGHT, font=persian_font)
accType_label.grid(row=2, column=7)

receipt_label = Label(insert_frame, text=":شماره فیش", justify=RIGHT, font=persian_font)
receipt_label.grid(row=2, column=4)

major_label = Label(insert_frame, text=":رشته", justify=RIGHT, font=persian_font)
major_label.grid(row=2, column=1)

# Entries in insert frame
f_name = Entry(insert_frame, justify=RIGHT)
f_name.grid(row=0, column=6)

l_name = Entry(insert_frame, justify=RIGHT)
l_name.grid(row=1, column=6)

accType_options = ["نیرو هوایی", "سایر نیروها", "آزاد"]
accType_Combo = ttk.Combobox(insert_frame, values=accType_options, justify=RIGHT, width=17)
accType_Combo.current(0)
accType_Combo.bind("<<ComboboxSelected>>")
accType_Combo.option_add('*TCombobox*Listbox.Justify', 'center')
accType_Combo.grid(row=2, column=6)

phone_number = Entry(insert_frame, justify=RIGHT)
phone_number.grid(row=0, column=3)

tuition = Entry(insert_frame, justify=RIGHT)
tuition.grid(row=1, column=3)
tuition.bind("<KeyRelease>", lambda event: format_entry(tuition))

receipt = Entry(insert_frame, justify=RIGHT)
receipt.grid(row=2, column=3)

date_frame = LabelFrame(insert_frame)
date_frame.grid(row=0, column=0)

day = Entry(date_frame, width=11, justify=RIGHT)
day.grid(row=0, column=3)
day.insert(0, "روز")
day.bind("<FocusIn>", lambda event: day.delete(0, END))

month = Entry(date_frame, width=11, justify=RIGHT)
month.grid(row=0, column=1)
Label(date_frame, text='/').grid(row=0, column=2)
month.insert(0, "ماه")
month.bind("<FocusIn>", lambda event: month.delete(0, END))

year_text = str(current_persian_date.year)+'/'
year = Label(date_frame, text=year_text, justify=RIGHT)
year.grid(row=0, column=0)

national_id = Entry(insert_frame, justify=RIGHT)
national_id.grid(row=1, column=0)

major_combo_i = ttk.Combobox(insert_frame, values=major_options, justify=RIGHT, width=17)
major_combo_i.current(0)
major_combo_i.bind("<<ComboboxSelected>>")
major_combo_i.option_add('*TCombobox*Listbox.Justify', 'center')
major_combo_i.grid(row=2, column=0)

# submit button
submit = Button(insert_frame, text="اضافه کردن", font=("B Nazanin", 10, "bold"), command=lambda: 
                insert(f_name, l_name, phone_number, tuition, day, month, national_id, major_combo_i, receipt, accType_Combo))
submit.grid(row=3,column=3, columnspan=2, ipadx=75, padx=10, pady=10)

# daily Tracking
daily_tracking_frame = LabelFrame(root, text="رهگیری روزانه", padx=10, pady=10, labelanchor='ne', font=persian_font_b, width=50, height=30)
daily_tracking_frame.grid(row=1, column=1, padx=10, pady=10)

daily_date_label = Label(daily_tracking_frame, text=":تاریخ", font= ("B Nazanin", 12, "normal"), justify=RIGHT, padx=6)
daily_date_label.grid(row=0, column=5)

major_label = Label(daily_tracking_frame, text=":رشته", justify=RIGHT, font=persian_font)
major_label.grid(row=1, column=5)

dayـT = Entry(daily_tracking_frame, width=11, justify=RIGHT)
dayـT.grid(row=0, column=4, padx=6, pady=10)
dayـT.insert(0, "روز")
dayـT.bind("<FocusIn>", lambda event: dayـT.delete(0, END))

month_T = Entry(daily_tracking_frame, width=11, justify=RIGHT)
month_T.grid(row=0, column=2, padx=25, pady=10)
Label(daily_tracking_frame, text='/').grid(row=0, column=3)
month_T.insert(0, "ماه")
month_T.bind("<FocusIn>", lambda event: month_T.delete(0, END))

major_combo_t = ttk.Combobox(daily_tracking_frame, values=major_options, justify=RIGHT, width=17)
major_combo_t.current(0)
major_combo_t.bind("<<ComboboxSelected>>")
major_combo_t.option_add('*TCombobox*Listbox.Justify', 'center')
major_combo_t.grid(row=1, column=4)

year_T = Label(daily_tracking_frame, text=year_text, justify=RIGHT)
year_T.grid(row=0, column=1, pady=10)

show_tracking = Button(daily_tracking_frame, text="نمایش", padx=10, font= ("B Nazanin", 10, "bold"), width=15, command=lambda:show_Tracking_table(dayـT.get(), month_T.get(), current_persian_date.year, major_combo_t))
show_tracking.grid(row=3, column=1, columnspan=2, padx=10)


# Search and edit
S_and_e_frame = LabelFrame(root, text="جستجو، ویرایش و تمدید", padx=10, pady=10, labelanchor='ne', font=persian_font_b, width=50, height=30)
S_and_e_frame.grid(row=1, column=0, padx=10, pady=10)

nid = Label(S_and_e_frame, text=":کدملی", justify=RIGHT, font=persian_font, padx=6, pady=10)
nid.grid(row=0, column=1, padx=6)

nid_entry = Entry(S_and_e_frame, width = 20, justify=RIGHT)
nid_entry.grid(row=0, column=0)
nid_entry.bind("<FocusIn>", lambda event: nid_entry.delete(0, END))

mj = Label(S_and_e_frame, text=":رشته", justify=RIGHT, font=persian_font, padx=6, pady=10)
mj.grid(row=1, column=1, padx=6)

mj_combo_t = ttk.Combobox(S_and_e_frame, values=major_options, justify=RIGHT, width=17)
mj_combo_t.current(0)
mj_combo_t.bind("<<ComboboxSelected>>")
mj_combo_t.option_add('*TCombobox*Listbox.Justify', 'center')
mj_combo_t.grid(row=1, column=0)

edit_button = Button(S_and_e_frame, text='ویرایش', font=("B Nazanin", 10, "bold"), command=lambda: search(nid_entry.get(), mj_combo_t.get()))
edit_button.grid(row=2, column=1, ipadx=30, padx=10, pady=10)

renewal_button = Button(S_and_e_frame, text='تمدید', font=("B Nazanin", 10, "bold"), command=lambda: renewal(nid_entry.get(), mj_combo_t.get()))
renewal_button.grid(row=2, column=0, ipadx=30, padx=10, pady=10)

# Accounting
accounting_frame = LabelFrame(root, text="حسابداری", padx=10, pady=10, labelanchor='ne', font=persian_font_b)
accounting_frame.grid(row=2, column=1, pady=10)

acc_month_label = Label(accounting_frame, text=":ماه", justify=RIGHT, font=persian_font, padx=10, pady=10)
acc_month_label.grid(row=0, column=2)

major_label_acc = Label(accounting_frame, text=":رشته", justify=RIGHT, font=persian_font, padx=10, pady=10)
major_label_acc.grid(row=1, column=2)

options = ["فروردین", "اردیبهشت", "خرداد", "تیر", "مرداد", "شهریور", "مهر", "آبان", "آذر", "دی", "بهمن", "اسفند"]
myCombo = ttk.Combobox(accounting_frame, values=options, justify=RIGHT)
myCombo.current(0)
myCombo.bind("<<ComboboxSelected>>")
myCombo.option_add('*TCombobox*Listbox.Justify', 'center')
myCombo.grid(row=0, column=1)

mj_combo_acc = ttk.Combobox(accounting_frame, values=major_options, justify=RIGHT)
mj_combo_acc.current(0)
mj_combo_acc.bind("<<ComboboxSelected>>")
mj_combo_acc.option_add('*TCombobox*Listbox.Justify', 'center')
mj_combo_acc.grid(row=1, column=1)

acc_button = Button(accounting_frame, text="نمایش", font=("B Nazanin", 10, "bold"), command=lambda: show_account(myCombo.get(), mj_combo_acc.get(), current_persian_date.year))
acc_button.grid(row=3, column=1, ipadx=30, padx=10, pady=10)

# show table button
show_table = Button(root, text='نمایش تمامی اعضاء', font=("B Nazanin", 14, "bold"), command=lambda: show_all_table())
show_table.grid(row=2, column=0)


def on_closing():
    backup_database()
    root.destroy()

def backup_database():
    database_path = "gym_db.db"
    backup_dir = "C:/Backup/"
    os.makedirs(backup_dir, exist_ok=True)
    timestamp = JalaliDate.today().strftime("%Y%m%d")
    backup_filename = f"backup_{timestamp}.db"
    backup_path = os.path.join(backup_dir, backup_filename)
    shutil.copyfile(database_path, backup_path)

root.protocol("WM_DELETE_WINDOW", on_closing)


root.mainloop()