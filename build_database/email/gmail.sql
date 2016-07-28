create schema email;

create table email.gmail_threads (
       thread_id varchar,
       email_id varchar primary key
);

create or replace function parse_gmail_threads(messages json)
returns void
as
$$
declare
mss json := messages -> 'messages';
message_id varchar;
thread_id varchar;
item json;
tid varchar;
mid varchar;

begin
for item in select * from json_array_elements(mss)
loop
	tid = item ->> 'threadId';
	mid = item ->> 'id';
	insert into email.gmail_threads (thread_id, email_id)
	values (tid, mid)
	on conflict (email_id)
	do nothing;
end loop;

end;
$$ language plpgsql;

create table email.gmail_valid_labels (
       label varchar primary key
);

create table email.gmail_chats (
       chat_id varchar primary key,
       history_id bigint unique,
       internal_date bigint,
       mime_type varchar,
       from_email varchar,
       to_email varchar,
       recieve_date varchar,
       snippet varchar,
       message varchar,
       filename varchar,
       foreign key (chat_id)
               references email.gmail_threads (email_id)
);
