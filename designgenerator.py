import streamlit as st
import random
import requests
from randomcolor import RandomColor
import colorsys

# Расширенный список бизнес-идей
business_ideas = [
    "Онлайн-школа для дизайнеров",
    "Сервис по доставке еды для веганов",
    "Приложение для планирования путешествий",
    "Маркетплейс цифровых товаров",
    "Платформа для обучения программированию",
    "Фитнес-приложение с AI-тренером",
    "VR-галерея цифрового искусства",
    "Сайт для поиска удалённой работы",
    "Мобильное приложение для медитации",
    "Онлайн-сервис для организации мероприятий",
    "Стартап по продаже кастомных футболок",
    "Сервис по подбору интерьера для дома",
    "Приложение для личных финансов",
    "Клуб подписки на редкие книги",
    "Генератор NFT-коллекций",
    "Интерактивный учебник по астрономии",
    "Сайт для знакомств по интересам",
    "Приложение для изучения языков",
    "Экосистема для фрилансеров",
    "Генератор идей для контента",
    "AI-консультант по моде",
    "Курс по нейросетям для дизайнеров",
    "Приложение для изучения истории",
    "Сайт для изучения карт Таро",
    "Облачный сервис для дизайнеров"
]

# Функция для генерации гармоничных цветов
def generate_harmonious_palette(base_color):
    base_hue = colorsys.rgb_to_hsv(*base_color)[0]  # Получаем оттенок (hue) из RGB
    harmonious_palette = []

    # Генерируем дополнительные цвета на основе теории гармонии
    for i in range(5):
        hue = (base_hue + i * 0.1) % 1  # Генерация гармоничных оттенков (сдвиг hue)
        rgb = colorsys.hsv_to_rgb(hue, 0.8, 0.8)  # Преобразуем обратно в RGB
        harmonious_palette.append(rgb)
    return harmonious_palette

# Генерация случайного цвета и гармоничных цветов
def generate_palette():
    rand_color = RandomColor()
    base_color = rand_color.generate(count=1)[0]
    base_rgb = [int(base_color[1:3], 16) / 255, int(base_color[3:5], 16) / 255, int(base_color[5:7], 16) / 255]
    return generate_harmonious_palette(base_rgb)

# Функция для загрузки палитры с Coolors API
def get_color_palette():
    try:
        response = requests.get("https://www.colr.org/json/colors/random/5")
        data = response.json()
        colors = [f"#{c['hex']}" for c in data["colors"] if c["hex"]]
        return colors if colors else generate_palette()
    except:
        return generate_palette()

# Генерация случайного названия
def generate_name():
    prefixes = ["Neo", "Tech", "Smart", "Vision", "Future", "Next", "Cloud", "AI", "Design", "Creative"]
    suffixes = ["Lab", "Hub", "Soft", "Studio", "Pro", "AI", "Space", "Works", "Forge", "Base"]
    return f"{random.choice(prefixes)} {random.choice(suffixes)}"

# Интерфейс Streamlit
st.title("🎨 Генератор идей для дизайна")

# Стилизация кнопки с изменённой обводкой и цветом текста
st.markdown("""
    <style>
        .stButton>button {
            border: 2px solid #ADD8E6;
            color: #ADD8E6;
            background-color: transparent;
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            transition: all 0.3s ease;
        }
        .stButton>button:hover {
            border-color: #87CEEB;
            color: #87CEEB;
        }
        .stButton>button:focus {
            border-color: #ADD8E6;
            color: #ADD8E6;
        }
        
        .hover-box {
            width: 180px;
            height: 180px;
            border-radius: 18px;
            transition: transform 0.3s ease, box-shadow 0.3s ease, background 0.3s ease;
            box-shadow: 8px 8px 12px rgba(0, 0, 0, 0.15), -8px -8px 12px rgba(255, 255, 255, 0.7);
        }
        
        .hover-box:hover {
            transform: translateY(-20px);
            box-shadow: 8px 8px 12px rgba(0, 0, 0, 0.3), -8px -8px 12px rgba(255, 255, 255, 0.3);
        }
    </style>
""", unsafe_allow_html=True)

# Создаем функцию для обработки нажатия кнопки
if st.button("Сгенерировать новую идею"):
    idea = random.choice(business_ideas)
    name = generate_name()
    palette = get_color_palette()
    font = random.choice(["Roboto", "Montserrat", "Lato", "Open Sans", "Poppins"])

    # Отображение результата
    st.subheader("📌 Идея проекта:")
    st.write(f"{idea}")

    st.subheader("🏷 Название:")
    st.write(f"{name}")

    st.subheader("🎨 Цветовая палитра:")
    cols = st.columns(len(palette))
    for i, color in enumerate(palette):
        hex_color = '#{:02x}{:02x}{:02x}'.format(int(color[0]*255), int(color[1]*255), int(color[2]*255))
        cols[i].markdown(f'''
            <div class="hover-box" style="background-color: {hex_color};"></div>
        ''', unsafe_allow_html=True)
        cols[i].write(hex_color)

    st.subheader("🔠 Шрифт:")
    st.write(f"{font}")
    st.markdown(f'<p style="font-family: {font}; font-size: 24px;">Пример текста этим шрифтом</p>', unsafe_allow_html=True)