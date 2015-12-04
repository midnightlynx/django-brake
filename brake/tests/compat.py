import django

if django.VERSION >= (1, 7):
    import unittest
else:
    from django.utils import unittest
