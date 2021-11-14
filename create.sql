drop database project;
create database project;

\c project

create type location as (line1 varchar(50),line2 varchar(50),city varchar(50),stateincountry varchar(50), zip int);

create table store(store_id varchar(4) primary key, store_name varchar, store_add location, store_phone bigint); 

create table seller(seller_id varchar(4) primary key, seller_name varchar, seller_email varchar, seller_phone bigint, seller_add location, ratings int, category varchar, store_id varchar(4)); 

create table clothes(item_id varchar(4) primary key, item_name varchar, price int, colour varchar, size varchar(4), material varchar, rating int, store_id varchar(4));

create table customer(cust_id int NOT NULL primary key, cust_name varchar, ph_number bigint , addr location, email varchar);

create table payment(transaction_id int primary key, method varchar, amount float, order_id int, p_status varchar);

create table order_det(order_no int primary key, item_id varchar, o_status varchar, price int, no_of_days int, c_id int);

create table delivery(d_id int primary key, addr location, customer_name varchar, d_status varchar, d_date date, order_no int, c_id int);

create table store_reviews(cust_id int, store_id varchar(4), item_id varchar(4), rat int);

alter table store_reviews add constraint foreign1 foreign key(cust_id) references customer(cust_id);

alter table store_reviews add constraint foreign2 foreign key(store_id) references store(store_id);

alter table store_reviews add constraint foreign3 foreign key(item_id) references clothes(item_id);

alter table order_det add constraint foreign4 foreign key(item_id) references clothes(item_id);

alter table order_det add constraint foreign6 foreign key(c_id) references customer(cust_id);

alter table payment add constraint foreign4 foreign key(order_id) references order_det(order_no);

alter table seller add constraint foreign5 foreign key(store_id) references store(store_id);



	
































