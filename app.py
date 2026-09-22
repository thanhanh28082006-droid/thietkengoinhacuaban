import streamlit as st
import time

st.set_page_config(page_title="Vui Tết Trung Thu", page_icon="🏮", layout="wide")

QUESTIONS = [
    {
        "id": 1,
        "word": "CHÚC",
        "question": "Hình ảnh dưới đây gợi nhớ đến loại bánh truyền thống nào không thể thiếu của dịp Tết Trung Thu?",
        "image": "https://images.unsplash.com/photo-1695428612140-5e3650ce892a?q=80&w=800",
        "options": ["A. Bánh in", "B. Bánh phu thê", "C. Bánh nướng, bánh dẻo", "D. Bánh gai"],
        "answer": "C. Bánh nướng, bánh dẻo"
    },
    {
        "id": 2,
        "word": "CÔ",
        "question": "Lắng nghe giai điệu trong đoạn video sau. Bài hát này gợi nhớ đến nhân vật nào trong sự tích Trung Thu?",
        "video": "https://youtu.be/5xX5pdNHMJM?si=mZVgZ5CbTz4HBWkm",
        "options": ["A. Hậu Nghệ", "B. Chú Cuội", "C. Thiên Lôi", "D. Ngọc Hoàng"],
        "answer": "B. Chú Cuội"
    },
    {
        "id": 3,
        "word": "VÀ",
        "question": "Đây là món đồ chơi rực rỡ làm từ tre và giấy bóng kính đỏ, gắn liền với tuổi thơ đêm rằm. Tên của nó là gì?",
        "image": "https://images.unsplash.com/photo-1599813295980-60b64d0bb033?q=80&w=800",
        "options": ["A. Tò he", "B. Đèn kéo quân", "C. Mặt nạ giấy bồi", "D. Đèn ông sao"],
        "answer": "D. Đèn ông sao"
    },
    {
        "id": 4,
        "word": "CẢ",
        "question": "Con vật thiêng liêng nào thường dẫn đầu đoàn múa rộn ràng trong tiếng trống đêm Trung thu?",
        "image": "mua_lan.jpg", # File hình ảnh offline (cần có trong máy)
        "options": ["A. Con lân", "B. Con rồng", "C. Con cá chép", "D. Con phượng hoàng"],
        "answer": "A. Con lân"
    },
    {
        "id": 5,
        "word": "LỚP",
        "question": "Mâm cỗ tết mang ý nghĩa gia đình đoàn tụ. Ngoài tên gọi 'Tết Thiếu nhi', Tết Trung thu còn được biết đến với tên gọi nào?",
        "options": ["A. Tết Trùng Cửu", "B. Tết Thanh Minh", "C. Tết Đoàn viên", "D. Tết Đoan Ngọ"],
        "answer": "C. Tết Đoàn viên"
    },
    {
        "id": 6,
        "word": "MỘT",
        "question": "Theo truyền thuyết dân gian Việt Nam, Chú Cuội đã vô tình bay lên trời cùng với loài cây nào?",
        "options": ["A. Cây khế", "B. Cây đa", "C. Cây tre", "D. Cây bồ đề"],
        "answer": "B. Cây đa"
    },
    {
        "id": 7,
        "word": "NGÀY",
        "question": "Tết Trung thu hằng năm được tổ chức vào ngày nào theo lịch Âm?",
        "options": ["A. Rằm tháng 7", "B. Rằm tháng 8", "C. Rằm tháng Giêng", "D. Mùng 1 tháng 8"],
        "answer": "B. Rằm tháng 8"
    },
    {
        "id": 8,
        "word": "TRUNG",
        "question": "Nhân vật nữ xinh đẹp, dịu dàng cai quản cung trăng trong tâm thức của người Việt là ai?",
        "options": ["A. Công chúa Bạch Tuyết", "B. Tiên nữ Giáng Hương", "C. Chị Hằng Nga", "D. Mẫu Thượng Ngàn"],
        "answer": "C. Chị Hằng Nga"
    },
    {
        "id": 9,
        "word": "THU",
        "question": "Hoạt động nào dưới đây mà trẻ em cực kỳ thích thú và thường đi cùng nhau vào đêm rằm tháng 8?",
        "options": ["A. Hái lộc", "B. Phá cỗ", "C. Du xuân", "D. Rước đèn"],
        "answer": "D. Rước đèn"
    },
    {
        "id": 10,
        "word": "TỐT",
        "question": "Điệu múa Lân - Sư - Rồng rộn rã trong đêm rằm tháng Tám mang ý nghĩa cầu mong điều gì?",
        "options": ["A. Mưa thuận gió hòa", "B. May mắn, thịnh vượng và bình an", "C. Trúng mùa vụ", "D. Xua đuổi thú dữ"],
        "answer": "B. May mắn, thịnh vượng và bình an"
    },
    {
        "id": 11,
        "word": "LÀNH",
        "question": "Trong mâm cỗ Trung thu, người ta thường dùng những múi của loại quả nào để xếp thành hình chú chó bưởi lấp lánh?",
        "options": ["A. Quả bưởi", "B. Quả dưa hấu", "C. Quả hồng", "D. Quả lựu"],
        "answer": "A. Quả bưởi"
    }
]

# Danh sách Icon lồng đèn dễ thương tương ứng 11 câu
LANTERN_ICONS = ["🐟", "⭐", "🦋", "💖", "🐰", "🐱", "🐯", "🐷", "🐻", "🌸", "🏮"]

if 'revealed_words' not in st.session_state:
    st.session_state.revealed_words = [False] * 11
if 'game_won' not in st.session_state:
    st.session_state.game_won = False
if 'victory_shown' not in st.session_state:
    st.session_state.victory_shown = False

@st.dialog("🏮 THỬ THÁCH TRUNG THU 🏮", width="large")
def show_question_modal(idx):
    q_data = QUESTIONS[idx]
    
    status_key = f"q_status_{idx}"
    if status_key not in st.session_state:
        st.session_state[status_key] = "playing"
    
    st.markdown(f"<div class='question-text'>{q_data['question']}</div>", unsafe_allow_html=True)
    
    # --- CHÈN HÌNH ẢNH HOẶC VIDEO ---
    if "image" in q_data:
        try:
            st.image(q_data["image"], use_container_width=True)
        except Exception:
            st.warning(f"🏮 Khung ảnh trống (Chưa tìm thấy file: '{q_data['image']}'). Lớp mình cứ đọc câu hỏi và trả lời nhé!")
        st.markdown("<br>", unsafe_allow_html=True)
        
    if "video" in q_data:
        try:
            st.video(q_data["video"])
        except Exception:
            st.warning("⚠️ Lỗi không phát được video. Vui lòng kiểm tra lại link hoặc file.")
        st.markdown("<br>", unsafe_allow_html=True)
    
    error_msg_placeholder = st.empty()
    
    if st.session_state[status_key] == "wrong":
        error_msg_placeholder.markdown("<div class='error-message'>❌ Sai rồi! Bạn hãy đọc kỹ và chọn lại đáp án nhé.</div>", unsafe_allow_html=True)
            
    ans_cols = st.columns(2)
    for i, option in enumerate(q_data['options']):
        with ans_cols[i % 2]:
            if st.button(option, key=f"opt_{idx}_{i}", use_container_width=True):
                if option == q_data['answer']:
                    st.session_state[status_key] = "correct"
                    st.session_state.revealed_words[idx] = True
                    st.rerun() 
                else:
                    st.session_state[status_key] = "wrong"
                    error_msg_placeholder.markdown("<div class='error-message'>❌ Sai rồi! Bạn hãy đọc kỹ và chọn lại đáp án nhé.</div>", unsafe_allow_html=True)

st.markdown("""
<style>
    /* Nền Đỏ - Hồng siêu ngọt ngào */
    .stApp { background: linear-gradient(135deg, #ffcdd2, #f8bbd0, #ff8a80); font-family: 'Segoe UI', Tahoma, Geneva, sans-serif; }
    
    /* Khung nội dung */
    .white-container { 
        background-color: rgba(255, 255, 255, 0.9); 
        backdrop-filter: blur(10px); 
        border-radius: 30px; 
        padding: 35px; 
        box-shadow: 0 15px 35px rgba(211, 47, 47, 0.2); 
        border: 4px solid #ff5252; 
        margin-bottom: 25px; 
    }
    
    /* Chữ câu hỏi KHỔNG LỒ, IN ĐẬM */
    .question-text { 
        font-size: 42px; color: #b71c1c; text-align: center; 
        margin-bottom: 30px; font-weight: 900; line-height: 1.4; 
    }
    
    /* Thông báo lỗi đỏ chói, to */
    .error-message { 
        background: linear-gradient(90deg, #ffeb3b, #ffc107); color: #d32f2f; 
        padding: 20px; border-radius: 20px; text-align: center; 
        font-size: 32px; font-weight: 900; margin-bottom: 25px; 
        box-shadow: 0 8px 20px rgba(211, 47, 47, 0.3); 
    }
    
    /* Chữ cái thông điệp lật mở */
    .word-box { 
        display: flex; justify-content: center; align-items: center; 
        height: 120px; background: linear-gradient(145deg, #ff5252, #c62828); 
        color: #fffde7; border-radius: 20px; font-size: 48px; font-weight: 900; 
        box-shadow: inset 0px 6px 12px rgba(255,255,255,0.4), 0px 10px 20px rgba(183, 28, 28, 0.5); 
        text-shadow: 2px 2px 6px rgba(0,0,0,0.5); border: 3px solid #ffd700; margin: 5px; 
    }
    .word-hidden { 
        background: linear-gradient(145deg, #ffffff, #eeeeee); color: #bdbdbd; 
        box-shadow: inset 0px 5px 10px rgba(255,255,255,1), 0px 8px 15px rgba(0,0,0,0.1); 
        border: 3px solid #e0e0e0; text-shadow: none; 
    }
    
    /* BIẾN NÚT BẤM THÀNH VIÊN KẸO/LỒNG ĐÈN CUTE */
    div.stButton > button { 
        border-radius: 50px !important; /* Bo tròn hoàn toàn 2 đầu như viên thuốc/lồng đèn tròn */
        border: 4px solid #FFD700 !important; 
        background: linear-gradient(180deg, #ff8a80 0%, #d32f2f 100%) !important; 
        box-shadow: 0 8px 15px rgba(211, 47, 47, 0.4), inset 0 8px 10px rgba(255,255,255,0.3) !important; 
        transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1.5) !important; 
        min-height: 100px !important;
        height: auto !important;
        padding: 15px 10px !important;
    }
    
    /* ÉP CHỮ TRONG NÚT BẤM SIÊU TO VÀ IN ĐẬM */
    div.stButton > button p, div.stButton > button span, div.stButton > button div { 
        font-size: 36px !important; 
        font-weight: 900 !important; 
        color: #FFFDE7 !important; 
        text-shadow: 2px 2px 4px rgba(0,0,0,0.6) !important; 
        margin: 0 !important;
        white-space: normal !important;
        line-height: 1.3 !important;
    }
    
    /* Hiệu ứng nảy lên khi hover */
    div.stButton > button:hover { 
        border-color: #FFFFFF !important; 
        background: linear-gradient(180deg, #ff5252 0%, #b71c1c 100%) !important; 
        transform: translateY(-8px) scale(1.05) !important; 
        box-shadow: 0 15px 25px rgba(211, 47, 47, 0.6), inset 0 8px 10px rgba(255,255,255,0.5) !important;
    }
    
    /* Trạng thái nút đã tắt (câu đã mở) */
    div.stButton > button:disabled {
        background: linear-gradient(180deg, #e0e0e0 0%, #9e9e9e 100%) !important;
        border-color: #bdbdbd !important;
        transform: none !important;
        box-shadow: inset 0 5px 10px rgba(255,255,255,0.5) !important;
    }
    div.stButton > button:disabled p {
        color: #ffffff !important;
        text-shadow: none !important;
    }
    
    /* Tiêu đề chính */
    .main-title { 
        text-align: center; font-size: 60px; font-weight: 900; margin-bottom: 30px; 
        text-transform: uppercase; color: #b71c1c;
        text-shadow: 3px 3px 0px #FFD700, 5px 5px 10px rgba(0,0,0,0.2); 
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">🌕 ĐÊM HỘI TRĂNG RẰM 🏮</div>', unsafe_allow_html=True)

st.markdown('<div class="white-container">', unsafe_allow_html=True)
cols = st.columns(11) # 11 cột cho 11 chữ
for i, col in enumerate(cols):
    with col:
        if st.session_state.revealed_words[i]:
            st.markdown(f'<div class="word-box">{QUESTIONS[i]["word"]}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="word-box word-hidden">?</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<div style='font-size: 38px; font-weight: 900; color: #b71c1c; margin-bottom: 20px; text-align: center; text-transform: uppercase;'>✨ CHỌN LỒNG ĐÈN ĐỂ GIẢI MÃ ✨</div>", unsafe_allow_html=True)

btn_cols = st.columns(11)
for i, b_col in enumerate(btn_cols):
    with b_col:
        # Nhét icon dễ thương và số vào nút (không còn chữ "Câu")
        btn_label = f"{LANTERN_ICONS[i]} {i+1}" if not st.session_state.revealed_words[i] else "✅"
        if st.button(btn_label, key=f"btn_{i}", disabled=st.session_state.revealed_words[i]):
            show_question_modal(i)

st.markdown("<br><br>", unsafe_allow_html=True)
col_empty1, col_guess, col_empty2 = st.columns([1, 2, 1])
with col_guess:
    st.markdown("<div style='text-align: center; font-size: 32px; font-weight: 900; color: #b71c1c; margin-bottom: 15px;'>💡 Lớp mình đã tìm ra thông điệp chưa?</div>", unsafe_allow_html=True)
    if st.button("🌟 LẬT MỞ TOÀN BỘ THÔNG ĐIỆP 🌟", key="btn_reveal_all", use_container_width=True):
        st.session_state.revealed_words = [True] * 11
        st.session_state.victory_shown = False 
        st.rerun()

@st.dialog("🎉 ĐÊM HỘI TRĂNG RẰM ĐÃ TỎA SÁNG 🎉", width="large")
def show_victory_modal():
    st.balloons()
    st.markdown("""
    <style>
    @keyframes fall {
        0% { transform: translateY(-10vh) rotate(0deg) scale(1); opacity: 1;}
        100% { transform: translateY(100vh) rotate(360deg) scale(1.5); opacity: 0;}
    }
    .flower { position: fixed; font-size: 50px; z-index: 9999; top: -10vh; animation: fall linear forwards; }
    </style>
    <script>
    const flowers = ['🏮', '🌕', '⭐', '✨', '🥮', '🐇', '💖']; 
    for(let i=0; i<70; i++) {
        let f = document.createElement('div');
        f.className = 'flower';
        f.innerText = flowers[Math.floor(Math.random() * flowers.length)];
        f.style.left = Math.random() * 100 + 'vw';
        f.style.animationDuration = (Math.random() * 3 + 2) + 's';
        f.style.animationDelay = Math.random() * 2 + 's';
        window.parent.document.body.appendChild(f);
    }
    </script>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style='text-align: center; padding: 20px 10px;'>
        <h1 style='color: #d32f2f; font-size: 55px; font-weight: 900; margin-bottom: 10px; line-height: 1.4; text-shadow: 2px 2px 5px rgba(0,0,0,0.1);'>
            CHÚC CÔ VÀ CẢ LỚP<br>MỘT NGÀY TRUNG THU TỐT LÀNH
        </h1>
        <p style='color: #ff9800; font-size: 45px; font-weight: 900; margin-top: 25px; text-shadow: 0 0 15px rgba(255, 152, 0, 0.8), 0 0 30px rgba(255, 193, 7, 0.6);'>
            luôn hạnh phúc và ngập tràn niềm vui 🏮🌕
        </p>
    </div>
    <br>
    """, unsafe_allow_html=True)
    
    if st.button("🌟 Tuyệt vời!", use_container_width=True):
        st.session_state.victory_shown = True
        st.rerun()

if all(st.session_state.revealed_words):
    if not st.session_state.victory_shown:
        show_victory_modal() 
    else:
        st.success("🎉 XUẤT SẮC! CẢ LỚP ĐÃ GIẢI MÃ THÀNH CÔNG THÔNG ĐIỆP TRUNG THU!")
