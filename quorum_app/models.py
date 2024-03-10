from django.db import models

class Legislator(models.Model):
    name = models.CharField(max_length=255)

class Bill(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    sponsor = models.ForeignKey(Legislator, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title

class Vote(models.Model):
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE)

class Voteresult(models.Model):
    LEGISLATOR_CHOICES = [(1, 'Yea'), (2, 'Nay')]
    legislator = models.ForeignKey(Legislator, on_delete=models.CASCADE)
    vote = models.ForeignKey(Vote, on_delete=models.CASCADE)
    vote_type = models.IntegerField(choices=LEGISLATOR_CHOICES)
