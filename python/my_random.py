import random

member =["A","B","C","D","E","F"]
random.shuffle(member)
group_a =[]
group_b =[]

num_per_group = [2,3]
group_a_num = random.choice(num_per_group) 

group_a = member[:group_a_num]
group_b = member[group_a_num:]

print(group_a)
print(group_b)