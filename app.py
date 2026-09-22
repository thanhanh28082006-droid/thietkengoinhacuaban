import streamlit as st
import time

# --- CẤU HÌNH TRANG ---
st.set_page_config(page_title="Vui Tết Trung Thu", page_icon="🏮", layout="wide")

QUESTIONS = [
    {
        "id": 1,
        "word": "CHÚC",
        "question": "Tết Trung thu là Tết đoàn viên, ai ai cũng muốn về nhà. Vậy cái gì trong đêm Trung thu càng đi xa thì lại càng gần, mà càng đứng yên thì lại càng xa?",
        "options": ["A. Ngôi sao", "B. Mặt Trăng", "C. Cơn gió", "D. Đám mây"],
        "answer": "B. Mặt Trăng"
    },
    {
        "id": 2,
        "word": "CÔ",
        "question": "Ba linh vật trong các điệu múa đêm hội trăng rằm là gì?",
        "options": ["A. Lân – Sư tử – Rồng", "B. Lân – Phượng hoàng – Rồng", "C. Lân – Rồng – Phụng", "D. Lân – Rồng – Rắn"],
        "answer": "A. Lân – Sư tử – Rồng"
    },
    {
        "id": 3,
        "word": "VÀ",
        "question": "Mỗi năm mỗi độ thu về, Bắc Nam xuôi ngược, chợ quê thị thành, Từng đoàn người ngựa diễu hành, Rước vui trẩy hội lượn quanh ngọn đèn - Là đèn gì?",
        "options": ["A. Đèn ông sao", "B. Đèn kéo quân", "C. Đèn cá chép", "D. Đèn lồng đỏ"],
        "answer": "B. Đèn kéo quân"
    },
    {
        "id": 4,
        "word": "CẢ",
        "question": "Trong truyện cổ tích, chú Cuội vì lý do gì mà phải trốn lên mặt trăng?",
        "options": ["A. Trốn nợ", "B. Mê chị Hằng nên theo chị", "C. Níu giữ cây Đa có phép cải tử hoàn sinh", "D. Đi lạc"],
        "answer": "C. Níu giữ cây Đa có phép cải tử hoàn sinh"
    },
    {
        "id": 5,
        "word": "LỚP",
        "question": "Khi bị kéo lên Cung Trăng, Chú Cuội mang theo vật gì?",
        "options": ["A. Cây rìu", "B. Con dao", "C. Cuộn dây", "D. Thanh kiếm"],
        "answer": "A. Cây rìu"
    },
    {
        "id": 6,
        "word": "MỘT",
        "question": "Mặt thì đỏ choét, bụng thì to. Đi cùng chú lân, gõ cộc cạch. Quạt mo phe phẩy, miệng cười toe. Lũ trẻ đuổi theo, reo hò thích chí? (Là ai?)",
        "options": ["A. Ông Địa", "B. Chú Cuội", "C. Thần Tài", "D. Ông Bụt"],
        "answer": "A. Ông Địa"
    },
    {
        "id": 7,
        "word": "NGÀY",
        "question": "7. Đuổi hình bắt chữ: Đây là gì?",
        "image": "hinh7.jpg", 
        "type": "reveal",
        "answer": "Mâm cỗ thưởng Nguyệt"
    },
    {
        "id": 8,
        "word": "TRUNG",
        "question": "8. Đuổi hình bắt chữ: Đây là gì?",
        "image": "hinh8.png", 
        "type": "reveal",
        "answer": "Cây đa"
    },
    {
        "id": 9,
        "word": "THU",
        "question": "Tết Trung thu hằng năm được tổ chức vào ngày nào theo lịch Âm?",
        "options": ["A. Rằm tháng 7", "B. Rằm tháng 8", "C. Rằm tháng Giêng", "D. Mùng 1 tháng 8"],
        "answer": "B. Rằm tháng 8"
    },
    {
        "id": 10,
        "word": "TỐT",
        "question": "Nhân vật nữ xinh đẹp, dịu dàng cai quản cung trăng trong tâm thức của người Việt là ai?",
        "options": ["A. Bạch Tuyết", "B. Tiên nữ Giáng Hương", "C. Chị Hằng Nga", "D. Mẫu Thượng Ngàn"],
        "answer": "C. Chị Hằng Nga"
    },
    {
        "id": 11,
        "word": "LÀNH",
        "question": "Hoạt động nào dưới đây mà trẻ em cực kỳ thích thú và thường đi cùng nhau vào đêm rằm tháng 8?",
        "options": ["A. Hái lộc", "B. Phá cỗ", "C. Du xuân", "D. Rước đèn"],
        "answer": "D. Rước đèn"
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
    show_answer_key = f"show_ans_{idx}"
    
    if status_key not in st.session_state:
        st.session_state[status_key] = "playing"
    if show_answer_key not in st.session_state:
        st.session_state[show_answer_key] = False
    
    st.markdown(f"<div class='question-text'>{q_data['question']}</div>", unsafe_allow_html=True)
    
    # Hiển thị hình ảnh nếu có
    if "image" in q_data:
        try:
            st.image(q_data["image"], use_container_width=True)
        except Exception:
            st.warning(f"🏮 Khung ảnh trống (Chưa tìm thấy file: '{q_data['image']}'). Hãy đảm bảo bạn đã tải file ảnh lên GitHub cùng thư mục với code!")
        st.markdown("<br>", unsafe_allow_html=True)
        
    error_msg_placeholder = st.empty()
    
    if st.session_state[status_key] == "wrong":
        error_msg_placeholder.markdown("<div class='error-message'>❌ Sai rồi! Bạn hãy đọc kỹ và chọn lại đáp án nhé.</div>", unsafe_allow_html=True)
            
    # Phân biệt dạng câu hỏi Reveal (Tự luận) và trắc nghiệm A B C D
    if q_data.get("type") == "reveal":
        if not st.session_state[show_answer_key]:
            if st.button("🎁 MỞ ĐÁP ÁN", key=f"btn_reveal_{idx}", use_container_width=True):
                st.session_state[show_answer_key] = True
                st.session_state.revealed_words[idx] = True # Lật chữ bên ngoài ngay lập tức
                st.rerun()
        else:
            st.markdown(f"<div style='text-align: center; font-size: 36px; font-weight: 900; color: #d32f2f; margin: 20px 0; padding: 20px; background-color: #ffebee; border-radius: 15px; border: 2px dashed #f44336;'>ĐÁP ÁN: {q_data['answer']}</div>", unsafe_allow_html=True)
            st.success("✨ Chữ trên bảng đã được lật mở! Khung vẫn giữ nguyên để lớp xem, cô hãy bấm dấu X ở góc trên bên phải để đóng bảng này lại nhé.")
    else:
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
    /* Nền Đỏ - Hồng Trung Thu */
    .stApp { background: linear-gradient(135deg, #ffebee, #ffcdd2, #ef9a9a); font-family: 'Segoe UI', Tahoma, Geneva, sans-serif; }
    
    /* Trang trí Lồng đèn & Ngôi sao lơ lửng */
    .lantern-decor { position: absolute; font-size: 50px; opacity: 0.2; animation: float 4s ease-in-out infinite; z-index: 0; }
    .star-decor { position: absolute; font-size: 30px; opacity: 0.4; animation: twinkle 2s infinite; z-index: 0; }
    .l1 { top: 10px; left: 5%; } .l2 { top: 30px; right: 5%; animation-delay: 1s; } .l3 { bottom: 20px; left: 10%; animation-delay: 2s; }
    .s1 { top: 15%; left: 15%; } .s2 { top: 50%; right: 10%; animation-delay: 1s; } .s3 { bottom: 10%; right: 20%; animation-delay: 0.5s; }
    
    @keyframes float { 0%, 100% { transform: translateY(0) rotate(-5deg); } 50% { transform: translateY(-15px) rotate(5deg); } }
    @keyframes twinkle { 0%, 100% { opacity: 0.2; transform: scale(0.8); } 50% { opacity: 0.8; transform: scale(1.2); } }
    
    /* Khung nội dung trắng */
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
    
    /* Chữ câu hỏi siêu to in đậm */
    .question-text { 
        font-size: 36px; color: #b71c1c; text-align: center; 
        margin-bottom: 30px; font-weight: 900; line-height: 1.5; 
        text-shadow: 1px 1px 3px rgba(0,0,0,0.1); 
    }
    
    /* Thông báo lỗi đỏ chói */
    .error-message { 
        background: linear-gradient(90deg, #ffeb3b, #ffc107); color: #b71c1c; 
        padding: 15px; border-radius: 15px; text-align: center; 
        font-size: 26px; font-weight: 900; margin-bottom: 25px; 
        border-left: 8px solid #d32f2f; box-shadow: 0 4px 15px rgba(211, 47, 47, 0.3); 
    }
    
    /* Chữ cái thông điệp lật mở */
    .word-box { 
        display: flex; justify-content: center; align-items: center; 
        height: 110px; background: linear-gradient(145deg, #f44336, #c62828); 
        color: #fffde7; border-radius: 15px; font-size: 40px; font-weight: 900; 
        box-shadow: inset 0px 6px 12px rgba(255,255,255,0.4), 0px 10px 20px rgba(183, 28, 28, 0.5); 
        text-shadow: 2px 2px 6px rgba(0,0,0,0.5); border: 3px solid #ff8a80; margin: 2px; 
    }
    .word-hidden { 
        background: linear-gradient(145deg, #ffffff, #eeeeee); color: #bdbdbd; 
        box-shadow: inset 0px 5px 10px rgba(255,255,255,1), 0px 8px 15px rgba(0,0,0,0.1); 
        border: 3px solid #e0e0e0; text-shadow: none; 
    }
    
    /* DÂY TREO VÀ LỒNG ĐÈN THÚ CƯNG 3D CHO 11 CÂU */
    div.stButton > button { 
        border-radius: 50% 50% 20% 20% / 40% 40% 30% 30% !important;
        border: 3px solid #FFD700 !important;
        background: radial-gradient(ellipse at center, #ff5252 0%, #b71c1c 85%) !important;
        box-shadow: 0 8px 15px rgba(183, 28, 28, 0.4), inset 0 10px 10px rgba(255,255,255,0.4), inset 0 -10px 10px rgba(0,0,0,0.4) !important;
        transition: all 0.3s ease !important;
        min-height: 100px !important;
        height: auto !important;
        padding: 5px 2px !important;
        position: relative;
    }
    
    /* VẼ DÂY TREO VÀO PHÍA TRÊN NÚT LỒNG ĐÈN */
    div.stButton > button::before {
        content: '';
        position: absolute;
        top: -15px;
        left: 50%;
        transform: translateX(-50%);
        width: 3px;
        height: 15px;
        background-color: #FFD700;
        z-index: 1;
    }
    
    /* Chữ bên trong lồng đèn: Ép hiển thị rõ số và icon, cấm cắt chữ */
    div.stButton > button p { 
        font-size: 20px !important; 
        font-weight: 900 !important; 
        color: #FFFDE7 !important; 
        text-shadow: 1px 1px 3px rgba(0,0,0,0.8), 0 0 8px #FFD700 !important; 
        margin: 0 !important;
        white-space: nowrap !important;
        overflow: visible !important;
    }
    
    /* Hiệu ứng khi rê chuột vào Lồng đèn */
    div.stButton > button:hover { 
        border-color: #FFFFFF !important; 
        background: radial-gradient(ellipse at center, #ff7961 0%, #d32f2f 85%) !important; 
        transform: translateY(-5px) scale(1.05) !important; 
        box-shadow: 0 12px 25px rgba(183, 28, 28, 0.7), 0 0 15px rgba(255, 215, 0, 0.6) !important;
    }
    
    /* Lồng đèn đã mở (màu xám) */
    div.stButton > button:disabled {
        background: radial-gradient(ellipse at center, #e0e0e0 0%, #9e9e9e 85%) !important;
        border-color: #bdbdbd !important;
        transform: none !important;
        box-shadow: inset 0 8px 8px rgba(255,255,255,0.3) !important;
    }
    div.stButton > button:disabled::before { background-color: #bdbdbd !important; }
    div.stButton > button:disabled p { color: #ffffff !important; text-shadow: none !important; }
    
    /* Tiêu đề chính */
    .main-title { 
        text-align: center; font-size: 52px; font-weight: 900; margin-bottom: 35px; 
        text-transform: uppercase; background: linear-gradient(to right, #b71c1c, #ff9800, #b71c1c); 
        -webkit-background-clip: text; -webkit-text-fill-color: transparent; 
        text-shadow: 3px 3px 8px rgba(0,0,0,0.15); 
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

st.markdown("<div style='font-size: 34px; font-weight: 900; color: #b71c1c; margin-bottom: 25px; text-align: center; text-transform: uppercase;'>✨ CHỌN LỒNG ĐÈN ĐỂ GIẢI MÃ ✨</div>", unsafe_allow_html=True)

# Danh sách icon thú cưng gắn vào 11 lồng đèn
animal_icons = ["🐟", "⭐", "🦋", "💖", "🐰", "🐱", "🐯", "🐷", "🐻", "🌸", "🏮"]

btn_cols = st.columns(11)
for i, b_col in enumerate(btn_cols):
    with b_col:
        # Gắn icon thú cưng và số thứ tự rõ ràng
        btn_label = f"{animal_icons[i]} {i+1}" if not st.session_state.revealed_words[i] else "✅"
        if st.button(btn_label, key=f"btn_{i}", disabled=st.session_state.revealed_words[i]):
            show_question_modal(i)

st.markdown("<br><br>", unsafe_allow_html=True)
col_empty1, col_guess, col_empty2 = st.columns([1, 2, 1])
with col_guess:
    st.markdown("<div style='text-align: center; font-size: 30px; font-weight: 900; color: #b71c1c; margin-bottom: 15px;'>💡 Lớp mình đã tìm ra thông điệp chưa?</div>", unsafe_allow_html=True)
    if st.button("🌟 LẬT MỞ TOÀN BỘ THÔNG ĐIỆP NGAY 🌟", key="btn_reveal_all", use_container_width=True):
        st.session_state.revealed_words = [True] * 11
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
        <h1 style='color: #d32f2f; font-size: 50px; font-weight: 900; margin-bottom: 10px; line-height: 1.4;'>
            CHÚC CÔ VÀ CẢ LỚP<br>MỘT NGÀY TRUNG THU TỐT LÀNH
        </h1>
        <p style='color: #ff9800; font-size: 38px; font-weight: 900; margin-top: 25px;'>
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
