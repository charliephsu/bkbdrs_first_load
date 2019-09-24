USE bookbinders_wp
LOAD DATA LOCAL INFILE 'image_load.tsv'
          INTO TABLE dbadmin_dirimages
FIELDS TERMINATED BY "\t"
LINES TERMINATED BY "\n"
IGNORE 1 LINES
(image,wppd_id)
