import imaplib, email, os, constant, sqlite3

conn = sqlite3.connect('New_Msg.db')

names = []

def down_attachments(msg):
	attachment_dir = '/home/chingiz/FlaskChoco/down_att'
	for part in msg.walk():
		if part.get_content_maintype()=='multipart':
			continue
		if part.get('Content-Disposition') is None:
			continue

		try:
			fileName = email.header.decode_header(part.get_filename())[0][0].decode('utf-8')
		except:
			fileName = email.header.decode_header(part.get_filename())[0][0]

		names.append(fileName)

		if bool(fileName):
			filePath = os.path.join(attachment_dir, fileName)
			with open(filePath,'wb') as f:
				f.write(part.get_payload(decode=True))

mail = imaplib.IMAP4_SSL(constant.imap_url)
mail.login(constant.user, constant.password)
mail.list()
mail.select('inbox')
typ, data = mail.search(None, 'ALL')

for msgId in data[0].split():
	typ, data = mail.fetch(msgId, '(RFC822)')
	raw = email.message_from_bytes(data[0][1])
	down_attachments(raw)
print(names)
