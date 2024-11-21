import streamlit as st
from openai import OpenAI


api_key = ""

client = OpenAI(api_key=api_key)
def ask_gpt(prompt):
    try:
        messages = [
            {"role": "system", "content": "You are the bat assistant for all questions ."},
            {"role": "user", "content": prompt}
        ]

        response = client.chat.completions.create(
            model="gpt-4o-mini",  # Replace with your preferred model
            messages=messages,
            temperature=0
        )

        # Correct way to access the content
        response_message = response.choices[0].message.content
        print(response_message)
        return response_message.strip()
    except Exception as e:
        return f"Сталася помилка: {e}"

# Інтерфейс 
st.title("Чат із GPT-подібним ботом")
st.write("Введіть ваше запитання, і бот відповість вам.")
model="gpt-4o-mini"

user_input = st.text_area("Ваше запитання:", placeholder="Напишіть щось...")

# Кнопка для відправлення запиту
if st.button("Отримати відповідь"):
    if user_input.strip():
        with st.spinner("Бот думає..."):
            response = ask_gpt(user_input)
        st.write(f"**Бот:** {response}")
    else:
        st.warning("Спочатку введіть текст!")



