def solution(id_list, report, k):
    report_list = []
    answer = []
    id_dic = {i.split(' ')[0]:0 for i in id_list}
    report = list(set(report))
    
    for i in range(len(report)):
        report_list.append(report[i].split()[1])

    for i in range(len(id_list)):
      for j in range(len(id_list)):
        if k <= report_list.count(id_list[j]):
          for l in range(len(report)):
            user = id_list[i] + ' ' + id_list[j]
            if user == report[l]:
              id_dic[id_list[i]] = id_dic[id_list[i]] + 1
    answer = [id_dic[i] for i in id_list]
    return answer

id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2

solution(id_list, report, k)