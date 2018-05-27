// Gives hashtag by day and total of times used
SELECT date_trunc('day',hashtag.hashtag_date) AS "Day" , hashtag_text , count(*)
FROM hashtag 
GROUP BY date_trunc('day',hashtag.hashtag_date), hashtag_text
ORDER BY date_trunc('day',hashtag.hashtag_date)desc

// Gives number of messages per day
SELECT date_trunc('day',message.message_date) AS "Day" , count(*) AS "No. of messages per day"
FROM message
GROUP BY date_trunc('day',message.message_date)
ORDER BY date_trunc('day',message.message_date) desc

// Gives replys per day
SELECT date_trunc('day',message.message_date) AS "Day" , count(*) AS "No. of replies per day"
FROM message natural inner join reply
where reply.reply_id = message.message_id
GROUP BY date_trunc('day',message.message_date)
ORDER BY date_trunc('day',message.message_date) desc

// GIves reactions per day
SELECT date_trunc('day',message.message_date) AS "Day" , count(*) AS "No. of reactions per day"
FROM message natural inner join reaction
where reaction.message_id = message.message_id
GROUP BY date_trunc('day',message.message_date)
ORDER BY date_trunc('day',message.message_date) desc

// GIve likes per day
SELECT date_trunc('day',message.message_date) AS "Day" , count(*) AS "No. of likes per day"
FROM message natural inner join reaction
where reaction.message_id = message.message_id
and reaction.reaction = 'like'
GROUP BY date_trunc('day',message.message_date)
ORDER BY date_trunc('day',message.message_date) desc

// GIve dislike per day
SELECT date_trunc('day',message.message_date) AS "Day" , count(*) AS "No. of dislikes per day"
FROM message natural inner join reaction
where reaction.message_id = message.message_id
and reaction.reaction = 'like'
GROUP BY date_trunc('day',message.message_date)
ORDER BY date_trunc('day',message.message_date) desc

// Give active users per day
SELECT date_trunc('day',message.message_date) AS "Day" , count(distinct users) AS "No. of active users per day"
FROM message natural inner join sent natural inner join users
where sent.message_id = message.message_id
GROUP BY date_trunc('day',message.message_date)
ORDER BY date_trunc('day',message.message_date) desc

