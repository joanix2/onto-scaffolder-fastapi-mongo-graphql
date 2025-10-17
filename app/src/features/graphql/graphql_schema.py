import strawberry
from app.src.features.t_box.query import TBoxQuery
from app.src.features.t_box.mutation import TBoxMutation
from app.src.features.a_box.mutation import ABoxMutation
from app.src.features.a_box.query import ABoxQuery
from app.src.features.template.query import TemplateQuery
from app.src.features.template.mutation import TemplateMutation
from app.src.features.model2text.query import Model2TextQuery
from app.src.features.model2text.mutation import Model2TextMutation

@strawberry.type
class Query(TBoxQuery, ABoxQuery, TemplateQuery, Model2TextQuery):
    pass
Model2TextMutation
@strawberry.type
class Mutation(TBoxMutation, ABoxMutation, TemplateMutation, Model2TextMutation):
    pass

schema = strawberry.Schema(query=Query, mutation=Mutation)