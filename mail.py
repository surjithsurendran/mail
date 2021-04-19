import smtplib

server = smtplib.SMTP_SSL("smtp.54.234.55.202.com", 465)
server.login("surjith@mail.surjithp.com", "1234")
server.sendmail("devops@mail.surjith1.com", "Hello, How are you?")

server.quit()
