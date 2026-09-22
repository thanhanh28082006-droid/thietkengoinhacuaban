import streamlit as st
import time

st.set_page_config(page_title="Vui Tết Trung Thu", page_icon="🏮", layout="wide")

QUESTIONS = [
    {
        "id": 1,
        "word": "CHÚC",
        "question": "Hình ảnh dưới đây gợi nhớ đến loại bánh truyền thống nào không thể thiếu của dịp Tết Trung Thu?",
        "image": "https://images.pexels.com/photos/10311746/pexels-photo-10311746.jpeg?auto=compress&cs=tinysrgb&w=800", 
        "options": ["A. Bánh in", "B. Bánh phu thê", "C. Bánh nướng, bánh dẻo", "D. Bánh gai"],
        "answer": "C. Bánh nướng, bánh dẻo"
    },
    {
        "id": 2,
        "word": "CÔ",
        "question": "Lắng nghe giai điệu trong đoạn video sau. Bài hát này gợi nhớ đến nhân vật nào trong sự tích Trung Thu?",
        "video": "https://youtu.be/5xX5pdNHMJM?si=mZVgZ5CbTz4HBWkm", # Link YouTube của bạn
        "options": ["A. Hậu Nghệ", "B. Chú Cuội", "C. Thiên Lôi", "D. Ngọc Hoàng"],
        "answer": "B. Chú Cuội"
    },
    {
        "id": 3,
        "word": "VÀ",
        "question": "Đây là món đồ chơi rực rỡ làm từ tre và giấy bóng kính đỏ, gắn liền với tuổi thơ đêm rằm. Tên của nó là gì?",
        "image": "https://images.pexels.com/photos/5418318/pexels-photo-5418318.jpeg?auto=compress&cs=tinysrgb&w=800",
        "options": ["A. Tò he", "B. Đèn kéo quân", "C. Mặt nạ giấy bồi", "D. Đèn ông sao"],
        "answer": "D. Đèn ông sao"
    },
    {
        "id": 4,
        "word": "CẢ",
        "question": "Con vật thiêng liêng nào thường dẫn đầu đoàn múa rộn ràng trong tiếng trống đêm Trung thu?",
        "image": "https://images.pexels.com/photos/3929314/pexels-photo-3929314.jpeg?auto=compress&cs=tinysrgb&w=800", 
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
        "question": "Trong mâm cỗ Trung thu, người ta thường dùng những múi của loại quả nào để xếp thành hình chú chó lấp lánh?",
        "options": ["A. Quả bưởi", "B. Quả dưa hấu", "C. Quả hồng", "D. Quả lựu"],
        "answer": "A. Quả bưởi"
    }
]

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
            st.warning("🏮 Lỗi tải ảnh mạng. Lớp mình cứ đọc câu hỏi và trả lời nhé!")
        st.markdown("<br>", unsafe_allow_html=True)
        
    if "video" in q_data:
        try:
            st.video(q_data["video"])
        except Exception:
            st.warning("⚠️ Lỗi không phát được video.")
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
    .stApp { background: linear-gradient(135deg, #ffebee, #ffcdd2, #ef9a9a); font-family: 'Segoe UI', Tahoma, Geneva, sans-serif; }
    
    .lantern-decor { position: absolute; font-size: 50px; opacity: 0.2; animation: float 4s ease-in-out infinite; z-index: 0; }
    .star-decor { position: absolute; font-size: 30px; opacity: 0.4; animation: twinkle 2s infinite; z-index: 0; }
    .l1 { top: 10px; left: 5%; } .l2 { top: 30px; right: 5%; animation-delay: 1s; } .l3 { bottom: 20px; left: 10%; animation-delay: 2s; }
    .s1 { top: 15%; left: 15%; } .s2 { top: 50%; right: 10%; animation-delay: 1s; } .s3 { bottom: 10%; right: 20%; animation-delay: 0.5s; }
    
    @keyframes float { 0%, 100% { transform: translateY(0) rotate(-5deg); } 50% { transform: translateY(-15px) rotate(5deg); } }
    @keyframes twinkle { 0%, 100% { opacity: 0.2; transform: scale(0.8); } 50% { opacity: 0.8; transform: scale(1.2); } }
    
    .white-container { 
        background-color: rgba(255, 255, 255, 0.85); 
        backdrop-filter: blur(15px); border-radius: 25px; padding: 35px; 
        box-shadow: 0 20px 40px rgba(211, 47, 47, 0.2); border: 3px solid #ffcdd2; 
        margin-bottom: 25px; position: relative; overflow: hidden; 
    }
    
    .question-text { 
        font-size: 38px; color: #b71c1c; text-align: center; 
        margin-bottom: 30px; font-weight: 900; line-height: 1.5; 
    }
    
    .error-message { 
        background: linear-gradient(90deg, #ffeb3b, #ffc107); color: #b71c1c; 
        padding: 15px; border-radius: 15px; text-align: center; 
        font-size: 28px; font-weight: 900; margin-bottom: 25px; border-left: 8px solid #d32f2f; 
    }
    
    .word-box { 
        display: flex; justify-content: center; align-items: center; height: 110px; 
        background: linear-gradient(145deg, #f44336, #c62828); color: #fffde7; 
        border-radius: 15px; font-size: 42px; font-weight: 900; border: 3px solid #ff8a80; margin: 5px; 
    }
    .word-hidden { 
        background: linear-gradient(145deg, #ffffff, #eeeeee); color: #bdbdbd; border: 3px solid #e0e0e0; 
    }
    
    /* GIAO DIỆN LỒNG ĐÈN TRÒN DỄ THƯƠNG (CHỈ CÓ SỐ) */
    div.stButton > button { 
        border-radius: 50% !important; /* Biến thành hình tròn hoàn hảo */
        aspect-ratio: 1 / 1 !important; /* Ép tỷ lệ 1:1 */
        border: 4px solid #FFD700 !important; /* Viền vàng */
        background: radial-gradient(circle at 30% 30%, #ff8a65 0%, #e53935 50%, #b71c1c 100%) !important; 
        box-shadow: 0 10px 20px rgba(183, 28, 28, 0.5), inset 0 10px 15px rgba(255,255,255,0.4), inset 0 -15px 15px rgba(0,0,0,0.4) !important;
        transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1) !important; 
        padding: 0 !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
    }
    
    /* Chữ (số) bên trong lồng đèn */
    div.stButton > button p { 
        font-size: 55px !important; /* Số to khổng lồ */
        font-weight: 900 !important; 
        color: #FFFDE7 !important; 
        text-shadow: 2px 2px 5px rgba(0,0,0,0.8), 0 0 15px #FFD700 !important; 
        margin: 0 !important;
    }
    
    div.stButton > button:hover { 
        border-color: #FFFFFF !important; 
        background: radial-gradient(circle at 30% 30%, #ffab91 0%, #ef5350 50%, #d32f2f 100%) !important; 
        transform: translateY(-8px) scale(1.05) !important; 
    }
    
    div.stButton > button:disabled {
        background: radial-gradient(circle at center, #e0e0e0 0%, #9e9e9e 80%) !important;
        border-color: #bdbdbd !important;
        transform: none !important;
    }
    
    /* Tiêu đề chính */
    .main-title { 
        text-align: center; font-size: 55px; font-weight: 900; margin-bottom: 40px; 
        text-transform: uppercase; background: linear-gradient(to right, #b71c1c, #ff9800, #b71c1c); 
        -webkit-background-clip: text; -webkit-text-fill-color: transparent; 
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">🌕 LẬT MỞ ĐÊM HỘI TRĂNG RẰM 🏮</div>', unsafe_allow_html=True)

st.markdown('<div class="white-container"><div class="lantern-decor l1">🏮</div><div class="lantern-decor l2">🏮</div><div class="lantern-decor l3">🌕</div><div class="star-decor s1">✨</div><div class="star-decor s2">⭐</div><div class="star-decor s3">✨</div>', unsafe_allow_html=True)
cols = st.columns(11) 
for i, col in enumerate(cols):
    with col:
        if st.session_state.revealed_words[i]:
            st.markdown(f'<div class="word-box">{QUESTIONS[i]["word"]}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="word-box word-hidden">?</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<div style='font-size: 36px; font-weight: 900; color: #b71c1c; margin-bottom: 20px; text-align: center; text-transform: uppercase;'>✨ CHỌN LỒNG ĐÈN ĐỂ GIẢI MÃ ✨</div>", unsafe_allow_html=True)

btn_cols = st.columns(11) 
for i, b_col in enumerate(btn_cols):
    with b_col:
        # CHỈ HIỂN THỊ SỐ 1, 2, 3...
        btn_label = f"{i+1}" if not st.session_state.revealed_words[i] else "✅"
        if st.button(btn_label, key=f"btn_{i}", disabled=st.session_state.revealed_words[i]):
            show_question_modal(i)

st.markdown("<br><br>", unsafe_allow_html=True)
col_empty1, col_guess, col_empty2 = st.columns([1, 2, 1])
with col_guess:
    st.markdown("<div style='text-align: center; font-size: 32px; font-weight: 900; color: #b71c1c; margin-bottom: 15px;'>💡 Lớp mình đã tìm ra thông điệp chưa?</div>", unsafe_allow_html=True)
    if st.button("🌟 LẬT MỞ TOÀN BỘ THÔNG ĐIỆP NGAY 🌟", key="btn_reveal_all", use_container_width=True):
        st.session_state.revealed_words = [True] * 11
        st.session_state.victory_shown = False 
        st.rerun()

@st.dialog("🎉 ĐÊM HỘI TRĂNG RẰM ĐÃ TỎA SÁNG 🎉", width="large")
def show_victory_modal():
    st.balloons()
    st.markdown("""
    <style>
    @keyframes fall { 0% { transform: translateY(-10vh) rotate(0deg); opacity: 1;} 100% { transform: translateY(100vh) rotate(360deg); opacity: 0;} }
    .flower { position: fixed; font-size: 40px; z-index: 9999; top: -10vh; animation: fall linear forwards; }
    </style>
    <script>
    const flowers = ['🏮', '🌕', '⭐', '✨', '🥮', '🐇']; 
    for(let i=0; i<70; i++) {
        let f = document.createElement('div'); f.className = 'flower';
        f.innerText = flowers[Math.floor(Math.random() * flowers.length)];
        f.style.left = Math.random() * 100 + 'vw';
        f.style.animationDuration = (Math.random() * 3 + 2) + 's'; f.style.animationDelay = Math.random() * 2 + 's';
        window.parent.document.body.appendChild(f);
    }
    </script>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style='text-align: center; padding: 20px 10px;'>
        <h1 style='color: #d32f2f; font-size: 55px; font-weight: 900; margin-bottom: 10px; line-height: 1.4;'>
            CHÚC CÔ VÀ CẢ LỚP<br>MỘT NGÀY TRUNG THU TỐT LÀNH
        </h1>
        <p style='color: #ff9800; font-size: 40px; font-weight: 900; margin-top: 25px;'>
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
