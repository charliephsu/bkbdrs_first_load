import csv
import shortuuid

### IN
infile_name = 'orig_data/bbdir_entry.csv'
### OUT
outfilename = 'output/outload_with_shortuuid.csv'

infields_list = ['id','name','city','state','slug','content']
outfile_header = ['first_name','last_name','city','state','slug','content','old_id','private_id']

def transform_data(infile_name):

    count = 0

    with open(infile_name,'r',newline='') as infile:
        #inreader = csv.reader(infile, delimiter=',', quotechar='"')
        inreader = csv.DictReader(infile)

        with open(outfilename,'w') as csv_outfile:
            writer = csv.DictWriter(csv_outfile,fieldnames=outfile_header,
                                    lineterminator='\n',
                                    quotechar="'",
                                    escapechar='\\',
                                    doublequote="False")
            writer.writeheader()
            for row in inreader:
                namelist = row['name'].split(",")
                lastname = namelist[0].strip()
                firstname = " ".join(namelist[1:]).strip()

                newcontent = row["content"].replace("\r","")
                #newcontent = newcontent.replace("\n","%$%")
                #newcontent = "<code>" + newcontent
                outdict = {
                    "first_name": firstname,
                    "last_name": lastname,
                    "city": row["city"],
                    "state": row["state"],
                    "slug": row["slug"],
                    "content": newcontent,
                    "old_id": row["id"],
                    "private_id": shortuuid.uuid(),
                }
                writer.writerow(outdict)
                count = count + 1


if __name__ == "__main__":
    transform_data(infile_name)
