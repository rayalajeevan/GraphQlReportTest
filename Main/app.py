from fastapi import FastAPI
from starlette.graphql import GraphQLApp
import graphene
from .graphene_services import Query
from  .database import SessionLocal

app=FastAPI()
schema = graphene.Schema()
schema.execute(context_value={'session': SessionLocal()})
app.add_route("/", GraphQLApp(schema=graphene.Schema(query=Query)))