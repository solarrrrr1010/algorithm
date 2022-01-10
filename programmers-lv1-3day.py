import re

eng_nums = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

def solution(s):
    for i in range(len(eng_nums)):
      s = re.sub(eng_nums[i], str(i), s)

    return int(s)