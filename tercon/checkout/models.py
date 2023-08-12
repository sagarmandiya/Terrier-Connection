from django.db import models
from django.contrib.auth.models import User

class Order(models.Model):
    # PLANS = (
    #     ('plan_F5eyGdYCvZPtON', 'Monthly - £24.99'),
    #     ('plan_F5ey2nnZwy5v8Q', '3 Months - £49.99'),
    #     ('price_1Naq9OJqwQehDf1DlaD7TCtL', '6 Months - £74.99'),
    #     )
    PLANS = (
        ('price_1NaqCpJqwQehDf1D2fgPtCRl', 'Monthly - £24.99'),
        ('price_1Nbt7BJqwQehDf1DvXF27HSf', '3 Months - £49.99'),
        ('price_1Naq9OJqwQehDf1DlaD7TCtL', '6 Months - £74.99'),
        )
    plans = models.CharField(choices=PLANS, default='price_1Naq9OJqwQehDf1DlaD7TCtL', blank=False, max_length=100)
    full_name = models.CharField(max_length=50, blank=False)
    phone_number = models.CharField(max_length=20, blank=False)
    country = models.CharField(max_length=40, blank=False)
    postcode = models.CharField(max_length=20, blank=True)
    town_or_city = models.CharField(max_length=40, blank=False)
    street_address1 = models.CharField(max_length=40, blank=False)
    street_address2 = models.CharField(max_length=40, blank=False)
    county = models.CharField(max_length=40, blank=False)
    date = models.DateField()
    
    def __str__(self):
        return "{0}-{1}-{2}".format(self.id, self.date, self.full_name)

class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    plan = models.CharField(max_length=255)
    customer_id = models.CharField(max_length=255)
    