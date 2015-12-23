######SQL Processing

JSON is inserted into staging tables and converted using PostgreSQL's json lib.

While PostgreSQL offers quite a few tools for querying JSON, the tools for processing are fairly straight-forward:

```SQL
v#>>'{Key1, key2, value}'
```

The # begins a path for json-type. The >> converts the final value to a varchar. 

```SQL
v#>'{Key1, key2, SomeArray}->1#>>'{value}'
```

The above code keeps the first part of the path json.
The '1' is an array index.
The >>, once again, coerces the final value to varchar.

Coercion to other data-types are done at the variable declaration level:

```SQL
delcare
p_jid int := jid;
p_ebay_time timestamp := v->'Timestamp'->>'value';
```

[PostgreSQL JSON documentation](http://www.postgresql.org/docs/current/static/functions-json.html)