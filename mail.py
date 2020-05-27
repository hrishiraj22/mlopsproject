import smtplib
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()

s.login("hrishiraj48@gmail.com", "**********")


    # message
message1 = "accuracy is less than 90%.Try again"
    

    # sending the mail 
s.sendmail("hrishiraj48@gmail.com", "1706505@kiit.ac.in", message1)
    

    # terminating the session
s.quit()
