'''import sqlite3, constant, imaplib, email


con = sqlite3.connect('New_Msg.db')

def main():
    mail = imaplib.IMAP4_SSL(constant.imap_url)
    mail.login(constant.user, constant.password)
    mail.list()
    print(mail.select('inbox'))

main()'''

'''
import email
import getpass, imaplib
import os
import sys

detach_dir = '.'
if 'attachments' not in os.listdir(detach_dir):
    os.mkdir('attachments')


try:
    imapSession = imaplib.IMAP4_SSL(constant.imap_url)
    typ, accountDetails = imapSession.login(constant.user, constant.password)
    if typ != 'OK':
        print('Not able to sign in!')
        raise
    
    imapSession.list()
    imapSession.select('inbox')
    typ, data = imapSession.search(None, 'ALL')
    if typ != 'OK':
        print ('Error searching Inbox.')
        raise
    
    # Iterating over all emails
    for msgId in data[0].split():
        typ, messageParts = imapSession.fetch(msgId, '(RFC822)')
        if typ != 'OK':
            print ('Error fetching mail.')
            raise

        emailBody = messageParts[0][1]
        mail = email.message_from_string(emailBody)
        for part in mail.walk():
            if part.get_content_maintype() == 'multipart':
                # print part.as_string()
                continue
            if part.get('Content-Disposition') is None:
                # print part.as_string()
                continue
            fileName = part.get_filename()

            if bool(fileName):
                filePath = os.path.join(detach_dir, 'attachments', fileName)
                if not os.path.isfile(filePath) :
                    print (fileName)
                    fp = open(filePath, 'wb')
                    fp.write(part.get_payload(decode=True))
                    fp.close()
    imapSession.close()
    imapSession.logout()
except :
    print ('Not able to download all attachments.')'''


import imaplib, email, os, constant

def get_attachments(msg):
	for part in msg.walk():
		if part.get_content_maintype()=='multipart':
			continue
		if part.get('Content-Disposition') is None:
			continue

		try:
			fileName = email.header.decode_header(part.get_filename())[0][0].decode('utf-8')
		except:
			fileName = email.header.decode_header(part.get_filename())[0][0]

		if bool(fileName):
			filePath = os.path.join(attachment_dir, fileName)
			with open(filePath,'wb') as f:
				f.write(part.get_payload(decode=True))


mail = imaplib.IMAP4_SSL(constant.imap_url)
mail.login(constant.user, constant.password)
mail.list()
mail.select('inbox')
typ, data = mail.search(None, 'ALL')

attachment_dir = '/home/chingiz/FlaskChoco/down_att'
for msgId in data[0].split():
	typ, data = mail.fetch(msgId, '(RFC822)')
	raw = email.message_from_bytes(data[0][1])
	get_attachments(raw)