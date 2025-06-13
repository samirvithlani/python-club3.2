data = [(85,"jeet"),(78,"parth"),(98,"parth"),(98,"jay"),(85,"parth")]
#{85:["jeet","parth"],78:["parth"],98:["jay","parth"]}

result ={}

for i,j in data: #85,"jeet" 78 ,parth,98 partg 98 jay
    if i in result:
        #98.append
        result[i].append(j)
    else: #
        #{85:["jeet"],78:["parth"],98:["parth"]}
        result[i]=[j]

print(result)
