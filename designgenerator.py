import streamlit as st
import random
import requests

# Расширенный список бизнес-идей (500 идей)
business_ideas = [f"Бизнес-идея #{i}" for i in range(1, 501)]

# Расширенный список названий (500 названий)
name_prefixes = ["Neo", "Tech", "Smart", "Vision", "Future", "Next", "Cloud", "AI", "Design", "Creative",
                 "Digital", "Hyper", "Ultra", "Pro", "Mega", "Inno", "Giga", "Cyber", "Quantum", "Nano"]
name_suffixes = ["Lab", "Hub", "Soft", "Studio", "Pro", "AI", "Space", "Works", "Forge", "Base",
                 "Solutions", "Systems", "Apps", "Tech", "Concepts", "Group", "Industries", "Network", "Platform", "Dynamics"]

# Генерация случайного названия
def generate_name():
    return f"{random.choice(name_prefixes)} {random.choice(name_suffixes)}"

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

# Список шрифтов
fonts = ["Roboto", "Montserrat", "Lato", "Open Sans", "Poppins", "Raleway", "Nunito", "Merriweather", 
         "Playfair Display", "Oswald", "Bebas Neue", "Source Sans Pro", "Ubuntu", "Fira Sans", "Caveat"]

# Интерфейс Streamlit
st.title("🎨 Генератор идей для дизайна")

# Стилизация кнопки
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
if "fonts" not in st.session_state:
    st.session_state.fonts = random.sample(fonts, 2)  # Выбираем два случайных шрифта

# Функция обновления данных
def generate_new_idea():
    st.session_state.idea = random.choice(business_ideas)
    st.session_state.name = generate_name()
    st.session_state.palette = get_color_palette()
    st.session_state.fonts = random.sample(fonts, 2)

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

st.subheader("🔠 Шрифты:")
for font in st.session_state.fonts:
    st.write(f"• {font}")
    st.markdown(f'<p style="font-family: {font}; font-size: 24px;">Пример текста этим шрифтом</p>', unsafe_allow_html=True)
