import streamlit as st
import time

# --- CẤU HÌNH TRANG ---
st.set_page_config(page_title="Vui Tết Trung Thu", page_icon="🏮", layout="wide")

# --- DỮ LIỆU 11 CÂU HỎI TRUNG THU ---
QUESTIONS = [
    {
        "id": 1,
        "word": "CHÚC",
        "question": "Hình ảnh dưới đây gợi nhớ đến loại bánh truyền thống nào của dịp Tết Trung Thu?",
        "image": "https://images.unsplash.com/photo-1600832345595-5c1dfa0d9b4b?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80", # Bạn có thể thay bằng file ảnh của bạn ví dụ "banh_trung_thu.jpg"
        "options": ["A. Bánh in", "B. Bánh phu thê", "C. Bánh dẻo", "D. Bánh gai"],
        "answer": "C. Bánh dẻo"
    },
    {
        "id": 2,
        "word": "CÔ",
        "question": "Lắng nghe đoạn nhạc sau. Theo sự tích dân gian Việt Nam, bài hát nhắc đến ai phải ngồi dưới gốc cây đa?",
        "audio": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3", # Bạn có thể để file nhạc của bạn vào cùng thư mục, ví dụ "nhac_cuoi.mp3"
        "options": ["A. Hậu Nghệ", "B. Chú Cuội", "C. Thiên Lôi", "D. Ngọc Hoàng"],
        "answer": "B. Chú Cuội"
    },
    {
        "id": 3,
        "word": "VÀ",
        "question": "Món đồ chơi rực rỡ làm từ tre và giấy bóng kính đỏ, gắn liền với tuổi thơ đêm rằm là gì?",
        "options": ["A. Tò he", "B. Đèn kéo quân", "C. Mặt nạ giấy bồi", "D. Đèn ông sao"],
        "answer": "D. Đèn ông sao"
    },
    {
        "id": 4,
        "word": "CẢ",
        "question": "Con vật thiêng liêng nào thường dẫn đầu đoàn múa rộn ràng trong tiếng trống đêm Trung thu?",
        "options": ["A. Con lân", "B. Con rồng", "C. Con cá chép", "D. Con phượng hoàng"],
        "answer": "A. Con lân"
    },
    {
        "id": 5,
        "word": "LỚP",
        "question": "Ngoài tên gọi 'Tết Thiếu nhi', Tết Trung thu còn được biết đến với tên gọi vô cùng ý nghĩa nào?",
        "options": ["A. Tết Trùng Cửu", "B. Tết Thanh Minh", "C. Tết Đoàn viên", "D. Tết Đoan Ngọ"],
        "answer": "C. Tết Đoàn viên"
    },
    {
        "id": 6,
        "word": "MỘT",
        "question": "Truyền thuyết dân gian kể rằng, chú Cuội đã bay lên trời cùng với loài cây nào?",
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
        "question": "Nhân vật nữ xinh đẹp, dịu dàng cai quản cung trăng cùng Thỏ Ngọc là ai?",
        "options": ["A. Công chúa Bạch Tuyết", "B. Tiên nữ Giáng Hương", "C. Chị Hằng Nga", "D. Mẫu Thượng Ngàn"],
        "answer": "C. Chị Hằng Nga"
    },
    {
        "id": 9,
        "word": "THU",
        "question": "Hoạt động trẻ em quây quần bên mâm quả, bánh kẹo và cùng nhau ăn uống đêm rằm gọi là gì?",
        "options": ["A. Hái lộc", "B. Phá cỗ", "C. Du xuân", "D. Lì xì"],
        "answer": "B. Phá cỗ"
    },
    {
        "id": 10,
        "word": "TỐT",
        "question": "Điệu múa Lân - Sư - Rồng trong đêm rằm tháng Tám mang ý nghĩa cầu mong điều gì?",
        "options": ["A. Mưa thuận gió hòa", "B. May mắn và thịnh vượng", "C. Trúng mùa vụ", "D. Xua đuổi thú dữ"],
        "answer": "B. May mắn và thịnh vượng"
    },
    {
        "id": 11,
        "word": "LÀNH",
        "question": "Trong mâm cỗ Trung thu, người ta thường dùng những múi của loại quả nào để xếp thành hình chú chó lấp lánh?",
        "options": ["A. Quả bưởi", "B. Quả dưa hấu", "C. Quả hồng", "D. Quả lựu"],
        "answer": "A. Quả bưởi"
    }
]

# --- KHỞI TẠO SESSION STATE ---
if 'revealed_words' not in st.session_state:
    st.session_state.revealed_words = [False] * 11 # 11 chữ cái
if 'game_won' not in st.session_state:
    st.session_state.game_won = False
if 'victory_shown' not in st.session_state:
    st.session_state.victory_shown = False

# --- HÀM XỬ LÝ CỬA SỔ POP-UP ---
@st.dialog("🏮 THỬ THÁCH TRUNG THU 🏮", width="large")
def show_question_modal(idx):
    q_data = QUESTIONS[idx]
    
    status_key = f"q_status_{idx}"
    if status_key not in st.session_state:
        st.session_state[status_key] = "playing"
    
    st.markdown(f"<div class='question-text'>{q_data['question']}</div>", unsafe_allow_html=True)
    
    # ---------------- THÊM HÌNH ẢNH / ÂM THANH ----------------
    # Nếu câu hỏi có hình ảnh, hiển thị hình ảnh
    if "image" in q_data and q_data["image"]:
        st.image(q_data["image"], use_container_width=True)
        st.markdown("<br>", unsafe_allow_html=True)
        
    # Nếu câu hỏi có âm thanh, hiển thị trình phát nhạc
    if "audio" in q_data and q_data["audio"]:
        st.audio(q_data["audio"])
        st.markdown("<br>", unsafe_allow_html=True)
    # ----------------------------------------------------------
    
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

# --- CSS GIAO DIỆN ĐỎ TRẮNG - LỒNG ĐÈN ---
st.markdown("""
<style>
    /* Nền Đỏ Trắng Lễ Hội */
    .stApp { 
        background: linear-gradient(135deg, #ffebee, #ffcdd2, #ef9a9a); 
        font-family: 'Segoe UI', Tahoma, Geneva, sans-serif; 
    }
    
    /* Trang trí lồng đèn lấp lánh */
    .lantern-decor {
        position: absolute;
        font-size: 50px;
        opacity: 0.15;
        animation: float 4s ease-in-out infinite;
        z-index: 0;
    }
    .l1 { top: 10px; left: 5%; }
    .l2 { top: 30px; right: 5%; animation-delay: 1s; }
    .l3 { bottom: 20px; left: 10%; animation-delay: 2s; }
    
    @keyframes float {
        0%, 100% { transform: translateY(0) rotate(-5deg); }
        50% { transform: translateY(-15px) rotate(5deg); }
    }

    .white-container { 
        background-color: rgba(255, 255, 255, 0.85); 
        backdrop-filter: blur(15px); 
        border-radius: 25px; 
        padding: 35px; 
        box-shadow: 0 20px 40px rgba(211, 47, 47, 0.2); 
        border: 3px solid #ffcdd2; 
        margin-bottom: 25px; 
        position: relative;
        overflow: hidden;
    }
    
    .question-text { 
        font-size: 34px; 
        color: #b71c1c; 
        text-align: center; 
        margin-bottom: 30px; 
        font-weight: 900; 
        line-height: 1.5; 
        text-shadow: 1px 1px 3px rgba(0,0,0,0.1); 
    }
    
    .error-message { 
        background: linear-gradient(90deg, #ffeb3b, #ffc107); 
        color: #b71c1c; 
        padding: 15px; 
        border-radius: 15px; 
        text-align: center; 
        font-size: 24px; 
        font-weight: 900; 
        margin-bottom: 25px; 
        border-left: 8px solid #d32f2f; 
        box-shadow: 0 4px 15px rgba(211, 47, 47, 0.3);
    }
    
    /* Ô chữ 11 ô cần thu nhỏ xíu để vừa màn hình */
    .word-box { 
        display: flex; justify-content: center; align-items: center; 
        height: 100px; 
        background: linear-gradient(145deg, #f44336, #c62828); 
        color: #fffde7; 
        border-radius: 15px; 
        font-size: 32px; 
        font-weight: 900; 
        box-shadow: inset 0px 6px 12px rgba(255,255,255,0.4), 0px 10px 20px rgba(183, 28, 28, 0.5); 
        text-shadow: 2px 2px 6px rgba(0,0,0,0.5); 
        border: 3px solid #ff8a80; 
        margin: 5px; 
    }
    .word-hidden { 
        background: linear-gradient(145deg, #ffffff, #eeeeee); 
        color: #bdbdbd; 
        box-shadow: inset 0px 5px 10px rgba(255,255,255,1), 0px 8px 15px rgba(0,0,0,0.1); 
        border: 3px solid #e0e0e0; 
        text-shadow: none;
    }
    
    /* Nút bấm (Câu hỏi & Đáp án) Đỏ - Vàng */
    div.stButton > button { 
        border-radius: 20px; 
        font-weight: 900; 
        height: auto; 
        min-height: 85px;
        padding: 10px;
        border: 3px solid #ef5350; 
        background: linear-gradient(to bottom, #ffffff, #ffebee); 
        color: #c62828 !important; 
        box-shadow: 0 6px 15px rgba(183, 28, 28, 0.15); 
        transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1); 
        white-space: normal; 
    }
    div.stButton > button p {
        font-size: 28px !important; /* Chữ siêu bự */
        font-weight: 900 !important; 
        margin: 0 !important;
        color: #c62828 !important;
    }
    div.stButton > button:hover { 
        border-color: #b71c1c; 
        background: linear-gradient(145deg, #e53935, #b71c1c); 
        box-shadow: 0 10px 25px rgba(183, 28, 28, 0.5); 
        transform: translateY(-5px); 
    }
    div.stButton > button:hover p {
        color: #ffffff !important; /* Đổi màu chữ thành trắng khi rê chuột */
    }
    
    /* Tiêu đề chính */
    .main-title { 
        text-align: center; 
        font-size: 55px; 
        font-weight: 900; 
        margin-bottom: 40px; 
        text-transform: uppercase; 
        background: linear-gradient(to right, #b71c1c, #ff9800, #b71c1c); 
        -webkit-background-clip: text; 
        -webkit-text-fill-color: transparent; 
        text-shadow: 3px 3px 8px rgba(0,0,0,0.15); 
    }
</style>
""", unsafe_allow_html=True)

# --- GIAO DIỆN CHÍNH ---
st.markdown('<div class="main-title">🌕 LẬT MỞ ĐÊM HỘI TRĂNG RẰM 🏮</div>', unsafe_allow_html=True)

st.markdown('<div class="white-container"><div class="lantern-decor l1">🏮</div><div class="lantern-decor l2">⭐</div><div class="lantern-decor l3">🌕</div>', unsafe_allow_html=True)
cols = st.columns(11) # 11 cột cho 11 chữ
for i, col in enumerate(cols):
    with col:
        if st.session_state.revealed_words[i]:
            st.markdown(f'<div class="word-box">{QUESTIONS[i]["word"]}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="word-box word-hidden">?</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<div style='font-size: 32px; font-weight: 900; color: #b71c1c; margin-bottom: 20px; text-align: center;'>✨ CHỌN LỒNG ĐÈN ĐỂ GIẢI MÃ:</div>", unsafe_allow_html=True)
btn_cols = st.columns(11) # 11 nút bấm
for i, b_col in enumerate(btn_cols):
    with b_col:
        btn_label = f"Câu {i+1}" if not st.session_state.revealed_words[i] else "✅"
        if st.button(btn_label, key=f"btn_{i}", disabled=st.session_state.revealed_words[i]):
            show_question_modal(i)

st.markdown("<br><br>", unsafe_allow_html=True)
col_empty1, col_guess, col_empty2 = st.columns([1, 2, 1])
with col_guess:
    st.markdown("<div style='text-align: center; font-size: 28px; font-weight: 900; color: #b71c1c; margin-bottom: 15px;'>💡 Lớp mình đã tìm ra thông điệp chưa?</div>", unsafe_allow_html=True)
    if st.button("🌟 LẬT MỞ TOÀN BỘ THÔNG ĐIỆP NGAY 🌟", key="btn_reveal_all", use_container_width=True):
        st.session_state.revealed_words = [True] * 11
        st.session_state.victory_shown = False 
        st.rerun()

# --- POPUP CHIẾN THẮNG ---
@st.dialog("🎉 ĐÊM HỘI TRĂNG RẰM ĐÃ TỎA SÁNG 🎉", width="large")
def show_victory_modal():
    st.balloons()
    # Mưa Bánh Trung Thu, Lồng đèn, Thỏ ngọc
    st.markdown("""
    <style>
    @keyframes fall {
        0% { transform: translateY(-10vh) rotate(0deg); opacity: 1;}
        100% { transform: translateY(100vh) rotate(360deg); opacity: 0;}
    }
    .flower { position: fixed; font-size: 35px; z-index: 9999; top: -10vh; animation: fall linear forwards; }
    </style>
    <script>
    const flowers = ['🏮', '🌕', '⭐', '✨', '🥮', '🐇']; 
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
        <h1 style='color: #d32f2f; font-size: 50px; font-weight: 900; margin-bottom: 10px; line-height: 1.4; text-shadow: 2px 2px 5px rgba(0,0,0,0.1);'>
            CHÚC CÔ VÀ CẢ LỚP<br>MỘT NGÀY TRUNG THU TỐT LÀNH
        </h1>
        <p style='color: #ff9800; font-size: 38px; font-weight: 900; margin-top: 25px; text-shadow: 0 0 15px rgba(255, 152, 0, 0.8), 0 0 30px rgba(255, 193, 7, 0.6);'>
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
