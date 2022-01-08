import re

def solution(new_id):
  new_id = new_id.lower()
  new_id = re.sub('\.\.',".", new_id)
  new_id = re.sub('[^a-z0-9\-\_\.]|^[\.]|[\.]$',"", new_id)
  answer = re.sub('^$',"a", new_id)
  return answer
