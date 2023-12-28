
from .schemas import *
import graphene


class ReservationAppQuery(object):
    search_reservation            = ReservationType.ListField(action=graphene.String(default_value="search_reservation"))

    
class ReservationAppMutation(object)   : 
    create_reservation            = ReservationType.CreateField()
    update_reservation            = ReservationType.UpdateField()