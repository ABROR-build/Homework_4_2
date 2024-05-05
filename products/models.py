from django.db import models


class Categories(models.Model):
    name = models.CharField(max_length=500)

    class Meta:
        db_table = 'Categories'

    def __str__(self):
        return self.name


class Products(models.Model):
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    model = models.CharField(max_length=200)
    manufactured_by = models.CharField(max_length=600)
    description = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    price = models.FloatField()

    class Meta:
        db_table = 'Products'

    def __str__(self):
        return f"{self.category.name} {self.model}"
