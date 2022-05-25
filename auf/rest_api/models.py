from django.db import models

class BBooks(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    year = models.IntegerField(default=20)

    def __str__(self):
        return self.title


class Album(models.Model):
    album_name = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)

class Track(models.Model):
    album = models.ForeignKey(Album, related_name='tracks', on_delete=models.CASCADE)
    order = models.IntegerField()
    title = models.CharField(max_length=100)
    duration = models.IntegerField()

    class Meta:
        unique_together = ['album', 'order']
        ordering = ['order']

    def __str__(self):
        return '%d: %s' % (self.order, self.title)

class Pep(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name

class Experience(models.Model):
    title = models.ForeignKey(Pep, related_name='pep', on_delete=models.CASCADE)
    organization = models.CharField(max_length=100)
    duration = models.IntegerField()

    # class Meta:
    #     unique_together = ['first_name']

    def __str__(self):
        return self.organization

# Selected_related and prtfecrure_related
class Producer(models.Model):
    title = models.CharField(max_length=200)
    productions = models.ManyToManyField('Production', related_name='productions', blank=True)

    def __str__(self):
        return self.title

class Production(models.Model):
    title = models.CharField(max_length=200)
    producers = models.ManyToManyField('Producer', related_name='producers', blank=True,default='Unknown')

    def __str__(self):
        return self.title