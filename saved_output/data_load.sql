USE bookbinders_wp
LOAD DATA LOCAL INFILE 'outload_with_shortuuid.csv'
          INTO TABLE wp_participants_database
FIELDS TERMINATED BY ","
         ENCLOSED BY "'"
LINES TERMINATED BY "\n"
IGNORE 1 LINES
(first_name,last_name,city,state,slug,content,old_id,private_id)
