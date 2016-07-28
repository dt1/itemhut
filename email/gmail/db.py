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
