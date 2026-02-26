import streamlit as st
import google.generativeai as genai

# API 키 설정
GOOGLE_API_KEY = "AIzaSyCh1giXK1ydG1wIKdsMJwBLtlAuIk1Lgzg"
genai.configure(api_key=GOOGLE_API_KEY)

st.title("🤖 챗봇")

# 1. 사용 가능한 모델 리스트 확인 (오류 방지용 로그)
try:
    available_models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
    st.write(f"현재 사용 가능한 모델: {available_models[0]}") # 가장 첫 번째 모델 표시
    target_model = available_models[0] # 자동으로 사용 가능한 모델 선택
except Exception as e:
    st.error(f"모델 목록을 불러오지 못했습니다: {e}")
    target_model = 'gemini-pro' # 기본값 설정

if prompt := st.chat_input("테스트 메시지를 입력하세요"):
    st.chat_message("user").markdown(prompt)
    
    with st.chat_message("assistant"):
        try:
            # 안전하게 검색된 모델 이름을 사용하거나 'gemini-pro' 사용
            model = genai.GenerativeModel(target_model)
            response = model.generate_content(prompt)
            st.markdown(response.text)
        except Exception as e:
            st.error(f"대답 생성 중 오류 발생: {e}")
