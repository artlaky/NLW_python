from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse

class TagCreatorView:
    '''
        responsability for interacting with HTPP
    '''

    def validade_and_create(self, http_request: HttpRequest) -> HttpResponse:
        body= http_request.body
        product_code = body["product_code"]

        # logica de regra de negocio
        print("Estou na minha view")
        print(product_code)
        # retorno HTPP
        return HttpResponse(status_code=200, body={"Hello": "world"})
