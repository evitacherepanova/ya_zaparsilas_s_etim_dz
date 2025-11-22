# Парсер расписания электричек

Простая программа для извлечения расписания электричек из HTML-страницы.

## Что делает программа

- Читает сохраненную HTML-страницу с расписанием
- Извлекает информацию о рейсах: время, маршрут и дни движения
- Позволяет фильтровать рейсы по будням или ежедневным
- Выводит результаты в консоль и может сохранить в JSON

## Как запускать
# Сначала нужно установить библиотеку, если не установлена
pip install beautifulsoup4
# Прoверьте, что Вы работаете не в PowerShell, а в CMD
# Итак, сам запуск:
- git clone https://github.com/evitacherepanova/ya_zaparsilas_s_etim_dz.git
- cd electric_schedule_parser
- python -m venv venv
- venv\Scripts\activate      # Windows
- source venv/bin/activate   # macOS/Linux
- python parse_sputnik.py
