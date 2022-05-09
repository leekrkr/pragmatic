from django.db import models


class Article(models.Model):

    title = models.CharField(max_length=20, null=True)
    image = models.ImageField(upload_to='project/', null=False)
    description = models.CharField(max_length=200, null=True)

    created_at = models.DateTimeField(auto_new=True)

    def __str__(self):
        return f'{self.pk} : {self.title}'
