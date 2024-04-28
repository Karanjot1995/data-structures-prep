class Solution:
  def reformatDate(self, date: str) -> str:
    months = {"Jan":'01', "Feb":'02', "Mar":'03', "Apr":'04', "May":'05', "Jun":'06', "Jul":'07', "Aug":'08', "Sep":'09', "Oct":'10', "Nov":'11', "Dec":'12'}
    arr = date.split()
    day = arr[0][:-2]
    month = months[arr[1]]
    year = arr[2]
    if int(day) < 10: day = '0'+day
    date = year+'-'+month+'-'+day
    return date