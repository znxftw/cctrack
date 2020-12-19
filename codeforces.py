from files import read, write


def cf_read():
    return read('codeforces.csv')


def cf_write(contents, today):
    write('codeforces.csv', contents, today)
