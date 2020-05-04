import smtplib
m = smtplib.SMTP('smtp.gmail.com', 587)
m.starttls()
m.login("saching1998@cet.ac.in", "12eiveocamg12")
message = "Sending gmail using SMTP implemented using python"
m.sendmail( "saching1998@cet.ac.in","sachoosrk@gmail.com", message)
m.quit()


