# First load of bookbinders archive database

* first_transform.py take original file, added private id
  creates:  outload_with_shortuuid.csv
* use data_load.sql to load into datbase, this creates new ids
* out_with_id.csv is made by dumping the table to file
* run image_ref to copy image files and create image data table
* load table 

