#Day 1: Introduction to Python

name = 'Rakshith'
experience = 1
expected_package = 40

print(f" My name is :{name}")
print(f"Experience: {experience} years")
print(f"Expected Package: {expected_package} LPA")

#List
skills = ['Python','AIML','Data Science','Web Development']
skills.append('Java')
skills.insert(2,'Git')
skills.extend(['C++','SQL'])
skills.remove('SQL')


#Dictionary
profile = {
    "Name":name,
    "Skills":skills,
    "target_city":'Bangalore'
}

print(profile)

def skill_count(skill_list):
    return len(skill_list)

print("Total skillls:", skill_count(skills))

for skill in skills:
    print(skill)
