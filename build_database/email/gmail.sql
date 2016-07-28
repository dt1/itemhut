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

create table email.gchats (
       chat_id varchar primary key,
       history_id bigint unique,
       internal_date varchar,
       mime_type varchar,
       from_email varchar,
       to_email varchar,
       recieve_date date,
       snippet varchar,
       message varchar,
       filename varchar,
       foreign key (chat_id)
               references email.gmail_threads (email_id)
);

drop function email.insert_gchats(json);
create or replace function email.insert_gchats(chat json)
returns void
as
$$
declare
t_chat_id varchar;
t_thread_id varchar;
t_history_id bigint;
t_internal_date varchar;
t_mime_type varchar;
t_from_email varchar;
t_to_email varchar;
t_recieve_date date;
t_snippet varchar;
t_message varchar;
t_filename varchar;

begin
t_chat_id = chat ->> 'id';
t_thread_id = chat ->> 'threadId';
t_history_id = chat ->> 'historyId';
t_internal_date = chat ->> 'internalDate';
t_from_email = chat -> 'headers' -> 0 ->> 'value';
-- t_recieve_date = chat ->> to_timestamp('internalDate');
t_snippet = chat -> 'snippet';
t_message = chat -> 'payload' -> 'body' ->> 'data';

insert into email.gmail_threads (thread_id, email_id)
values (t_thread_id, t_chat_id)
on conflict(email_id) do nothing;

insert into email.gchats
       (chat_id, history_id, internal_date, mime_type,
       from_email, snippet, message)
values
	(t_chat_id, t_history_id, t_internal_date, t_mime_type,
	t_from_email, t_snippet, t_message)
on conflict (chat_id) do nothing;
end;
$$ language plpgsql;
