

from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from app.src.features.graphql.graphql_schema import schema

app = FastAPI()

# Health check
@app.get("/ping")
def ping():
    return {"message": "pong"}

graphql_app = GraphQLRouter(schema)
app.include_router(graphql_app, prefix="/graphql")
