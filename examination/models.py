from djongo import models
from django.utils import timezone


# QUESTION MODELS
class TypeFourQuestion(models.Model):
    TYPES = (
        ('sol', 'Solicits'),
        ('wil', 'Willingness')
    )
    text = models.CharField(help_text='Question text', max_length=150)
    optionA = models.TextField(help_text='Option A', max_length=150)
    optionB = models.TextField(help_text='Option B', max_length=150)
    question_type = models.CharField(max_length=3, choices=TYPES)

    class Meta:
        abstract = True

    def __str__(self):
        return self.text


# SECTION MODELS
class SectionFour(models.Model):
    name = models.CharField(max_length=100)
    questions = models.ArrayField(TypeFourQuestion)

    class Meta:
        verbose_name = 'Model 4'
        verbose_name_plural = 'Model 4'

    def __str__(self):
        return self.name


# EXAM MODEL
class Exam(models.Model):
    name = models.CharField(max_length=100)
    scheduled_on = models.DateTimeField(default=timezone.now())
    # scheduled_by
    section_four = models.ForeignKey(SectionFour, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
