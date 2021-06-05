from django.db import models

from django.db import models


class Employee(models.Model):
    def create_login(self):
        login_letters = [self.first_name[0:3].lower(), self.last_name[0:3].lower()]
        return "".join(login_letters)

    def create_email(self):
        return f"{self.login}@mp.com"

    first_name = models.CharField(max_length=64, null=False)
    last_name = models.CharField(max_length=64, null=False)
    login = models.CharField(max_length=28, default=create_login)
    email = models.EmailField(default=create_email)
    birth_date = models.DateField()
    address_street = models.CharField(max_length=128, null=False)
    address_city = models.CharField(max_length=64, null=False)
    address_postal = models.CharField(max_length=12)
    is_active = models.BooleanField(default=True)


class Location(models.Model):
    city = models.CharField(max_length=64, null=False)
    building_id = models.CharField(max_length=28, null=False)


class Position(models.Model):
    class Levels(models.IntegerChoices):
        APPRENTICE = 1
        INTERN = 2,
        ASSOCIATE = 3
        SPECIALIST = 4
        TEAM_LEADER = 5
        MANAGER = 6
        DIRECTOR = 7

    # .label to get enum member name

    level = models.IntegerField(choices=Levels.choices)
    annual_salary = models.DecimalField(decimal_places=2, max_digits=12)

    def salary_validation(self):
        if self.level == 1:
            pass
        elif self.level == 2:
            pass
        elif self.level == 3:
            pass
        elif self.level == 4:
            pass
        elif self.level == 5:
            pass
        else:
            pass


class Contract(models.Model):

    class ContractType(models.TextChoices):
        UNLIMITED = 'UNL'
        LIMITED = 'LTD'
        INTERNSHIP = 'INT'
        APPRENTICESHIP = 'APR'

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.PROTECT)
    position = models.ForeignKey(Position, on_delete=models.PROTECT)
    # deletion: try/except
    # try:
    # # DELETE STUFF
    # except ProtectedError:
    # # CUSTOM MESSAGE
    hire_date = models.DateField()
    termination_date = models.DateField(default=None)
    contract_type = models.CharField(max_length=28, choices=ContractType.choices)
    working_hours = models.DecimalField(decimal_places=2, max_digits=4)


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
