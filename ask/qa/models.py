from django.db import models
from django.contrib.auth.models import User


class QuestionManager(models.Manager):
    def new():
        return Question.objects.order_by('added_at')[:5]

    def popular():
        return Question.objects.order_by('rating')


# Create your models here.
class Question(models.Model):
    objects = QuestionManager()
    title = models.CharField(default="", max_length=1024)
    text = models.TextField(default="")
    added_at = models.DateField(null=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    likes = models.ManyToManyField(User, related_name="q_to_likes")

    def __str__(self):
        return self.title

    def get_url(self):
        return "/question/{}/".format(self.id)


class Answer(models.Model):
    text = models.TextField(default="")
    added_at = models.DateField(null=True)
    question = models.ForeignKey(Question, null=True, on_delete=models.SET_NULL)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.text
