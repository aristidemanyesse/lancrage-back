
import datetime
from dateutil.easter import *

def form_to_model(modelform, suffix = 'Form'):
    if suffix and modelform.endswith(suffix):
        return modelform[:-len(suffix)]
    return modelform



def is_ferie(date):
    day = date.day
    month = date.month
    year = date.year

    #samedi et dimanche
    if date.weekday() == 0 or date.weekday() == 6: return True #

    ## dates fériées fixes
    if day == 1 and month == 1 : return True # 1er janvier
    if day == 1 and month == 5: return True # 1er mai
    if day == 8 and month == 5: return True # 8 mai
    if day == 7 and month == 8: return True # 7 Aout
    if day == 15 and month == 8: return True # 15 aout
    if day == 1 and month == 11: return True # 1 novembre
    if day == 15 and month == 11: return True # 15 novembre
    if day == 25 and month == 12: return True # 25 décembre

    ##fetes religieuses mobiles
    easter_day = easter(year)

    if easter_day.day == day and easter_day.month == month: return True  # Pâques

    new_day = easter_day + datetime.timedelta(days=1)
    if new_day.day == day and new_day.month == month: return True  # Lundi de Pâques

    new_day = easter_day + datetime.timedelta(days=40)
    if new_day.day == day and new_day.month == month: return True  # Ascension

    new_day = easter_day + datetime.timedelta(days=50)
    if new_day.day == day and new_day.month == month: return True  # Pentecote

    new_day = easter_day + datetime.timedelta(days=51)
    if new_day.day == day and new_day.month == month: return True  # Lundi de Pentecote
