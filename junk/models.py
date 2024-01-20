from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=200)
    image = models.FileField(upload_to="uploads/courses/")

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    
    def __str__(self):
        if self.name:
            return self.name
        else:
            person = self.person_set.first()
            return person.last_name if person else "Unknown"

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


class Loop(models.Model):
    date  = models.DateField("date published")
    wage = models.IntegerField()
    bags = models.FloatField()
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    courses  = models.ManyToManyField(Course, through="LoopCourse")

    def __str__(self):
        return self.date.strftime("%m-%d-%Y")


class LoopCourse(models.Model):
    loop = models.ForeignKey(Loop, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)


