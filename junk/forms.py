from datetime import date
from django import forms
from django.core.exceptions import ValidationError
from django.forms import inlineformset_factory
from .models import Course, Day, Group, Person, Loop

class LoopForm(forms.ModelForm):
    class Meta:
        model = Loop
        exclude = ()


DayFormSet = inlineformset_factory(Day, Loop, form=LoopForm, extra=3)

class DayForm(forms.Form):
    # template_name = "form_courses.html"
    date = forms.DateField(initial=date.today)
    wage = forms.IntegerField()
    bags = forms.FloatField()
    group = forms.ModelChoiceField(
            queryset=Group.objects.all(),
            initial=Group.objects.first())
    courses = forms.ModelMultipleChoiceField(
        template_name="form_courses.html",
        queryset=Course.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    def clean_date(self):
        date = self.cleaned_data["date"]
        if Day.objects.filter(date=date).count() > 0:
            raise ValidationError("This date has already been recorded, update the existing.")
        return date

    def save(self, commit=True):
        date, wage, bags, group, courses = self.cleaned_data.values()
        day = Day(date=date, wage=wage)
        day.save()
        if len(courses) == 1:
            loop = Loop(bags=bags, group=group, course=courses.first(), day=day)
            loop.save()
        else:
            if not bags%len(courses):
                bags = bags/len(courses)
                for course in courses:
                    loop = Loop(bags=bags, group=group, course=course, day=day)
                    loop.save()
            else:
                b = len(courses)
                for course in courses:
                    print(f"{b=}")
                    loop = Loop(bags=b, group=group, course=course, day=day)
                    loop.save()
                    b = bags % len(courses)


class PlayerForm(forms.ModelForm):

    class Meta:
        model = Person
        fields = "__all__"
        widgets = {
            "last_name": forms.TextInput(
                attrs={
                    "class": ("bg-gray-50 border border-gray-300 "
                              "text-gray-900 text-sm rounded-lg "
                              "focus:ring-blue-500 focus:border-blue-500 "
                              "block w-full p-2.5 dark:bg-gray-700 "
                              "dark:border-gray-600 dark:placeholder-gray-400 "
                              "dark:text-white dark:focus:ring-blue-500 "
                              "dark:focus:border-blue-500"),
                    "placeholder": "Post group name",
                }
            ),
        }
