
import smtplib

from string import Template

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def get_contacts(filename):
	names = []
	emails = []
	with open(filename, mode='r') as contacts_file:
		for a_contact in contacts_file:
			names.append(a_contact.split()[0])
			emails.append(a_contact.split()[1])
	return names, emails

def read_template(filename):
	with open(filename, 'r') as template_file:
		template_file_content = template_file.read()
	return Template(template_file_content)

def main():
	
	names, emails = get_contacts('mycontacts.txt') 
	message_template = read_template('message.txt')
	# set up the SMTP server
	s = smtplib.SMTP(host='smtp.gmail.com', port=587)
	s.starttls()
	s.login('rakeshkumarkhetwal@gmail.com','9911496854' )
	# For each contact, send the email:
	for name, email in zip(names, emails):
		msg = MIMEMultipart()       # create a message

		# add in the actual person name to the message template
		message = message_template.substitute(PERSON_NAME=name.title())

		# Prints out the message body for our sake
		print(message)

		# setup the parameters of the message
		msg['From']='abhikhandelwal1234@gmail.com'
		msg['To']=email
		msg['Subject']="hello bhai"
		
		# add in the message body
		msg.attach(MIMEText(message, 'plain'))
		
		# send the message via the server set up earlier.
		#s.send_message(msg)
		s.sendmail('abhikhandelwal1234gmail.com', email, msg.as_string())
		del msg
		
	# Terminate the SMTP session and close the connection
	s.quit()
	
if __name__ == '__main__':
	main()
