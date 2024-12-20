-- 1) Count the number of users who signed up on each date
SELECT signup_date, COUNT(*) AS user_count
FROM users
GROUP BY signup_date
ORDER BY signup_date;

-- 2) List all unique email domains
SELECT DISTINCT domain
FROM users;

-- 3) Retrieve all users who signed up within the last 7 days
SELECT *
FROM users
WHERE signup_date >= NOW() - INTERVAL '7 days';

-- 4) The most popular domain
SELECT domain, COUNT(*) AS domain_count
FROM users
GROUP BY domain
ORDER BY domain_count DESC
LIMIT 1;

-- Users with the most popular domain
SELECT *
FROM users
WHERE domain = (
    SELECT domain
    FROM users
    GROUP BY domain
    ORDER BY COUNT(*) DESC
    LIMIT 1
);

-- 5) Delete records where the email domain is not from the allowed list
DELETE FROM users
WHERE domain NOT IN ('gmail.com', 'yahoo.com', 'example.com');
