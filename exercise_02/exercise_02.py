import csv
import argparse

# 1.A
def print_file_content(file):
    with open(file) as file_read:
        print(file_read.read())

# 1.B.a
def write_list_to_file(output_file, *text):
    with open(output_file, 'w') as file:
        out_file = csv.writer(file)
        for i in text:
            out_file.writerow(i)
# 1.C
def read_csv(input_file):
     with open(input_file) as file_read:
        lst = []
        for i in file_read:
            lst.append(i)
        print(lst)

# print_file_content('exercise_02_file.csv')
# write_list_to_file('test.csv',['jeh','dem','gid'],["test"])
# read_csv('test')

# 2/3
if __name__ == '__main__':
    parser= argparse.ArgumentParser(description='file writer')
    parser.add_argument('path', help= 'path to file')
    parser.add_argument('-f','--file',help= 'write content to file_name')
    args = parser.parse_args()
    if args.file == None:
        print_file_content(args.path)
    else:
        write_list_to_file(args.path,args.file)
        


