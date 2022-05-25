# import telebot
# bot = telebot.TeleBot('5101538599:AAEhGpnGX752tH1hbsXf4R0odifRnTRbuts')
# @bot.message_handler(func = lambda message: True)
# def send(message):
#     bot.reply_to(message, 'Ну и кого это волнует')
# @bot.message_handler(func = lambda messages: messages.text=='Aloha')
# def aloha(message):
#     bot.reply_to(message, 'Удачи')
# @bot.message_handler(func = lambda messages: True)
# def aloha(message):
#     bot.reply_to(message, 'Пока рано')
# bot.polling()
import telebot
bot = telebot.TeleBot('5101538599:AAEhGpnGX752tH1hbsXf4R0odifRnTRbuts')
@bot.message_handler(content_types=['text', 'audio', 'document', 'photo', 'sticker', 'video', 'video_note', 'voice', 'location', 'contact', 'new_chat_members', 'left_chat_member', 'new_chat_title', 'new_chat_photo', 'delete_chat_photo', 'group_chat_created', 'supergroup_chat_created', 'channel_chat_created', 'migrate_to_chat_id', 'migrate_from_chat_id', 'pinned_message'])
def fn(messages):
    bot.send_message(messages.chat.id, messages.content_type)
bot.polling()