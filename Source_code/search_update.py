from tkinter import *
from tkinter import ttk
import sqlite3
from khayyam import JalaliDate
from format_entry import format_entry
from window import war_window, show_info_message
from date_check import is_valid_date


persian_font = ("B Nazanin", 13, "normal")
persian_font_b = ("B Nazanin", 12, "bold")

# Current date
current_persian_date = JalaliDate.today()

def search(nid, mj):
            #connect to Database 
            gym = sqlite3.connect('gym_db.db')

            # Create cursor
            c = gym.cursor()

            c.execute("SELECT * FROM members WHERE national_id = ? and major = ?", (nid, mj))
            record = c.fetchall()
                
            if record != []:
                edit = Toplevel()
                edit.iconbitmap('eagle.ico')

                # Labels in edit frame 
                f_name_label = Label(edit, text=":نام", justify=RIGHT, font=persian_font, pady=10, padx=10)
                f_name_label.grid(row=0, column=5)

                l_name_label = Label(edit, text=":نام‌خانوادگی", justify=RIGHT, font=persian_font, pady=10, padx=10)
                l_name_label.grid(row=1, column=5)

                phone_number_label = Label(edit, text=":شماره تماس", justify=RIGHT, font=persian_font, pady=10, padx=10)
                phone_number_label.grid(row=0, column=3)

                tuition_label = Label(edit, text=": شهریه _ تومان", justify=RIGHT, font=persian_font, pady=10, padx=10)
                tuition_label.grid(row=1, column=3)

                date_label = Label(edit, text=":تاریخ", justify=RIGHT, font=persian_font, pady=10, padx=10)
                date_label.grid(row=0, column=1)

                national_id_label = Label(edit, text=":کد ملی", justify=RIGHT, font=persian_font, pady=10, padx=10)
                national_id_label.grid(row=1, column=1)

                accType_label = Label(edit, text=":نوع پذیرش", justify=RIGHT, font=persian_font, pady=10, padx=10)
                accType_label.grid(row=2, column=5)

                receipt_label = Label(edit, text=":شماره فیش", justify=RIGHT, font=persian_font, pady=10, padx=10)
                receipt_label.grid(row=2, column=3)

                major_label = Label(edit, text=":رشته", justify=RIGHT, font=persian_font, pady=10, padx=10)
                major_label.grid(row=2, column=1)

                # Entrise in edit frame
                f_name = Entry(edit, justify=RIGHT)
                f_name.insert(0, record[0][5])
                f_name.bind("<FocusIn>", lambda event: f_name.delete(0, END))
                f_name.grid(row=0, column=4)

                l_name = Entry(edit, justify=RIGHT)
                l_name.insert(0, record[0][4])
                l_name.bind("<FocusIn>", lambda event: l_name.delete(0, END))
                l_name.grid(row=1, column=4)

                accType_options = ["نیرو هوایی", "سایر نیروها", "آزاد"]
                accType_Combo = ttk.Combobox(edit, values=accType_options, justify=RIGHT, width=17)
                accType_Combo.current(accType_options.index(record[0][7]))
                accType_Combo.bind("<<ComboboxSelected>>")
                accType_Combo.option_add('*TCombobox*Listbox.Justify', 'center')
                accType_Combo.grid(row=2, column=4)

                phone_number = Entry(edit, justify=RIGHT)
                phone_number.insert(0, record[0][3])
                phone_number.bind("<FocusIn>", lambda event: phone_number.delete(0, END))
                phone_number.grid(row=0, column=2)

                tuition = Entry(edit, justify=RIGHT)
                tuition.insert(0, record[0][2])
                tuition.bind("<KeyRelease>", lambda event: format_entry(tuition))
                tuition.grid(row=1, column=2)
                tuition.bind("<FocusIn>", lambda event: tuition.delete(0, END))

                receipt = Label(edit, text = record[0][8], justify=RIGHT, font=persian_font_b)
                receipt.grid(row=2, column=2)

                national_id = Label(edit, text=nid, justify=RIGHT, font=persian_font_b)
                national_id.grid(row=1, column=0)

                date_frame = LabelFrame(edit)
                date_frame.grid(row=0, column=0)

                day = Entry(date_frame, width=11, justify=RIGHT)
                day.grid(row=0, column=3)
                day.insert(0, record[0][1].split('-')[-1])
                day.bind("<FocusIn>", lambda event: day.delete(0, END))

                month = Entry(date_frame, width=11, justify=RIGHT)
                month.grid(row=0, column=1)
                month.insert(0, record[0][1].split('-')[1])
                month.bind("<FocusIn>", lambda event: month.delete(0, END))
                Label(date_frame, text='/', justify=RIGHT).grid(row=0, column=2)

                year_text = str(current_persian_date.year)+'/'
                year = Label(date_frame, text=year_text, justify=RIGHT)
                year.grid(row=0, column=0)

                major = Label(edit, text=mj, justify=RIGHT, font=persian_font_b)
                major.grid(row=2, column=0)

                update = Button(edit, text="ویرایش",  font=("B Nazanin", 10, "bold"), command= lambda: update_func(day, tuition, month, nid, f_name, l_name, mj, accType_Combo, record[0][8], phone_number, edit))
                update.grid(row=3,column=2, columnspan=2, ipadx=75, padx=10, pady=10)
            else:
                    war_window(".فرد مورد نظر یافت نشد")

def renewal(nid, mj):
       #connect to Database 
            gym = sqlite3.connect('gym_db.db')

            # Create cursor
            c = gym.cursor()

            c.execute("SELECT * FROM members WHERE national_id = ? and major = ?", (nid, mj))
            record = c.fetchall()
                
            if record != []:
                edit = Toplevel()
                edit.iconbitmap('eagle.ico')

                # Labels in edit frame 
                f_name_label = Label(edit, text=":نام", justify=RIGHT, font=persian_font, pady=10, padx=10)
                f_name_label.grid(row=0, column=5)

                l_name_label = Label(edit, text=":نام‌خانوادگی", justify=RIGHT, font=persian_font, pady=10, padx=10)
                l_name_label.grid(row=1, column=5)

                phone_number_label = Label(edit, text=":شماره تماس", justify=RIGHT, font=persian_font, pady=10, padx=10)
                phone_number_label.grid(row=0, column=3)

                tuition_label = Label(edit, text=": شهریه _ تومان", justify=RIGHT, font=persian_font, pady=10, padx=10)
                tuition_label.grid(row=1, column=3)

                date_label = Label(edit, text=":تاریخ", justify=RIGHT, font=persian_font, pady=10, padx=10)
                date_label.grid(row=0, column=1)

                national_id_label = Label(edit, text=":کد ملی", justify=RIGHT, font=persian_font, pady=10, padx=10)
                national_id_label.grid(row=1, column=1)

                accType_label = Label(edit, text=":نوع پذیرش", justify=RIGHT, font=persian_font, pady=10, padx=10)
                accType_label.grid(row=2, column=5)

                receipt_label = Label(edit, text=":شماره فیش", justify=RIGHT, font=persian_font, pady=10, padx=10)
                receipt_label.grid(row=2, column=3)

                major_label = Label(edit, text=":رشته", justify=RIGHT, font=persian_font, pady=10, padx=10)
                major_label.grid(row=2, column=1)

                national_id = Label(edit, text=nid, justify=RIGHT, font=persian_font_b)
                national_id.grid(row=1, column=0)

                f_name = Label(edit, text=record[0][5], justify=RIGHT, font=persian_font_b)
                f_name.grid(row=0, column=4)

                l_name = Label(edit, text=record[0][4], justify=RIGHT, font=persian_font_b)
                l_name.grid(row=1, column=4)

                accType = Label(edit, text=record[0][7], justify=RIGHT, font=persian_font_b)
                accType.grid(row=2, column=4)

                phone_number = Label(edit, text=record[0][3], justify=RIGHT, font=persian_font_b)
                phone_number.grid(row=0, column=2)

                major = Label(edit, text=record[0][6], justify=RIGHT, font=persian_font_b)
                major.grid(row=2, column=0)

                # Entries in edit frame 
                tuition = Entry(edit, justify=RIGHT, width=13)
                tuition.insert(0, record[0][2])
                tuition.bind("<KeyRelease>", lambda event: format_entry(tuition))
                tuition.grid(row=1, column=2)
                tuition.bind("<FocusIn>", lambda event: tuition.delete(0, END))

                receipt = Entry(edit, justify=RIGHT, width=13)
                receipt.insert(0, record[0][8])
                receipt.grid(row=2, column=2)
                receipt.bind("<FocusIn>", lambda event: receipt.delete(0, END))

                date_frame = LabelFrame(edit)
                date_frame.grid(row=0, column=0)

                day = Entry(date_frame, width=11, justify=RIGHT)
                day.grid(row=0, column=2)
                day.insert(0, record[0][1].split('-')[-1])
                day.bind("<FocusIn>", lambda event: day.delete(0, END))

                month_text = str(current_persian_date.month)+'/'
                month = Label(date_frame, text=month_text, justify=RIGHT)
                month.grid(row=0, column=1)

                year_text = str(current_persian_date.year)+'/'
                year = Label(date_frame, text=year_text, justify=RIGHT)
                year.grid(row=0, column=0)

                renewal = Button(edit, text="تمدید",  font=("B Nazanin", 10, "bold"), command= lambda: renewal_func(day, tuition, nid, mj, record[0][7], receipt, edit))
                renewal.grid(row=3,column=2, columnspan=2, ipadx=75, padx=10, pady=10)
            else:
                    war_window(".فرد مورد نظر یافت نشد")

def renewal_func(d, t, nnid, mj, acc, r, edit):
        try:
            if is_valid_date(current_persian_date.year, current_persian_date.month, d.get()):
                    int(t.get().replace(",", ""))
                    date = JalaliDate(int(current_persian_date.year), int(current_persian_date.month), int(d.get())).strftime('%Y-%m-%d')
                    #connect to Database 
                    gym = sqlite3.connect('gym_db.db')

                    # Create cursor
                    c = gym.cursor()
                    
                    c.execute("INSERT INTO tuitions VALUES(:receipt, :date, :tuition, :major, :national_id, :acc_type)",
                        {
                            'receipt': r.get(),
                            'tuition': t.get(),
                            'date': date,
                            'major': mj,
                            'national_id': nnid,
                            'acc_type': acc,
                        }
                        )
                    
                    c.execute("""UPDATE members
                        SET date = ?, tuition = ?, receipt = ?
                        WHERE national_id = ? and major = ?""", (date, t.get(), r.get(), nnid, mj))
                    # # Commit chages
                    gym.commit()

                    show_info_message("تاییدیه", ".تمدید انجام شد")
                    edit.destroy()

        except ValueError:
               war_window(".لطفاً عدد وارد کنید")
        except sqlite3.IntegrityError:
              war_window(".شماره فیش تکراری است")

def update_func(d, t, m, nnid, first, last, mj, acctype, receip, phone, edit):
    try:
        # Validate date
        if is_valid_date(current_persian_date.year, m.get(), d.get()):
            # Format the date to the correct format
            date = JalaliDate(int(current_persian_date.year), int(m.get()), int(d.get())).strftime('%Y-%m-%d')

            # Connect to Database using context manager
            with sqlite3.connect('gym_db.db') as gym:
                c = gym.cursor()
                
                # Update the members table
                c.execute("""
                    UPDATE members
                    SET date = ?, tuition = ?, f_name = ?, l_name = ?, acc_type = ?, receipt = ?, phone_number = ?
                    WHERE national_id = ? and major = ?
                """, (date, t.get(), first.get(), last.get(), acctype.get(), receip, phone.get(), nnid, mj))
                
                # Update the tuitions table
                c.execute("""
                    UPDATE tuitions
                    SET date = ?, tuition = ?, acc_type = ?
                    WHERE receipt = ?
                """, (date, t.get(), acctype.get(), receip))
                # # Commit chages
                gym.commit()
                
            # Show success message
            show_info_message("تاییدیه", ".اطلاعات ویرایش شد")

            edit.destroy()

    except ValueError:
        # Handle invalid numeric value error
        war_window(".لطفاً عدد وارد کنید")
