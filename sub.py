import csv
import os

from progressbar import *

csv_file_path = './test_20180506_01.csv'

csv_write_path = './res_01.csv'

if not os.path.exists(csv_write_path):
    f = open(csv_write_path, 'w')
    f.close()


with open(csv_file_path) as csv_file:
    csv_reader = csv.reader(csv_file)
    csv_head = next(csv_reader)
    print(csv_head)
    with open(csv_write_path, 'a',newline='') as out_file:
        csv_writer = csv.writer(out_file,dialect='excel')
        tmp = csv_head[2]
        csv_head[2] = csv_head[3]
        csv_head[3] = tmp
        csv_writer.writerow(csv_head)
        name_dict={}
        pbar = ProgressBar().start()
        for row in csv_reader:
            '''
            if row[0] not in name_dict:
                name_dict[row[0]] = row[0]
                tmp = row[2]
                row[2] = row[3]
                row[3] = tmp
                csv_writer.writerow(row)
            '''
            # elif( float(row[2]) > 0.9 and float(row[3]) > 5000):
            if( float(row[2]) > 0.5 and float(row[3]) > 5000):
                if row[0] not in name_dict:
                    name_dict[row[0]] = row[0]
                tmp = row[2]
                row[2] = row[3]
                row[3] = tmp
                csv_writer.writerow(row)
        pbar.finish()
        print(len(name_dict))



