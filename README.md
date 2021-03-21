# Калькулятор: для подсчёта денег и калорий

В родительском классе **Calculator** заложена общая функциональность:     

- Хранение записей (о еде или деньгах, по сути - всё числа и даты)
- Хранение дневного лимита (сколько в день можно истратить денег или сколько калорий можно получить)   
- Суммирование записей за конкретные даты   

От класса **Calculator** унаследованы классы **CaloriesCalculator** и **CashCalculator**.  
Для создания записей, создан отдельный класс **Record**. В нём хранятся записи:   

- Число <font color="red">`amount`</font> (денежная сумма или количество килокалорий)  
- Дату создания записи `date` (передаётся в явном виде в конструктор, либо присваивается значение по умолчанию — текущая дата)  
- Комментарий `comment`, поясняющий, на что потрачены деньги или откуда взялись калории.

##  Функциональность для калькулятора денег

1. Сохранять новую запись о расходах методом `add_record()`  
2. Считать, сколько денег потрачено сегодня методом `get_today_stats()`  
3. Определять, сколько ещё денег можно потратить сегодня в рублях, долларах или евро — метод `get_today_cash_remained(currency)`  
4. Считать, сколько денег потрачено за последние 7 дней — метод `get_week_stats()`

##  Функциональность для калькулятора калорий

1. Сохранять новую запись о приёме пищи— метод `add_record()`  
2. Считать, сколько калорий уже съедено сегодня — метод `get_today_stats()`   
3. Определять, сколько ещё калорий можно/нужно получить сегодня — метод `get_calories_remained()`  
4. Считать, сколько калорий получено за последние 7 дней — метод `get_week_stats()`  

## Формат вывода  

Метод `get_calories_remained()` калькулятора калорий должен возвращать ответ
- «Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более N кКал», если лимит limit не достигнут,  
- «Хватит есть!», если лимит достигнут или превышен.  

Метод `get_today_cash_remained(currency)` денежного калькулятора должен принимать на вход код валюты: одну из строк "rub", "usd" или "eur".  
Возвращает он сообщение о состоянии дневного баланса в этой валюте, округляя сумму до двух знаков после запятой (до сотых):  
- «На сегодня осталось N руб/USD/Euro» — в случае, если лимит limit не достигнут,  
- «Денег нет, держись», если лимит достигнут,  
- «Денег нет, держись: твой долг - N руб/USD/Euro», если лимит превышен.  

