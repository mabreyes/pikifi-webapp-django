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
    ('Grade 8', 'Grade 8'),
    ('Grade 9', 'Grade 9'),
    ('Grade 10', 'Grade 10'),
    ('Grade 11', 'Grade 11'),
    ('Grade 12', 'Grade 12'),
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
    ('Retained', 'Retained'),
    ('Retained, Inactive', 'Retained, Inactive'),
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
    school_last_attended = models.CharField(max_length=200)
    school_current = models.CharField(max_length=200)
    date_ikp_enrollment = models.DateField()
    sponsors_name = models.CharField(max_length=100)
    student_bio = models.TextField()
    educational_status = models.CharField(max_length=100,
                                          default='None', choices=PROMOTION_CHOICES)
    created_date = models.DateTimeField(default=timezone.now)
