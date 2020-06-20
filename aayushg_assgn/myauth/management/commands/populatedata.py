import random, names, string

from django.core.management.base import BaseCommand
from myauth.models import UserContacts


class Command(BaseCommand):

    def get_name(self):
        name = names.get_full_name()
        return name


    def get_regid(self):
        #just assumed any number between 1 & 5, as only 5 registered users with passwords added
        final_id = random.randint(1,5)
        return final_id
        

    def get_mobno(self):
        mobno = ""
        mobno += str(random.randint(1,9))
        for i in range(9):
            mobno += str(random.randint(0,9))

        return int(mobno)


    def handle(self, *args, **options):
        records1 = []
        
        for i in range(40):
            
            kwargs1 = {
                'uc_id' : int(i+1),
                'contact_regid' : self.get_regid(),
                'uc_name' : self.get_name(),
                'uc_mobno' : self.get_mobno()
            }

            record1 = UserContacts(**kwargs1)
            records1.append(record1)

        UserContacts.objects.bulk_create(records1)