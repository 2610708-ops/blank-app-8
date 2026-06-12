import streamlit as st

# 1. 초기 데이터 설정 (오타 및 변수명 완전 수정)
stations = ["서울역", "부산역", "대전역", "홍대입구역"]
prices = [15000, 20000, 50000, 30000]

# 데이터 유지용 세션 상태(Session State) 안전하게 초기화
if "order_list" not in st.session_state:
    st.session_state.order_list = []
if "total_price" not in st.session_state:
    st.session_state.total_price = 0

# 타이틀 및 헤더 표시
st.title("🤖 AI 매표소 키오스크")
st.subheader("원하시는 목적지의 티켓을 예매하세요.")
st.divider()

# 2. 사이드바: 티켓 선택 및 장바구니 추가
st.sidebar.header("🎫 티켓 선택")

# 목적지와 가격을 묶어서 선택 박스 제공
options = [f"{stations[i]} ({prices[i]:,}원)" for i in range(len(stations))]
selected_option = st.sidebar.selectbox("목적지를 선택하세요", options)

# 선택된 역의 인덱스를 찾아 가격과 이름 추출
selected_idx = options.index(selected_option)
selected_station = stations[selected_idx]
selected_price = prices[selected_idx]

# [장바구니 담기] 버튼 클릭 로직
if st.sidebar.button("장바구니에 담기"):
    st.session_state.order_list.append(selected_station)
    st.session_state.total_price += selected_price
    # st.rerun()을 쓰지 않고 toast 알림으로 안전하게 처리
    st.toast(f"🛒 {selected_station} 티켓이 장바구니에 담겼습니다.")

# 3. 메인 화면: 장바구니 내역 및 결제 처리
col1, col2 = st.columns(2)

with col1:
    st.markdown("### 🛒 현재 장바구니 내역")
    
    # 장바구니에 내용이 있을 때만 출력
    if st.session_state.order_list:
        for item in st.session_state.order_list:
            st.write(f"- 🎫 [기차표] {item}")
        
        # 장바구니 비우기 버튼
        if st.button("장바구니 비우기"):
            st.session_state.order_list = []
            st.session_state.total_price = 0
            st.write("장바구니를 비웠습니다. 새 티켓을 담아주세요.")
    else:
        st.info("장바구니가 비어 있습니다.")

with col2:
    st.markdown("### 💳 결제하기")