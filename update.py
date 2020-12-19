from datetime import date
from codeforces import cf_read, cf_write

today = str(date.today())

cf_write(cf_read(), today)
