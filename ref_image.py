import csv
import os
from shutil import copyfile
import re

infile = 'saved_output/out_with_id.csv'
img_src_dir = 'orig_data/attachments/bbdir_entry'

out_image_dir = 'saved_output/images/'

image_load_file = 'saved_output/image_load.tsv'

image_prefix = 'directory/'

def read_id_from_table():
    data_old_id = {}
    with open(infile) as csv_infile:
        reader = csv.DictReader(csv_infile, delimiter='\t')
        for row in reader:
            data_old_id[row['old_id']] = row
    return data_old_id


def read_image_files(image_path,id_lookup):

    images_by_path = {}
    
    for item in os.listdir(image_path):
        id_dir_fullpath = os.path.join(image_path,item)
        for diritem in os.listdir(id_dir_fullpath):
            if os.path.isdir(id_dir_fullpath):
                # img_fullpath is the src path for the image
                image_filename = diritem                
                img_fullpath = os.path.join(id_dir_fullpath,image_filename)
                #print("id {} --  file: {}".format(item,img_fullpath))
                images_by_path[img_fullpath] = {}
                images_by_path[img_fullpath]['id'] = item
                images_by_path[img_fullpath]['filename'] = image_filename

    image_list = []
    with open(image_load_file,'w') as imageout:
        writer = csv.writer(imageout, delimiter='\t')
        for path,value in images_by_path.items():
            # path is the fullpath
        
            filename = value['filename']
            old_id = value['id']
            
            table_data = id_lookup.get(old_id,{})
            private_id = table_data.get('private_id',None)
            new_id = table_data.get('new_id',None)

            #print("{} -- {} :: {}".format(path,filename,new_id))

            # create new filename

            # split extension
            fname,fext = os.path.splitext(filename)

            # reaplce whitespace with underscore        
            new_filename = fname.replace(" ","_")
            new_filename = new_filename.replace(".","_")
            # collaspe double underscores
            new_filename = re.sub('__+','_',new_filename)

            new_filename = new_filename + fext
            new_filename = private_id + "-" + new_filename

            new_fullpath = os.path.join(out_image_dir,new_filename)
            #print("Old: {}  --> New: {}".format(filename,new_fullpath))
            copyfile(path,new_fullpath)

            # file will have image path, new_id
            # file path will be  directory/ + new file name
            image_name_for_db = image_prefix + new_filename
            writer.writerow((image_name_for_db,new_id))
        
if __name__ == "__main__":
    data_id = read_id_from_table()
    read_image_files(img_src_dir,data_id)
