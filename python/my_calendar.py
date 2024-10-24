import datetime
import sys

def get_argument():
  arg = None
  if len(sys.argv) == 3:
    judge = sys.argv[1]
    if judge == "-m":
      try:
        arg = int(sys.argv[2])
        if not(1 <= arg <=12):
          print(f"{arg} is neither a month number (1..12) nor a name")
          sys.exit()
      except ValueError:
        print(f"{sys.argv[2]} is neither a month number (1..12) nor a name")
        sys.exit()
  return arg

def main():
  dm = None
  dm = get_argument()
  dt = datetime.datetime.today().date()
  dy = dt.year

  if dm is not None:
      dt = datetime.date(dy,int(dm),int(1))

  dm = "{:02}".format(dt.month)

  for i in range(31,27,-1):
      try:
          last_date = datetime.date(dy,int(dm),int(i))
          break
      except ValueError:
          # 無効な日付の場合は次の繰り返しへ進む
          continue

  first_date = datetime.date(dy,int(dm),int(1))
  weekday_int = datetime.date.weekday(first_date)
  date_arry = [ "  " for v in range(weekday_int)]
  date_arry = date_arry + ["{:02}".format(v) for v in range(first_date.day,last_date.day)]

  print(f"      {dm}月  {dy}年")
  weekday_array = ['月', '火', '水', '木', '金', '土', '日']
  weekday_array = "  ".join(weekday_array)
  print(weekday_array)
  chunk_size = 7
  for i in range(0, len(date_arry), chunk_size):
      week_dates = date_arry[i:(i+chunk_size)]
      week_dates = "　".join(week_dates)
      print(week_dates)


if __name__ == "__main__":
    main()
