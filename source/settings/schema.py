import graphene
from graphene_django_extras import all_directives
from AuthApp.routes import AuthAppMutation, AuthAppQuery
from HotelApp.routes import HotelAppMutation, HotelAppQuery
from ReservationApp.routes import ReservationAppMutation, ReservationAppQuery


class RootQuery(
    HotelAppQuery,
    ReservationAppQuery,
    AuthAppQuery,
    graphene.ObjectType):
    pass


class RootMutations(
    HotelAppMutation,
    ReservationAppMutation,
    AuthAppMutation,
    graphene.ObjectType
):
    pass


schema = graphene.Schema(query=RootQuery, mutation=RootMutations, directives=all_directives)
