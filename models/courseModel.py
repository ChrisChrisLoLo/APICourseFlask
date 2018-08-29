from app import db

class Faculty(db.Model):
    """Class that represents the Faculty table."""

    __tablename__ = 'faculty'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255),unique=True,nullable=False)

    def __repr__(self):
        return '<Faculty %r>' % self.name

class Subject(db.Model):
    """Class that represents the Subject table."""

    __tablename__ = 'subject'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120),unique=True,nullable=False)
    subject_code = db.Column(db.String(6),unique=True,nullable=False)

    faculty_id = db.Column(db.Integer, db.ForeignKey('faculty.id'),
        nullable=False)
    faculty = db.relationship('Faculty',
        backref=db.backref('subjects',lazy=True))

    def __repr__(self):
        return '<Subject %r>' % self.name

class Course(db.Model):
    """Class that represents the Course table."""

    __tablename__ = 'course'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120),unique=True,nullable=False)
    number_code = db.Column(db.Integer,nullable=False)
    description = db.Column(db.String(1600))


    subject_id = db.Column(db.Integer, db.ForeignKey('subject.id'),
        nullable=False)
    subject = db.relationship('Subject',
        backref=db.backref('courses',lazy=True))

    def __repr__(self):
        return '<Course %r>' % self.name