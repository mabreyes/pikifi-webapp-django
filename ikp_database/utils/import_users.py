import pandas as pd
from ikp_sis.models import StudentInfo
from django.contrib.auth.models import User


def bulk_add_users():
    me = User.objects.get(username='marcreyesph')
    data_all = pd.read_csv('data.csv')
    ctr = len(data_all['family_name'])

    for i in range(ctr):
        new_data = StudentInfo(author=me,
                               family_name=data_all['family_name'][i],
                               first_name=data_all['first_name'][i],
                               gender=data_all['gender'][i],
                               level=data_all['level'][i],
                               educational_status=data_all['educational_status'][i])
        new_data.save()
        print('Currently in {0}: {1}'.format(i, data_all['family_name'][i]))


if __name__ == '__main__':
    bulk_add_users()
