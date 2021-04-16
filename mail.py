import smtplib

server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server.login("surjith6666@gmail.com", "9846026274")
server.sendmail("surjithsurendranp@gmail.com", "Hello, How are you?")

server.quit()
