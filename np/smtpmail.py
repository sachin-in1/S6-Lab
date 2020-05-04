import smtplib
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login("saching1998@cet.ac.in", "12eiveocamg12")
message = "Sending gmail using SMTP implemented using python"
s.sendmail( "saching1998@cet.ac.in","sachoosrk@gmail.com", message)
s.quit()
