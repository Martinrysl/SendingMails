import smtplib
from datetime import datetime
import pandas as pd
import random


data = pd.read_csv('birthdays.csv')


today = datetime.now()
today_tuple = (today.month, today.day)

birthday_dict = {
    (data_row['month'], data_row['day']): data_row for (index, data_row) in data.iterrows()
}

if today_tuple in birthday_dict:
    file_path = 'letter_1.txt'
    with open(file_path) as letter_file:
        b_person = birthday_dict[today_tuple]
        contents = letter_file.read()
        contents.replace('[NAME]', b_person['name'])


my_email = 'martinrysl@outlook.com'
password = ''
connection = smtplib.SMTP('smtp.office365.com')
connection.starttls()
connection.login(user=my_email, password=password)
connection.sendmail(from_addr=my_email, to_addrs=my_email, msg=f'Happy Birthday:Quote\n\n{contents}')
connection.close()
