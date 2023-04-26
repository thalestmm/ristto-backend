from django.db import models
import uuid
import logging

# Create your models here.


class ClientSession(models.Model):
    """
    This class will be used to register the time when a new user is registered.
    This will allow for later access to some interesting analytics data.
    """
    entrance_time = models.DateTimeField(auto_now_add=True)
    exit_time = models.DateTimeField(default=None, blank=True, null=True)

    def total_time(self):
        pass


class ClientOrders(models.Model):
    """
    This class will be used to register the orders of a given customer.
    This will allow for later access to some interesting analytics data.
    """
    pass


# TODO: When scanning an unregisterd card, still allow to read the menu but not make any requests
class ClientCard(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    ) # The ID of the card will be used to generate the QR Code
    client_name = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        default=None
    )
    table_number = models.IntegerField(default=None, blank=True, null=True)
    card_is_active = models.BooleanField(default=False) # Only staff will be able to activate a card

    def __str__(self) -> str:
        return str(self.id)
    
    def checkin(self, client_name: str) -> None:
        logging.log(f"Card {self.id} registered to {client_name}")
        self.client_name = client_name
        self.card_is_active = True
    
    def checkout(self) -> None:
        logging.log(f"Card {self.id} checked out")
        self.client_name = None
        self.card_is_active = False