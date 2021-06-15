from djongo import models
from examination.models import SectionFour


class User(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=150)
    is_blocked = models.BooleanField(default=False)
    ip = models.CharField(max_length=150, help_text='User IP')

    def __str__(self):
        return self.email


class AnswerTemplate(models.Model):
    question_id = models.CharField(max_length=100, help_text='Question Id')
    option = models.IntegerField(max_length=1)

    class Meta:
        abstract = True


class Result(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_submitted = models.BooleanField(default=False)
    answers = models.EmbeddedField(AnswerTemplate)

    def __str__(self):
        return self.user.email
