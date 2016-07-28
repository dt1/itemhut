import sys
sys.path.append("/itemhut/pydb")
import dbconn

import gmail_db
import auth
import base64

CREDENTIALS = auth.get_credentials()
HTTP = CREDENTIALS.authorize(auth.httplib2.Http())
SERVICE = auth.discovery.build('gmail', 'v1', http=HTTP)

def get_labels():
    results = SERVICE.users().labels().list(userId='me').execute()
    labels = results.get('labels', [])

    if not labels:
        pass
    else:
        for label in labels:
            gmail_db.insert_gmail_valid_labels(label["name"])

def get_gmail_threads():
    emails = SERVICE.users().messages().list(userId="me").execute()
    gmail_db.insert_email_threads(emails)
    print('done')

def get_gmail(email_id, format_key):
    email = SERVICE.users().messages().get(userId = "me",
                                           id = email_id,
                                           format = format_key).execute()
    return email
            
def get_gmail_by_label(labels):
    messages = SERVICE.users().messages().list(userId = "me",
                                               labelIds = labels).execute()
    return messages

def get_gmail_chats():
    messages = get_gmail_by_label(["CHAT"])
    for message in messages["messages"]:
        chat = get_gmail(message["id"], "full")
        chat["payload"]["body"]["data"] = str(base64.urlsafe_b64decode(chat["payload"]["body"]["data"]))
        gmail_db.insert_gchats(chat)
    print('done')
    

#get_labels()
#get_gmail_data()
#a = get_gmail("1562a223525510e6", "metadata")
#aa = base64.urlsafe_b64decode(a)
#print(a)

get_gmail_chats()
