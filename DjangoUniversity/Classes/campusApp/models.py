from django.db import models

#Adding ability to input campus selections
class UniversityCampus(models.Model):
    Campus_name = models.CharField(max_length=60, default="", blank=True, null=False)
    State = models.CharField(max_length=2, default="", blank=True, null=False)
    Campus_ID = models.IntegerField(default="", blank=True, null=False)

    object = models.manager
#Adding return of inputted campus information
    def __str__(self):
        display_campus = '{0.Campus_name}: {0.Campus_ID}'
        return display_campus.format(self)

    class Meta:
        verbose_name_plural = "University Campus"

