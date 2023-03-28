from django.db import models

class MyModel(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    @staticmethod
    def search(query):
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM django_migrations WHERE name = %s", [query])
            results = cursor.fetchall()
            return results
