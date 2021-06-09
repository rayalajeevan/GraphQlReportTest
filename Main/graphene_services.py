import graphene
from pydantic import BaseModel
from graphene_sqlalchemy import SQLAlchemyObjectType,SQLAlchemyConnectionField
from .models import Reports, User
from graphene import relay

class ReportsGrapheneNode(SQLAlchemyObjectType):
    class Meta:
        model = Reports
        interfaces = (relay.Node,)
class Query(graphene.ObjectType):
    print(ReportsGrapheneNode.connection)
    reports= SQLAlchemyConnectionField(ReportsGrapheneNode.connection)

    # def resolve_reports(self, info):
    #     query = ReportsGraphene.get_query(info)
    #     return query.all()