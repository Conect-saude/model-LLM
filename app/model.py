from joblib import load
from pathlib import Path
from .schemas import PatientData

MODEL_PATH = Path("/app/models/modelo_regressao_linear.joblib")

class Model:
    def __init__(self, model_path: Path):
        print(f"Tentando carregar modelo de: {model_path}")
        print(f"O arquivo existe? {model_path.exists()}")
        if model_path.exists():
            print("Carregando modelo...")
            self.model = load(model_path)
            print("Modelo carregado com sucesso!")
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

        # Faça a predição usando o modelo de regressão linear
        prediction = self.model.predict(input_data)
        
        # Define um limiar para considerar como outlier (pode ser ajustado conforme necessário)
        threshold = 0.5
        is_outlier = bool(prediction[0] > threshold)
        
        return is_outlier

# Cria uma instância única do modelo para ser usada pela API
model_instance = Model(MODEL_PATH)