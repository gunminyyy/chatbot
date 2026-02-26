import streamlit as st
import google.generativeai as genai

# 1. 제미나이 API 키 설정 (보내주신 키를 적용했습니다)
GOOGLE_API_KEY = "AIzaSyCh1giXK1ydG1wIKdsMJwBLtlAuIk1Lgzg"
genai.configure(api_key=GOOGLE_API_KEY)

# 2. 페이지 레이아웃 설정
st.set_page_config(page_title="우리 회사 전용 챗봇", page_icon="🤖")
st.title("🤖 제미나이 챗봇")
st.info("이제 이 챗봇은 공유 폴더의 수만 개 파일을 읽을 준비를 할 수 있습니다.")

# 3. 대화 기록 저장 공간 만들기
if "messages" not in st.session_state:
    st.session_state.messages = []

# 4. 이전 대화 화면에 그리기
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 5. 사용자 채팅 입력 처리
if prompt := st.chat_input("질문을 입력해 보세요 (예: 회사 매뉴얼 찾아줘)"):
    # 사용자 메시지 화면에 표시 및 저장
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # 6. 제미나이 모델에게 답변 요청
    with st.chat_message("assistant"):
        try:
            # 성능이 좋고 빠른 1.5-flash 모델 사용
            model = genai.GenerativeModel('gemini-1.5-flash')
            response = model.generate_content(prompt)
            
            # 답변 출력 및 저장
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
            
        except Exception as e:
            st.error(f"오류가 발생했어요: {e}")
