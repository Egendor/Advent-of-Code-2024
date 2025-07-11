list1 = []
list2 = []
with open("input01.txt", "r") as f:
    for row in f:
        row_elements = row.strip().split()
        list1.append(int(row_elements[0]))
        list2.append(int(row_elements[1]))
        
if not (len(list1) == len(list2)):
    print("Listorna olika långa, det är fel!")

list1_sort = sorted(list1)
list2_sort = sorted(list2)
sum = 0
for i in range(len(list1_sort)):
    sum += abs(list1_sort[i] - list2_sort[i])
print(sum)

right_dict = dict()
for num in list2:
    if num not in right_dict:
        right_dict[num] = 1
    else:
        right_dict[num] += 1

#print(right_dict)

sim_score = 0
for number in list1:
    if number in right_dict:
        sim_score += number * right_dict[number]
print(sim_score)

