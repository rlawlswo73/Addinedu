-- 정책 금리
create table interest_rate (
    date date PRIMARY KEY,
    k_interest_rate float,
    usa_interest_rate float
);

-- 원/달러 환율
create table exchange_rate (
    date date PRIMARY KEY,
    exchange_rate_wd float
);

create table cofix (
    cofix_id int PRIMARY key,
    date date,
    value float
);

create table khai (
    khai_id int PRIMARY key,
    date date,
    value float
);

create table housing_price (
    housing_price_id int PRIMARY key,
    date date,
    value float
);

-- 금 시세
create table gold (
    date date PRIMARY key,
    price float,
    rate_of_change float
);

-- 물가 지수
create table price_index (
    date date PRIMARY key,
    k_price_index float,
    usa_price_index float
);