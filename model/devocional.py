from sqlalchemy import Column, String, Integer, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from  model import Base


class Devocional(Base):
    __tablename__ = 'devocional'

    id = Column("pk_devocional", Integer, primary_key=True)
    referencia = Column(String(50))
    versiculo = Column(String(1000))
    pensamento = Column(String(1000))    
    oracao = Column(String(1000))
    data_insercao = Column(DateTime, default=datetime.now())

    def __init__(self, referencia:str, versiculo:str, pensamento:str, oracao:str,
                 data_insercao:Union[DateTime, None] = None):
        """
        Cria um Devocional

        Arguments:
            referencia: referencia biblica
            versiculo: texto biblico
            pensamento: pensamento referente ao versiculo
            oracao: oração referente ao versiculo
            data_insercao: data de quando o devocional
        """
        self.referencia = referencia
        self.versiculo = versiculo
        self.pensamento = pensamento
        self.oracao = oracao

        # se não for informada, será o data exata da inserção no banco
        if data_insercao:
            self.data_insercao = data_insercao
