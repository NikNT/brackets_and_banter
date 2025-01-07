from django.db import models


class WishList(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    priority = models.CharField(
        choices=[("High", "High"), ("Medium", "Medium"), ("Low", "Low")],
        default="Medium",
        max_length=10,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_at']
