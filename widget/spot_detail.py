import streamlit as st

def get_spot_detail():
    st.header(st.session_state['detail'])
    # 여행지 상세보기
    st.image(st.session_state['map'], use_column_width=True)
    link = st.session_state['link']
    st.write(f"[**🔗 여행지 홈페이지 or 네이버 플레이스 링크**]({link})")