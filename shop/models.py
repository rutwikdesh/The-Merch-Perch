from django.db import models
from django.db.models.fields import AutoField

class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=300, default="blank")
    pub_date = models.DateField()
    image = models.ImageField(upload_to = "shop/images", default = "")

    def __str__(self) -> str:
        return self.product_name

class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    desc = models.CharField(max_length=400, default="")

    def __str__(self) -> str:
        return self.name

class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=4000)
    name = models.CharField(max_length=70)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=100)
    state=models.CharField(max_length=111, default="")
    city = models.CharField(max_length=100)
    phone = models.CharField(max_length=100, default="")

    def __str__(self) -> str:
        return self.name
