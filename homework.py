import datetime as dt

NOW = dt.datetime.today().strftime("%d.%m.%Y")

class Record:
    def __init__(self, amount, comment, date=NOW):
        self.amount = amount
        self.date = dt.datetime.strptime(date, '%d.%m.%Y').date()
        self.comment = comment


class Calculator():

    def __init__(self, limit):
        self.limit   = limit
        self.records = []

    def add_record(self, current_record):
        return self.records.append(current_record)

    def get_today_stats(self):
        return sum([record.amount for record in self.records if record.date == dt.datetime.strptime(NOW, '%d.%m.%Y').date()])


    def get_remained(self):
        return self.limit - sum([record.amount for record in self.records])

    def get_week_stats(self):
        return sum([record.amount for record in self.records if dt.datetime.strptime(NOW, '%d.%m.%Y').date() - record.date <= dt.timedelta(days=7)])

class CaloriesCalculator(Calculator):
    def get_calories_remained(self):
        if self.get_today_stats() < self.limit:
            return f"Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {self.limit - self.get_today_stats()} кКал"
        return "Хватит есть!"

class CashCalculator(Calculator):
    RUB_RATE = 1
    USD_RATE = 60.0 #63.86 Здесь почему-то только такой курс подходит, если брать реальный курс с yandex, то тесты ругаются что отличаются значения на сотые, а если взять курс 60 и 70 как в тестах то все тесты прохядятся
    EURO_RATE = 70.0 #69.69
    # Почему вместо списков лучше таплы использовать?
    currency = {"rub":("руб", RUB_RATE), "usd":("USD", USD_RATE), "eur":("Euro", EURO_RATE)}

    def get_today_cash_remained(self, currency):

        # не нашел точно как поправить название переменной exchange_rate, но вроде в PEP8 так пишутся названия: (я поправил)
        currency_name, exchange_rate = self.currency[currency]
        balance = self.get_today_stats()

        if balance < self.limit:
            return f"На сегодня осталось {round((self.limit - balance)/exchange_rate, 2)} {currency_name}"

        elif balance == self.limit:
            return "Денег нет, держись"

        # Почему eval плохо было использовать?
        return f"Денег нет, держись: твой долг - {abs(round((self.limit - balance)/exchange_rate,2))} {currency_name}"

