from fastapi import FastAPI
from schemas import PatientData, ClassificationResponse
from model import model_instance

app = FastAPI(
    title="Conecta+Saúde - Serviço de Classificação",
    description="API para detectar pacientes outliers com base em dados clínicos.",
    version="1.0.0"
)

@app.post("/classify", response_model=ClassificationResponse)
def classify_patient(patient_data: PatientData):
    """
    Recebe os dados de um paciente e retorna se ele é classificado como um outlier.
    """
    is_outlier = model_instance.predict(patient_data)
    return {"is_outlier": is_outlier}

@app.get("/")
def health_check():
    return {"status": "ok"}