import os,time
def RanNum(top):
  number = os.getpid()*time.time_ns()%top
  return int(number)



print(RanNum(1000)) 