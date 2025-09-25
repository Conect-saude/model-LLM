from pydantic import BaseModel

class PatientData(BaseModel):
    idade: int
    nivel_glicose: float
    pressao_sistolica: int
    pressao_diastolica: int
    historico_familiar: bool

class ClassificationResponse(BaseModel):
    is_outlier: bool