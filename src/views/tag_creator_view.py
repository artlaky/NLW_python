from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.controllers.tag_creator_controler import TagCreatorControler

class TagCreatorView:
    '''
        responsability for interacting with HTPP
    '''

    def validade_and_create(self, http_request: HttpRequest) -> HttpResponse:
        tag_creator_controler = TagCreatorControler()
        
        body= http_request.body
        product_code = body["product_code"]

        # logica de regra de negocio
        formatted_response = tag_creator_controler.create(product_code)

        # retorno HTPP
        return HttpResponse(status_code=200, body=formatted_response)
