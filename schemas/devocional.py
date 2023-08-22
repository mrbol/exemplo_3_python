from pydantic import BaseModel
from typing import Optional, List
from model.devocional import Devocional



class DevocionalSchema(BaseModel):
    """ Define como um novo devocional a ser inserido deve ser representado
    """
    referencia: str = "texto"
    versiculo: str = "texto"
    pensamento: str = "texto"
    oracao: str = "texto"


class DevocionalBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no nome do devocional.
    """
    deviconal_id: int = 1


class ListagemDevocionalsSchema(BaseModel):
    """ Define como uma listagem de devocionals será retornada.
    """
    devocionais:List[DevocionalSchema]


def apresenta_devocionais(devocionais: List[Devocional]):
    """ Retorna uma representação do devocional seguindo o schema definido em
        DevocionalViewSchema.
    """
    result = []
    for devocional in devocionais:
        result.append({
            "referencia": devocional.referencia,
            "versiculo": devocional.versiculo,
            "pensamento": devocional.pensamento,
            "oracao": devocional.oracao,
        })

    return {"devocionais": result}


class DevocionalViewSchema(BaseModel):
    """ Define como um devocional será retornado: devocional.
    """
    id: int = 1
    referencia: str = "texto"
    versiculo: str = "texto"
    pensamento: str = "texto"
    oracao: str = "texto"

class DevocionalDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    mesage: str
    nome: str

def apresenta_devocional(devocional: Devocional):
    """ Retorna uma representação do devocional seguindo o schema definido em
        DevocionalViewSchema.
    """
    return {
        "id": devocional.id,
        "referencia": devocional.referencia,
        "versiculo": devocional.versiculo,
        "pensamento": devocional.pensamento,
        "oracao": devocional.oracao,
    }
