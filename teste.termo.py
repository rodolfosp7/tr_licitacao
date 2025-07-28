# EXEMPLO DE AGENTE DE LICITAÇÕES EM PYTHON (TERMO DE REFERÊNCIA)
# Atualizado para funcionar com um único campo de entrada: o objeto da contratação, com descrições detalhadas por capítulo

import streamlit as st

st.set_page_config(page_title="Gerador de Termo de Referência", layout="centered")

st.title("📑 Gerador de Termo de Referência Automático - Prefeitura de Brasnorte")

st.markdown("Informe apenas o objeto da contratação. O sistema irá gerar automaticamente o Termo de Referência completo e detalhado, com base na Lei 14.133/2021 e no Decreto Municipal nº 09/2024.")

# Entrada única
objeto = st.text_area("📝 Objeto da contratação", placeholder="Ex: Contratação de empresa especializada para fornecimento de refeições prontas para servidores em viagem técnica.", height=150)

if st.button("🔧 Gerar Termo de Referência") and objeto:
    termo = f"""
PREFEITURA MUNICIPAL DE BRASNORTE - MT
SECRETARIA MUNICIPAL DE ADMINISTRAÇÃO

TERMO DE REFERÊNCIA

1. DAS CONDIÇÕES GERAIS DA CONTRATAÇÃO

1.1 O presente Termo de Referência tem por objeto a {objeto}, observando os princípios da legalidade, eficiência e economicidade, conforme previsto no art. 6º, XXIII, alínea “a” e “i” da Lei nº 14.133/2021 e art. 30, I do Decreto Municipal nº 09/2024.

1.2 O objeto desta contratação não se enquadra como sendo de bem de luxo, conforme Decreto Municipal nº 03/2024, art. 5º, que veda aquisição de bens considerados de luxo.

1.3 O prazo de vigência da contratação será de 12 (doze) meses, contados a partir da assinatura do contrato, podendo ser prorrogado conforme interesse da Administração e permissivo legal.

1.4 O custo estimado da contratação será definido com base em pesquisas de mercado, memórias de cálculo e cotações, devidamente documentadas em processo administrativo próprio.

2. DA NECESSIDADE DA CONTRATAÇÃO E FUNDAMENTAÇÃO LEGAL

2.1 A presente contratação se fundamenta na necessidade administrativa de garantir a continuidade e eficiência dos serviços públicos prestados pelo Município de Brasnorte, conforme apurado no Estudo Técnico Preliminar anexo, em consonância com o art. 6º, XXIII, alínea "b" da Lei nº 14.133/2021 e art. 30, II do Decreto Municipal nº 09/2024.

3. DA SOLUÇÃO COMO UM TODO CONSIDERADO O CICLO DE VIDA DO OBJETO E ESPECIFICAÇÃO DOS SERVIÇOS

3.1 Para atendimento à necessidade identificada, foram consideradas duas alternativas:

- **Solução 1:** Execução direta pela Administração, utilizando recursos humanos próprios. Esta solução mostrou-se inviável por ausência de servidores com capacitação técnica e operacional para o desempenho adequado das atividades.

- **Solução 2:** Contratação de empresa especializada por meio de procedimento licitatório. Essa opção garante maior eficiência, especialização técnica, cumprimento de prazos e qualidade na prestação dos serviços.

3.2 **Conclusão:** Opta-se pela Solução 2, por ser mais vantajosa à Administração sob os aspectos técnico-operacionais e econômicos.

3.3 O ciclo de vida do objeto compreenderá as fases de planejamento, execução, acompanhamento, avaliação e encerramento contratual, considerando requisitos de durabilidade, qualidade, desempenho e sustentabilidade.

4. DOS REQUISITOS DA CONTRATAÇÃO

4.1 A contratação deverá observar os seguintes requisitos mínimos:

4.1.1 Apresentação de documentação de habilitação jurídica, fiscal e trabalhista, conforme exigido em edital;

4.1.2 Comprovação de aptidão técnica por meio de atestados de capacidade técnica;

4.1.3 Regularidade junto aos órgãos de fiscalização profissional, quando aplicável;

4.1.4 Garantia de fornecimento de materiais e/ou execução dos serviços conforme as normas técnicas vigentes;

4.1.5 Atendimento às normas de segurança, saúde do trabalho, proteção de dados pessoais e preservação ambiental.

5. DO MODELO DE EXECUÇÃO CONTRATUAL

5.1 A execução contratual dar-se-á por meio de ordens de serviço ou fornecimento emitidas pela Administração, acompanhadas pela fiscalização designada.

5.2 A contratada deverá cumprir fielmente o cronograma de entrega e as especificações técnicas estabelecidas no edital e seus anexos.

5.3 Os pagamentos serão realizados mediante apresentação de notas fiscais, relatórios de execução e aceite da fiscalização, respeitando os prazos e condições previstas contratualmente.

5.4 O contrato poderá ser executado por sistema de registro de preços, quando cabível, ou mediante contratação direta para atendimento de demanda específica e imediata.

6. DOS CRITÉRIOS DE MEDIÇÃO

6.1 A medição será realizada com base na efetiva entrega do objeto contratado, mediante conferência pela fiscalização designada.

6.2 A aceitação dos serviços prestados ou bens fornecidos dependerá de verificação de conformidade com os requisitos técnicos e funcionais descritos no edital e seus anexos.

6.3 O pagamento será condicionado ao aceite formal da Administração, sendo emitido relatório circunstanciado de medição com descrição dos serviços executados, período de execução e conformidade verificada.

6.4 Para os contratos de natureza continuada, a medição será mensal e proporcional à execução contratual, podendo incluir indicadores de desempenho pactuados.

**Brasnorte - MT, Julho de 2025**

---

Este modelo poderá ser ajustado conforme as peculiaridades da contratação. Recomenda-se consulta à Procuradoria Jurídica e ao Controle Interno antes da publicação do edital.
"""

    st.markdown("### 📄 Resultado do Termo de Referência")
    st.text_area("Termo Gerado:", termo, height=600)
