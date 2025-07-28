# EXEMPLO DE AGENTE DE LICITAÇÕES EM PYTHON (TERMO DE REFERÊNCIA)
# Atualizado para funcionar com um único campo de entrada: o objeto da contratação

import streamlit as st

st.set_page_config(page_title="Gerador de Termo de Referência", layout="centered")

st.title("📑 Gerador de Termo de Referência Automático - Prefeitura de Brasnorte")

st.markdown("Informe apenas o objeto da contratação. O sistema irá gerar automaticamente o Termo de Referência com base na Lei 14.133/2021 e no Decreto Municipal nº 09/2024.")

# Entrada única
objeto = st.text_area("📝 Objeto da contratação", placeholder="Ex: Contratação de empresa especializada para fornecimento de refeições prontas para servidores em viagem técnica.", height=150)

if st.button("🔧 Gerar Termo de Referência") and objeto:
    termo = f"""
PREFEITURA MUNICIPAL DE BRASNORTE - MT
SECRETARIA MUNICIPAL DE ADMINISTRAÇÃO

TERMO DE REFERÊNCIA

1. DAS CONDIÇÕES GERAIS DA CONTRATAÇÃO

O presente Termo de Referência tem por objeto a {objeto}, conforme previsto no art. 6º, XXIII, alínea "a" e "i" da Lei nº 14.133/2021 e art. 30, I do Decreto Municipal nº 09/2024.

A vigência do contrato será de 12 (doze) meses, podendo ser prorrogada conforme o interesse público. O regime de execução será empreitada por preço global, com pagamento mediante medição mensal dos serviços prestados.

2. DA NECESSIDADE DA CONTRATAÇÃO E FUNDAMENTAÇÃO LEGAL

A presente contratação visa atender necessidade essencial da Administração Pública, assegurando a continuidade das atividades públicas relacionadas. Fundamenta-se no art. 6º, XXIII, "b" da Lei nº 14.133/2021 e art. 30, II do Decreto Municipal nº 09/2024.

3. DA SOLUÇÃO E CICLO DE VIDA DO OBJETO

A solução contempla a execução integral do serviço por empresa contratada, desde o planejamento, operação e controle da entrega, até o encerramento contratual. O serviço será executado conforme cronograma físico-financeiro a ser pactuado. (Lei nº 14.133/21, art. 6º, XXIII, "c" e art. 40, §1º, I)

4. DOS REQUISITOS DA CONTRATAÇÃO

A empresa contratada deverá comprovar capacidade técnica, apresentar atestados de desempenho anterior compatível, manter regularidade fiscal e cumprir as normas ambientais, de segurança e de proteção de dados pessoais, conforme legislação aplicável. (Lei nº 14.133/21, art. 6º, XXIII, "d")

5. DO MODELO DE EXECUÇÃO CONTRATUAL

A execução se dará com base em ordens de serviço emitidas pela contratante. A contratada deverá executar os serviços em até 5 (cinco) dias úteis após a emissão da ordem. A fiscalização será exercida por servidor designado em portaria específica. (Lei nº 14.133/21, art. 6º, XXIII, "e" e art. 40, §1º, II)

**Brasnorte - MT, Julho de 2025**

---

Este modelo pode ser ajustado conforme as peculiaridades da contratação e os anexos necessários. Consulte o setor jurídico ou controle interno em caso de dúvidas ou divergências normativas.
"""

    st.markdown("### 📄 Resultado do Termo de Referência")
    st.text_area("Termo Gerado:", termo, height=600)
