from joblib import load
from pathlib import Path
from schemas import PatientData # Importação corrigida (sem ponto)

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

    # --- CORREÇÃO AQUI ---
    # A função 'predict' deve estar indentada DENTRO da 'class Model'
    def predict(self, patient_data: PatientData) -> bool:
        if not self.model:
            # Lógica de simulação (com verificação de None)
            if (
                patient_data.glicemia_jejum_mg_dl is not None and patient_data.glicemia_jejum_mg_dl > 140
            ) or (
                patient_data.pressao_sistolica_mmHg is not None and patient_data.pressao_sistolica_mmHg > 140
            ):
                return True # Simula um outlier
            return False # Simula um não-outlier

        # --- LÓGICA DO MODELO REAL ---
        # Mapeamento do schema de 22 features para as 5 que o modelo espera
        input_data = [[
            patient_data.idade,
            patient_data.glicemia_jejum_mg_dl,
            patient_data.pressao_sistolica_mmHg,
            patient_data.pressao_diastolica_mmHg,
            int(patient_data.historico_familiar_dc)
        ]]

        # Faça a predição
        prediction = self.model.predict(input_data)
        
        # Define um limiar
        threshold = 0.5
        is_outlier = bool(prediction[0] > threshold)
        
        return is_outlier

# Cria uma instância única do modelo para ser usada pela API
model_instance = Model(MODEL_PATH)