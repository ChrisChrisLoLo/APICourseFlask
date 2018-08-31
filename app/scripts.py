import csv
from models.courseModel import *
from app import db

CSV_FILE_PATH = './app/scriptResources/UAlbertaCoursesSingleTable.csv'

def seedFromCSV():
    """
    Seeds the DB with course information from a csv
    """

    print('Running... Please be patient')
    with open(CSV_FILE_PATH, newline='') as csvFile:
        csvReader = csv.reader(csvFile)
        #Skip first row (the title row)
        next(csvReader)
        for row in csvReader:
            print(row)
            facultyObj = getOrCreate(Faculty,
                name = row[0]
            )
            subjectObj = getOrCreate(Subject,
                name = row[1],
                subject_code = row[2],
                faculty_id = facultyObj.id,
                faculty = facultyObj
            )
            courseObj = getOrCreate(Course,
                course_code = row[3],
                name = row[4],
                description = row[5],
                subject_id = subjectObj.id,
                subject = subjectObj
            )

def getOrCreate(Model, **kwargs):
    instance = Model.query.filter_by(**kwargs).first()
    if instance:
        pass
    else:
        params = dict((k, v) for k, v in kwargs.items())
        instance = Model(**params)
        db.session.add(instance)
        db.session.commit()
    return instance