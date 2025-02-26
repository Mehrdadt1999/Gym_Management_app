from tkinter import *
from tkinter import ttk
import sqlite3
from print import print_excel
from window import war_window
from date_check import is_valid_date
from khayyam import JalaliDate

# query function
def show_all_table():
    # Connect to Database 
    gym = sqlite3.connect('gym_db.db')

    # Create cursor
    c = gym.cursor()

    query = "select acc_type, national_id, phone_number, date, tuition, major, receipt, l_name, f_name, oid from members"
    c.execute(query)
    records = c.fetchall()

    # Commit changes
    gym.commit()

    # Create a new window
    table = Toplevel()
    table.iconbitmap('eagle.ico')

    column_names = ('acc_type', 'national_id', 'phone_number', 'date', 'tuition', 'major', 'receipt', 'l_name', 'f_name', 'row')
    tree = ttk.Treeview(table, columns=column_names, show='headings')

    style = ttk.Style()
    style.configure("Treeview.Heading", font=("B Nazanin", 12, "bold"))
    style.configure("Treeview", font=("B Nazanin", 13, "normal"), rowheight=25)

    tree.heading('acc_type', text='نوع پذیرش', anchor=E)
    tree.heading('national_id', text='کد‌ملی', anchor=E)
    tree.heading('phone_number', text='شماره تلفن', anchor=E)
    tree.heading('date', text='تاریخ', anchor=E)
    tree.heading('tuition', text='شهریه', anchor=E)
    tree.heading('major', text='رشته', anchor=E)
    tree.heading('receipt', text='شماره فیش', anchor=E)    
    tree.heading('l_name', text='نام‌خانوادگی', anchor=E)
    tree.heading('f_name', text='نام', anchor=E)
    tree.heading('row', text='ردیف', anchor=E)

    for column in column_names:
        tree.column(column, width=100)

    # Insert data into the Treeview widget
    for record in records:
        tree.insert('', END, value=record)

    # Set the font and justify for each cell
    for col in column_names:
        tree.column(col, anchor=E)

    for i, item in enumerate(tree.get_children()):
        values = list(tree.item(item, "values"))
        values[-1] = str(i + 1)  # Update "Row Number" (oid) to the new value
        tree.item(item, values=values)

    tree.pack(expand=True, fill=BOTH)

    print_button = Button(table, text="چاپ", font=("B Nazanin", 12, "bold"), command=lambda : print_excel(records, ['نوع پذیرش', 'کدملی' ,'شماره تلفن', 'تاریخ', 'شهریه', 'رشته', 'شماره فیش', '‌نام‌خانوادگی', 'نام', 'ردیف'], 'تمامی اعضاء', 20, 13, 0.5))
    print_button.pack()


def show_Tracking_table(day, month, year, major):
    if is_valid_date(year, month, day):
        try:
            # Connect to Database 
            gym = sqlite3.connect('gym_db.db')

            # Create cursor
            c = gym.cursor()

            if (day == '1' and month == '8'):
                tracking_date = JalaliDate(int(year), int(month) - 1, int(day))
                formated_date1 = tracking_date.strftime('%Y-%m-%d')
                sh_date = JalaliDate(int(year), 6, 31)
                formated_date2 = sh_date.strftime('%Y-%m-%d')
                c.execute("SELECT date, l_name, f_name, oid FROM members WHERE date = ? and major = ? OR date = ? and major = ?", (formated_date1, major.get(), formated_date2, major.get()))
            elif (month == '1'):
                far_date = JalaliDate(int(year)-1, 12, int(day))
                formated_date = far_date.strftime('%Y-%m-%d')
                c.execute("SELECT date, l_name, f_name, oid FROM members WHERE date = ? and major = ?", (formated_date, major.get()))
            else:
                tracking_date = JalaliDate(int(year), int(month) - 1, int(day))
                formated_date = tracking_date.strftime('%Y-%m-%d')
                c.execute("SELECT date, l_name, f_name, oid FROM members WHERE date = ? and major = ?", (formated_date, major.get()))

            records = c.fetchall()

            # Commit changes
            gym.commit()

            # Create a new window
            table = Toplevel()
            table.iconbitmap('eagle.ico')

            column_names = ('date', 'l_name', 'f_name', 'row')
            tree = ttk.Treeview(table, columns=column_names, show='headings')

            style = ttk.Style()
            style.configure("Treeview.Heading", font=("B Nazanin", 12, "bold"))
            style.configure("Treeview", font=("B Nazanin", 13, "normal"), rowheight=25)

            tree.heading('date', text='تاریخ', anchor=E)
            tree.heading('l_name', text='نام‌خانوادگی', anchor=E)
            tree.heading('f_name', text='نام', anchor=E)
            tree.heading('row', text='ردیف', anchor=E)

            # Insert data into the Treeview widget
            for record in records:
                tree.insert('', END, value=record)

            # Set the font and justify for each cell
            for col in column_names:
                tree.column(col, anchor=E)
            
            for i, item in enumerate(tree.get_children()):
                values = list(tree.item(item, "values"))
                values[-1] = str(i + 1)  # Update "Row Number" (oid) to the new value
                tree.item(item, values=values)

            tree.pack(expand=True, fill=BOTH)

            print_button = Button(table, text="چاپ", font=("B Nazanin", 12, "bold"), command=lambda : print_excel(records, ['تاریخ', 'نام‌خانوادگی', 'نام', 'ردیف'], major.get(), 20, 15, 14))
            print_button.pack()

        except ValueError:
            war_window(".لطفاً تاریخ را کامل وارد کنید")

def show_account(month, major, year):
            month_dict = {"فروردین":'01', "اردیبهشت":'02', "خرداد":'03', "تیر":'04', "مرداد":'05', "شهریور":'06', "مهر":'07', "آبان":'08', "آذر":'09', "دی":10, "بهمن":11, "اسفند":12}
            
            # Connect to Database 
            gym = sqlite3.connect('gym_db.db')

            # Create cursor
            c = gym.cursor()

            c.execute('''SELECT 
            t.receipt, t.date, t.tuition, t.acc_type, m.l_name, m.f_name, t.oid  
            FROM 
                tuitions t
            JOIN 
                members m 
            ON 
                t.national_id = m.national_id AND t.major = m.major

            WHERE 
            t.date LIKE ? AND t.major = ?''', ('{}-{}-%'.format(year, month_dict[month]), major))

            records = c.fetchall()


            table = Toplevel()
            table.iconbitmap('eagle.ico')

            column_names = ('receipt', 'date', 'tuition', 'acc_type', 'l_name', 'f_name', 'row')
            tree = ttk.Treeview(table, columns=column_names, show='headings')

            style = ttk.Style()
            style.configure("Treeview.Heading", font=("B Nazanin", 12, "bold"))
            style.configure("Treeview", font=("B Nazanin", 13, "normal"), rowheight=25)

            tree.heading('receipt', text='شماره فیش', anchor=E)
            tree.heading('date', text='تاریخ', anchor=E)
            tree.heading('tuition', text='شهریه', anchor=E)
            tree.heading('acc_type', text='نوع پذیرش', anchor=E)
            tree.heading('l_name', text='نام‌خانوادگی', anchor=E)
            tree.heading('f_name', text='نام', anchor=E)
            tree.heading('row', text='ردیف', anchor=E)

            # Insert data into the Treeview widget
            for record in records:
                tree.insert('', END, value=record)

            # Set the font and justify for each cell
            for col in column_names:
                tree.column(col, anchor=E)

            for i, item in enumerate(tree.get_children()):
                values = list(tree.item(item, "values"))
                values[-1] = str(i + 1)  # Update "Row Number" (oid) to the new value
                tree.item(item, values=values)

            tree.pack(expand=True, fill=BOTH)

            print_button = Button(table, text="چاپ", font=("B Nazanin", 12, "bold"), command=lambda : print_excel(records, ['شماره فیش', 'تاریخ', 'شهریه', 'نوع پذیرش', 'نام‌خانوادگی', 'نام','ردیف'], major, 20, 15, 2))
            print_button.pack()
