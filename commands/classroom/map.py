import getlinks
import json

course_alias = {
    "Grade 10 Math" : 'G10Math',
    "Chemistry" : 'ChemSat',
    "Physics Saturday": 'PhysSat',
    "Chemistry Saturday": 'ChemSat',
    "Biology Saturday 11-1": 'BioSat',
}

def get_classes():
    courses = getlinks.main()
    data = {}
    for course in courses:
        if (course not in course_alias):
            continue
        data[course_alias[course]] = courses[course]
    return data

def update_links():
    data = get_classes()
    with open('../../data.json', 'w') as file:
        file.write(json.dumps(data))