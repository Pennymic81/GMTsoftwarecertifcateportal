from django.db import models

class Certificate(models.Model):
    name = models.CharField(max_length=255)
    year_of_graduation = models.PositiveIntegerField()
    certificate_number = models.CharField(max_length=50, unique=True)
    course_of_study = models.CharField(max_length=255)
    certificate_file = models.FileField(upload_to='certificates/')

    def __str__(self):
        return f"{self.name} - {self.certificate_number}"
