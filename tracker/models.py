import random
import string

from django.core.exceptions import ValidationError
from django.db import models

from django.db import models


class Employee(models.Model):
    def create_login(self):
        login_letters = [self.first_name[0:3].lower(), self.last_name[0:3].lower()]
        login = "".join(login_letters)
        if Employee.objects.filter(login=login).exists():
            random_letter = random.choice(string.ascii_lowercase)
            login_letters = [self.first_name[0:2].lower(), random_letter, self.last_name[0:3].lower()]
            login = "".join(login_letters)
            return login
        return login

    def create_email(self):
        return f"{self.login}@mp.com"

    first_name = models.CharField(max_length=64, null=False)
    last_name = models.CharField(max_length=64, null=False)
    login = models.CharField(max_length=28)
    email = models.EmailField(max_length=28)
    birth_date = models.DateField()
    address_street = models.CharField(max_length=128, null=False)
    address_city = models.CharField(max_length=64, null=False)
    address_postal = models.CharField(max_length=12)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Location(models.Model):
    city = models.CharField(max_length=64, null=False)
    building_id = models.CharField(max_length=28, null=False)

    def __str__(self):
        return f'{self.building_id} ({self.city})'


class Position(models.Model):
    APPRENTICE = 1
    INTERN = 2
    ASSOCIATE = 3
    SPECIALIST = 4
    TEAM_LEADER = 5
    MANAGER = 6
    DIRECTOR = 7
    LEVEL_CHOICES = [
        (APPRENTICE, 'Apprentice'),
        (INTERN, 'Intern'),
        (ASSOCIATE, 'Associate'),
        (SPECIALIST, 'Specialist'),
        (TEAM_LEADER, 'Team Leader'),
        (MANAGER, 'Manager'),
        (DIRECTOR, 'Director')
    ]

    level = models.IntegerField(choices=LEVEL_CHOICES)
    job_title = models.CharField(max_length=64)

    def __str__(self):
        return f'(L{self.level}) {self.job_title}'


class Contract(models.Model):
    UNLIMITED = 'UNL'
    LIMITED = 'LTD'
    INTERNSHIP = 'INT'
    APPRENTICESHIP = 'APR'
    CONTRACT_TYPES = [
        (UNLIMITED, 'Unlimited'),
        (LIMITED, 'Limited'),
        (INTERNSHIP, 'Internship'),
        (APPRENTICESHIP, 'Apprenticeship')
    ]

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.PROTECT)
    position = models.ForeignKey(Position, on_delete=models.PROTECT)
    # deletion: try/except
    # try:
    # # DELETE STUFF
    # except ProtectedError:
    # # CUSTOM MESSAGE
    start_date = models.DateField()
    end_date = models.DateField(default=None, null=True, blank=True)
    contract_type = models.CharField(max_length=28, choices=CONTRACT_TYPES, null=False)
    working_hours = models.DecimalField(decimal_places=2, max_digits=4)
    annual_salary = models.DecimalField(decimal_places=2, max_digits=12)


class LeaveOfAbsence(models.Model):

    class LoaType(models.TextChoices):
        MATERNITY_LEAVE = 'MAT'
        PATERNITY_LEAVE = 'PAT'
        SICK_LEAVE = 'SCK'
        UNPAID_LEAVE = 'UNP'
        UNEXCUSED = 'UEX'

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    leave_type = models.CharField(max_length=28, choices=LoaType.choices)
    leave_start = models.DateField()
    leave_end = models.DateField(default=None)
