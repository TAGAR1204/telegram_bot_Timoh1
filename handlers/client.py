from aiogram import types, Dispatcher
from create_bot import dp, bot
 
 #Общение клиента с ботом	

#Старт бота
async def start_bot(message : types.Message):
	try:
		await bot.send_message(message.from_user.id, 'Бот готов к работе!')
		await message.delete()
	except:
		await message.reply('Общение с ботом через ЛС:\nhttps://t.me/testtesttestforAinur_bot')

#Статистика сайта
async def static_of_website(message : types.Message):
	await bot.send_message(message.from_user.id, 'Всего игроков:\nИгроков за 24 часа:\nУбийств в голову:')

#Ссылка на группу вк
async def group_vk(message : types.Message):
	await bot.send_message(message.from_user.id, 'Наша группа в ВК:\nhttps://vk.com/public211950764')

#Пополнить баланс на сервере
async def replenish_balance(message : types.Message):
	await bot.send_message(message.from_user.id, 'Пополнить баланс на сервере здесь:\nhttps://meroco-cs.myarena.site/lk/')	

#Ссылка на сервер и на сайт
async def serevr_ip_and_name_website(message : types.Message):
	await bot.send_message(message.from_user.id, 'Информация о сервере CS:GO\nСайт:https://meroco-cs.myarena.site/n\nIP:62.122.213.114:27015')

def register_handlers_client(dp  : Dispatcher):
	dp.register_message_handler(start_bot, commands=['start', 'help'])
	dp.register_message_handler(static_of_website, commands=['Статистика_сайта'])
	dp.register_message_handler(group_vk, commands=['Наша_группа_вк'])
	dp.register_message_handler(replenish_balance, commands=['Пополнить_баланс'])
	dp.register_message_handler(serevr_ip_and_name_website, commands=['Ссылка_на_сайт_и_ip'])

