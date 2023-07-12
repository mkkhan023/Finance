import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'finance_project.settings')

import django
django.setup()

import random
from registration_app.models import AccessRecords, Webpage, Topic, User
from faker import Faker

fakegen = Faker()

topics = ['Search', 'Social', 'News', 'Games', 'Market']

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save
    return t

def populate(N=5):

    for entry in range(N):

        top = add_topic()

        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()
        fake_fname = fakegen.first_name()
        fake_lname = fakegen.last_name()
        fake_mail = fakegen.email()


        
        webpg = Webpage.objects.get_or_create(topic=top, url=fake_url, name=fake_name)[0]

        acc_rec = AccessRecords.objects.get_or_create(name=webpg, date=fake_date)[0]

        user = User.objects.get_or_create(ffname=fake_fname, l_name=fake_lname, e_mail=fake_mail)[0]

if __name__=='__main__':
    print('Populating Scripts')
    populate(25)
    print('Complete!')