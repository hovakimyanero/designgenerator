import streamlit as st
import random
import requests

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

# Функция для генерации случайного цвета
def get_random_color():
    return "#{:06x}".format(random.randint(0, 0xFFFFFF))

# Генерация случайной цветовой палитры
def generate_palette():
    return [get_random_color() for _ in range(5)]

# Функция для загрузки палитры с Coolors API (fallback на локальную генерацию)
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

# Создаём переменные в сессии Streamlit
if "idea" not in st.session_state:
    st.session_state.idea = random.choice(business_ideas)
if "name" not in st.session_state:
    st.session_state.name = generate_name()
if "palette" not in st.session_state:
    st.session_state.palette = get_color_palette()
if "font" not in st.session_state:
    st.session_state.font = random.choice(["Roboto", "Montserrat", "Lato", "Open Sans", "Poppins"])

# Функция обновления данных
def generate_new_idea():
    st.session_state.idea = random.choice(business_ideas)
    st.session_state.name = generate_name()
    st.session_state.palette = get_color_palette()
    st.session_state.font = random.choice(["Roboto", "Montserrat", "Lato", "Open Sans", "Poppins"])

# Кнопка для генерации новой идеи
st.button("Сгенерировать новую идею", on_click=generate_new_idea)

st.subheader("📌 Идея проекта:")
st.write(st.session_state.idea)

st.subheader("🏷 Название:")
st.write(st.session_state.name)

st.subheader("🎨 Цветовая палитра:")
cols = st.columns(len(st.session_state.palette))
for i, color in enumerate(st.session_state.palette):
    cols[i].markdown(f'''
        <div class="hover-box" style="background-color: {color};"></div>
    ''', unsafe_allow_html=True)
    cols[i].write(color)

st.subheader("🔠 Шрифт:")
st.write(st.session_state.font)
st.markdown(f'<p style="font-family: {st.session_state.font}; font-size: 24px;">Пример текста этим шрифтом</p>', unsafe_allow_html=True)
