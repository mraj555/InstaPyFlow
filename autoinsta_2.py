from instabot import Bot
import os
import random
from PIL import Image
import smtplib

bot = Bot()
bot.login(username="Insta_UserName", password="Insta_Password")

email = "YOUR_EMAIL_ID"
password = "YOUR_PASSWORD"

files_name = os.listdir(f"{os.getcwd()}/photos")


def send_email(to, subject, body):
    message = f"Subject: {subject}\n\n{body}"

    with smtplib.SMTP("smtp.gmail.com", 587) as s:
        s.starttls()
        s.login(email, password)
        s.sendmail(email, to, message)
        s.quit()  # ✅ added parentheses


# ✅ added body argument
send_email(
    "RECEIVER_EMAIL_ID",
    "Photo Storage Update",
    f"Available Photos in Storage: {len(files_name)}",
)

file = random.choice(files_name)
split_file_name = str(file).split(".")
ext = str(split_file_name[1])

if ext == "png":
    img = Image.open(f"{os.getcwd()}/photos/{file}")
    img.convert("RGB").save(f"{os.getcwd()}/photos/converted_{file}.jpg")
    conv_file = f"converted_{file}.jpg"
    bot.upload_photo(f"{os.getcwd()}/photos/{conv_file}", "caption")
    os.remove(f"{os.getcwd()}/photos/{conv_file}")
elif len(files_name) <= 10:
    # ✅ added body argument here too
    send_email(
        "RECEIVER_EMAIL_ID",
        "Low Storage Warning",
        f"Available Photos in Storage: {len(files_name)}",
    )
else:
    bot.upload_photo(f"{os.getcwd()}/photos/{file}", "caption")
    os.remove(f"{os.getcwd()}/photos/{file}")
