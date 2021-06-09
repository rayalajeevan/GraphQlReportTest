from fastapi import FastAPI
from graphene.types import schema
from sqlalchemy.orm import query_expression
from starlette.graphql import GraphQLApp
import graphene
from .graphene_services import Query
from  .database import SessionLocal

app=FastAPI()
schema = graphene.Schema(query=Query)

schema.execute(context_value={'session': SessionLocal()})

app.add_route("/", GraphQLApp(schema=schema))
