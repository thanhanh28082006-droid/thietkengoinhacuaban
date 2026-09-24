import streamlit as st
import time

st.set_page_config(page_title="Vui Tết Trung Thu", page_icon="🏮", layout="wide")

# THÔNG ĐIỆP 10 CHỮ: TRĂNG SÁNG NHẤT KHI LÒNG NGƯỜI LUÔN HƯỚNG VỀ NHAU
QUESTIONS = [
    {
        "id": 1,
        "word": "TRĂNG",
        "type": "reveal", 
        "question": "1. Tết Trung thu là Tết đoàn viên, ai ai cũng muốn về nhà. Vậy cái gì trong đêm Trung thu càng đi xa thì lại càng gần, mà càng đứng yên thì lại càng xa?",
        "answer": "Mặt Trăng"
    },
    {
        "id": 2,
        "word": "SÁNG",
        "type": "choice", 
        "question": "2. Ba linh vật trong các điệu múa đêm hội trăng rằm là gì?",
        "options": ["A. Lân – Sư tử – Rồng", "B. Lân – Phượng hoàng – Rồng", "C. Lân – Rồng – Phụng", "D. Lân – Rồng – Rắn"],
        "answer": "A. Lân – Sư tử – Rồng"
    },
    {
        "id": 3,
        "word": "NHẤT",
        "type": "reveal",
        "question": "3. Mỗi năm mỗi độ thu về, Bắc Nam xuôi ngược, chợ quê thị thành. Từng đoàn người ngựa diễu hành, Rước vui trẩy hội lượn quanh ngọn đèn. Là đèn gì?",
        "answer": "Đèn kéo quân"
    },
    {
        "id": 4,
        "word": "KHI",
        "type": "choice",
        "question": "4. Trong truyện cổ tích, chú Cuội vì lý do gì mà phải trốn lên mặt trăng?",
        "options": ["A. Trốn nợ", "B. Mê chị Hằng nên theo chị", "C. Níu giữ cây Đa có phép cải tử hoàn sinh", "D. Bị Ngọc Hoàng bắt đi"],
        "answer": "C. Níu giữ cây Đa có phép cải tử hoàn sinh"
    },
    {
        "id": 5,
        "word": "LÒNG",
        "type": "reveal",
        "question": "5. Khi bị kéo lên Cung Trăng, Chú Cuội mang theo vật gì?",
        "answer": "Cây rìu"
    },
    {
        "id": 6,
        "word": "NGƯỜI",
        "type": "reveal",
        "question": "6. Mặt thì đỏ choét, bụng thì to<br>Đi cùng chú lân, gõ cộc cạch<br>Quạt mo phe phẩy, miệng cười toe<br>Lũ trẻ đuổi theo, reo hò thích chí?<br>(Là ai?)",
        "answer": "Ông Địa"
    },
    {
        "id": 7,
        "word": "LUÔN",
        "type": "reveal",
        "question": "7. Đuổi hình bắt chữ: Đây là gì?",
        "image": "anh7.png", # Đã khớp với file trên GitHub của bạn
        "answer": "Mâm cỗ thưởng Nguyệt"
    },
    {
        "id": 8,
        "word": "HƯỚNG",
        "type": "reveal",
        "question": "8. Đuổi hình bắt chữ: Đây là gì?",
        "image": "anh8.png", # Đã khớp với file trên GitHub của bạn
        "answer": "Cây đa"
    },
    {
        "id": 9,
        "word": "VỀ",
        "type": "choice",
        "question": "9. Lắng nghe giai điệu sau đây. Theo bạn, bài hát này mang tên là gì?",
        "audio": "buontrang.mp3", # Đã ghép file âm thanh
        "options": ["A. Trăng vàng", "B. Đêm trăng", "C. Buồn Trăng", "D. Vầng trăng"],
        "answer": "C. Buồn Trăng"
    },
    {
        "id": 10,
        "word": "NHAU",
        "type": "choice",
        "question": "10. Lắng nghe giai điệu rộn ràng sau đây. Nhạc phẩm này có tên là gì?",
        "audio": "hoitrangram.mp3", # Đã ghép file âm thanh
        "options": ["A. Ngày hội trăng tròn", "B. Hội Trăng Rằm", "C. Đêm nghe hội trăng", "D. Hội trăng tròn"],
        "answer": "B. Hội Trăng Rằm"
    }
]

# Đổi thành 10 chữ cái tương ứng với 10 câu
if 'revealed_words' not in st.session_state:
    st.session_state.revealed_words = [False] * 10
if 'game_won' not in st.session_state:
    st.session_state.game_won = False
if 'victory_shown' not in st.session_state:
    st.session_state.victory_shown = False

@st.dialog("🏮 Giải mã cùng chúng mình 🏮", width="large")
def show_question_modal(idx):
    q_data = QUESTIONS[idx]
    
    status_key = f"q_status_{idx}"
    if status_key not in st.session_state:
        st.session_state[status_key] = "playing"
        
    # Key để theo dõi việc hiển thị đáp án cho câu hỏi mở
    show_answer_key = f"show_answer_{idx}"
    if show_answer_key not in st.session_state:
        st.session_state[show_answer_key] = False
    
    st.markdown(f"<div class='question-text'>{q_data['question']}</div>", unsafe_allow_html=True)
    
    # Xử lý Hình ảnh
    if "image" in q_data:
        try:
            st.image(q_data["image"], use_container_width=True)
        except Exception:
            st.warning(f"🏮 Khung ảnh trống (Chưa tìm thấy file: '{q_data['image']}').")
        st.markdown("<br>", unsafe_allow_html=True)
        
    # Xử lý Video
    if "video" in q_data:
        try:
            st.video(q_data["video"])
        except Exception:
            st.warning("⚠️ Lỗi không phát được video.")
        st.markdown("<br>", unsafe_allow_html=True)
        
    # Xử lý Âm thanh (Audio mp3)
    if "audio" in q_data:
        try:
            st.audio(q_data["audio"])
        except Exception:
            st.warning(f"⚠️ Khung nhạc trống (Chưa tìm thấy file: '{q_data['audio']}').")
        st.markdown("<br>", unsafe_allow_html=True)
    
    error_msg_placeholder = st.empty()
    if st.session_state[status_key] == "wrong":
        error_msg_placeholder.markdown("<div class='error-message'>❌ Sai rồi! Bạn hãy thử lại nhé.</div>", unsafe_allow_html=True)
            
    # PHÂN BIỆT 2 DẠNG CÂU HỎI
    if q_data.get("type") == "reveal":
        # Dạng Câu hỏi Mở: Hiển thị đáp án và lật chữ cùng lúc
        if not st.session_state[show_answer_key]:
            if st.button("🎁 MỞ ĐÁP ÁN", key=f"btn_reveal_first_{idx}", use_container_width=True, type="secondary"):
                st.session_state[show_answer_key] = True
                st.session_state.revealed_words[idx] = True # Lật ô chữ ở màn hình chính cùng lúc
                st.rerun()
        else:
            # Khi đã bấm mở, hiển thị đáp án. Cửa sổ giữ nguyên cho đến khi bấm ĐÓNG
            st.markdown(f"<div style='text-align: center; font-size: 32px; font-weight: 900; color: #d32f2f; margin: 20px 0; padding: 20px; background-color: #ffebee; border-radius: 15px; border: 2px dashed #f44336;'>Đáp án: {q_data['answer']}</div>", unsafe_allow_html=True)
            if st.button("❌ ĐÓNG", key=f"btn_reveal_final_{idx}", use_container_width=True, type="primary"):
                st.rerun() 
                
    else:
        # Dạng Trắc nghiệm A B C D
        if not st.session_state[show_answer_key]:
            ans_cols = st.columns(2)
            for i, option in enumerate(q_data['options']):
                with ans_cols[i % 2]:
                    if st.button(option, key=f"opt_{idx}_{i}", use_container_width=True, type="secondary"):
                        if option == q_data['answer']:
                            # Trả lời đúng -> Hiện thông báo thành công và nút Đóng
                            st.session_state[status_key] = "playing" # Xóa thông báo lỗi nếu có
                            st.session_state[show_answer_key] = True
                            st.session_state.revealed_words[idx] = True
                            st.rerun() 
                        else:
                            st.session_state[status_key] = "wrong"
                            st.rerun()
        else:
            # Khi đã trả lời đúng, hiển thị màn hình chúc mừng
            st.markdown("<div style='text-align: center; font-size: 32px; font-weight: 900; color: #2e7d32; margin: 20px 0; padding: 20px; background-color: #e8f5e9; border-radius: 15px; border: 2px dashed #4caf50;'>✅ CHÍNH XÁC!</div>", unsafe_allow_html=True)
            st.markdown(f"<div style='text-align: center; font-size: 28px; font-weight: 700; color: #d32f2f; margin-bottom: 20px;'>Đáp án: {q_data['answer']}</div>", unsafe_allow_html=True)
            if st.button("❌ ĐÓNG", key=f"btn_close_correct_{idx}", use_container_width=True, type="primary"):
                st.rerun()

st.markdown("""
<style>
    /* Nền Đỏ - Hồng Trung Thu */
    .stApp { background: linear-gradient(135deg, #ffebee, #ffcdd2, #ef9a9a); font-family: 'Segoe UI', Tahoma, Geneva, sans-serif; }
    
    /* Trang trí Lồng đèn & Ngôi sao */
    .lantern-decor { position: absolute; font-size: 50px; opacity: 0.2; animation: float 4s ease-in-out infinite; z-index: 0; }
    .star-decor { position: absolute; font-size: 30px; opacity: 0.4; animation: twinkle 2s infinite; z-index: 0; }
    .l1 { top: 10px; left: 5%; } .l2 { top: 30px; right: 5%; animation-delay: 1s; } .l3 { bottom: 20px; left: 10%; animation-delay: 2s; }
    .s1 { top: 15%; left: 15%; } .s2 { top: 50%; right: 10%; animation-delay: 1s; } .s3 { bottom: 10%; right: 20%; animation-delay: 0.5s; }
    
    @keyframes float { 0%, 100% { transform: translateY(0) rotate(-5deg); } 50% { transform: translateY(-15px) rotate(5deg); } }
    @keyframes twinkle { 0%, 100% { opacity: 0.2; transform: scale(0.8); } 50% { opacity: 0.8; transform: scale(1.2); } }
    
    /* Khung nội dung trắng */
    .white-container { 
        background-color: rgba(255, 255, 255, 0.85); backdrop-filter: blur(15px); border-radius: 25px; 
        padding: 35px; box-shadow: 0 20px 40px rgba(211, 47, 47, 0.2); border: 3px solid #ffcdd2; 
        margin-bottom: 25px; position: relative; overflow: hidden; 
    }
    
    .question-text { font-size: 38px; color: #b71c1c; text-align: center; margin-bottom: 30px; font-weight: 900; line-height: 1.5; text-shadow: 1px 1px 3px rgba(0,0,0,0.1); }
    .error-message { background: linear-gradient(90deg, #ffeb3b, #ffc107); color: #b71c1c; padding: 15px; border-radius: 15px; text-align: center; font-size: 28px; font-weight: 900; margin-bottom: 25px; border-left: 8px solid #d32f2f; box-shadow: 0 4px 15px rgba(211, 47, 47, 0.3); }
    
    /* Chữ cái thông điệp lật mở */
    .word-box { 
        display: flex; justify-content: center; align-items: center; height: 85px; 
        background: linear-gradient(145deg, #f44336, #c62828); color: #fffde7; 
        border-radius: 40px; /* Làm ô tròn tròn giống viên thuốc/viên kẹo */
        font-size: 19px; /* Thu nhỏ chữ để vừa khít 1 dòng, không bị tràn mép */
        font-weight: 900; box-shadow: inset 0px 6px 12px rgba(255,255,255,0.4), 0px 10px 20px rgba(183, 28, 28, 0.5); 
        text-shadow: 2px 2px 6px rgba(0,0,0,0.5); border: 3px solid #ff8a80; 
        margin: 5px 0px; 
        white-space: nowrap; /* Lệnh cấm tuyệt đối chữ rớt dòng */
        overflow: visible;
        text-align: center;
        padding: 0;
        letter-spacing: -0.5px; /* Ép khoảng cách các chữ lại gần nhau 1 chút */
    }
    .word-hidden { background: linear-gradient(145deg, #ffffff, #eeeeee); color: #bdbdbd; box-shadow: inset 0px 5px 10px rgba(255,255,255,1), 0px 8px 15px rgba(0,0,0,0.1); border: 3px solid #e0e0e0; text-shadow: none; font-size: 38px;}
    
    /* Khoảng cách giữa các cột trong Streamlit */
    div[data-testid="column"] {
        padding: 0 5px; /* Tạo khoảng trống giữa các cột */
    }

    /* ============================================== */
    /* 1. LỒNG ĐÈN THÚ CƯNG DỄ THƯƠNG (Type Primary) */
    /* ============================================== */
    button[kind="primary"] { 
        border-radius: 50% !important; 
        border: 4px solid #FFD700 !important; 
        background: radial-gradient(circle at center, #ff7961 0%, #d32f2f 80%) !important; 
        box-shadow: 0 10px 20px rgba(183, 28, 28, 0.5), inset 0 10px 15px rgba(255,255,255,0.5), inset 0 -10px 15px rgba(0,0,0,0.6), 0 0 15px #FFD700 !important; 
        transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1) !important; 
        height: 80px !important;
        position: relative !important;
        overflow: visible !important; /* CẤM CẮT CHỮ */
        white-space: nowrap !important; /* CẤM XUỐNG DÒNG */
        padding: 0 !important;
        margin-top: 20px !important;
    }
    /* Dây treo lồng đèn tỏa sáng */
    button[kind="primary"]::before {
        content: ''; position: absolute; top: -30px; left: 50%; transform: translateX(-50%);
        width: 3px; height: 30px; background: #FFD700; box-shadow: 0 0 8px #FFD700;
    }
    /* Chữ bên trong Lồng Đèn (Icon + Số) */
    button[kind="primary"] p { 
        font-size: 24px !important; /* Chỉnh nhỏ lại xíu cho vừa 10 cột */
        font-weight: 900 !important; 
        color: #FFFDE7 !important; 
        text-shadow: 2px 2px 5px rgba(0,0,0,0.8), 0 0 10px #FFD700 !important; 
        margin: 0 !important;
        letter-spacing: 0px !important;
    }
    button[kind="primary"]:hover { 
        background: radial-gradient(circle at center, #ff8a80 0%, #b71c1c 80%) !important; 
        transform: translateY(-8px) scale(1.1) !important; 
        box-shadow: 0 15px 30px rgba(183, 28, 28, 0.8), 0 0 25px rgba(255, 215, 0, 1) !important;
    }
    button[kind="primary"]:disabled {
        background: radial-gradient(circle at center, #e0e0e0 0%, #9e9e9e 80%) !important;
        border-color: #bdbdbd !important; transform: none !important; box-shadow: none !important;
    }
    
    /* ============================================== */
    /* 2. NÚT ĐÁP ÁN DỄ THƯƠNG (Type Secondary) */
    /* ============================================== */
    button[kind="secondary"] {
        border-radius: 40px !important; /* Tròn như viên kẹo */
        border: 3px solid #ffcc80 !important;
        background: linear-gradient(145deg, #fff3e0, #ffe0b2) !important;
        color: #e65100 !important;
        box-shadow: 0 6px 15px rgba(230, 81, 0, 0.15) !important;
        transition: all 0.3s ease !important;
        min-height: 80px !important;
        white-space: normal !important; /* Cho phép rớt dòng nếu đáp án dài */
    }
    button[kind="secondary"] p {
        font-size: 26px !important;
        font-weight: 900 !important;
        margin: 0 !important;
    }
    button[kind="secondary"]:hover {
        transform: translateY(-5px) !important;
        box-shadow: 0 10px 20px rgba(230, 81, 0, 0.3) !important;
        background: linear-gradient(145deg, #ffe0b2, #ffcc80) !important;
        border-color: #ff9800 !important;
        color: #d84315 !important;
    }

    .main-title { text-align: center; font-size: 55px; font-weight: 900; margin-bottom: 40px; text-transform: uppercase; background: linear-gradient(to right, #b71c1c, #ff9800, #b71c1c); -webkit-background-clip: text; -webkit-text-fill-color: transparent; text-shadow: 3px 3px 8px rgba(0,0,0,0.15); }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">🌕 GIẢI MÃ ĐÊM TRĂNG 🏮</div>', unsafe_allow_html=True)

st.markdown('<div class="white-container"><div class="lantern-decor l1">🏮</div><div class="lantern-decor l2">🏮</div><div class="lantern-decor l3">🌕</div><div class="star-decor s1">✨</div><div class="star-decor s2">⭐</div><div class="star-decor s3">✨</div>', unsafe_allow_html=True)
# Chia thành 10 cột cho 10 chữ
cols = st.columns(10)
for i, col in enumerate(cols):
    with col:
        if st.session_state.revealed_words[i]:
            st.markdown(f'<div class="word-box">{QUESTIONS[i]["word"]}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="word-box word-hidden">?</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<div style='font-size: 36px; font-weight: 900; color: #b71c1c; margin-bottom: 30px; text-align: center; text-transform: uppercase;'>✨ CHỌN LỒNG ĐÈN ĐỂ GIẢI MÃ ✨</div>", unsafe_allow_html=True)

# 10 Icon dễ thương cho 10 lồng đèn
lantern_emojis = ['🐟', '⭐', '🦋', '💖', '🐰', '🐱', '🐯', '🐷', '🐻', '🌸']

# Chia thành 10 cột cho nút lồng đèn
btn_cols = st.columns(10)
for i, b_col in enumerate(btn_cols):
    with b_col:
        btn_label = f"{lantern_emojis[i]} {i+1}" if not st.session_state.revealed_words[i] else "✅"
        if st.button(btn_label, key=f"btn_{i}", disabled=st.session_state.revealed_words[i], type="primary"):
            show_question_modal(i)

st.markdown("<br><br>", unsafe_allow_html=True)
col_empty1, col_guess, col_empty2 = st.columns([1, 2, 1])
with col_guess:
    st.markdown("<div style='text-align: center; font-size: 32px; font-weight: 900; color: #b71c1c; margin-bottom: 15px;'>💡 Lớp mình đã tìm ra thông điệp chưa?</div>", unsafe_allow_html=True)
    if st.button("🌟 LẬT MỞ TOÀN BỘ THÔNG ĐIỆP NGAY 🌟", key="btn_reveal_all", use_container_width=True, type="secondary"):
        st.session_state.revealed_words = [True] * 10
        st.session_state.victory_shown = False 
        st.rerun()

@st.dialog("🎉 ĐÊM HỘI TRĂNG RẰM ĐÃ TỎA SÁNG 🎉", width="large")
def show_victory_modal():
    st.balloons()
    st.markdown("""
    <style>
    @keyframes fall {
        0% { transform: translateY(-10vh) rotate(0deg); opacity: 1;}
        100% { transform: translateY(100vh) rotate(360deg); opacity: 0;}
    }
    .flower { position: fixed; font-size: 40px; z-index: 9999; top: -10vh; animation: fall linear forwards; }
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
            THÔNG ĐIỆP TRUNG THU
        </h1>
        <p style='color: #ff9800; font-size: 40px; font-weight: 900; margin-top: 25px; text-shadow: 0 0 15px rgba(255, 152, 0, 0.8), 0 0 30px rgba(255, 193, 7, 0.6);'>
            "Trăng sáng nhất khi lòng người luôn hướng về nhau" 🏮🌕
        </p>
    </div>
    <br>
    """, unsafe_allow_html=True)
    
    if st.button("🌟 Tuyệt vời!", use_container_width=True, type="secondary"):
        st.session_state.victory_shown = True
        st.rerun()

if all(st.session_state.revealed_words):
    if not st.session_state.victory_shown:
        show_victory_modal() 
    else:
        st.success("🎉 XUẤT SẮC! CẢ LỚP ĐÃ GIẢI MÃ THÀNH CÔNG THÔNG ĐIỆP TRUNG THU!")
