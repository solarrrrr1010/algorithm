import re

def solution(new_id):
  answer = new_id.lower() 
  answer = re.sub('[^a-z0-9\-\_\.]',"", answer) 
  answer = re.sub('\.+',".", answer) 
  answer = re.sub('^[.]|[.]$', "", answer)  
  answer = re.sub('^$',"a", answer)
  answer = answer[:15] 
  answer = re.sub('^[.]|[.]$', "", answer) 

  if len(answer) < 3:
    add_str = answer[-1]
    while 3-len(answer):
      answer = answer + add_str
    
  return answer