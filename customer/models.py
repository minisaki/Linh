from django.db import models
from user.models import MyUser
from products.models import Products

# Create your models here.

class TextReport(models.Model):
    tittle = models.CharField(max_length=500, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.tittle


class Report(models.Model):
    user_report = models.ForeignKey(MyUser, on_delete=models.CASCADE,
                                  related_name="user_report")
    user_get_report = models.ForeignKey(MyUser, on_delete=models.CASCADE,
                                  related_name="user_get_report")
    content_report = models.ManyToManyField(TextReport,
                                  related_name="text_report", null=True)
    text = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('user_report', 'user_get_report')
        index_together = ('user_report', 'user_get_report')

class Follow(models.Model):
    user_follow = models.ForeignKey(MyUser, on_delete=models.CASCADE,
                                    related_name="user_follow")
    user_get_follow = models.ForeignKey(MyUser, on_delete=models.CASCADE,
                                        related_name="user_get_follow")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('user_follow', 'user_get_follow')
        index_together = ('user_follow', 'user_get_follow')