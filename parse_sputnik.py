
import json
from bs4 import BeautifulSoup

# Читаем HTML файл
with open('page.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Создаем объект для разбора HTML
soup = BeautifulSoup(html_content, 'html.parser')

# Будем хранить все поезда здесь
all_trains = []

# Ищем все строки в таблице с расписанием
rows = soup.find_all('tr') # Поиск всех строк таблицы

for row in rows:
    # Пытаемся найти время отправления
    time_cells = row.find_all('td')
    if len(time_cells) > 1: # если в строке больше 1 ячейки
        time_span = time_cells[1].find('span') # та проверка отсекает пустые строки или строки-заголовки
        if time_span:
            time_text = time_span.text.strip()
            
            # Пытаемся найти маршрут
            route_link = row.find('a')
            if route_link:
                route_text = route_link.text.strip() # метод строки, удаляет пробелы, табуляции и переносы строк в начале и конце строки
                
                # Пытаемся найти тип поезда и дни
                train_type = "Электричка"  # по умолчанию
                days_type = "Ежедневно"    # по умолчанию
                
                # Ищем тип поезда (Спутник, Иволга и т.д.)
                type_spans = row.find_all('span')
                for span in type_spans:
                    text = span.text.strip()
                    if text in ['Спутник', 'Иволга', 'Ласточка', 'Электричка']:
                        train_type = text
                    if text in ['Ежедневно', 'Будни', 'Выходные']:
                        days_type = text
                
                # Добавляем поезд в список
                train_info = {
                    'time': time_text,
                    'route': route_text,
                    'type': train_type,
                    'days': days_type
                }
                all_trains.append(train_info)

# Фильтруем только Спутники
sputnik_trains = []
for train in all_trains:
    if train['type'] == 'Спутник':
        sputnik_trains.append(train)

# Выводим результаты
print("Расписание поездов типа 'Спутник':")
print("=" * 50)

for i, train in enumerate(sputnik_trains, 1):
    print(f"{i}. Время: {train['time']}")
    print(f"   Маршрут: {train['route']}")
    print(f"   Дни: {train['days']}")
    print("-" * 30)

# Сохраняем в JSON
with open('sputnik_trains.json', 'w', encoding='utf-8') as f:
    json.dump(sputnik_trains, f, ensure_ascii=False, indent=2)

print(f"\nНайдено поездов 'Спутник': {len(sputnik_trains)}")
print("Данные сохранены в файл: sputnik_trains.json")
