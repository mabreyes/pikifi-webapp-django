from django.db import models
from django.utils import timezone

from django.contrib.auth.models import AbstractUser


class DatabaseUser(AbstractUser):
    is_viewer = models.BooleanField(default=False)
    is_editor = models.BooleanField(default=False)


class Viewer(models.Model):
    user = models.OneToOneField(
        DatabaseUser, on_delete=models.CASCADE, primary_key=True)


GENDER_CHOICES = [
    ('None', 'Select Gender'),
    ('Male', 'Male'),
    ('Female', 'Female'),
]

LEVEL_CHOICES = [
    ('None', 'Select Level'),
    ('Pre-School', (
        ('Kindergarten', 'Kindergarten'),
        ('Kindergarten A', 'Kindergarten A'),
        ('Kindergarten B', 'Kindergarten B'),
    )),
    ('Alternative/Special Classes', (
        ('SPED', 'SPED'),
        ('Alternative Reading Class', 'Alternative Reading Class'),
        ('Alternative Tutorial Class', 'Alternative Tutorial Class'),
    )),
    ('Grade School', (
        ('Grade 1', 'Grade 1'),
        ('Grade 2', 'Grade 2'),
        ('Grade 3', 'Grade 3'),
        ('Grade 4', 'Grade 4'),
        ('Grade 5', 'Grade 5'),
        ('Grade 6', 'Grade 6'),
    )),
    ('Junior High School', (
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
    )),
    ('Senior High School', (
        ('Grade 11', 'Grade 11'),
        ('Grade 11 (ALS)', 'Grade 11 (ALS)'),
        ('Grade 11 (Open High)', 'Grade 11 (Open High)'),
        ('Grade 12', 'Grade 12'),
        ('Grade 12 (ALS)', 'Grade 12 (ALS)'),
        ('Grade 12 (Open High)', 'Grade 12 (Open High)'),
    )),
    ('College', (
        ('First Year College', 'First Year College'),
        ('Second Year College', 'Second Year College'),
        ('Third Year College', 'Third Year College'),
        ('Fourth Year College', 'Fourth Year College'),
    ))
]

PROMOTION_CHOICES = [
    ('None', 'Select Status'),
    ('General Promotions', (
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
    )),
    ('Pre-School Promotions', (
        ('Promoted to Kindergarten', 'Promoted to Kindergarten'),
        ('Promoted to Kindergarten A', 'Promoted to Kindergarten B'),
        ('Promoted to Kindergarten A', 'Promoted to Kindergarten B'),
    )),
    ('Grade School Promotions', (
        ('Promoted to Grade 1', 'Promoted to Grade 1'),
        ('Promoted to Grade 2', 'Promoted to Grade 2'),
        ('Promoted to Grade 3', 'Promoted to Grade 3'),
        ('Promoted to Grade 4', 'Promoted to Grade 4'),
        ('Promoted to Grade 5', 'Promoted to Grade 5'),
        ('Promoted to Grade 6', 'Promoted to Grade 6'),
    )),
    ('Junior High School Promotions', (
        ('Promoted to Grade 7', 'Promoted to Grade 7'),
        ('Promoted to Grade 8', 'Promoted to Grade 8'),
        ('Promoted to Grade 9', 'Promoted to Grade 9'),
        ('Promoted to Grade 10', 'Promoted to Grade 10'),
    )),
    ('Senior High School Promotions', (
        ('Promoted to Grade 11', 'Promoted to Grade 11'),
        ('Promoted to Grade 12', 'Promoted to Grade 12'),
    )),
    ('College Promotions', (
        ('Promoted to First Year College', 'Promoted to First Year College'),
        ('Promoted to Second Year College', 'Promoted to Second Year College'),
        ('Promoted to Third Year College', 'Promoted to Third Year College'),
        ('Promoted to Fourth Year College', 'Promoted to Fourth Year College'),
    )),
]

COURSE_CHOICES = [
    ('Select Course', 'Select Course'),
    ('Humanities', (
        ('Bachelor of Arts in History (AB History)',
         'Bachelor of Arts in History (AB History)'),
        ('Bachelor of Arts in Philosophy (AB Philosophy)',
         'Bachelor of Arts in Philosophy (AB Philosophy)'),
        ('Bachelor of Fine Arts Major in Industrial Design (BFA)',
         'Bachelor of Fine Arts Major in Industrial Design (BFA)'),
        ('Bachelor of Fine Arts Major in Painting (BFA)',
         'Bachelor of Fine Arts Major in Painting (BFA)'),
        ('Bachelor of Fine Arts Major in Sculpture (BFA)',
         'Bachelor of Fine Arts Major in Sculpture (BFA)'),
        ('Bachelor of Fine Arts Major in Visual Communication (BFA)',
         'Bachelor of Fine Arts Major in Visual Communication (BFA)'),
    )),
    ('Social Sciences', (
        ('Bachelor of Arts in Economics (AB Economics)',
         'Bachelor of Arts in Economics (AB Economics)'),
        ('Bachelor of Science in Economics (BS Economics)',
         'Bachelor of Science in Economics (BS Economics)'),
        ('Bachelor of Arts in Psychology (AB Psychology)',
         'Bachelor of Arts in Psychology (AB Psychology)'),
        ('Bachelor of Science in Psychology (BS Psychology)',
         'Bachelor of Science in Psychology (BS Psychology)'),
        ('Bachelor of Science in Criminology (BS Criminology)',
         'Bachelor of Science in Criminology (BS Criminology)'),
        ('Bachelor of Arts in Political Science (AB Political Science)',
         'Bachelor of Arts in Political Science (AB Political Science)'),
        ('Bachelor of Arts in English (AB English)',
         'Bachelor of Arts in English (AB English)'),
        ('Bachelor of Arts in Linguistics (AB Linguistics)',
         'Bachelor of Arts in Linguistics (AB Linguistics)'),
        ('Bachelor of Arts in Literature (AB Literature)',
         'Bachelor of Arts in Literature (AB Literature)'),
        ('Bachelor of Arts in Anthropology (AB Anthropology)',
         'Bachelor of Arts in Anthropology (AB Anthropology)'),
        ('Bachelor of Arts in Sociology (AB Sociology)',
         'Bachelor of Arts in Sociology (AB Sociology)'),
        ('Bachelor of Arts in Filipino (AB Filipino)',
         'Bachelor of Arts in Filipino (AB Filipino)'),
        ('Bachelor of Science in Forensic Science (BSFS)',
         'Bachelor of Science in Forensic Science (BSFS)'),
        ('Bachelor of Arts in Islamic Studies (AB Islamic Studies)',
         'Bachelor of Arts in Islamic Studies (AB Islamic Studies)'),
    )),
    ('Natural Sciences', (
        ('Bachelor of Science in Environmental Science (BSES)',
         'Bachelor of Science in Environmental Science (BSES)'),
        ('Bachelor of Science in Forestry (BS Forestry)',
         'Bachelor of Science in Forestry (BS Forestry)'),
        ('Bachelor of Science in Fisheries (BSFi)',
         'Bachelor of Science in Fisheries (BSFi)'),
        ('Bachelor of Science in Geology (BS Geology)',
         'Bachelor of Science in Geology (BS Geology)'),
        ('Bachelor of Science in Biology (BS Biology)',
         'Bachelor of Science in Biology (BS Biology)'),
        ('Bachelor of Science in Molecular Biology (BS Molecular Biology)',
         'Bachelor of Science in Molecular Biology (BS Molecular Biology)'),
        ('Bachelor of Science in Physics (BS Physics)',
         'Bachelor of Science in Physics (BS Physics)'),
        ('Bachelor of Science in Applied Physics (BS Applied Physics)',
         'Bachelor of Science in Applied Physics (BS Applied Physics)'),
        ('Bachelor of Science in Chemistry (BS Chemistry)',
         'Bachelor of Science in Chemistry (BS Chemistry)'),
    )),
    ('Formal Sciences', (
        ('Bachelor of Science in Computer Science (BSCS)',
         'Bachelor of Science in Computer Science (BSCS)'),
        ('Bachelor of Science in Information Technology (BSIT)',
         'Bachelor of Science in Information Technology (BSIT)'),
        ('Bachelor of Science in Information Systems (BSIS)',
         'Bachelor of Science in Information Systems (BSIS)'),
        ('Bachelor of Science in Mathematics (BS Mathematics)',
         'Bachelor of Science in Mathematics (BS Mathematics)'),
        ('Bachelor of Science in Applied Mathematics (BS Applied Math)',
         'Bachelor of Science in Applied Mathematics (BS Applied Math)'),
        ('Bachelor of Science in Statistics (BS Stat)',
         'Bachelor of Science in Statistics (BS Stat)'),
    )),
    ('Agriculture', (
        ('Bachelor of Science in Agriculture',
         'Bachelor of Science in Agriculture'),
        ('Bachelor of Science in Agribusiness (BS Agribusiness)',
         'Bachelor of Science in Agribusiness (BS Agribusiness)'),
        ('Bachelor of Science in Agroforestry (BS Agroforestry)',
         'Bachelor of Science in Agroforestry (BS Agroforestry)'),
    )),
    ('Architecture and Design', (
        ('Bachelor of Science in Architecture (BS Architecture)',
         'Bachelor of Science in Architecture (BS Architecture)'),
        ('Bachelor in Landscape Architecture (BLA)',
         'Bachelor in Landscape Architecture (BLA)'),
        ('Bachelor of Science in Interior Design (BS Interior Design)',
         'Bachelor of Science in Interior Design (BS Interior Design)'),
    )),
    ('Business', (
        ('Bachelor of Science in Accountancy (BSA)',
         'Bachelor of Science in Accountancy (BSA)'),
        ('Bachelor of Science in Accounting Technology (BSAcT)',
         'Bachelor of Science in Accounting Technology (BSAcT)'),
        ('Bachelor of Science in Business Administration',
         'Bachelor of Science in Business Administration'),
        ('Bachelor of Science in Business Administration Major in Business Economics (BSBA)',
         'Bachelor of Science in Business Administration Major in Business Economics (BSBA)'),
        ('Bachelor of Science in Business Administration Major in Financial Management (BSBA major in FM)',
         'Bachelor of Science in Business Administration Major in Financial Management (BSBA major in FM)'),
        ('Bachelor of Science in Business Administration Major in Human Resource Development (BSBA major in HRDM)',
         'Bachelor of Science in Business Administration Major in Human Resource Development (BSBA major in HRDM)'),
        ('Bachelor of Science in Business Administration Major in Marketing Management (BSBA major in MM)',
         'Bachelor of Science in Business Administration Major in Marketing Management (BSBA major in MM)'),
        ('Bachelor of Science in Business Administration Major in Operations Management (BSBA major in OM)',
         'Bachelor of Science in Business Administration Major in Operations Management (BSBA major in OM)'),
        ('Bachelor of Science in Bachelor of Science in Hotel and Restaurant Management (BS HRM)',
         'Bachelor of Science in Bachelor of Science in Hotel and Restaurant Management (BS HRM)'),
        ('Bachelor of Science in Entrepreneurship (BS Entrep)',
         'Bachelor of Science in Entrepreneurship (BS Entrep)'),
        ('Bachelor of Science in Office Administration (BSOA)',
         'Bachelor of Science in Office Administration (BSOA)'),
        ('Bachelor of Science in Real Estate Management (BS REM)',
         'Bachelor of Science in Real Estate Management (BS REM)'),
        ('Bachelor of Science in Tourism Management (BSTM)',
         'Bachelor of Science in Tourism Management (BSTM)'),
    )),
    ('Health Sciences', (
        ('Bachelor of Science in Medical Technology (BS Med Tech)',
         'Bachelor of Science in Medical Technology (BS Med Tech)'),
        ('Bachelor of Science in Midwifery (BS Midwifery)',
         'Bachelor of Science in Midwifery (BS Midwifery)'),
        ('Bachelor of Science in Nursing (BSN)',
         'Bachelor of Science in Nursing (BSN)'),
        ('Bachelor of Science in Occupational Therapy (BSOT)',
         'Bachelor of Science in Occupational Therapy (BSOT)'),
        ('Bachelor of Science in Pharmacy (BS Pharmacy)',
         'Bachelor of Science in Pharmacy (BS Pharmacy)'),
        ('Bachelor of Science in Physical Therapy (BSPT)',
         'Bachelor of Science in Physical Therapy (BSPT)'),
        ('Bachelor of Science in Radiologic Technology (BS Rad Tech)',
         'Bachelor of Science in Radiologic Technology (BS Rad Tech)'),
        ('Bachelor of Science in Respiratory Therapy (BSRT)',
         'Bachelor of Science in Respiratory Therapy (BSRT)'),
        ('Bachelor of Science in Speech-Language Pathology',
         'Bachelor of Science in Speech-Language Pathology'),
        ('Bachelor of Science in Sports Science',
         'Bachelor of Science in Sports Science'),
    )),
    ('Education', (
        ('Bachelor in Secondary Education (BSED)',
         'Bachelor in Secondary Education (BSED)'),
        ('Bachelor in Elementary Education (BEED)',
         'Bachelor in Elementary Education (BEED)'),
        ('Bachelor in Secondary Education Major in Technology and Livelihood Education (BSED)',
         'Bachelor in Secondary Education Major in Technology and Livelihood Education (BSED)'),
        ('Bachelor in Secondary Education Major in Biological Sciences (BSED)',
         'Bachelor in Secondary Education Major in Biological Sciences (BSED)'),
        ('Bachelor in Secondary Education Major in English (BSED)',
         'Bachelor in Secondary Education Major in English (BSED)'),
        ('Bachelor in Secondary Education Major in Filipino (BSED)',
         'Bachelor in Secondary Education Major in Filipino (BSED)'),
        ('Bachelor in Secondary Education Major in Mathematics (BSED)',
         'Bachelor in Secondary Education Major in Mathematics (BSED)'),
        ('Bachelor in Secondary Education Major in Islamic Studies (BSED)',
         'Bachelor in Secondary Education Major in Islamic Studies (BSED)'),
        ('Bachelor in Secondary Education Major in Music, Arts, Physical and Health Education (BSED)',
         'Bachelor in Secondary Education Major in Music, Arts, Physical and Health Education (BSED)'),
        ('Bachelor in Secondary Education Major in Physical Sciences (BSED)',
         'Bachelor in Secondary Education Major in Physical Sciences (BSED)'),
        ('Bachelor in Secondary Education Major in Social Studies (BSED)',
         'Bachelor in Secondary Education Major in Social Studies (BSED)'),
        ('Bachelor in Secondary Education Major in Values Education (BSED)',
         'Bachelor in Secondary Education Major in Values Education (BSED)'),
        ('Bachelor in Elementary Education Major in Preschool Education (BEED)',
         'Bachelor in Elementary Education Major in Preschool Education (BEED)'),
        ('Bachelor in Elementary Education Major in Special Education (BEED)',
         'Bachelor in Elementary Education Major in Special Education (BEED)'),
        ('Bachelor of Library and Information Science in the Philippines (BLIS)',
         'Bachelor of Library and Information Science in the Philippines (BLIS)'),
        ('Bachelor of Physical Education (BPE)',
         'Bachelor of Physical Education (BPE)'),
    )),
    ('Engineering', (
        ('Bachelor of Science in Aeronautical Engineering (BS AeroE)',
         'Bachelor of Science in Aeronautical Engineering (BS AeroE)'),
        ('Bachelor of Science in Ceramic Engineering (BSCerE)',
         'Bachelor of Science in Ceramic Engineering (BSCerE)'),
        ('Bachelor of Science in Chemical Engineering (BSChE)',
         'Bachelor of Science in Chemical Engineering (BSChE)'),
        ('Bachelor of Science in Civil Engineering (BSCE)',
         'Bachelor of Science in Civil Engineering (BSCE)'),
        ('Bachelor of Science in Computer Engineering (BSCpE)',
         'Bachelor of Science in Computer Engineering (BSCpE)'),
        ('Bachelor of Science in Electrical Engineering (BSEE)',
         'Bachelor of Science in Electrical Engineering (BSEE)'),
        ('Bachelor of Science in Electronics and Communications Engineering (BSECE)',
         'Bachelor of Science in Electronics and Communications Engineering (BSECE)'),
        ('Bachelor of Science in Geodetic Engineering (BSGE)',
         'Bachelor of Science in Geodetic Engineering (BSGE)'),
        ('Bachelor of Science in Geological Engineering (BSGeoE)',
         'Bachelor of Science in Geological Engineering (BSGeoE)'),
        ('Bachelor of Science in Industrial Engineering (BSIE)',
         'Bachelor of Science in Industrial Engineering (BSIE)'),
        ('Bachelor of Science in Marine Engineering in (BSMarE)',
         'Bachelor of Science in Marine Engineering in (BSMarE)'),
        ('Bachelor of Science in Materials Engineering (BSMatE)',
         'Bachelor of Science in Materials Engineering (BSMatE)'),
        ('Bachelor of Science in Mechanical Engineering (BSME)',
         'Bachelor of Science in Mechanical Engineering (BSME)'),
        ('Bachelor of Science in Metallurgical Engineering (BSMetE)',
         'Bachelor of Science in Metallurgical Engineering (BSMetE)'),
        ('Bachelor of Science in Mining Engineering (BSEM)',
         'Bachelor of Science in Mining Engineering (BSEM)'),
        ('Bachelor of Science in Petroleum Engineering (BSPetE)',
         'Bachelor of Science in Petroleum Engineering (BSPetE)'),
        ('Bachelor of Science in Sanitary Engineering (BSSE)',
         'Bachelor of Science in Sanitary Engineering (BSSE)'),
    )),
    ('Media and Communication', (
        ('Bachelor of Arts in Broadcasting (AB Broadcasting)',
         'Bachelor of Arts in Broadcasting (AB Broadcasting)'),
        ('Bachelor of Arts in Communication (AB Communication)',
         'Bachelor of Arts in Communication (AB Communication)'),
        ('Bachelor of Science in in Development Communication (BS DevComm)',
         'Bachelor of Science in in Development Communication (BS DevComm)'),
        ('Bachelor of Arts in Journalism (AB Journalism)',
         'Bachelor of Arts in Journalism (AB Journalism)'),
        ('Bachelor of Arts in Mass Communication',
         'Bachelor of Arts in Mass Communication'),
    )),
    ('Public Administration', (
        ('Bachelor of Science in Community Development(BS Community Development)',
         'Bachelor of Science in Community Development(BS Community Development)'),
        ('Bachelor of Science in Customs Administration (BSCA)',
         'Bachelor of Science in Customs Administration (BSCA)'),
        ('Bachelor of Science in Foreign Service (BS Foreign Service)',
         'Bachelor of Science in Foreign Service (BS Foreign Service)'),
        ('Bachelor of Science in International Studies (BSIS)',
         'Bachelor of Science in International Studies (BSIS)'),
        ('Bachelor of Public Administration (BPA)',
         'Bachelor of Public Administration (BPA)'),
        ('Bachelor of Science in Public Safety (BSPS)',
         'Bachelor of Science in Public Safety (BSPS)'),
        ('Bachelor of Science in Social Work (BS Social Work)',
         'Bachelor of Science in Social Work (BS Social Work)'),
    )),
    ('Transportation', (
        ('Bachelor of Science in Marine Transportation (BSMT)',
         'Bachelor of Science in Marine Transportation (BSMT)'),
    )),
    ('Nutrition', (
        ('Bachelor of Science in Food Technology (BS Food Tech)',
         'Bachelor of Science in Food Technology (BS Food Tech)'),
        ('Bachelor of Science in Nutrition and Dietetics (BS Nutrition and Dietetics)',
         'Bachelor of Science in Nutrition and Dietetics (BS Nutrition and Dietetics)'),
    )),
]

CIVIL_STATUS_CHOICES = [
    ('None', 'Select Civil Status'),
    ('Married', 'Married'),
    ('Separated', 'Separated'),
    ('Widow/Widower', 'Widow/Widower'),
    ('Solo', 'Solo'),
    ('Common Law', 'Common Law'),
]

CHILD_STATUS_CHOICES = [
    ('None', 'Select Status'),
    ('Orphaned', 'Orphaned'),
]


class StudentInfo(models.Model):
    profile_image = models.ImageField(
        upload_to='uploads/%Y/%m/%d/', default='default_none.png')
    author = models.ForeignKey(
        'ikp_sis.DatabaseUser', on_delete=models.CASCADE)
    family_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    gender = models.CharField(
        max_length=100, choices=GENDER_CHOICES, default='None')
    birthdate = models.DateField(default=timezone.now)
    age = models.CharField(max_length=100)
    address = models.CharField(max_length=500)
    parent_guardian_1 = models.CharField(max_length=100)
    parent_guardian_2 = models.CharField(max_length=100)
    parent_civil_status = models.CharField(
        max_length=100, choices=CIVIL_STATUS_CHOICES, default='None')
    child_status = models.CharField(
        max_length=100, default='None', choices=CHILD_STATUS_CHOICES)
    level = models.CharField(
        max_length=100, default='None', choices=LEVEL_CHOICES)
    section = models.CharField(max_length=100)
    course = models.CharField(
        max_length=100, default='None', choices=COURSE_CHOICES)
    school_last_attended = models.CharField(max_length=200)
    school_current = models.CharField(max_length=200)
    date_ikp_enrollment = models.DateField(default=timezone.now)
    sponsors_name = models.CharField(max_length=100)
    student_bio = models.TextField(max_length=1000)
    educational_status = models.CharField(max_length=100,
                                          default='None', choices=PROMOTION_CHOICES)
    created_date = models.DateTimeField(default=timezone.now)
