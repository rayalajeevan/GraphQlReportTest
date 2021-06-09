import graphene
from sqlalchemy.util.langhelpers import group_expirable_memoized_property
from graphene_sqlalchemy import SQLAlchemyObjectType,SQLAlchemyConnectionField
from .models import Reports,Tests, User
from graphene import relay
from sqlalchemy import func

class TestsGrapheneNode(SQLAlchemyObjectType):
    passed=graphene.Int()
    failed=graphene.Int()
    non_attempt=graphene.Int()
    class Meta:
        model = Tests
        interfaces = (relay.Node, )
    def resolve_passed(self,info):
        query=ReportGraphene.get_query(info)
        return query.filter(Reports.test_id==self.test_id,Reports.status=="PASS").count()
    def resolve_failed(self,info):
        query=ReportGraphene.get_query(info)
        return query.filter(Reports.test_id==self.test_id,Reports.status=="FAIL").count()
    def resolve_non_attempt(self,info):
        return 0
    
    
class ReportGraphene(SQLAlchemyObjectType):
    class Meta:
        model = Reports
class UserGraphene(SQLAlchemyObjectType):
    class Meta:
        model = User

class Query(graphene.ObjectType):
    tests=graphene.List(TestsGrapheneNode,start=graphene.Int(),end=graphene.Int(),id=graphene.Int())
    tests_for_charts=SQLAlchemyConnectionField(TestsGrapheneNode.connection)
    
    def resolve_tests(self,info,start=0,end=10,id=None):
        query=TestsGrapheneNode.get_query(info)
        if id:
            return query.filter(Tests.test_id==id)
        return query[start:end]
        
        