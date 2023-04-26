# **Ristto App**

*v 0.1.0*

## Description

The initial idea of this app is for each instance of the project to be hosted on the restaurant's server (but we as the service provider could also host the app on our side). The point is that one Django project won't handle many different restaurants (at least for the time being).

The Ristto App will be a facility for the restaurants to deal with the clients requests at a given moment. Each client, upon entering the restaurant, will receive a card with a QR Code (that will be registered to it's name upon entry). By scanning the QR Code, each client will be able to access the menu and also request any given item.

However, the app should also allow the client to only see the menu and make the request to a waiter at the spot.

When asking the bill, the waiter will be able to handle each client an individual bill, with each client's items to be paid.

What should we implement?

- Be able to split an item between different people when making a request
- Split the bill between people at the end
- When first accessing the menu and making a request, save the selected table for later requests
- Client registration to a set QR code card on the restaurant entry

## Development Process

### Internal Apps

#### `Clients`

This app will handle all the logic related to a client's actions within the restaurant.

