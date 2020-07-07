import smtplib 
# creates SMTP session 
s = smtplib.SMTP('smtp.gmail.com', 587) 
# start TLS for security 
s.starttls()   
# Authentication 
s.login("anubhavpahwa2608@gmail.com", "anubhav@26") 
# message to be sent 
message = "Hey Developer,Our website is up."
# sending the mail 
s.sendmail("anubhavpahwa007@gmail.com", "anubhavpahwa2608@gmail.com", message) 
# terminating the session 
s.quit()
