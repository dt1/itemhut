        with new_order (internal_order_id) as
            (insert into orders.market_orders (market_order_id,
                  marketplace, salesperson_id)
             values (%s, %s, %s)
             returning internal_order_id)
             ,
             new_moi (internal_order_id) as
             (insert into orders.moi_company (internal_order_id,
                                              company_id,
                                              company_contact_id)
              select internal_order_id, %s::int, %s::int
              from new_order
              returning internal_order_id)
	      ,
	      company_info (company_name, contact_name, company_street,
	      company_city, company_state, company_zip,
	      company_country) as (

	      select company_name, contact_name, company_street,
	      company_city, company_state, company_zip,
	      company_country
	      from company.companies
	      join company.company_contact
	      using (company_id)
	      join company.contacts
	      using (company_contact_id)
	      )
	      ,
	      shipto_insertion as (
	      insert into orders.shipto_companies
	      (shipto_company, shipto_attn, shipto_street, shipto_city, shipto_state, shipto_zip, shipto_country)
	      select company_name, contact_name, company_street,
	      company_city, company_state, company_zip,
	      company_country
	      from company_info)
	      ,
	      shipto_company_id (id) as
	      (select 

        returning internal_order_id;

create or replace function orders.insert_company_sameship
       (n_salesperson_id varchar, n_marketplace varchar,
       n_company_id int)
returns r_internal_order_id int
as
$$
t_internal_order_id int;

begin

insert into orders.market_orders (market_order_id,
marketplace, salesperson_id)
values (%s, %s, %s)
returning internal_order_id into t_internal_order_id;

orders.insert_shipto_customer
       (n_order_id int, n_shipto_company varchar,
       n_shipto_attn varchar,
       n_shipto_street varchar, n_shipto_city varchar,
       n_shipto_state varchar, n_shipto_zip varchar,
       n_shipto_country varchar, n_ship_by_date date,
       n_deliver_by_date date)
select t_internal_order_id, company_name, contact_name, company_street,
company_city, company_state, company_zip, null, null
company_country
from company.companies
join company.company_contact
using (company_id)
join company.contacts
using (company_contact_id)
where company_id = n_company_id;


end;
$$ language plpgsql;


create or replace function orders.testing
       (out s int)
as
$$
begin

s := 5;

end;
$$ language plpgsql;

select orders.testing();
