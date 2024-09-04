from model import Querys
from datetime import datetime

date = datetime.today().date()
query = Querys()


query.daily_report_check(date)