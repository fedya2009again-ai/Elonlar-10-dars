from django.db import models


class Advertisement(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=12, decimal_places=2)
    image = models.ImageField(upload_to='advertisements/', blank=True, null=True)
    owner = models.ForeignKey('user.User', on_delete=models.CASCADE)
    favorites = models.ManyToManyField('user.User', related_name='favorite_ads', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title