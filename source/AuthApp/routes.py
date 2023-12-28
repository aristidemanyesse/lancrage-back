
from .schemas import *
import graphene


class AuthAppQuery(object):
    search_employe            = EmployeType.ListField(action=graphene.String(default_value="search_employe"))

    
class AuthAppMutation(object)   : 
    create_employe            = EmployeType.CreateField()
    update_employe            = EmployeType.UpdateField()