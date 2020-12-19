from utils import create_file, delete_file, rename_file
import csv


def read(filename):
    create_file(filename)
    read_file = open(filename, "r", newline='')
    reader = csv.reader(read_file, delimiter=',')

    contents = []
    for row in reader:
        contents.append(list(row))
    read_file.close()

    return contents


def write(filename, contents, today, data):
    write_file = open('temporary_file.csv', "w", newline='')
    writer = csv.writer(write_file, delimiter=',')

    # write today if empty
    if(len(contents) == 0):
        write_today(writer, today, data)

    # copy already existing dates
    for line in contents:
        if(len(line) < 1):
            continue
        if line[0] != today:
            writer.writerow(line)
        else:
            write_today(writer, today, data)

    # update today
    if(len(contents) > 0 and contents[-1][0] != today):
        write_today(writer, today, data)

    write_file.close()

    delete_file(filename)
    rename_file('temporary_file.csv', filename)


def write_today(writer, today, data):
    row = [today]
    row.extend(data)
    writer.writerow(row)
