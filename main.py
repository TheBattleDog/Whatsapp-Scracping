from BOT_Func import BOT

bot = BOT("C:/Users/AK PC/Documents/Programmes/Python/WhatsApp_Bot/msedgedriver.exe")

bot.url_open("https://web.whatsapp.com")
bot.nav_to_group()
bot.nav_to_link()
bot.get_link()
bot.write_link_file()
bot.invoke_js_file()
