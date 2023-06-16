import streamlit as st

def set_detail(name):
    st.session_state['detail'] = name

def get_spot_list(spots):
    # 여행지 리스트
    # n개 열 -> n개 열마다 사진, 여행지명, 간단한 설명.
    # for col in st.columns(3):
    for idx, col in enumerate(st.columns(len(spots))):
        # st.columns(n) -> n개의 열이 묶인 리스트
        # 해당 열들을 순서대로 col이라는 변수로 사용
        # ...
        spot = spots[idx]

        #col.header(spot["name"])
        name = spot["name"]
        col.markdown(f"<h3 style='text-align: center;'>{name}</h1>", unsafe_allow_html=True)
        col.image(spot["img"])
        star_count = spot["star"]
        col.write("".join(["⭐"] * star_count))
        col.write(spot['desc'])
        # There are multiple identical st.button widgets with the same generated key.
        # st.button -> bool => 눌리면 해당 button => True
        if col.button("지도 보기", key=f"button{idx}", use_container_width=True):
            # 눌렀을 때 실행되는 코드...
            # col.write(spots["name"])
            st.session_state['detail'] = spot["name"]
            st.session_state['map'] = spot["map"]
            st.session_state['link'] = spot["link"]
        # 버튼마다 다른 key가 있어야함.