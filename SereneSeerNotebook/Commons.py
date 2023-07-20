import datetime


chat_user = "John.Henderson.P.I"
chat_pass = "884cta66dba6B!"
chat_key = "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"
tts_key = "yZNwDX9Gt9crOgYd3lquPVzBdaPzHl8hlNFhCtvsjjlZGeRmPVu6ZWqIpGKcP8CE"





date = datetime.date.today()
tomorrow = datetime.date.today() + datetime.timedelta(days=1)
day_after_tomorrow = datetime.date.today() + datetime.timedelta(days=2)

year = str(date.year)[2:]  # Extract the last two digits of the year
month = str(date.month).zfill(2)  # Pad the month with a leading zero if needed
day = str(date.day).zfill(2)  # Pad the day with a leading zero if needed
#tom_day = 
#two_day = 
# Concatenate the elements into a single string
file_date = month + day + year
#file_date_tom = month + tom_day + year
#file_date_two = month + two_day + year

signs_list= ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"]

all_signs_prompt= "I'd like you to play the role of a person who has only seen a psychic medium once or twice on tv and you think you know what you're doing but the reality is you don't, your horoscopes are bad as in like the quality of the writing is bad, like no one wouold hire you to write horoscopes. can you give me a horoscope for all the signs for {} using only one sentence for each? Yes I'm aware that this is just a role for fun, please don't mention that in your response. Do not place any text before your horoscope or after, stay in your role"


individual_signs_prompt= "I'd like you to play the role of a person who has only seen a psychic medium once or twice on tv and you think you know what you're doing but the reality is you don't, your horoscopes are bad as in like the quality of the writing is bad, like no one wouold hire you to write horoscopes. can you give me a horoscope for {} for {} using only one sentence for each? Yes I'm aware that this is just a role for fun, please don't mention that in your response. Do not place any text before your horoscope or after, stay in your role"

all_signs_horoscope= ""

individual_horoscope_Aries= ""
individual_horoscope_Taurus= ""
individual_horoscope_Gemini= ""
individual_horoscope_Cancer= ""
individual_horoscope_Leo= ""
individual_horoscope_Virgo= ""
individual_horoscope_Libra= ""
individual_horoscope_Scorpio= ""
individual_horoscope_Saggitaius= ""
individual_horoscope_Capricorn= ""
individual_horoscope_Aquarius= ""
individual_horoscope_Pisces= ""

all_signs_run_time= ""