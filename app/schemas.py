# model-LLM/app/schemas.py
# (VERSÃO CORRIGIDA COM AS 22 FEATURES)

from pydantic import BaseModel
from typing import Optional

class PatientData(BaseModel):
    # Baseado na sua imagem (os 22 campos de input)
    idade: int
    sexo: Optional[str] = None
    escolaridade: Optional[str] = None
    renda_familiar_sm: Optional[str] = None
    atividade_fisica: Optional[str] = None
    consumo_alcool: Optional[str] = None
    tabagismo_atual: Optional[bool] = None
    qualidade_dieta: Optional[str] = None
    qualidade_sono: Optional[str] = None
    nivel_estresse: Optional[str] = None
    suporte_social: Optional[str] = None
    historico_familiar_dc: Optional[bool] = None
    acesso_servico_saude: Optional[str] = None
    aderencia_medicamento: Optional[str] = None
    consultas_ultimo_ano: Optional[int] = None
    imc: Optional[float] = None
    pressao_sistolica_mmHg: Optional[int] = None
    pressao_diastolica_mmHg: Optional[int] = None
    glicemia_jejum_mg_dl: Optional[int] = None
    colesterol_total_mg_dl: Optional[int] = None
    hdl_mg_dl: Optional[int] = None
    triglicerides_mg_dl: Optional[int] = None

class ClassificationResponse(BaseModel):
    is_outlier: bool
    # Se o seu modelo também retornar confiança, adicione-a aqui
    # confidence: Optional[float] = None