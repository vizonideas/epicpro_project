from django.utils.crypto import get_random_string

# Create a random SECRET_KEY hash to put it in the main settings.
chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
print get_random_string(50, chars)