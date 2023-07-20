import requests
import openai
import Commons

username = Commons.chat_user
password = Commons.chat_pass

openai.api_key = Commons.chat_key
url = "https://api.openai.com/v1/chat/completions"
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {openai.api_key}"
}

chatgpt_prompt = Commons.all_signs_prompt.format(Commons.date)

completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": chatgpt_prompt}]
)

horoscope = completion.choices[0].message.content

# Save the response as a variable in commons.py
Commons.all_signs_horoscope = horoscope

print("Horoscope saved successfully!", Commons.all_signs_horoscope)