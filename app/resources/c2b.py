from main import api,Resource,fields

ns_c2b = api.namespace('c2b', description="MPESA c2b")

@ns_c2b.route('')
class C2b(Resource):
    pass