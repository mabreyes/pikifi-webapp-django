from django.db import models
from django.utils import timezone

GENDER_CHOICES = [
    ('None', 'Select Gender'),
    ('Male', 'Male'),
    ('Female', 'Female'),
]

LEVEL_CHOICES = [
    ('None', 'Select Level'),
    ('Kindergarten', 'Kindergarten'),
    ('Kindergarten A', 'Kindergarten A'),
    ('Kindergarten B', 'Kindergarten B'),
    ('SPED', 'SPED'),
    ('Alternative Reading Class', 'Alternative Reading Class'),
    ('Alternative Tutorial Class', 'Alternative Tutorial Class'),
    ('Grade 1', 'Grade 1'),
    ('Grade 2', 'Grade 2'),
    ('Grade 3', 'Grade 3'),
    ('Grade 4', 'Grade 4'),
    ('Grade 5', 'Grade 5'),
    ('Grade 6', 'Grade 6'),
    ('Grade 7', 'Grade 7'),
    ('Grade 7 (ALS)', 'Grade 7 (ALS)'),
    ('Grade 7 (Open High)', 'Grade 7 (Open High)'),
    ('Grade 8', 'Grade 8'),
    ('Grade 8 (ALS)', 'Grade 8 (ALS)'),
    ('Grade 8 (Open High)', 'Grade 8 (Open High)'),
    ('Grade 9', 'Grade 9'),
    ('Grade 9 (ALS)', 'Grade 9 (ALS)'),
    ('Grade 9 (Open High)', 'Grade 9 (Open High)'),
    ('Grade 10', 'Grade 10'),
    ('Grade 10 (ALS)', 'Grade 10 (ALS)'),
    ('Grade 10 (Open High)', 'Grade 10 (Open High)'),
    ('Grade 11', 'Grade 11'),
    ('Grade 11 (ALS)', 'Grade 11 (ALS)'),
    ('Grade 11 (Open High)', 'Grade 11 (Open High)'),
    ('Grade 12', 'Grade 12'),
    ('Grade 12 (ALS)', 'Grade 12 (ALS)'),
    ('Grade 12 (Open High)', 'Grade 12 (Open High)'),
    ('First Year College', 'First Year College'),
    ('Second Year College', 'Second Year College'),
    ('Third Year College', 'Third Year College'),
    ('Fourth Year College', 'Fourth Year College'),
]

PROMOTION_CHOICES = [
    ('None', 'Select Status'),
    ('Graduated', 'Graduated'),
    ('Waiting for Accreditation and Equivalency Test Result',
     'Waiting for Accreditation and Equivalency Test Result'),
    ('Recommended for Philippine Educational Placement Test',
     'Recommended for Philippine Educational Placement Test'),
    ('Retained', 'Retained'),
    ('Retained; Active', 'Retained; Active'),
    ('Retained; Inactive', 'Retained; Inactive'),
    ('Promoted', 'Promoted'),
    ('Promoted (Status Quo)', 'Promoted (Status Quo)'),
    ('Promoted to Kindergarten', 'Promoted to Kindergarten'),
    ('Promoted to Kindergarten A', 'Promoted to Kindergarten B'),
    ('Promoted to Kindergarten A', 'Promoted to Kindergarten B'),
    ('Promoted to Grade 1', 'Promoted to Grade 1'),
    ('Promoted to Grade 2', 'Promoted to Grade 2'),
    ('Promoted to Grade 3', 'Promoted to Grade 3'),
    ('Promoted to Grade 4', 'Promoted to Grade 4'),
    ('Promoted to Grade 5', 'Promoted to Grade 5'),
    ('Promoted to Grade 6', 'Promoted to Grade 6'),
    ('Promoted to Grade 7', 'Promoted to Grade 7'),
    ('Promoted to Grade 8', 'Promoted to Grade 8'),
    ('Promoted to Grade 9', 'Promoted to Grade 9'),
    ('Promoted to Grade 10', 'Promoted to Grade 10'),
    ('Promoted to Grade 11', 'Promoted to Grade 11'),
    ('Promoted to Grade 12', 'Promoted to Grade 12'),
    ('Promoted to First Year College', 'Promoted to First Year College'),
    ('Promoted to Second Year College', 'Promoted to Second Year College'),
    ('Promoted to Third Year College', 'Promoted to Third Year College'),
    ('Promoted to Fourth Year College', 'Promoted to Fourth Year College'),
]

COURSE_CHOICES = [
    ('None', 'None')
]


class StudentInfo(models.Model):
    profile_image = models.ImageField(
        upload_to='uploads/%Y/%m/%d/', default='default_none.png')
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    family_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    gender = models.CharField(
        max_length=100, choices=GENDER_CHOICES, default='None')
    level = models.CharField(
        max_length=100, default='None', choices=LEVEL_CHOICES)
    section = models.CharField(max_length=100, default='Not Applicable')
    course = models.CharField(
        max_length=100, default='None', choices=COURSE_CHOICES)
    school_last_attended = models.CharField(max_length=200, default='None')
    school_current = models.CharField(max_length=200, default='None')
    date_ikp_enrollment = models.DateField(default=timezone.now)
    sponsors_name = models.CharField(max_length=100, default='None')
    student_bio = models.TextField(default='Add a description')
    educational_status = models.CharField(max_length=100,
                                          default='None', choices=PROMOTION_CHOICES)
    created_date = models.DateTimeField(default=timezone.now)
