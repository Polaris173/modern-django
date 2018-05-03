from .base import *

SECRET_KEY = env('DJANGO_SECRET_KEY', default='+4&4c53$d97r)l+qugp5!ze)k@bre_2cf_b^!d30&e)pau6^12')

DEBUG = env.bool('DJANGO_DEBUG', default=True)