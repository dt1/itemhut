import sys
sys.path.append("/itemhut/pydb")
import dbconn

import json

def insert_email_threads(emails):
    dbconn.cur.execute(
        """
        begin;
        select parse_gmail_threads(%s::json);
        commit;
        """, [json.dumps(emails)])

def insert_gmail_valid_labels (label):
    dbconn.cur.execute(
        """
        begin;
        insert into email.gmail_valid_labels
        values (%s)
        on conflict (label) do nothing;
        commit;
        """, [label])

def insert_gchats(chat):
    dbconn.cur.execute(
        """
        begin;
        select email.insert_gchats(%s);
        commit
        """, [json.dumps(chat)])
