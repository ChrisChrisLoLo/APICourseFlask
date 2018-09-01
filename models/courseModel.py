from app import db,ma
from marshmallow import Schema, fields, pre_load, validate
class Faculty(db.Model):
    """Class that represents the Faculty table."""

    __tablename__ = 'faculties'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255),unique=True,nullable=False)

    def __repr__(self):
        return '<Faculty %r>' % self.name

class FacultySchema(ma.Schema):
    id = fields.Integer
    name = fields.String(required=True)

class Subject(db.Model):
    """Class that represents the Subject table."""

    __tablename__ = 'subjects'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120),nullable=False)
    subject_code = db.Column(db.String(6),unique=True,nullable=False)

    faculty_id = db.Column(db.Integer, db.ForeignKey('faculties.id'),
        nullable=False)
    faculty = db.relationship('Faculty',
        backref=db.backref('subjects',lazy=True))

    def __repr__(self):
        return '<Subject %r>' % self.name

class SubjectSchema(ma.Schema):
    id = fields.Integer()
    name = fields.String()
    subject_code = fields.String()
    faculty_id = fields.String()

class Course(db.Model):
    """Class that represents the Course table."""

    __tablename__ = 'courses'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120),nullable=False)
    course_code = db.Column(db.Integer,nullable=False)
    description = db.Column(db.String(1600))

    subject_id = db.Column(db.Integer, db.ForeignKey('subjects.id'),
        nullable=False)
    subject = db.relationship('Subject',
        backref=db.backref('courses',lazy=True))

    def __repr__(self):
        return '<Course %r>' % self.name

class CourseSchema(ma.Schema):
    id = fields.Integer()
    name = fields.String()
    course_code = fields.Integer()
    description = fields.String()
    subject_id = fields.Integer()