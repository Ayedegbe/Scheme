from datetime import datetime, timedelta
from client import Client
from email_sender import send_email
import pandas as pd
clients = {}
df = pd.read_excel('client details.xlsx')

# Populate the clients dictionary
for index, row in df.iterrows():
    client = Client(
        row['name'],
        row['start_date'],
        row['duration'],
        row['account_number'],
        row['amount_paid'],
        row['amount_borrowed'],
        row['phone_number'],
        row['e_mail']
    )
    clients[client.account_number] = client

for account_number, client in clients.items():
    print(f"\nAccount Number: {account_number}")
    payment_split, duration = client.calculate_payment_split()
    owed = client.calculate_owed()
    print(payment_split, duration, owed, client.name)
    if datetime.today == client.start_date + timedelta(days=7):
        owed = client.calculate_owed()
        message = client.create_reminder_message()

        print(owed)
    else:
        print("Code is working as planned soo far.")





























# for account_number, client in clients.items():
#     print(f"\nAccount Number: {account_number}")
#     print(f"Name: {client.name}")
#     print(f"Start Date: {client.start_date.strftime('%d/%m/%Y')}")
#     print(f"Duration: {client.duration} months")
#     print(f"Phone Number: {client.phone_number}")
#     print(f"Email: {client.e_mail}")
#     print(f"Amount Paid: {client.amount_paid}")
#     print(f"Amount Borrowed: {client.amount_borrowed}")
#     print(f"Amount Owed: {client.amount_owed:.2f}")

