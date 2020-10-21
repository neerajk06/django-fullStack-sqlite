import os

# Configuring settings for models
os.environ.setdefault('DJNANGO_SETTINGS_MODULE', 'my_django_stuff.settings')

import django
django.setup()

# fake population script
import random
from first_project.models import AccessRecord, Webpage, Topic
from faker import Faker

fakegen = Faker()
topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

# N=5 is default param value that can be modified externally
def populate(N=5):

    for entry in range(N):
        # get the topic for the entry
        top = add_topic()

        # create the fake data for that entry
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        # create new webpage entry
        webpg = Webpage.objects.get_or_create(topic=top, url=fake_url, name=fake_name)[0]

        # create a fake access record for the webpage
        acc_rec = AccessRecord.objects.get_or_create(name=webpg, date=fake_date)[0]

if __name__ == '__man__':
    print("populating script")
    populate(20)
    print("populating complete !")

