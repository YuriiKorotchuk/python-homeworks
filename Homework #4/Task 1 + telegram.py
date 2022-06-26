# Task 1 - Дана довільна строка. Напишіть код, який знайде в ній і виведе на екран кількість слів,
# які містять дві голосні літери підряд.

import telebot

bot = telebot.TeleBot('5586002843:AAEv21GjFiPWzyWIFoAwhiKzxMml7o9ZZWM')


@bot.message_handler(commands=['start'])
def start(message):
    sent_first_message = f'Хай, {message.from_user.first_name}, введи набір слів у поле тексту :)'
    bot.send_message(message.chat.id, sent_first_message)
    sent_second_message = 'І я відображу тобі кількість слів, які містять дві голосні літери підряд'
    bot.send_message(message.chat.id, sent_second_message)

@bot.message_handler()
def get_user_text(message):
    vowels_letters = ["а", "е", "є", "и", "і", "ї", "о", "у", "ю", "я", "a", "e", "i", "o", "u", "y"]
    vowels_letters2 = []
    for a in vowels_letters:
        for b in vowels_letters:
            vowels_letters2.append(a + b)

    expected_data = message.text.lower()
    each_word_number = 0

    for each_word in expected_data.split():
        for wordlist in vowels_letters2:
            if each_word.count(wordlist):
                each_word_number += 1
                break
    bot.send_message(message.chat.id, f"Саме {each_word_number} слів містять дві голосні літери підряд. Хай щастить :)")


bot.polling(none_stop=True)
