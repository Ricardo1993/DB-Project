-- Inserting into users --

insert into users (first_name,last_name,users_phone,users_email,users_password) values('Diego','Capre',7879009873,'dcapre@live.com','mypassword');

insert into users (first_name,last_name,users_phone,users_email,users_password) values('Victor','Fermin',7878901111,'victor.fermin@upr.edu','password12');

insert into users (first_name,last_name,users_phone,users_email,users_password) values('Ricardo','Casares',7875639978,'ricardo.casares@upr.edu','pass123');

insert into users (first_name,last_name,users_phone,users_email,users_password) values('Manuel','Rodriguez',7876669999,'profesores@upr.edu','dbmaster');

-- Deleting users --

DELETE from users
where users_id=6

-- Insert into contacts (who knows who) -- 
insert into contacts(super_id, contact_id) values(8,1);
insert into contacts(super_id, contact_id) values(8,2);
insert into contacts(super_id, contact_id) values(8,3);

insert into contacts(super_id, contact_id) values(1,8);
insert into contacts(super_id, contact_id) values(1,2);
insert into contacts(super_id, contact_id) values(1,3);

insert into contacts(super_id, contact_id) values(2,8);
insert into contacts(super_id, contact_id) values(2,1);
insert into contacts(super_id, contact_id) values(2,3);

insert into contacts(super_id, contact_id) values(3,8);
insert into contacts(super_id, contact_id) values(3,1);
insert into contacts(super_id, contact_id) values(3,2);

-- Inserting into message --
insert into message (message_text) values('Profe que viene para el examen???');
insert into message (message_text) values('Todo');
insert into message (message_text) values('Ah diache profe.');
insert into message (message_text) values('Ese examen va a estar feo. #PRSeLevanta');
insert into message (message_text) values('Enserio?');
insert into message (message_text) values('A estudiar');
insert into message (message_text) values('Super feo');
insert into message (message_text) values('Buena pregunta');
insert into message (message_text) values('???? #100x35 #PRSeLevanta');
insert into message (message_text) values('Ya lo sabes');

-- Inserting into sent (who sent, what message) -- 
insert into sent(users_id,message_id) values (,);
insert into sent(users_id,message_id) values(2,2);
insert into sent(users_id,message_id) values(8,3);
insert into sent(users_id,message_id) values(1,5);
insert into sent(users_id,message_id) values(3,10);

-- Insert into group_chat --
insert into group_chat(group_name, group_number_users, group_active) values('DB Class',4,4);

-- Insert into administrates (owner of a group_chat) --
insert into administrates(users_id,group_id) values(8,2);

-- Insert into member_of (group_chat in which a member participates) -- 
insert into member_of(users_id,group_id) values(8,2);
insert into member_of(users_id,group_id) values(2,2);
insert into member_of(users_id,group_id) values(1,2);
insert into member_of(users_id,group_id) values(3,2);

-- Insert into messages (what message is from what group_chat) --
insert into messages(message_id,group_id) values(2,2);
insert into messages(message_id,group_id) values(3,2);
insert into messages(message_id,group_id) values(5,2);
insert into messages(message_id,group_id) values(10,2);

-- Insert into reply (original message, reply)--
insert into reply(owner_id, reply_id) values (5,10);

-- Insert into reaction (reactions of a message like or dislike)-- 
insert into reaction(users_id,message_id,reaction) values (8,5,'dislike');
insert into reaction(users_id,message_id,reaction) values (2,5,'like');
insert into reaction(users_id,message_id,reaction) values (3,5,'like');

-- Insert into hashtag -- 
insert into hashtag(hashtag_text, hashtag_uses) values ('#PRSeLevanta',2);
insert into hashtag(hashtag_text, hashtag_uses) values ('#100x35',1);

-- Insert into has (which message has which tag)-- 
insert into has(message_id, hashtag_id) values(5,2);
insert into has(message_id, hashtag_id) values(10,2);
insert into has(message_id, hashtag_id) values(10,3);


