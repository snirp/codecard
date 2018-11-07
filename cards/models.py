from django.db import models
from django.contrib.auth.models import User
from ordered_model.models import OrderedModel


class Card(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    source = models.URLField()
    starred = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return self.title


class Stack(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    starred = models.ManyToManyField(User, blank=True)
    cards = models.ManyToManyField(
        Card,
        through='StackCard',
        through_fields=('stack', 'card'),
    )

    def __str__(self):
        return self.name


class StackCard(OrderedModel):
    stack = models.ForeignKey(Stack, on_delete=models.CASCADE)
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    order_with_respect_to = 'stack'

    class Meta:
        unique_together = ('stack', 'card')

    def __str__(self):
        return self.card.__str__()


class Question(models.Model):
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    question = models.TextField()
    pub_date = models.DateTimeField('date published')
    explanation = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.question


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.CharField(max_length=200)
    correct = models.BooleanField(default=False)

    def __str__(self):
        return self.choice

