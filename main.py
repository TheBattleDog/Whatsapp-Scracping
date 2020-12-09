from BOT_F import BOT


bot = BOT("C:/Users/AK/Documents/Code/Whatsapp/chromedriver.exe")

bot.url_open("https://web.whatsapp.com")
bot.nav_to_group()
bot.nav_to_link()
bot.get_link()
