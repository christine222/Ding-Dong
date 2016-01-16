import smtplib

def emailPerson(reciever, subject, message):
	myEmail = "ideahacks36@mail.com"

	msg = MIMEText(message)
	msg['Subject'] = subject
	msg['From'] = myEmail
	msg['To'] = reciever

	s = smtplib.SMTP('localhost')
	s.sendmail(myEmail, [subject], msg.as_string())
	s.quit()



if __name__ == "__main__":
	message = "Hello how are you doing today."
	emailPerson("rzalog@gmail.com", "Hello", message)
