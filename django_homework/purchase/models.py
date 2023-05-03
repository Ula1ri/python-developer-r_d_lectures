from django.db import models


# Create your models here.
class Purchase(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    user_id = models.ForeignKey('user.User', on_delete=models.CASCADE)
    book_id = models.ForeignKey('book.Book', on_delete=models.CASCADE)
    date = models.PositiveIntegerField(null=False)

    class Meta:
        db_table = 'purchase'

    def __str__(self):
        return f"{self.id}: {self.user_id} {self.book_id} {self.date}"
