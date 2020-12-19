from datetime import date
from codeforces import cf_read, cf_write

today = str(date.today())

cf_contents = cf_read()
cf_write(cf_contents, today)