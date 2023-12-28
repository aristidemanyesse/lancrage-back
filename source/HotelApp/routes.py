
from .schemas import *
import graphene


class HotelAppQuery(object):
    search_pack               = PackType.ListField(action=graphene.String(default_value="search_pack"))
    search_activity           = ActivityType.ListField(action=graphene.String(default_value="search_officine_pack"))
    search_category_option    = CategoryOptionType.ListField(action=graphene.String(default_value="search_ligne_pack"))
    search_option             = OptionType.ListField(action=graphene.String(default_value="search_reponse"))

    
class HotelAppMutation(object)   : 
    create_pack               = PackType.CreateField()
    update_pack               = PackType.UpdateField()
    
    create_activity           = ActivityType.CreateField()
    update_activity           = ActivityType.UpdateField()
    
    create_category_option    = CategoryOptionType.CreateField()
    update_category_option    = CategoryOptionType.UpdateField()
    
    create_option             = OptionType.CreateField()
    update_option             = OptionType.UpdateField()