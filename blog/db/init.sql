create table article (
  id serial not null primary key,
  title text,
  content text,
  created_at timestamp,
  popularity_level text,
  is_published boolean,
  published_at timestamp
);