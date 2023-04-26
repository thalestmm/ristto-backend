from django.db import models
import uuid
import logging

# Create your models here.


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

    def __str__(self) -> str:
        return str(self.id + ' - ' + self.client_name)
    
    def checkin(self, client_name: str):
        logging.log(f"Card {self.id} registered to {client_name}")
        self.client_name = client_name
    
    def checkout(self):
        logging.log(f"Card {self.id} checked out")
        self.client_name = None