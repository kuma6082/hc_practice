import random

member =["A","B","C","D","E","F"]
random.shuffle(member)
group_a =[]
group_b =[]

num_per_group = [2,3]
group_a_num = random.choice(num_per_group) 

for v in member:
    if len(group_a) < group_a_num: 
        group_a.append(v)
    else:
        group_b.append(v)

print(group_a)
print(group_b)