from django.db import models
from django.contrib.auth.models import User

from cards.models import Choice, Card, StackCard


class Profile(models.Model):
    """ Extend user profile """
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.__str__()


class Progress(models.Model):
    """ Track user progress on various stacks """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    progress = models.ForeignKey(StackCard, on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.progress.stack.__str__()

    def save(self, *args, **kwargs):
        # TODO OPTIMIZE:
        # Update prior record rather than replace. 
        # Beware of infinite recursion on save method
        try:
            prior = Progress.objects.get(user=self.user, progress__stack=self.progress.stack)
            if self.progress.order < prior.progress.order:
                # Do not update progress towards earlier cards (no negative progress)
                self.progress = prior.progress
            prior.delete()
        except Progress.DoesNotExist:
            pass
        super().save(*args, **kwargs)

    class Meta:
        ordering = ('user', '-updated',)


class View(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)


class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.choice.__str__()


class Familiarity(models.Model):
    """ De-normalized model to calculate scheduling without additional queries and calculations """
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_view = models.DateTimeField(null=True, blank=True)
    latest_view = models.DateTimeField(null=True, blank=True)
    view_count = models.IntegerField(default=0)
    # total_duration
    answer_count = models.IntegerField(default=0)
    correct_count = models.IntegerField(default=0)
    latest_answer = models.DateTimeField(null=True, blank=True)
    score = models.IntegerField(default=0)  # TODO figure out how to do this
