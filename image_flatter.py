import os
from shutil import copyfile

image_path  = "data/attachments/bbdir_entry"
sql_outfile = "data/attachments/sql_image_id.sql"

id_to_files = {}
for item in os.listdir(image_path):
    id_dir_fullpath = os.path.join(image_path,item)
    if os.path.isdir(id_dir_fullpath):
        for diritem in os.listdir(id_dir_fullpath):
            image_fullpath = os.path.join(id_dir_fullpath,diritem)
            if os.path.isfile(image_fullpath):
                #print(" id {}, file: {}".format(item,diritem))
                new_filename = "directory_image_{}_{}".format(item,diritem)
                new_fullpath = os.path.join("data","attachments","new_filenames",new_filename)
                #print(image_fullpath,"--",new_fullpath)
                copyfile(image_fullpath,new_fullpath)
                if item not in id_to_files:
                    id_to_files[item] = []
                id_to_files[item].append(new_filename)


with open(sql_outfile,'w') as outfile:
    for entry_id,entry_files in id_to_files.items():
        new_entries = []
        for ii in entry_files:
            print(ii)
            fname,fext = ii.rsplit(".",1)
            fname = fname.replace(".","-")
            new_entries.append(fname)
        #print(entry_id, entry_files) 
        file_entry = ",".join(new_entries)
        sql_string = "UPDATE wp_participants_database SET image01 = \"{}\" WHERE old_id = {}".format(file_entry,entry_id)
        outfile.write(sql_string + ';\n')