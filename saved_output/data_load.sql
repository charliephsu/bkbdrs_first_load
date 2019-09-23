USE bookbinders_wp
LOAD DATA LOCAL INFILE '/home/charlie/devel/bkbdrs_first_load/saved_output/short.csv'
          INTO TABLE wp_participants_database
FIELDS TERMINATED BY ','
         ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(first_name,last_name,city,state,slug,content,old_id,private_id)
