# -*- coding: cp949 -*-

import streamlit as st

def main():
    st.title("POST ��� ���� ����ϱ�")
    
    # POST ������� ���� �����͸� �ޱ�
    post_data = st.text_input("POST ������� ���� ������ �Է��ϼ���")
    
    # ���� ������ ���
    if post_data:
        st.write("POST ������� ���� ����:", post_data)

if __name__ == "__main__":
    main()


