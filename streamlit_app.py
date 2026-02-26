# ... (상단 설정 코드는 동일)

# [수정] 대화 기록을 제미나이가 이해할 수 있는 형식으로 변환
history = []
for msg in st.session_state.messages:
    # 제미나이는 'assistant' 대신 'model'이라는 단어를 사용합니다.
    role = "model" if msg["role"] == "assistant" else "user"
    history.append({"role": role, "parts": [msg["content"]]})

# [수정] 대화 세션 시작 (과거 기록을 통째로 넘겨줌)
chat_session = model.start_chat(history=history)

if prompt := st.chat_input("질문을 입력하세요"):
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("assistant"):
        # 이제 AI가 이전 대화를 다 알고 답변합니다!
        response = chat_session.send_message(prompt)
        st.markdown(response.text)
        st.session_state.messages.append({"role": "assistant", "content": response.text})
