create schema if not exists email;

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

--select parse_gmail_threads('{"messages": [{"id": "1562d875236701d2", "threadId": "1562d875236701d2"}, {"id": "1562cf53239ba9cf", "threadId": "1562cf53239ba9cf"}, {"id": "1562c231c2bfb122", "threadId": "1562c231c2bfb122"}, {"id": "1562abd0f50fea18", "threadId": "15629bf4cf3fc08d"}, {"id": "1562ab950858e0a8", "threadId": "15629bf4cf3fc08d"}, {"id": "1562ab8f43061460", "threadId": "15629bf4cf3fc08d"}, {"id": "1562ab895983e64b", "threadId": "15629bf4cf3fc08d"}, {"id": "1562a223525510e6", "threadId": "15629bf4cf3fc08d"}, {"id": "15629bf4cf3fc08d", "threadId": "15629bf4cf3fc08d"}, {"id": "15629397450fa7f9", "threadId": "15629397450fa7f9"}, {"id": "156244a4b0ab0771", "threadId": "156244a4b0ab0771"}, {"id": "15623b654a5964f2", "threadId": "15623b654a5964f2"}, {"id": "156237ee98af1e0d", "threadId": "156237a3673e5d01"}, {"id": "156237a3673e5d01", "threadId": "156237a3673e5d01"}, {"id": "1562322b3248054f", "threadId": "1562322b3248054f"}, {"id": "15620f85a8528a0d", "threadId": "15620f85a8528a0d"}, {"id": "15620f7eb12bb1cf", "threadId": "15620f7eb12bb1cf"}, {"id": "1561eb54bc15587d", "threadId": "1561eb54bc15587d"}, {"id": "1561bcabe334a3d4", "threadId": "1561bcabe334a3d4"}, {"id": "1561a7bc160e0b5a", "threadId": "1561a6d9f3c2b5c4"}, {"id": "15617e43ee9b42b4", "threadId": "15617e43ee9b42b4"}, {"id": "15610c4a4c72ed92", "threadId": "15610c4a4c72ed92"}, {"id": "1561016af7c4bf6e", "threadId": "15610148f0682bdd"}, {"id": "15610148f0682bdd", "threadId": "15610148f0682bdd"}, {"id": "1560f2694aeec500", "threadId": "1560ee0565105ec5"}, {"id": "1560f249a16fd276", "threadId": "1560ee0565105ec5"}, {"id": "1560f23966b897c2", "threadId": "1560ee0565105ec5"}, {"id": "1560f236b04876df", "threadId": "1560ee0565105ec5"}, {"id": "1560f1cb19f6ef17", "threadId": "1560ee0565105ec5"}, {"id": "1560ef2d9b5e772c", "threadId": "1560ef2d9b5e772c"}, {"id": "1560eec882062724", "threadId": "1560eec882062724"}, {"id": "1560ee0565105ec5", "threadId": "1560ee0565105ec5"}, {"id": "1560ed51de5f7a46", "threadId": "1560ed51de5f7a46"}, {"id": "1560ae71c73f9932", "threadId": "1560a6a4e37523a5"}, {"id": "1560a6a4e37523a5", "threadId": "1560a6a4e37523a5"}, {"id": "1560805317a37924", "threadId": "1560805317a37924"}, {"id": "15602667cf5195a4", "threadId": "15602524d97fe5dc"}, {"id": "155f7f539d9c0bd5", "threadId": "155f7f45fc605986"}, {"id": "155f7f4b1108c7d0", "threadId": "155f7f45fc605986"}, {"id": "155f7f45fc605986", "threadId": "155f7f45fc605986"}, {"id": "155f7638b96bc010", "threadId": "155f7638b96bc010"}, {"id": "155f048f703fa619", "threadId": "1559acba6cf0e2cd"}, {"id": "155f045580112f5a", "threadId": "155efcde26f415f5"}, {"id": "155f0420208a9678", "threadId": "155ef5db71ab45ba"}, {"id": "155e8cdbf49e4334", "threadId": "155e8c24f5cd46c7"}, {"id": "155e79eae5159b6b", "threadId": "155e76f013f0b810"}, {"id": "155e79e8b972d9ca", "threadId": "155e76f013f0b810"}, {"id": "155e79e49d92f912", "threadId": "155e76f013f0b810"}, {"id": "155e79e262579cef", "threadId": "155e76f013f0b810"}, {"id": "155e79e2144cebaa", "threadId": "155e76f013f0b810"}, {"id": "155e7791994865a2", "threadId": "155e76f013f0b810"}, {"id": "155e7784a9465878", "threadId": "155e76f013f0b810"}, {"id": "155e7780af85b0ca", "threadId": "155e76f013f0b810"}, {"id": "155e777e83525d64", "threadId": "155e76f013f0b810"}, {"id": "155e777dc30a7acc", "threadId": "155e76f013f0b810"}, {"id": "155e7778f87242e2", "threadId": "155e76f013f0b810"}, {"id": "155e77772b7d4c1b", "threadId": "155e76f013f0b810"}, {"id": "155e7775bb4d4e6b", "threadId": "155e76f013f0b810"}, {"id": "155e776fc5d6e319", "threadId": "155e76f013f0b810"}, {"id": "155e776c630c7858", "threadId": "155e76f013f0b810"}, {"id": "155e77467722069b", "threadId": "155e76f013f0b810"}, {"id": "155e77369eae1bb4", "threadId": "155e76f013f0b810"}, {"id": "155e772dfde862d3", "threadId": "155e76f013f0b810"}, {"id": "155e772af9c46c6d", "threadId": "155e76f013f0b810"}, {"id": "155e771b7ac93e83", "threadId": "155e76f013f0b810"}, {"id": "155e76f013f0b810", "threadId": "155e76f013f0b810"}, {"id": "155e751e175bbbfb", "threadId": "155e751e175bbbfb"}, {"id": "155e407a2c44f8e5", "threadId": "155e407a2c44f8e5"}, {"id": "155e278d097a30f8", "threadId": "155e20a324ff0c49"}, {"id": "155e278235ac316a", "threadId": "155e20a324ff0c49"}, {"id": "155e276933e644c0", "threadId": "155e20a324ff0c49"}, {"id": "155e275a8d2ee8c2", "threadId": "155e20a324ff0c49"}, {"id": "155e273466a5ef16", "threadId": "155e20a324ff0c49"}, {"id": "155e248296e5feb1", "threadId": "155e20a324ff0c49"}, {"id": "155e247bb64ab48b", "threadId": "155e20a324ff0c49"}, {"id": "155e24771fefee5e", "threadId": "155e20a324ff0c49"}, {"id": "155e20a324ff0c49", "threadId": "155e20a324ff0c49"}, {"id": "155e14d9fda9fa49", "threadId": "155e14d9fda9fa49"}, {"id": "155dd0ee8dd34655", "threadId": "155dc5bf4a583149"}, {"id": "155dcf80c9fe4204", "threadId": "155dc5bf4a583149"}, {"id": "155dcf60901c264b", "threadId": "155dc5bf4a583149"}, {"id": "155dcf4d55fd9ca5", "threadId": "155dc5bf4a583149"}, {"id": "155dcd796ca3e475", "threadId": "155dc5bf4a583149"}, {"id": "155dcd78d67768d5", "threadId": "155dc5bf4a583149"}, {"id": "155dc5c0eff331e7", "threadId": "155dc5bf4a583149"}, {"id": "155dc5bf4a583149", "threadId": "155dc5bf4a583149"}, {"id": "155c8ec793bb0d3f", "threadId": "155c8e483389aa90"}, {"id": "155c8ea81125cecb", "threadId": "155c8e483389aa90"}, {"id": "155c8ea5a636b5b1", "threadId": "155c8e483389aa90"}, {"id": "155c8e9c7d495e51", "threadId": "155c8e483389aa90"}, {"id": "155c8e95e1bfd9f7", "threadId": "155c8e483389aa90"}, {"id": "155c8e883689f187", "threadId": "155c8e483389aa90"}, {"id": "155c8e84683d56d0", "threadId": "155c8e483389aa90"}, {"id": "155c8e7fdada78fa", "threadId": "155c8e483389aa90"}, {"id": "155c8e7be0affc19", "threadId": "155c8e483389aa90"}, {"id": "155c8e483389aa90", "threadId": "155c8e483389aa90"}, {"id": "155c132193c4c67a", "threadId": "155c0f25b22cf224"}, {"id": "155c0f37fb9cd93c", "threadId": "155c0f25b22cf224"}, {"id": "155c0f2e364ad52e", "threadId": "155c0f25b22cf224"}, {"id": "155c0f2cd6bcab46", "threadId": "155c0f25b22cf224"}], "resultSizeEstimate": 309, "nextPageToken": "02073912569002741880"}');

-- select thread_id::json->'messages'
-- from email.gmail_threads;

-- select *
-- from email.gmail_threads;
