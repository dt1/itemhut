import sys
sys.path.append("/itemhut/pydb")
import dbconn

import db
import auth
import base64

CREDENTIALS = auth.get_credentials()
HTTP = CREDENTIALS.authorize(auth.httplib2.Http())
SERVICE = auth.discovery.build('gmail', 'v1', http=HTTP)

def get_labels():
    results = SERVICE.users().labels().list(userId='me').execute()
    labels = results.get('labels', [])

    if not labels:
        print('No labels found.')
    else:
        print('Labels:')
        for label in labels:
            print(label['name'])

def get_email(email_id, format_key):
    email = SERVICE.users().messages().get(userId = "me",
                                           id = email_id,
                                           format = format_key).execute()
    return email
            
def get_email_data():
    emails = SERVICE.users().messages().list(userId="me").execute()
    db.insert_email_threads(emails)
    print('done')

#get_labels()
#get_email_data()
a = get_email("15629397450fa7f9", "full")
#aa = base64.urlsafe_b64decode(a)
print(a)
