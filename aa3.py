import random
import streamlit as st

# ==========================================
# [데이터 및 상수 정의]
# ==========================================
FOOD_DATABASE = {
    "달고나 커피": {
        "emoji": "☕", "start": "2020년 2월", "end": "2020년 5월",
        "features": ["홈메이드", "시각적 챌린지", "직접 만들기"]
    },
    "미니 팬케이크 시리얼": {
        "emoji": "🥞", "start": "2020년 5월", "end": "2020년 7월",
        "features": ["홈메이드", "시각적 화려함", "귀여운 비주얼"]
    },
    "크로플": {
        "emoji": "🧇", "start": "2020년 9월", "end": "2021년 7월",
        "features": ["식감(바삭/쫄깃)", "홈메이드 간식", "기존 디저트 퓨전"]
    },
    "로제 떡볶이": {
        "emoji": "🍚", "start": "2021년 4월", "end": "2021년 9월",
        "features": ["매운맛/부드러움(단짠)", "대중적 소스 융합", "배달/외식 트렌드"]
    },
    "민트초코": {
        "emoji": "🌿", "start": "2021년 6월", "end": "2021년 8월",
        "features": ["호불호/마니아층", "이색 조합", "밈(Meme) 문화"]
    },
    "전통 달고나 뽑기": {
        "emoji": "⭐", "start": "2021년 11월", "end": "2021년 12월",
        "features": ["미디어(방송/게임)", "레트로", "도전 정신"]
    },
    "포켓몬 빵": {
        "emoji": "🍞", "start": "2022년 2월", "end": "2022년 10월",
        "features": ["캐릭터 IP 결합", "수집/랜덤성(띠부씰)", "추억 소환(레트로)"]
    },
    "블랑제베르 버터 맥주": {
        "emoji": "🍺", "start": "2022년 7월", "end": "2022년 12월",
        "features": ["이색 주류", "한정판 마케팅", "유통 트렌드"]
    },
    "약과 디저트류": {
        "emoji": "🍯", "start": "2022년 5월", "end": "2024년 5월",
        "features": ["할매니얼", "재해석(쿠키 결합)", "꾸덕함"]
    },
    "탕후루": {
        "emoji": "🍓", "start": "2023년 2월", "end": "2024년 2월",
        "features": ["식감(바삭한 소리)", "시각적 화려함", "길거리 간식"]
    },
    "로제마라 메뉴": {
        "emoji": "🥘", "start": "2023년 2월", "end": "2023년 11월",
        "features": ["매운맛/부드러움(단짠)", "대중적 소스 융합", "배달/외식 트렌드"]
    },
    "두바이 초콜릿": {
        "emoji": "🍫", "start": "2024년 4월", "end": "2024년 12월",
        "features": ["식감(바삭/꾸덕)", "SNS(틱톡/인스타)", "이색 재료(카다이프)"]
    },
    "요아정": {
        "emoji": "🍦", "start": "2024년 5월", "end": "2024년 11월~(현재)",
        "features": ["커스텀 조합", "입맛대로 선택", "상큼/달달"]
    },
    "밤 티라미수": {
        "emoji": "🌰", "start": "2024년 9월", "end": "2024년 12월",
        "features": ["미디어(방송)", "편의점 재료 변형", "셰프 레시피"]
    }
}

PREDICTION_POOLS = {
    "crunchy": [
        "소리나 독특한 식감을 극대화한 'ASMR형 이색 제과류'가 다음 유행을 선도할 것입니다.",
        "씹는 재미를 강조한 바삭·꾸덕한 크런치 계열의 신개념 베이커리가 주목받을 가능성이 높습니다.",
        "겉은 바삭하고 속은 부드러운 '반전 식감'을 가진 길거리 간식류가 새롭게 떠오를 것입니다."
    ],
    "media": [
        "숏폼 플랫폼을 통해 대중이 직접 레시피를 변형하고 인증하는 '참여형 챌린지 퓨전 요리'가 유행할 것입니다.",
        "유명 인플루언서나 방송 프로그램의 서브 브랜딩을 업은 '한정판 협업 메뉴'가 시장을 장악할 것입니다.",
        "누구나 집에 있는 흔한 재료로 따라 할 수 있는 '초간단 셀프 리폼 디저트'가 대세를 이룰 것입니다."
    ],
    "custom": [
        "소비자가 직접 토핑과 소스를 선택해 조합하는 '모듈형 커스텀 디저트' 카테고리가 확장될 것입니다.",
        "전통 식재료를 젊은 감각으로 재해석해 전혀 다른 폼팩터와 결합하는 시도가 이어질 것입니다.",
        "개인의 취향을 세분화하여 만족시키는 '나만의 조합 공유형' 프리미엄 디저트가 인기를 끌 것입니다."
    ],
    "spicy_fusion": [
        "자극적인 매운맛과 부드러운 크림·로제 계열을 결합해 대중성을 극대화한 '퓨전 소스 요리'가 지속적으로 인기를 끌 것입니다.",
        "배달 및 간편식 시장에서 기존 스테디셀러 메뉴에 이색 소스를 접목한 '크로스오버 배달 음식'이 대세를 이룰 것입니다.",
        "알싸한 향신료의 맛을 한국인의 입맛에 맞춰 부드럽게 중화시킨 '마일드 매운맛 베이스의 요리'가 확산될 것입니다."
    ],
    "meme_taste": [
        "극단적인 호불호 요소를 마케팅 포인트로 삼아 소비자의 놀이 문화(밈)를 자극하는 '이색 취향 저격 제품'이 흥행할 것입니다.",
        "상쾌함과 달콤함을 동시에 주는 독특한 향을 다양한 제과 및 음료 카테고리에 이식하는 시도가 늘어날 것입니다.",
        "특정 마니아층의 지지를 기반으로 시작해 대중적인 라인업으로 확장되는 '반전 마케팅형 상품'이 주목받을 것입니다."
    ],
    "ip_collection": [
        "강력한 IP와 수집형 굿즈를 결합하여 소장 욕구를 자극하는 '체험형 유통 상품'이 대박을 터뜨릴 것입니다.",
        "기성세대의 향수를 자극하는 레트로 콘셉트에 현대적인 감각의 캐릭터를 더한 '추억 소환형 소비'가 주류가 될 것입니다.",
        "제품 본질의 맛뿐만 아니라 언박싱의 재미를 극대화한 '굿즈 동봉형 푸드 마케팅'이 업계 표준으로 자리 잡을 것입니다."
    ]
}

# ==========================================
# [헬퍼 함수]
# ==========================================
def select_prediction_pool(features):
    """음식의 특징에 알맞은 예측 메시지 풀을 선택합니다."""
    for f in features:
        if "식감" in f:
            return PREDICTION_POOLS["crunchy"]
        elif "미디어" in f or "SNS" in f:
            return PREDICTION_POOLS["media"]
        elif "매운맛" in f or "배달" in f:
            return PREDICTION_POOLS["spicy_fusion"]
        elif "호불호" in f or "마니아" in f:
            return PREDICTION_POOLS["meme_taste"]
        elif "캐릭터" in f or "수집" in f:
            return PREDICTION_POOLS["ip_collection"]
    return PREDICTION_POOLS["custom"]

# ==========================================
# [Streamlit UI 구성]
# ==========================================
st.set_page_config(page_title="트렌드 음식 분석 AI", page_icon="🍲", layout="centered")

st.title("🍲 트렌드 음식 분석 및 다음 유행 예측 대시보드")
st.markdown("과거 큰 인기를 끌었던 트렌드 음식을 직접 입력하고 성공 요인과 다음 유행 전망을 확인해 보세요.")
st.markdown("---")

# 사이드바 설정
st.sidebar.header("📌 이용 안내")
st.sidebar.info(
    "• 입력창에 분석하고 싶은 음식 이름을 **직접 입력**하세요.\n"
    "• 등록되지 않은 이름을 입력하면 **재입력**을 안내합니다.\n"
    "• 종료하려면 **'그만'**을 입력하세요."
)

# 사용자 입력 받기 (텍스트 입력 위젯)
user_input = st.text_input(
    "🔍 분석할 음식 이름을 입력하세요:",
    placeholder="예: 두바이 초콜릿, 탕후루, 요아정 등"
).strip()

# 버튼 클릭 또는 값이 입력된 경우 처리
if st.button("🚀 분석 및 예측 실행", type="primary"):
   
    # 1. 종료 조건 처리
    if user_input == "그만":
        st.warning("👋 프로그램을 종료합니다. 이용해 주셔서 감사합니다!")
        st.stop()
       
    # 2. 빈 값 입력 처리
    elif not user_input:
        st.warning("⚠️ 음식 이름을 입력해 주세요.")
       
    # 3. 데이터베이스에 없는 음식 입력 시 재입력 유도
    elif user_input not in FOOD_DATABASE:
        st.error(
            f"❌ **[등록되지 않은 음식]** '{user_input}'은(는) 데이터베이스에 없습니다.\n\n"
            "📋 올바른 음식명을 다시 입력해 주시거나, 종료를 원하시면 **'그만'**을 입력해 주세요."
        )
       
    # 4. 정상 입력 시 데이터 분석 및 시각화 출력
    else:
        info = FOOD_DATABASE[user_input]
        emoji = info["emoji"]
        start_date = info["start"]
        end_date = info["end"]
        features = info["features"]
       
        pool = select_prediction_pool(features)
        selected_prediction = random.choice(pool)

        # 결과 시각화 레이아웃
        st.success(f"분석 완료: **{emoji} {user_input}**")
       
        # 기간 정보 2열 지표 배치
        col1, col2 = st.columns(2)
        with col1:
            st.metric(label="📅 유행 시작 시점", value=start_date)
        with col2:
            st.metric(label="🏁 유행 종료 시점", value=end_date)
           
        st.markdown("### 🤖 핵심 성공 요인")
        features_md = " ".join([f"`{feat}`" for feat in features])
        st.markdown(features_md)
       
        st.markdown("---")
       
        st.markdown("### 🔮 다음 유행 예측")
        st.info(selected_prediction)
