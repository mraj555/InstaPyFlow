from instabot import Bot

bot = Bot()
bot.login(username="Insta_UserName", password="Insta_Password")

# Only JPEG and JPG Format
bot.upload_photo("image.jpg", "Test Caption")
