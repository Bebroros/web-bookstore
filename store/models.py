from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    genre = models.CharField(max_length=255)
    author = models.ForeignKey("Author", on_delete=models.PROTECT, related_name="books")
    price = models.IntegerField()
    popularity = models.IntegerField(default=100)
    publisher = models.ForeignKey("Publisher", on_delete=models.PROTECT, related_name="books")
    year = models.IntegerField()

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name


class Publisher(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name


class User(models.Model):
    email = models.EmailField()
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.username


class Order(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE)
    total = models.IntegerField()
    date = models.DateField()

    def __str__(self):
        return f"{self.pk}: {self.user}"


class OrderItem(models.Model):
    order_id = models.ForeignKey("Order", on_delete=models.CASCADE)
    book_id = models.ForeignKey("Book", on_delete=models.CASCADE)
    total = models.IntegerField()


class CartItem(models.Model):
    book_id = models.ForeignKey("Book", on_delete=models.CASCADE)
    total = models.IntegerField()
    user = models.ForeignKey("User", on_delete=models.CASCADE)
