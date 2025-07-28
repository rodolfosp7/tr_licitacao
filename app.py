import streamlit as st

st.set_page_config(page_title="Gerador de Termo de Referência", layout="centered")

st.title("📑 Gerador de Termo de Referência - Lei 14.133/21")

st.markdown("Preencha os campos abaixo para gerar um Termo de Referência automático conforme a nova Lei de Licitações e Decreto Municipal nº 09/2024.")

# Formulário de entrada
objeto = st.text_area("1️⃣ Objeto da contratação", height=100)
necessidade = st.text_area("2️⃣ Descrição da necessidade da contratação", height=100)
prazo_execucao = st.text_input("3️⃣ Prazo de execução contratual")
quantidade_estimativa = st.text_input("4️⃣ Quantitativo estimado (profissionais, itens, serviços, etc.)")
requisitos = st.text_area("5️⃣ Requisitos da empresa contratada (um por linha)", height=100)
modelo_execucao = st.text_area("6️⃣ Modelo de execução contratual", height=100)

if st.button("🔧 Gerar Termo de Referência"):
    requisitos_formatados = "\n".join(f"- {r}" for r in requisitos.splitlines() if r.strip())

    termo = f"""
1. DAS CONDIÇÕES GERAIS DA CONTRATAÇÃO

O presente Termo de Referência tem por objeto a {objeto}
O prazo de execução contratual será de {prazo_execucao}.
A execução será realizada sob regime de empreitada por preço global.

2. DA NECESSIDADE DA CONTRATAÇÃO E FUNDAMENTAÇÃO LEGAL

A presente contratação visa {necessidade}, conforme previsto no art. 6º, XXIII, 'b' da Lei nº 14.133/2021 e Art. 30 II do Decreto Municipal nº 09/2024.

3. DA SOLUÇÃO COMO UM TODO E ESPECIFICAÇÃO DOS SERVIÇOS

A solução contratada abrangerá o ciclo completo da prestação do objeto. A estimativa de serviços prevê {quantidade_estimativa}.

4. DOS REQUISITOS DA CONTRATAÇÃO

A empresa contratada deverá atender aos seguintes requisitos mínimos:
{requisitos_formatados}

5. DO MODELO DE EXECUÇÃO CONTRATUAL

{modelo_execucao}
"""
    st.markdown("### 📄 Resultado do Termo de Referência")
    st.text_area("Texto gerado:", termo, height=500)
