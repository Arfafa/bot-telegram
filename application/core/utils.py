HTTP_STATUS_CODE = {
    'OK': 200,
    'BAD_REQUEST': 400
}


def get_json(request):
    if not request.is_json:
        raise Exception('Arquivo JSON nao encontrado')

    else:
        return request.get_json()
