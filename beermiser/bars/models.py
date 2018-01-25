from decimal import Decimal
from django.db import models

class Bar(models.Model):
    name = models.CharField(max_length=256)
    street_address = models.TextField(null=True)
    city = models.CharField(max_length=100, null=True)
    state = models.CharField(max_length=2, null=True)

    @property
    def best_beer(self):
        beers = self.beer_set.all()
        if beers.count() > 0:
            return max(beers, key=lambda beer: beer.alcohol_per_dollar)
        else:
            return None

    def __str__(self):
        return self.name


class Beer(models.Model):
    bar = models.ForeignKey(Bar, on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    # Assuming no beer is going to be served in volume greater than 99.99 ounces.
    fluid_ounces = models.DecimalField(max_digits=4, decimal_places=2)
    # Assuming no beer is going to cost more than $99.99.
    price_usd = models.DecimalField(max_digits=4, decimal_places=2)
    # ABV percentage should be between 0.0 and 99.9. If it's 100%, that's not beer.
    alcohol_by_volume = models.DecimalField(max_digits=3, decimal_places=1)
    updated = models.DateTimeField(auto_now=True)

    @property
    def alcohol_fluid_ounces(self):
        return self.alcohol_by_volume * self.fluid_ounces / Decimal(100.0)

    @property
    def alcohol_per_dollar(self):
        if self.price_usd == Decimal(0.00):
            # Don't want a divide by zero, but if the beer is free then the alcohol
            # per dollar approaches infinity!
            return sys.float_info.max
        return self.alcohol_fluid_ounces / self.price_usd

    def __str__(self):
        return '{0} ({1}% ABV / {2} fl. oz. / ${3} / {4} / {5} fl. oz. alcohol/$)'.format(
                self.name,
                self.alcohol_by_volume,
                self.fluid_ounces,
                self.price_usd,
                self.bar.name,
                self.alcohol_per_dollar
                )
