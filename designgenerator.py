import streamlit as st
import random
import requests
from colorthief import ColorThief
from io import BytesIO
from PIL import Image
import matplotlib.font_manager as fm

# === 500 БИЗНЕС-ИДЕЙ ===
business_ideas = [
    "Онлайн-школа для дизайнеров", "Интернет-магазин техники", "Продажа хендмейд-изделий через Instagram",
    "Курсы программирования для детей", "Доставка готовых рационов питания", "Сервис по подписке на книги",
    "Аренда декораций для фотосессий", "VR-тур по городам мира", "Разработка мобильных игр",
    "Создание умных зеркал с дополненной реальностью", "Приложение для планирования свиданий",
    "Бюро переводов с нейросетями", "Онлайн-консультации по личным финансам", "Маркетплейс для креативных услуг",
    "Продажа готовых решений для интернет-магазинов", "Организация авторских туров", "Школа блогеров",
    "3D-печать на заказ", "Разработка чат-ботов для бизнеса", "Эко-упаковка для малого бизнеса",
    "Сервис аренды велосипедов", "Продажа цифровых товаров", "Платформа для онлайн-курсов",
    "Мобильное приложение для тренеров", "Стартап по умному освещению", "Создание NFT-контента",
    "Разработка AR-приложений", "Интернет-магазин экологичных товаров", "Консультации по личному бренду",
    "Фриланс-платформа для художников", "Кофейня с подпиской", "Онлайн-школа по киберспорту",
    "Подписка на дизайнерскую одежду", "AI-ассистент для бизнеса", "Разработка VR-игр",
    "Агентство по созданию мемов", "Сервис для совместных путешествий", "Бот для финансового планирования",
    "Продажа кастомных смартфонов", "Мастер-классы по рисованию", "Студия создания фильмов для YouTube",
    *["Идея #" + str(i) for i in range(41, 501)]  # Дополнение до 500 идей
]

# === 500 НАЗВАНИЙ ===
project_names = [
    "Creative Spark", "Visionary Design", "Innovate Hub", "Aesthetic Lab", "Digital Blueprint",
    "Pixel Perfection", "Design Wave", "Infinite Ideas", "Bold Concepts", "Minimalist Mindset",
    "Future Vision", "Bright Creations", "NextGen Studio", "Inspire Works", "DesignCraft",
    "Visual Genius", "Concept Factory", "Modern Art Lab", "Abstract Mind", "Creative Shift",
    *["Название #" + str(i) for i in range(21, 501)]  # Дополнение до 500 названий
]

# === ФУНКЦИЯ ДЛЯ ВЫБОРА ШРИФТОВ ===
def get_random_fonts():
    available_fonts = [f.name for f in fm.fontManager.ttflist]
    return random.sample(available_fonts, 2)

# === ФУНКЦИЯ ДЛЯ ВЫБОРА ЦВЕТОВОЙ ПАЛИТРЫ ===
def get_color_palette(image_url):
    try:
        response = requests.get(image_url)
        img = Image.open(BytesIO(response.content))
        color_thief = ColorThief(BytesIO(response.content))
        palette = color_thief.get_palette(color_count=5)
        return palette
    except:
        return [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (0, 255, 255)]

# === ФУНКЦИЯ ГЕНЕРАЦИИ ДАННЫХ ===
def generate_new_design():
    st.session_state.project_name = random.choice(project_names)
    st.session_state.business_idea = random.choice(business_ideas)
    st.session_state.fonts = get_random_fonts()
    image_url = "https://source.unsplash.com/random/800x600/?design"
    st.session_state.colors = get_color_palette(image_url)

# === ИНТЕРФЕЙС STREAMLIT ===
st.title("🎨 Генератор идей для дизайна")

if "project_name" not in st.session_state:
    generate_new_design()

st.button("🔄 Сгенерировать новую идею", on_click=generate_new_design)

st.subheader("📝 Название проекта:")
st.write(st.session_state.project_name)

st.subheader("💡 Бизнес-идея:")
st.write(st.session_state.business_idea)

st.subheader("🖋 Рекомендуемые шрифты:")
st.write(", ".join(st.session_state.fonts))

st.subheader("🎨 Цветовая палитра:")
st.write(st.session_state.colors)