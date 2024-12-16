
import tabula as tb
import streamlit as st
import time

st.set_page_config(layout="wide")

with st.sidebar:
    password = st.text_input('Didite a senha do PDF', type='password', placeholder='Em branco caso nao tenha senha')
    pdf_file = st.file_uploader("Selecione o PDF")




if pdf_file is not None:
    lista_tabelas = tb.read_pdf(pdf_file , password=password, pages="2", multiple_tables=False)

    for tabela in lista_tabelas:
        st.divider()
        col1, col2, col3 = st.columns(3)
        with col1:
            # Pegando o valor líquido das operações
            st.write(':star: _Valor Liquido das Operações_')
            st.write(f":dollar: R$ {str(tabela['Unnamed: 3'][1])}")
        with col2:
            # Pegando a taxa de liquidação
            st.write(':star: _Taxa de liquidação_')
            st.write(f":dollar: R$ {str(tabela['Unnamed: 3'][2])}")
        with col3:
            # Pegando emolumentos
            st.write(':star: _Emolumentos_')
            st.write(f":dollar: R$ {str(tabela['Unnamed: 3'][10])}")

        col4, col5, col6 = st.columns(3)
        with col4:
            # Pegando valor total de corretagem
            st.write(':star: _Total de Corretagem / Despesas_')
            st.write(f":dollar: R$ {str(tabela['Resumo Financeiro'][18].split('Total Corretagem / Despesas')[1])}")
        with col5:
            # Pegando Total CBLC
            st.write(':star: _Total CBLC_')
            st.write(f":dollar: R$ {str(tabela['Unnamed: 3'][5])}")
        with col6:
            st.write(':star: _Corretora_')
            st.write(f":classical_building: {str(tabela['Resumo Financeiro'][32])}")


