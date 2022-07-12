# youtube-stats-python
Simple python based scripts to use the YouTube API to store viewership in a PostgresQL database. Similar to socialblade.com.

Currently implemented tracking channel statistics, TODO: Video statistics, tracking channels in groups (named "companies"). I created a table in postgres with 2 foreign keys to create a many2many for companies. You can group channels by niche / similar as well. 
