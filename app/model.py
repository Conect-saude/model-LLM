import pandas as pd
from joblib import load
from pathlib import Path
from schemas import PatientData 

# --- Caminho Corrigido ---
CURRENT_FILE_PATH = Path(__file__).resolve()
APP_DIR = CURRENT_FILE_PATH.parent
PROJECT_ROOT = APP_DIR.parent
MODEL_PATH = PROJECT_ROOT / "models" / "modelo_regressao_linear.joblib"
# --- Fim da Correção de Caminho ---

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
        
        # --- CORREÇÃO TEMPORÁRIA (IGNORANDO O MODELO) ---
        # O modelo .joblib está fazendo previsões erradas (ex: estável para IMC 58).
        # Vamos forçar a lógica de simulação manual até que o modelo seja retreinado.
        
        print("FORÇADO: Usando lógica de simulação manual (regras de negócio).")
        
        # Regra 1: Glicemia
        if (
            patient_data.glicemia_jejum_mg_dl is not None and 
            patient_data.glicemia_jejum_mg_dl > 140
        ):
            return True # Outlier

        # Regra 2: Pressão
        if (
            patient_data.pressao_sistolica_mmHg is not None and 
            patient_data.pressao_sistolica_mmHg > 140
        ):
            return True # Outlier

        # Regra 3: IMC (Obesidade severa)
        if (
            patient_data.imc is not None and 
            patient_data.imc > 40
        ):
            return True # Outlier (IMC 58 do paciente se encaixa aqui)

        # Se não caiu em nenhuma regra, é estável
        return False
        
        # --- FIM DA CORREÇÃO TEMPORÁRIA ---
        
        
        # --- O CÓDIGO DO MODELO REAL (IGNORADO POR ENQUANTO) ---
        # patient_data_dict = patient_data.model_dump()
        # input_df = pd.DataFrame([patient_data_dict])
        # prediction = self.model.predict(input_df)
        # is_outlier = bool(prediction[0] == 1) 
        # return is_outlier

# Cria uma instância única do modelo
model_instance = Model(MODEL_PATH)