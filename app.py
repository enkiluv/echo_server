# -*- coding: cp949 -*-

import streamlit as st

def main():
    st.title("POST 명령 정보 출력하기")
    
    # POST 명령으로 들어온 데이터를 받기
    post_data = st.text_input("POST 명령으로 받은 정보를 입력하세요")
    
    # 받은 데이터 출력
    if post_data:
        st.write("POST 명령으로 받은 정보:", post_data)

if __name__ == "__main__":
    main()


