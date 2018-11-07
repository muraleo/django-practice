import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')

import django
django.setup()

# Faker Pop Script
import random
from first_app.models import Topic, Webpage, AccessRecord
from faker import Faker

fakeGen = Faker()
topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    print(Topic.objects.get_or_create(top_name=random.choice(topics)))
    t.save()
    return t

def populate(N=5):
    for entry in range(N):
        # get the topic for the entry
        top = add_topic()

        # create the fake data for the entry
        fake_url = fakeGen.url()
        fake_date = fakeGen.date()
        fake_name = fakeGen.company()

        # create new webpage
        webpg = Webpage.objects.get_or_create(topic=top, name=fake_name, url=fake_url)[0]

        # create a fake access record for that webpage
        acc_rec = AccessRecord.objects.get_or_create(name=webpg, date=fake_date)[0]

if __name__ == "__main__":
    print("populating script!")
    populate(6)
    print("populating complete!")