import datetime as dt

NOW = dt.datetime.today().strftime("%d.%m.%Y")

class Record:
    def __init__(self, amount, comment, date=NOW):
        self.amount  = amount
        self.date    = dt.datetime.strptime(date, '%d.%m.%Y').date()
        self.comment = comment


class Calculator():

    def __init__(self, limit):
        self.limit   = limit
        self.records = []

    def add_record(self, current_record):
        return self.records.append(current_record)

    def get_today_stats(self, currency=1):
        today = 0
        coefficient = {1:1, 'rub':1, 'usd':63.86, 'eur':69.69 }

        for record in self.records:
            if record.date == dt.datetime.strptime(NOW, '%d.%m.%Y').date():
                today += record.amount
        return today/coefficient[currency]


    def get_remained(self):
        state = self.limit

        for record in self.records:
            state -= record.amount
        return state


    def get_week_stats(self):
        during_week = 0

        for record in self.records:
            if dt.datetime.strptime(NOW, '%d.%m.%Y').date() - record.date <= dt.timedelta(days=7):
                during_week += record.amount
        return during_week


class CaloriesCalculator(Calculator):
    def get_calories_remained(self):
        if self.get_today_stats() < self.limit:
            return "Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более " + str(int(self.limit - self.get_today_stats())) + " кКал"
        else:
            return "Хватит есть!"

class CashCalculator(Calculator):
    RUB_RATE = 1
    USD_RATE = 63.86
    EURO_RATE = 69.69
    #currency_dictionary = {"rub":["руб","RUB"], "usd":["USD","USD"], "EURO":["Euro", "EURO"]}

    def get_today_cash_remained(self, currency):
        RUB_RATE =  1
        USD_RATE =  60
        EURO_RATE = 70
        currency_dictionary = {"rub":["руб","RUB"], "usd":["USD","USD"], "eur":["Euro", "EURO"]}

        Exchange_Rate = currency_dictionary[currency][1].upper() + "_RATE"
        balance = self.get_today_stats()
        currency_name = currency_dictionary[currency][0]

        if balance < self.limit:
            return "На сегодня осталось " + str(round((self.limit - balance)/eval(Exchange_Rate), 2)) + ' ' +  str(currency_name)

        elif balance == self.limit:
            return "Денег нет, держись"
        else:
            return "Денег нет, держись: твой долг - " + str(abs(round((self.limit - balance)/eval(Exchange_Rate),2))) + " " + str(currency_name)


