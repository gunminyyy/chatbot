import streamlit as st
import google.generativeai as genai

# 1. 페이지 설정 및 제목
st.set_page_config(page_title="나만의 제미나이 챗봇", layout="centered")
st.title("🤖 제미나이 챗봇에 오신 걸 환영합니다!")
st.caption("OpenAI 대신 구글 제미나이 API를 사용하는 챗봇입니다.")

# 2. API 키 설정 (직접 입력하거나 Secrets 사용)
# 테스트를 위해 아래 따옴표 안에 발급받은 제미나이 키를 넣으세요.
GOOGLE_API_KEY = "여기에_복사한_제미나이_키를_넣으세요"

if not GOOGLE_API_KEY or GOOGLE_API_KEY == "여기에_복사한_제미나이_키를_넣으세요":
    st.warning("⚠️ 제미나이 API 키를 코드에 입력해주세요!")
    st.stop()

genai.configure(api_key=GOOGLE_API_KEY)

# 3. 대화 기록 관리 (세션 상태)
if "messages" not in st.session_state:
    st.session_state.messages = []

# 기존 대화 표시
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 4. 채팅 입력창
if prompt := st.chat_input("무엇이든 물어보세요!"):
    # 사용자 메시지 표시 및 저장
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # 제미나이 답변 생성
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        message_placeholder.markdown("생각 중... 🤔")
        
        try:
            model = genai.GenerativeModel('gemini-1.5-flash')
            response = model.generate_content(prompt)
            full_response = response.text
            
            message_placeholder.markdown(full_response)
            # 답변 저장
            st.session_state.messages.append({"role": "assistant", "content": full_response})
        except Exception as e:
            message_placeholder.error(f"에러가 발생했습니다: {e}")
