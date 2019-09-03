import smtplib

content = "Message to send"
mail = smtplib.SMTP("smtp.gmail.com",587)
mail.ehlo()
mail.starttls()

mail.login('youremail@gmail.com','password')
mail.sendmail("youremail@gmail.com","targetmail@gmail.com",content)
