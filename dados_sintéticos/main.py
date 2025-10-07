import pandas as pd
import numpy as np
import random


params_clinicos = {
    'normal': {
        'pressao_sistolica_mmHg': {'mean': 120, 'std': 8},
        'pressao_diastolica_mmHg':{'mean': 78, 'std': 6},
        'glicemia_jejum_mg_dl':   {'mean': 90,  'std': 5},
        'imc':                    {'mean': 22.5,'std': 2},
        'colesterol_total_mg_dl': {'mean': 180, 'std': 20},
        'hdl_mg_dl':              {'mean': 55,  'std': 10},
        'triglicerides_mg_dl':    {'mean': 120, 'std': 30},
    },
    'outlier': {
        'pressao_sistolica_mmHg': {'mean': 145, 'std': 15},
        'pressao_diastolica_mmHg':{'mean': 92, 'std': 8},
        'glicemia_jejum_mg_dl':   {'mean': 130, 'std': 25},
        'imc':                    {'mean': 29,  'std': 4},
        'colesterol_total_mg_dl': {'mean': 225, 'std': 40},
        'hdl_mg_dl':              {'mean': 35,  'std': 8},
        'triglicerides_mg_dl':    {'mean': 200, 'std': 50},
    }
}


opcoes_atividade_fisica = ['Sedentário', 'Leve (1-2 dias/sem)', 'Moderado (3-4 dias/sem)', 'Intenso (5+ dias/sem)']
pesos_atividade_fisica = [0.4, 0.3, 0.2, 0.1]

opcoes_consumo_alcool = ['Nenhum', 'Ocasional', 'Frequente']
pesos_consumo_alcool = [0.5, 0.4, 0.1]

opcoes_qualidade_sono = ['Ruim', 'Regular', 'Boa']
pesos_qualidade_sono = [0.3, 0.5, 0.2]

opcoes_aderencia = ['Baixa', 'Média', 'Alta']
pesos_aderencia = [0.2, 0.4, 0.4]

n_amostras = 10000  
lista_pacientes = []


for i in range(n_amostras):
    paciente = {"id": i + 1}
    
    paciente['idade'] = random.randint(25, 80)
    paciente['sexo'] = random.choice(['Masculino', 'Feminino'])
    paciente['escolaridade'] = random.choices(['Fundamental', 'Médio', 'Superior'], [0.4, 0.4, 0.2])[0]
    paciente['renda_familiar_sm'] = random.choices(['Até 1', '1 a 3', '> 3'], [0.4, 0.5, 0.1])[0]
    
    paciente['atividade_fisica'] = random.choices(opcoes_atividade_fisica, pesos_atividade_fisica)[0]
    paciente['consumo_alcool'] = random.choices(opcoes_consumo_alcool, pesos_consumo_alcool)[0]
    paciente['tabagismo_atual'] = random.choices([True, False], [0.25, 0.75])[0]
    paciente['qualidade_dieta'] = random.choices(['Ruim', 'Regular', 'Boa'], [0.3, 0.5, 0.2])[0]
    paciente['qualidade_sono'] = random.choices(opcoes_qualidade_sono, pesos_qualidade_sono)[0]
    
    paciente['nivel_estresse'] = random.choices(['Baixo', 'Médio', 'Alto'], [0.4, 0.4, 0.2])[0]
    paciente['suporte_social'] = random.choices(['Fraco', 'Moderado', 'Forte'], [0.2, 0.5, 0.3])[0]
    paciente['historico_familiar_dc'] = random.choices([True, False], [0.4, 0.6])[0] # Doença Crônica

    paciente['acesso_servico_saude'] = random.choices(['Difícil', 'Regular', 'Fácil'], [0.2, 0.4, 0.4])[0]
    paciente['aderencia_medicamento'] = random.choices(opcoes_aderencia, pesos_aderencia)[0] if random.random() > 0.5 else 'N/A'
    paciente['consultas_ultimo_ano'] = random.randint(0, 10)

    escore_risco = 0

    if paciente['idade'] > 50: escore_risco += (paciente['idade'] - 50) / 10
    if paciente['renda_familiar_sm'] == 'Até 1': escore_risco += 2
    if paciente['atividade_fisica'] == 'Sedentário': escore_risco += 2
    if paciente['consumo_alcool'] == 'Frequente': escore_risco += 1
    if paciente['tabagismo_atual']: escore_risco += 3
    if paciente['qualidade_dieta'] == 'Ruim': escore_risco += 2
    if paciente['qualidade_sono'] == 'Ruim': escore_risco += 1
    if paciente['nivel_estresse'] == 'Alto': escore_risco += 1.5
    if paciente['historico_familiar_dc']: escore_risco += 1
    if paciente['acesso_servico_saude'] == 'Difícil': escore_risco += 1
    if paciente['aderencia_medicamento'] == 'Baixa': escore_risco += 1.5


    if paciente['atividade_fisica'] == 'Intenso': escore_risco -= 1
    if paciente['qualidade_dieta'] == 'Boa': escore_risco -= 1
    if paciente['suporte_social'] == 'Forte': escore_risco -= 1

    # --- Passo 3: Atribuir classe (Normal/Outlier) de forma probabilística ---
    prob_ser_outlier = 1 / (1 + np.exp(-(escore_risco - 5))) # Ajustando o ponto central do risco
    
    paciente['classificacao'] = 'outlier' if random.random() < prob_ser_outlier else 'normal'

    # --- Passo 4: Gerar dados clínicos com base na classe ---
    p_clinico = params_clinicos[paciente['classificacao']]
    paciente['imc'] = round(np.random.normal(loc=p_clinico['imc']['mean'], scale=p_clinico['imc']['std']), 1)
    paciente['pressao_sistolica_mmHg'] = int(np.random.normal(loc=p_clinico['pressao_sistolica_mmHg']['mean'], scale=p_clinico['pressao_sistolica_mmHg']['std']))
    paciente['pressao_diastolica_mmHg'] = int(np.random.normal(loc=p_clinico['pressao_diastolica_mmHg']['mean'], scale=p_clinico['pressao_diastolica_mmHg']['std']))
    paciente['glicemia_jejum_mg_dl'] = int(np.random.normal(loc=p_clinico['glicemia_jejum_mg_dl']['mean'], scale=p_clinico['glicemia_jejum_mg_dl']['std']))
    paciente['colesterol_total_mg_dl'] = int(np.random.normal(loc=p_clinico['colesterol_total_mg_dl']['mean'], scale=p_clinico['colesterol_total_mg_dl']['std']))
    paciente['hdl_mg_dl'] = int(np.random.normal(loc=p_clinico['hdl_mg_dl']['mean'], scale=p_clinico['hdl_mg_dl']['std']))
    paciente['triglicerides_mg_dl'] = int(np.random.normal(loc=p_clinico['triglicerides_mg_dl']['mean'], scale=p_clinico['triglicerides_mg_dl']['std']))
    
    lista_pacientes.append(paciente)

# ==============================================================================
# 3. CRIAÇÃO E EXPORTAÇÃO PARA CSV
# ==============================================================================
df_robusto = pd.DataFrame(lista_pacientes).sample(frac=1).reset_index(drop=True)

# Reordenar colunas para melhor visualização
colunas_ordem = [
    'id', 'idade', 'sexo', 'escolaridade', 'renda_familiar_sm', # Demográfico/Social
    'atividade_fisica', 'consumo_alcool', 'tabagismo_atual', 'qualidade_dieta', 'qualidade_sono', # Comportamental
    'nivel_estresse', 'suporte_social', 'historico_familiar_dc', # Psicossocial
    'acesso_servico_saude', 'aderencia_medicamento', 'consultas_ultimo_ano', # Acesso Saúde
    'imc', 'pressao_sistolica_mmHg', 'pressao_diastolica_mmHg', 'glicemia_jejum_mg_dl', # Clínico
    'colesterol_total_mg_dl', 'hdl_mg_dl', 'triglicerides_mg_dl', # Laboratorial
    'classificacao' # Alvo
]
df_robusto = df_robusto[colunas_ordem]

# Salvar em CSV
df_robusto.to_csv('dataset_sintetico_robusto.csv', index=False, encoding='utf-8-sig')

print(f"Dataset robusto com {len(df_robusto.columns)} colunas e {len(df_robusto)} amostras salvo com sucesso!")
print("\n--- Amostra do Dataset Final ---")
print(df_robusto.head())