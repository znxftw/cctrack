import csv
from utils import delete_file, rename_file, create_file


def cf_read():
    create_file('codeforces.csv')
    codeforces_read_file = open("codeforces.csv", "r", newline='')
    codeforces_reader = csv.reader(codeforces_read_file, delimiter=',')

    contents = []
    for row in codeforces_reader:
        contents.append(list(row))
    codeforces_read_file.close()

    return contents


def cf_write(contents, today):
    codeforces_write_file = open("tmp.csv", "w", newline='')
    codeforces_writer = csv.writer(codeforces_write_file, delimiter=',')

    # write today if empty
    if(len(contents) == 0):
        write_today(codeforces_writer, today)

    # copy already existing dates
    for line in contents:
        if(len(line) < 1):
            continue
        if line[0] != today:
            codeforces_writer.writerow(line)
        else:
            write_today(codeforces_writer, today)

    # update today
    if(len(contents) > 1 and contents[-1][0] != today):
        write_today(codeforces_writer, today)

    codeforces_write_file.close()

    delete_file('codeforces.csv')
    rename_file('tmp.csv', 'codeforces.csv')


def write_today(codeforces_writer, today):
    codeforces_writer.writerow([today, '1234'])
