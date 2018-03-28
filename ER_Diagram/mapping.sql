
create table users(users_id serial primary key, first_name varchar(125) NOT NULL, last_name varchar(125) NOT NULL, users_phone char(10) NOT NULL, users_email varchar(254) NOT NULL, users_password varchar(64) NOT NULL,users_date timestamp default current_timestamp);
create table message(message_id serial primary key, message_text text NOT NULL, message_date timestamp default current_timestamp);
create table hashtag(hashtag_id serial primary key, hashtag_text text NOT NULL, hashtag_uses int, hashtag_date timestamp default current_timestamp);
create table group_chat(group_id serial primary key, group_name varchar(20),group_number_users int, group_active int, group_date timestamp default current_timestamp);

create table administrates(users_id integer references users(users_id),group_id integer references group_chat(group_id),primary key(users_id,group_id));
create table member_of(users_id integer references users(users_id),group_id integer references group_chat(group_id),primary key(users_id,group_id));
create table sent(users_id integer references users(users_id),message_id integer references message(message_id),primary key(users_id,message_id));
create table reaction(users_id integer references users(users_id),message_id integer references message(message_id),primary key(users_id,message_id));

create table messages(message_id integer references message(message_id),group_id integer references group_chat(group_id),primary key(message_id,group_id));
create table has(message_id integer references message(message_id), hashtag_id integer references hashtag(hashtag_id),primary key(message_id,hashtag_id));

create table contacts(super_id integer references users(users_id), contact_id integer references users(users_id),primary key(super_id,contact_id));
create table reply(owner_id integer references message(message_id), reply_id integer references message(message_id),primary key(owner_id,reply_id));
