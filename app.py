import streamlit as st
import time

st.set_page_config(page_title="Vui Tết Trung Thu", page_icon="🏮", layout="wide")

QUESTIONS = [
    {
        "id": 1,
        "word": "CHÚC",
        "question": "Hình ảnh dưới đây gợi nhớ đến loại bánh truyền thống nào không thể thiếu của dịp Tết Trung Thu?",
        "image": "https://images.unsplash.com/photo-1601002241512-466e3b2b910e?w=800", # Ảnh Bánh Trung Thu
        "options": ["A. Bánh in", "B. Bánh phu thê", "C. Bánh nướng, bánh dẻo", "D. Bánh gai"],
        "answer": "C. Bánh nướng, bánh dẻo"
    },
    {
        "id": 2,
        "word": "CÔ",
        "question": "Lắng nghe giai điệu trong đoạn video sau. Bài hát này gợi nhớ đến nhân vật nào trong sự tích Trung Thu?",
        "video": "https://www.youtube.com/watch?v=5xX5pdNHMJM", # Video Chú Cuội
        "options": ["A. Hậu Nghệ", "B. Chú Cuội", "C. Thiên Lôi", "D. Ngọc Hoàng"],
        "answer": "B. Chú Cuội"
    },
    {
        "id": 3,
        "word": "VÀ",
        "question": "Đây là món đồ chơi rực rỡ làm từ tre và giấy bóng kính đỏ, gắn liền với tuổi thơ đêm rằm. Tên của nó là gì?",
        "image": "https://images.unsplash.com/photo-1599813295980-60b64d0bb033?w=800", # Ảnh Lồng Đèn
        "options": ["A. Tò he", "B. Đèn kéo quân", "C. Mặt nạ giấy bồi", "D. Đèn ông sao"],
        "answer": "D. Đèn ông sao"
    },
    {
        "id": 4,
        "word": "CẢ",
        "question": "Con vật thiêng liêng nào thường dẫn đầu đoàn múa rộn ràng trong tiếng trống đêm Trung thu?",
        "image": "https://images.unsplash.com/photo-1582236906236-8a9d06283db8?w=800", # Ảnh Múa Lân
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
    
    # Render Hình Ảnh và Video với tỷ lệ đẹp mắt
    if "image" in q_data:
        try:
            st.image(q_data["image"], use_container_width=True)
            st.markdown("<br>", unsafe_allow_html=True)
        except Exception:
            st.warning("⚠️ Đang tải ảnh, lớp mình cứ đọc câu hỏi và trả lời nhé!")
            
    if "video" in q_data:
        try:
            st.video(q_data["video"])
            st.markdown("<br>", unsafe_allow_html=True)
        except Exception:
            st.warning("⚠️ Không tải được video, lớp mình cứ đọc câu hỏi và trả lời nhé!")
    
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
    
    .white-container { 
        background-color: rgba(255, 255, 255, 0.85); backdrop-filter: blur(15px); 
        border-radius: 25px; padding: 35px; box-shadow: 0 20px 40px rgba(211, 47, 47, 0.2); 
        border: 3px solid #ffcdd2; margin-bottom: 25px; 
    }
    
    .question-text { 
        font-size: 38px; color: #b71c1c; text-align: center; 
        margin-bottom: 30px; font-weight: 900; line-height: 1.5; 
        text-shadow: 1px 1px 3px rgba(0,0,0,0.1); 
    }
    
    .error-message { 
        background: linear-gradient(90deg, #ffeb3b, #ffc107); color: #b71c1c; 
        padding: 15px; border-radius: 15px; text-align: center; 
        font-size: 28px; font-weight: 900; margin-bottom: 25px; 
        border-left: 8px solid #d32f2f; box-shadow: 0 4px 15px rgba(211, 47, 47, 0.3); 
    }
    
    /* Ô chứa chữ cái bí mật */
    .word-box { 
        display: flex; justify-content: center; align-items: center; 
        height: 110px; background: linear-gradient(145deg, #f44336, #c62828); 
        color: #fffde7; border-radius: 15px; font-size: 42px; font-weight: 900; 
        box-shadow: inset 0px 6px 12px rgba(255,255,255,0.4), 0px 10px 20px rgba(183, 28, 28, 0.5); 
        text-shadow: 2px 2px 6px rgba(0,0,0,0.5); border: 3px solid #ff8a80; margin: 5px; 
    }
    .word-hidden { 
        background: linear-gradient(145deg, #ffffff, #eeeeee); color: #bdbdbd; 
        box-shadow: inset 0px 5px 10px rgba(255,255,255,1), 0px 8px 15px rgba(0,0,0,0.1); 
        border: 3px solid #e0e0e0; text-shadow: none; 
    }
    
    /* === HIỆU ỨNG LỒNG ĐÈN PHÁT SÁNG & DÂY TREO === */
    /* Tạo khoảng trống phía trên nút để vẽ dây treo */
    div.stButton {
        position: relative;
        margin-top: 30px; 
    }
    
    /* Vẽ sợi dây treo phát sáng bằng CSS ::before */
    div.stButton::before {
        content: '';
        position: absolute;
        top: -30px;
        left: 50%;
        transform: translateX(-50%);
        width: 4px;
        height: 30px;
        background: linear-gradient(to bottom, #FF8C00, #FFD700);
        box-shadow: 0 0 10px #FFD700, 0 0 20px #FFD700;
        border-radius: 2px;
        z-index: 0;
    }

    /* Hiệu ứng nhấp nháy ánh sáng cho Lồng đèn */
    @keyframes lanternGlow {
        0% { box-shadow: 0 0 10px #FFD700, inset 0 5px 15px rgba(255,255,255,0.4); }
        100% { box-shadow: 0 0 30px #FFD700, 0 0 40px #ff5252, inset 0 5px 25px rgba(255,255,255,0.8); }
    }

    /* Định hình nút bấm thành chiếc Lồng đèn bầu bĩnh */
    div.stButton > button { 
        border-radius: 40px !important; 
        border: 4px solid #FFD700 !important; 
        background: radial-gradient(circle at 50% 30%, #ff8a80, #d32f2f) !important;
        animation: lanternGlow 1.5s infinite alternate !important; 
        position: relative;
        z-index: 2;
        min-height: 100px !important;
        height: auto !important;
        padding: 10px 5px !important;
    }
    
    /* Chữ và con vật (🐰 1) hòa làm 1 khối to, rõ ràng */
    div.stButton > button p, div.stButton > button span { 
        font-size: 34px !important; 
        font-weight: 900 !important; 
        color: #FFFDE7 !important; 
        text-shadow: 2px 2px 6px rgba(0,0,0,0.8), 0 0 12px #FFD700 !important; 
        margin: 0 !important;
        font-family: 'Segoe UI', sans-serif !important;
    }
    
    /* Khi rê chuột vào lồng đèn */
    div.stButton > button:hover { 
        border-color: #FFFFFF !important; 
        background: radial-gradient(circle at 50% 30%, #ff5252, #b71c1c) !important; 
        transform: translateY(-5px) scale(1.05) !important; 
    }
    
    /* === XÓA DÂY TREO VÀ CHỈNH LẠI CÁC NÚT ĐÁP ÁN (BÊN TRONG POP-UP) === */
    /* Các nút A B C D không được có dây treo, không chớp nháy */
    div[role="dialog"] div.stButton {
        margin-top: 0px !important;
    }
    div[role="dialog"] div.stButton::before {
        display: none !important; /* Xóa dây treo */
    }
    div[role="dialog"] div.stButton > button {
        animation: none !important; /* Tắt nhấp nháy */
        border-radius: 20px !important; /* Hình viên thuốc */
        background: linear-gradient(135deg, #ffb74d 0%, #f57c00 100%) !important; /* Màu kẹo cam pastel */
        box-shadow: 0 8px 15px rgba(211, 47, 47, 0.3) !important;
    }
    div[role="dialog"] div.stButton > button:hover {
        transform: translateY(-4px) !important;
        background: linear-gradient(135deg, #ffa726 0%, #ef6c00 100%) !important;
    }
    
    /* Lồng đèn bị tắt (Đã mở) */
    div.stButton > button:disabled {
        background: radial-gradient(circle, #e0e0e0, #9e9e9e) !important;
        border-color: #bdbdbd !important;
        animation: none !important;
        transform: none !important;
        box-shadow: inset 0 10px 10px rgba(255,255,255,0.3) !important;
    }
    div.stButton > button:disabled p { color: #ffffff !important; text-shadow: none !important; }
    
    /* Tiêu đề chính */
    .main-title { 
        text-align: center; font-size: 55px; font-weight: 900; margin-bottom: 40px; 
        text-transform: uppercase; background: linear-gradient(to right, #b71c1c, #ff9800, #b71c1c); 
        -webkit-background-clip: text; -webkit-text-fill-color: transparent; 
        text-shadow: 3px 3px 8px rgba(0,0,0,0.15); 
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">🌕 LẬT MỞ ĐÊM HỘI TRĂNG RẰM 🏮</div>', unsafe_allow_html=True)

st.markdown('<div class="white-container">', unsafe_allow_html=True)
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
        # Gom Icon Thú cưng và Số thứ tự vào cùng 1 ô (Ví dụ: 🐰 1)
        btn_label = f"{LANTERN_ICONS[i]} {i+1}" if not st.session_state.revealed_words[i] else "✅"
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
    .flower { position: fixed; font-size: 45px; z-index: 9999; top: -10vh; animation: fall linear forwards; }
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
        <h1 style='color: #d32f2f; font-size: 55px; font-weight: 900; margin-bottom: 10px; line-height: 1.4; text-shadow: 2px 2px 5px rgba(0,0,0,0.1);'>
            CHÚC CÔ VÀ CẢ LỚP<br>MỘT NGÀY TRUNG THU TỐT LÀNH
        </h1>
        <p style='color: #ff9800; font-size: 40px; font-weight: 900; margin-top: 25px; text-shadow: 0 0 15px rgba(255, 152, 0, 0.8), 0 0 30px rgba(255, 193, 7, 0.6);'>
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
