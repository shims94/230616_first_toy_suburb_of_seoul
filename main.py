# streamlit
import streamlit as st

from widget.spot_list import get_spot_list
from widget.spot_detail import get_spot_detail

st.title("서울 근교 여행지 추천 Best 3")
# streamlit run app.py

def make_travel_spot(name, img, star, desc, map, link): #이름,이미지, 별점, 설명, 지도, 플레이스링크
    return dict(name=name, img=img, star=star, desc=desc, map=map, link=link)

spot1 = make_travel_spot(
    "강화도",#name
    "img/img1.jpg", #img
    5, #star
    "**강화도**는 강화도는 해변, 산과 강이 조화롭게 어우러진 자연 경관이 특징입니다."\
    "청정한 바다에서 해돋이나 노을을 감상하며 힐링할 수 있으며, 해안을 따라 산책이나 등산을 즐길 수 있습니다."\
    "또한, 강화도의 전통적인 마을과 문화재를 방문하며 한국의 전통문화를 체험할 수 있습니다."\
    "강화도 여행은 아름다운 자연 경관, 역사와 문화의 보고, 그리고 풍부한 해산물과 맛있는 음식을 경험할 수 있는 멋진 여행지입니다.", #desc
    "img/m1.jpg", #map
    "https://travel.naver.com/domestic/11710/summary" #link
)

spot2 = make_travel_spot(
    "남이섬",#name
    "img/img2.jpg", #img
    4, #star
    "**남이섬**은 아름다운 자연 환경과 예술이 조화롭게 어우러진 곳으로 알려져 있습니다. "\
    "섬 전체가 자연공원으로 지정되어 있어 숲과 호수, 그리고 조용한 산책로 등 풍부한 자연 경관을 즐길 수 있습니다."\
    "또한, 섬 곳곳에 설치된 다양한 예술 작품들을 감상하면서 창의적인 영감을 얻을 수 있습니다."\
    "남이섬 여행은 아름다운 자연과 예술의 만남, 문화적인 즐거움과 휴식, 그리고 편안하고 조용한 휴양지로서 다양한 즐길 거리를 제공하는 멋진 여행지입니다."
    , #desc
    "img/m2.jpg", #map
    "https://m.place.naver.com/place/11491866/home" #link
)

spot3 = make_travel_spot(
    "석촌 호수공원",#name
    "img/img3.jpg", #img
    5, #star
    "**석촌 호수공원**은 아름다운 호수와 주변의 공원으로 구성되어 있어요. "\
    "산책, 자전거 타기, 보트 타기 등 자연을 즐기며 여유로운 시간을 보낼 수 있어요."\
    "송파대로를 기준으로 서호와 동호로 나누어져 있고 주변에는"\
    "롯데월드어드벤처, 카페거리, 방이동먹자골목 등 다양한 풍경을 만나볼 수 있어요. "\
    "매년 봄, 벚꽃이 만개할 때 ‘석촌호수 벚꽃축제’가 열리기도 한답니다.", #desc
    "img/m3.jpg", #map
    "https://m.place.naver.com/place/13491520/home" #link
)

spots = [spot1, spot2, spot3]

# 일종의 딕셔너리 (페이지가 모두 공유하는 딕셔너리)
if 'detail' not in st.session_state:  # key를 확인해서
    st.session_state['detail'] = ""  # 초기값
    st.session_state['map'] = ""  # 초기값
    st.session_state['link'] = ""  # 초기값

# 여행지 리스트
get_spot_list(spots)

# 여행지 상세보기
if st.session_state['detail']:  # 초기값의 빈 문자열
    get_spot_detail()  # 처음에는 실행하지 않고... 클릭했을 때 반응해서 그려지게