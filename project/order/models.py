from django.db import models

STATUS = {
    "tan": "Tanlangan",
    "jar": "Jarayonda",
    "bekor": "Bekor qilingan",
    "yet": "Yetkazib berilgan",
}


class Order(models.Model):
    user = models.ForeignKey("user.User", on_delete=models.SET_NULL, null=True)
    created = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    status = models.CharField(max_length=10, choices=STATUS, default="tan")
    address = models.CharField(max_length=255, blank=True)

    def get_total(self):
        return sum(item.get_price() for item in self.items.select_related("product"))

    def __str__(self):
        return f"Buyurtma #{self.pk} - {self.user} ({self.get_status_display()})"


class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey("main.Advertisement", on_delete=models.CASCADE)
    quantity = models.SmallIntegerField(default=0)

    def get_price(self):
        return self.product.price * self.quantity

    def __str__(self):
        return f"{self.product} x {self.quantity}"
