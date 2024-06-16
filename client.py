from datetime import datetime, timedelta

class Client:
    def __init__(self, name, start_date, duration, account_number, amount_paid, amount_borrowed, phone_number, e_mail):
        self.name = name
        self.start_date =start_date
        self.duration = duration
        self.account_number = account_number
        self.amount_paid = float(amount_paid)
        self.amount_borrowed = amount_borrowed
        self.phone_number = phone_number
        self.e_mail = e_mail
        self.interest = 7  # interest rate
        self.amount_owed = self.calculate_owed()

    def calculate_owed(self):
        interest_amount = (self.amount_borrowed * (self.interest / 100) * self.duration)
        total_owed = self.amount_borrowed + interest_amount
        return total_owed

    def calculate_payment_split(self):
        long_duration = self.duration * 30
        duration_in_days = timedelta(days=long_duration)
        n_weeks = duration_in_days.days // 7
        payment_split = self.amount_owed / n_weeks
        return round(payment_split, 1), duration_in_days

    def create_reminder_message(self):
        payment_split, duration_in_days = self.calculate_payment_split()
        reminder_date = self.start_date + duration_in_days
        subject = 'Payment Reminder'
        body = f'''Dear {self.name},

Your payment of {payment_split:.2f} is due on {reminder_date.strftime("%d/%m/%Y")}. Please make payment by {reminder_date.strftime("%d/%m/%Y")} to avoid penalty.

Thank you,
Your Finance Team
'''
        message = f'Subject: {subject}\n\n{body}'
        return message, reminder_date

    def update_amounts(self, amount_paid, amount_borrowed):
        self.amount_paid = float(amount_paid)
        self.amount_borrowed = amount_borrowed
        self.amount_owed = self.calculate_owed()