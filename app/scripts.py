import csv
from models.courseModel import *

CSV_FILE_PATH = './app/scriptResources/UAlbertaCoursesSingleTable.csv'
def seedFromCSV(db):
    """
    Seeds the DB with course information from a csv
    """

    print('Running... Please be patient')
    with open(CSV_FILE_PATH, newline='') as csvFile:
        csvReader = csv.reader(csvFile)
        #Skip first row (the title row)
        next(csvReader)
        for row in csvReader:
            # #Note: Obj is the resulting entry created as an object
            # #Created is a boolean.
            # facultyObj, facultyCreated = Faculty.objects.get_or_create(
            #     name=row[0],
            # )
            # subjectObj, subjectCreated = Subject.objects.get_or_create(
            #     name=row[1],
            #     letter_code=row[2],
            #     faculty=facultyObj
            # )
            # courseObj, courseCreated = Course.objects.get_or_create(
            #     number_code=row[3],
            #     name=row[4],
            #     description=row[5],
            #     subject=subjectObj
            # )
            faculty = getOrCreate(Faculty)
            print(faculty)

def getOrCreate(Model):
    object = Model.query.get(1)
    if object == None:
        print('CREATE')
        return #return created
    return object