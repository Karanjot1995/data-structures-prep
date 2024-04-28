from collections import defaultdict
import math

def bestAverageGrade(scores):
  dict = {}

  max_avg = 0

  for pair in scores:
    if len(pair) != 2: return 0
    name = pair[0]
    if name not in dict:
      dict[name] = [0,0]
    score = int(dict[name][0])+int(pair[1])
    count = dict[name][1]+1
    avg = score/count
    max_avg = max(max_avg,avg)
    dict[name] = [avg, count]

  return int(max_avg)

scores = [("Bob","87"), ("Mike", "35"),("Bob", "52"), ("Jason","35"), ("Mike", "55"), ("Jessica", "99")]
print(bestAverageGrade(scores))

def bestAverageGrade2(scores):
    if not scores or len(scores) == 0:
        return 0
    
    grades = {}
    
    for row in scores:
        # solves clarifying question 1
        if len(row) != 2: return 0
        name, score = row
        
        if name not in grades:
            grades[name] = [0, 0]
        average, count = grades[name]
        new_average = (average * count + int(score)) / (count + 1)
        grades[name] = [new_average, count + 1]
    
    all_averages = map(lambda x: x[0], grades.values())
    
    return int(math.floor(max(all_averages)))
  
print(bestAverageGrade2(scores))