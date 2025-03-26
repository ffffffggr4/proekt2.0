import streamlit as st
from datetime import datetime, timedelta
from PIL import Image
import os

# Создаем список праздников
holidays = {
    "Новогодние праздники": datetime(2023, 12, 31),
    "Рождество": datetime(2024, 1, 7),
    "Международный женский день": datetime(2024, 3, 8),
}

# Функция для отображения календаря с праздниками
def display_calendar():
    st.header("Календарь праздников")
    current_date = datetime.now()
    
    for holiday, date in holidays.items():
        if date.date() >= current_date.date():
            st.markdown(f"**{holiday} :** {date.strftime('%d-%m-%Y')}")
            if st.button('☀️', key=str(date)):
                st.success(f"Вы нажали на иконку праздника: {holiday}")

# Функция для добавления собственных праздников
def add_holiday():
    st.header("Добавить свой праздник")
    holiday_name = st.text_input("Введите название праздника")
    holiday_date = st.date_input("Выберите дату праздника", value=datetime.now())
    
    if st.button("Добавить"):
        if holiday_name and holiday_date:
            holidays[holiday_name] = holiday_date
            st.success(f"{holiday_name} добавлен на {holiday_date.strftime('%d-%m-%Y')}")
        else:
            st.error("Пожалуйста, заполните все поля")

# Функция для создания расписания с уведомлениями
def schedule_events():
    st.header("Создать расписание мероприятий")
    event_name = st.text_input("Введите название мероприятия")
    event_date = st.date_input("Выберите дату мероприятия", value=datetime.now())
    notify_time = st.time_input("Выберите время уведомления", value=datetime.now().time())
    
    if st.button("Добавить мероприятие"):
        if event_name:
            st.success(f"{event_name} добавлено на {event_date} в {notify_time}. Уведомление будет отправлено.")
            # Здесь можно добавить логику для отправки уведомлений (например, с помощью библиотеки `playsound` или `pygame`)
        else:
            st.error("Пожалуйста, заполните все поля")

# Основная часть приложения
st.title("Календарь и планировщик мероприятий")
display_calendar()
add_holiday()
schedule_events()
