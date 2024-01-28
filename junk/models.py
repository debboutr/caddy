from django.db import models

from .validators import validate_bags


class Course(models.Model):
    name = models.CharField(max_length=200)
    image = models.FileField(upload_to="uploads/courses/")

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    
    def __str__(self):
        return self.name.capitalize()

    class Meta:
        ordering = ["-id"]

    def courses(self):
        return Course.objects.filter(loop__in=self.loop_set.all()).distinct()


class Person(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    notes = models.CharField(max_length=200, null=True, blank=True)
    lat = models.CharField(max_length=200, null=True, blank=True)
    lon = models.CharField(max_length=200, null=True, blank=True)
    image = models.FileField(upload_to="uploads/people/", null=True, blank=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.first_name.capitalize()} {self.last_name.capitalize()}'

    def save(self, *args, **kwargs):
        if not self.group:
            group = Group.objects.create(name=self.last_name)
            self.group = group
        super(Person, self).save(*args, **kwargs)


class Day(models.Model):
    date  = models.DateField("caddy date", unique=True)
    wage = models.IntegerField()

    def __str__(self):
        return self.date.strftime("%m-%d-%Y")


class Loop(models.Model):
    bags = models.FloatField(validators=[validate_bags])
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    course  = models.ForeignKey(Course, on_delete=models.CASCADE)
    day = models.ForeignKey(Day, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.group.name.capitalize()} -- {self.id}'

