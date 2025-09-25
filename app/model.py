import pickle
from pathlib import Path
from .schemas import PatientData

MODEL_PATH = Path(__file__).parent.parent / "models/outlier_detector_v1.pkl"

class Model:
    def __init__(self, model_path: Path):
        if model_path.exists():
            with open(model_path, "rb") as f:
                self.model = pickle.load(f)
        else:
            print(f"AVISO: Modelo não encontrado em {model_path}. Usando um modelo de simulação.")
            self.model = None

    def predict(self, patient_data: PatientData) -> bool:
        if not self.model:
            # Lógica de simulação se o arquivo .pkl não for encontrado
            if patient_data.nivel_glicose > 140 or patient_data.pressao_sistolica > 140:
                return True # Simula um outlier
            return False # Simula um não-outlier

        # Transforme os dados de entrada no formato que seu modelo espera
        input_data = [[
            patient_data.idade,
            patient_data.nivel_glicose,
            patient_data.pressao_sistolica,
            patient_data.pressao_diastolica,
            int(patient_data.historico_familiar)
        ]]

        # Faça a predição (Ex: -1 para outlier, 1 para não-outlier)
        prediction = self.model.predict(input_data)
        is_outlier = bool(prediction[0] == -1)
        return is_outlier

# Cria uma instância única do modelo para ser usada pela API
model_instance = Model(MODEL_PATH)