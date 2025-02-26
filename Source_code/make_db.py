import sqlite3

#Create Database 
gym = sqlite3.connect('gym_db.db')

# Create cursor
c = gym.cursor()

create_members = """
    CREATE TABLE members(   national_id text NOT NULL,
                            date numeric NOT NULL,
                            tuition integer NOT NULL,
                            phone_number text NOT NULL,
                            l_name text NOT NULL,
                            f_name text NOT NULL,
                            major text NOT NULL,
                            acc_type text NOT NULL,
                            receipt text NOT NULL,
                            PRIMARY KEY(national_id, major));
"""

# Create Table
c.execute(create_members)

create_tuitions = """
    CREATE TABLE tuitions(  receipt text NOT NULL,
                            date NUMERIC NOT NULL,
                            tuition INTEGER NOT NULL,
                            major text NOT NULL,
                            national_id text NOT NULL,
                            acc_type text NOT NULL,
                            FOREIGN KEY (national_id) REFERENCES members(national_id),
                            FOREIGN KEY (major) REFERENCES members(major),
                            PRIMARY KEY(receipt, major));
"""

c.execute(create_tuitions)

# Commit chages
gym.commit()

#close connection
gym.close()
