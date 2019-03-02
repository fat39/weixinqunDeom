from django.db import models


class QunInfo(models.Model):
    url = models.CharField(max_length=128, null=False)
    title = models.CharField(max_length=128, null=False)
    description = models.CharField(max_length=128, null=False)
    hangye = models.CharField(max_length=32, null=False)
    district = models.CharField(max_length=32, null=False)
    buildTime = models.CharField(max_length=32, null=False)
    tags = models.CharField(max_length=128, null=False)
    weixinhao = models.CharField(max_length=32, null=False)
    imgUrl = models.CharField(max_length=128, null=False)
    imgPath = models.CharField(max_length=128, null=False)

    def __str__(self):
        return "{}:{}".format(self.title,self.url)