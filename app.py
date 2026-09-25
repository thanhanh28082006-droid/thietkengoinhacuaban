import streamlit as st
import time
import streamlit.components.v1 as components
import base64

st.set_page_config(page_title="Giải Mã Đêm Trăng", page_icon="🏮", layout="wide")

# ĐỌC VÀ LƯU BỘ NHỚ ĐỆM FILE NHẠC ĐỂ CHẠY MƯỢT MÀ
@st.cache_data
def get_audio_base64(file_path):
    try:
        with open(file_path, "rb") as f:
            data = f.read()
            return base64.b64encode(data).decode()
    except Exception:
        return None

# XÁO TRỘN CÂU HỎI (Ghép thành: TRĂNG SÁNG NHẤT KHI LÒNG NGƯỜI LUÔN HƯỚNG VỀ NHAU)
QUESTIONS = [
    {
        "id": 1,
        "word": "TRĂNG",
        "type": "reveal",
        "question": "1. Đuổi hình bắt chữ: Đây là gì?",
        "image": "anh7.png",
        "answer": "Mâm cỗ thưởng Nguyệt"
    },
    {
        "id": 2,
        "word": "SÁNG",
        "type": "choice",
        "question": "2. Trong truyện cổ tích, chú Cuội vì lý do gì mà phải trốn lên mặt trăng?",
        "options": ["A. Trốn nợ", "B. Mê chị Hằng nên theo chị", "C. Níu giữ cây Đa có phép cải tử hoàn sinh", "D. Bị Ngọc Hoàng bắt đi"],
        "answer": "C. Níu giữ cây Đa có phép cải tử hoàn sinh"
    },
    {
        "id": 3,
        "word": "NHẤT",
        "type": "choice",
        "question": "3. Lắng nghe giai điệu sau đây. Theo bạn, bài hát này mang tên là gì?",
        "audio": "buontrang.mp3", 
        "options": ["A. Trăng vàng", "B. Đêm trăng", "C. Vầng trăng", "D. Buôn Trăng"],
        "answer": "D. Buôn Trăng"
    },
    {
        "id": 4,
        "word": "KHI",
        "type": "reveal", 
        "question": "4. Tết Trung thu là Tết đoàn viên, ai ai cũng muốn về nhà. Vậy cái gì trong đêm Trung thu càng đi xa thì lại càng gần, mà càng đứng yên thì lại càng xa?",
        "answer": "Mặt Trăng"
    },
    {
        "id": 5,
        "word": "LÒNG",
        "type": "reveal",
        "question": "5. Đuổi hình bắt chữ: Đây là gì?",
        "image": "anh8.png", 
        "answer": "Cây đa"
    },
    {
        "id": 6,
        "word": "NGƯỜI",
        "type": "choice", 
        "question": "6. Ba linh vật trong các điệu múa đêm hội trăng rằm là gì?",
        "options": ["A. Lân – Sư tử – Rồng", "B. Lân – Phượng hoàng – Rồng", "C. Lân – Rồng – Phụng", "D. Lân – Rồng – Rắn"],
        "answer": "A. Lân – Sư tử – Rồng"
    },
    {
        "id": 7,
        "word": "LUÔN",
        "type": "choice",
        "question": "7. Lắng nghe giai điệu rộn ràng sau đây. Nhạc phẩm này có tên là gì?",
        "audio": "hoitrangram.mp3", 
        "options": ["A. Ngày hội trăng tròn", "B. Hội Trăng Rằm", "C. Hội trăng tròn", "D. Đêm nghe hội trăng"],
        "answer": "B. Hội Trăng Rằm"
    },
    {
        "id": 8,
        "word": "HƯỚNG",
        "type": "reveal",
        "question": "8. Mặt thì đỏ choét, bụng thì to<br>Đi cùng chú lân, gõ cộc cạch<br>Quạt mo phe phẩy, miệng cười toe<br>Lũ trẻ đuổi theo, reo hò thích chí?<br>(Là ai?)",
        "answer": "Ông Địa"
    },
    {
        "id": 9,
        "word": "VỀ",
        "type": "reveal",
        "question": "9. Khi bị kéo lên Cung Trăng, Chú Cuội mang theo vật gì?",
        "answer": "Cây rìu"
    },
    {
        "id": 10,
        "word": "NHAU",
        "type": "reveal",
        "question": "10. Mỗi năm mỗi độ thu về, Bắc Nam xuôi ngược, chợ quê thị thành. Từng đoàn người ngựa diễu hành, Rước vui trẩy hội lượn quanh ngọn đèn. Là đèn gì?",
        "answer": "Đèn kéo quân"
    }
]

if 'revealed_words' not in st.session_state:
    st.session_state.revealed_words = [False] * 10
if 'game_won' not in st.session_state:
    st.session_state.game_won = False
if 'victory_shown' not in st.session_state:
    st.session_state.victory_shown = False

@st.dialog("🏮 GIẢI MÃ CÙNG CHÚNG MÌNH NHAAAA 🏮", width="large")
def show_question_modal(idx):
    q_data = QUESTIONS[idx]
    
    status_key = f"q_status_{idx}"
    timer_key = f"timer_end_{idx}"
    show_answer_key = f"show_answer_{idx}"
    last_clicked_key = f"last_clicked_{idx}"
    
    # Dự phòng khởi tạo (thực tế đã được reset lúc bấm nút ngoài màn hình chính)
    if status_key not in st.session_state:
        st.session_state[status_key] = "playing"
        st.session_state[timer_key] = time.time() + 40
        st.session_state[show_answer_key] = False
        st.session_state[last_clicked_key] = ""
    
    # ================== CÁC HÀM CALLBACKS ==================
    def handle_choice(option):
        st.session_state[last_clicked_key] = option
        if option == q_data['answer']:
            st.session_state[status_key] = "correct"
            st.session_state[show_answer_key] = True 
        else:
            st.session_state[status_key] = "wrong"
            
    def handle_reveal():
        st.session_state[show_answer_key] = True
        st.session_state[status_key] = "correct"
    # =======================================================
    
    is_answered = st.session_state[show_answer_key] or (st.session_state[status_key] == "correct")
    
    # 1. CÂU HỎI (Luôn luôn hiển thị ở trên cùng)
    st.markdown(f"<div class='question-text'>{q_data['question']}</div>", unsafe_allow_html=True)
    
    # 2. KHU VỰC HÌNH ẢNH / MEDIA (Đã giới hạn chiều cao trong CSS)
    media_placeholder = st.empty()
    with media_placeholder.container():
        if is_answered and idx == 4:
            # Nếu câu 5 ĐÃ MỞ: Hiện Video Meme, Ẩn hình ảnh cây đa đi
            try: 
                st.video("meme.mp4", autoplay=True)
            except: 
                st.warning("⚠️ Không tìm thấy file 'meme.mp4'.")
        else:
            # Nếu chưa mở hoặc là câu khác: Hiện hình ảnh/âm thanh bình thường
            if "image" in q_data:
                try: st.image(q_data["image"], use_container_width=True)
                except Exception: st.warning(f"🏮 Khung ảnh trống (Chưa tìm thấy: '{q_data['image']}').")
            if "audio" in q_data:
                try: st.audio(q_data["audio"])
                except Exception: st.warning(f"⚠️ Khung nhạc trống (Chưa tìm thấy: '{q_data['audio']}').")

    st.markdown("<br>", unsafe_allow_html=True)

    # 3. KHU VỰC ĐÁP ÁN VÀ NÚT BẤM
    interaction_placeholder = st.empty()
    with interaction_placeholder.container():
        if not is_answered:
            # --- TRƯỚC KHI MỞ ĐÁP ÁN ---
            if st.session_state[status_key] == "wrong":
                last_choice = st.session_state[last_clicked_key]
                st.markdown(f"<div class='error-message'>❌ Bạn vừa chọn: <b>{last_choice}</b><br>SAI RỒI! Hãy suy nghĩ và chọn lại nhé.</div>", unsafe_allow_html=True)
                
            if q_data.get("type") == "reveal":
                st.button("🎁 MỞ ĐÁP ÁN", key=f"btn_reveal_first_{idx}", on_click=handle_reveal, use_container_width=True, type="secondary")
            else:
                ans_cols = st.columns(2)
                for i, option in enumerate(q_data['options']):
                    with ans_cols[i % 2]:
                        st.button(option, key=f"opt_{idx}_{i}", on_click=handle_choice, args=(option,), use_container_width=True, type="secondary")
        else:
            # --- SAU KHI MỞ ĐÁP ÁN ---
            if idx != 4: # Chỉ in chữ đáp án cho CÁC CÂU KHÁC
                st.markdown("""
                <style>
                @keyframes popIn { 0% { transform: scale(0.3); opacity: 0; } 70% { transform: scale(1.05); opacity: 1; } 100% { transform: scale(1); opacity: 1; } }
                .answer-box { background-color: #ffebee; border-radius: 15px; border: 4px dashed #f44336; padding: 20px; text-align: center; color: #d32f2f; font-size: 32px; font-weight: 900; box-shadow: 0 8px 20px rgba(0,0,0,0.2); width: 100%; margin-bottom: 20px; animation: popIn 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275) forwards; }
                </style>
                """, unsafe_allow_html=True)
                
                if q_data.get("type") == "reveal":
                    st.markdown(f"<div class='answer-box'>Đáp án là:<br>{q_data['answer']}</div>", unsafe_allow_html=True)
                else:
                    st.markdown(f"<div class='answer-box'><span style='color: #2e7d32; font-size: 38px;'>✅ CHÍNH XÁC!</span><br><br>Đáp án là:<br>{q_data['answer']}</div>", unsafe_allow_html=True)
            
            # Nút đóng
            btn_text = "❌ ĐÓNG VÀ LẬT CHỮ" if q_data.get("type") == "choice" else "❌ ĐÓNG"
            if st.button(btn_text, key=f"btn_close_final_{idx}", use_container_width=True, type="primary"):
                st.session_state.revealed_words[idx] = True
                st.rerun()

    # 4. KHU VỰC ĐỒNG HỒ 40 GIÂY NÂNG CẤP VÀ NÚT THOÁT KHẨN CẤP
    needs_timer = ("audio" not in q_data) and ("video" not in q_data)
    if needs_timer:
        if not is_answered:
            remaining = int(st.session_state[timer_key] - time.time())
            if remaining < 0: remaining = 0
            components.html(f"""
            <script>
                const parent = window.parent.document;
                let existing = parent.getElementById("custom-timer-wrapper");
                if (existing) {{ clearInterval(existing.dataset.intervalId); existing.remove(); }}
                
                const wrapper = parent.createElement("div"); 
                wrapper.id = "custom-timer-wrapper";
                wrapper.innerHTML = `
                    <style>
                        @keyframes pulseRed {{
                            0% {{ transform: scale(1); box-shadow: 0 0 0 0 rgba(211,47,47,0.7); }}
                            70% {{ transform: scale(1.1); box-shadow: 0 0 0 10px rgba(211,47,47,0); }}
                            100% {{ transform: scale(1); box-shadow: 0 0 0 0 rgba(211,47,47,0); }}
                        }}
                        #force-close-btn:hover {{ transform: scale(1.05); box-shadow: 0 10px 20px rgba(211,47,47,0.6); }}
                    </style>
                    <div id="timer-container" style="position: absolute; top: 10px; left: 10px; z-index: 999999; display: flex; flex-direction: column; align-items: center;">
                        <div id="cute-timer-box" style="width: 65px; height: 65px; border-radius: 50%; background: radial-gradient(circle, #ffffff, #fce4ec); border: 4px solid #e91e63; color: #c2185b; display: flex; flex-direction: column; align-items: center; justify-content: center; font-size: 26px; font-weight: 900; box-shadow: 0 4px 10px rgba(0,0,0,0.2); transition: 0.3s;">{remaining}</div>
                        <div id="timer-warning" style="display: none; background: #d32f2f; color: white; font-size: 13px; font-weight: 900; padding: 2px 8px; border-radius: 8px; margin-top: 6px; box-shadow: 0 4px 8px rgba(211,47,47,0.3); text-transform: uppercase;">Sắp hết giờ!</div>
                    </div>
                    <div id="timeout-blocker" style="display: none; position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: rgba(255,255,255,0.95); z-index: 999998; flex-direction: column; align-items: center; justify-content: center; border-radius: 1rem;">
                        <span style="font-size: 60px; margin-bottom: 15px;">⏰</span>
                        <h1 style="color: #d32f2f; font-size: 40px; font-weight: 900; margin: 0; text-align: center;">HẾT THỜI GIAN!</h1>
                        <button id="force-close-btn" style="margin-top: 30px; padding: 15px 40px; background: #d32f2f; color: white; font-size: 20px; font-weight: 900; border: 3px solid #b71c1c; border-radius: 40px; cursor: pointer; box-shadow: 0 6px 15px rgba(211,47,47,0.4); transition: 0.2s;">❌ ĐÓNG LẠI</button>
                    </div>
                `;
                
                const modalDialog = parent.querySelector('[data-testid="stDialog"] > div, [data-testid="stModal"] > div');
                
                if (modalDialog) {{ 
                    modalDialog.style.position = 'relative'; 
                    modalDialog.appendChild(wrapper);
                    
                    // Xử lý nút bấm ĐÓNG LẠI khi hiển thị HẾT THỜI GIAN
                    const forceCloseBtn = parent.getElementById("force-close-btn");
                    if (forceCloseBtn) {{
                        forceCloseBtn.addEventListener("click", () => {{
                            // Tìm nút X mặc định của Streamlit và mô phỏng thao tác Click
                            const stCloseBtn = parent.querySelector('button[aria-label="Close"]') || parent.querySelector('[data-testid="stModalCloseButton"]');
                            if (stCloseBtn) {{ stCloseBtn.click(); }}
                            else {{ wrapper.remove(); }}
                        }});
                    }}
                    
                    let timeLeft = {remaining};
                    const timerInterval = setInterval(() => {{
                        if (!parent.querySelector('[data-testid="stDialog"], [data-testid="stModal"]')) {{ 
                            clearInterval(timerInterval); 
                            if(wrapper.parentNode) wrapper.remove(); 
                            return; 
                        }}
                        
                        timeLeft--; 
                        const display = parent.getElementById("cute-timer-box"); 
                        const warning = parent.getElementById("timer-warning");
                        if (display) display.innerText = timeLeft;
                        
                        if (timeLeft <= 10 && timeLeft > 0) {{
                            if(display) {{
                                display.style.borderColor = "#d32f2f";
                                display.style.color = "#d32f2f";
                                display.style.animation = "pulseRed 1s infinite";
                            }}
                            if(warning) warning.style.display = "block";
                        }}
                        
                        if (timeLeft <= 0) {{ 
                            clearInterval(timerInterval); 
                            const blocker = parent.getElementById("timeout-blocker"); 
                            if (blocker) blocker.style.display = "flex"; 
                        }}
                    }}, 1000); 
                    wrapper.dataset.intervalId = timerInterval;
                }} else {{
                    parent.body.appendChild(wrapper);
                }}
            </script>
            """, height=0)


# =========================================================================
# GIAO DIỆN CHÍNH Ở NGOÀI 
# =========================================================================
st.markdown("""
<style>
    /* Canh giữa tiêu đề Dialog để không bị đồng hồ che khuất */
    div[data-testid="stDialog"] h2, div[data-testid="stModal"] h2 {
        text-align: center !important;
        justify-content: center !important;
        width: 100% !important;
        padding-top: 10px;
    }

    /* Nền Đỏ - Hồng Trung Thu */
    .stApp { background: linear-gradient(135deg, #ffebee, #ffcdd2, #ef9a9a); font-family: 'Segoe UI', Tahoma, Geneva, sans-serif; }
    
    /* Khung nội dung trắng - Padding nhỏ giữ form gọn */
    .white-container { 
        background-color: rgba(255, 255, 255, 0.85); backdrop-filter: blur(15px); border-radius: 20px; 
        padding: 20px; box-shadow: 0 15px 30px rgba(211, 47, 47, 0.15); border: 2px solid #ffcdd2; 
        margin-bottom: 20px; position: relative; overflow: hidden; 
    }
    
    /* TĂNG font chữ câu hỏi và lỗi */
    .question-text { font-size: 32px; color: #b71c1c; text-align: center; margin-bottom: 15px; font-weight: 900; line-height: 1.4; }
    .error-message { background: linear-gradient(90deg, #ffeb3b, #ffc107); color: #b71c1c; padding: 10px; border-radius: 12px; text-align: center; font-size: 22px; font-weight: 900; margin-bottom: 20px; border-left: 6px solid #d32f2f; box-shadow: 0 4px 10px rgba(211, 47, 47, 0.2); }
    
    /* Chữ cái thông điệp lật mở - Tăng font chữ nhưng giữ khối gọn */
    .word-box { 
        display: flex; justify-content: center; align-items: center; height: 70px; 
        background: linear-gradient(145deg, #f44336, #c62828); color: #fffde7; 
        border-radius: 25px; 
        font-size: 24px; font-weight: 900; box-shadow: inset 0px 4px 8px rgba(255,255,255,0.3), 0px 6px 12px rgba(183, 28, 28, 0.4); 
        text-shadow: 1px 1px 4px rgba(0,0,0,0.4); border: 2px solid #ff8a80; 
        margin: 5px 1px; 
        white-space: nowrap; overflow: visible; text-align: center; padding: 0 5px; letter-spacing: -0.5px; 
    }
    .word-hidden { background: linear-gradient(145deg, #ffffff, #eeeeee); color: #bdbdbd; box-shadow: inset 0px 3px 6px rgba(255,255,255,0.8), 0px 5px 10px rgba(0,0,0,0.1); border: 2px solid #e0e0e0; text-shadow: none; font-size: 32px;}
    
    /* NÚT LỒNG ĐÈN & NÚT ĐÓNG - Tăng font chữ lên */
    button[kind="primary"] { 
        border-radius: 50% !important; border: 3px solid #FFD700 !important; background: radial-gradient(circle at center, #ff7961 0%, #d32f2f 80%) !important; 
        box-shadow: 0 6px 12px rgba(183, 28, 28, 0.4), inset 0 6px 10px rgba(255,255,255,0.4), inset 0 -6px 10px rgba(0,0,0,0.5), 0 0 10px #FFD700 !important; 
        transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1) !important; height: 70px !important; position: relative !important; white-space: nowrap !important; padding: 0 !important; margin-top: 15px !important;
    }
    button[kind="primary"]::before { content: ''; position: absolute; top: -20px; left: 50%; transform: translateX(-50%); width: 3px; height: 20px; background: #FFD700; box-shadow: 0 0 6px #FFD700; }
    button[kind="primary"] p { font-size: 22px !important; font-weight: 900 !important; color: #FFFDE7 !important; text-shadow: 1px 1px 3px rgba(0,0,0,0.8), 0 0 8px #FFD700 !important; margin: 0 !important; }
    button[kind="primary"]:hover { background: radial-gradient(circle at center, #ff8a80 0%, #b71c1c 80%) !important; transform: translateY(-5px) scale(1.05) !important; box-shadow: 0 10px 20px rgba(183, 28, 28, 0.6), 0 0 15px rgba(255, 215, 0, 0.8) !important; }
    button[kind="primary"]:disabled { background: radial-gradient(circle at center, #e0e0e0 0%, #9e9e9e 80%) !important; border-color: #bdbdbd !important; transform: none !important; box-shadow: none !important; }
    
    /* NÚT ĐÁP ÁN (A B C D & MỞ ĐÁP ÁN) - Tăng font chữ */
    button[kind="secondary"] {
        border-radius: 30px !important; border: 2px solid #ffcc80 !important; background: linear-gradient(145deg, #fff3e0, #ffe0b2) !important; color: #e65100 !important;
        box-shadow: 0 4px 10px rgba(230, 81, 0, 0.1) !important; transition: all 0.3s ease !important; min-height: 65px !important; white-space: normal !important; 
    }
    button[kind="secondary"] p { font-size: 24px !important; font-weight: 900 !important; margin: 0 !important; }
    button[kind="secondary"]:hover { transform: translateY(-3px) !important; box-shadow: 0 6px 15px rgba(230, 81, 0, 0.2) !important; background: linear-gradient(145deg, #ffe0b2, #ffcc80) !important; border-color: #ff9800 !important; color: #d84315 !important; }

    /* Tiêu đề chính */
    .main-title { text-align: center; font-size: 45px; font-weight: 900; margin-bottom: 25px; text-transform: uppercase; background: linear-gradient(to right, #b71c1c, #ff9800, #b71c1c); -webkit-background-clip: text; -webkit-text-fill-color: transparent; text-shadow: 2px 2px 5px rgba(0,0,0,0.1); }
    
    /* Khống chế kích thước hình ảnh và video không bị tràn màn hình */
    [data-testid="stImage"] img { max-height: 40vh !important; object-fit: contain !important; border-radius: 10px; }
    [data-testid="stVideo"] video { max-height: 40vh !important; object-fit: contain !important; }
    [data-testid="stVideo"] { border: 6px dashed #ff9800 !important; border-radius: 15px !important; box-shadow: 0 10px 25px rgba(0,0,0,0.3) !important; margin: 0 auto; text-align: center; display: flex; justify-content: center; }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">🌕 GIẢI MÃ ĐÊM TRĂNG 🏮</div>', unsafe_allow_html=True)

st.markdown('<div class="white-container">', unsafe_allow_html=True)
cols = st.columns(10)
for i, col in enumerate(cols):
    with col:
        if st.session_state.revealed_words[i]:
            st.markdown(f'<div class="word-box">{QUESTIONS[i]["word"]}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="word-box word-hidden">?</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<div style='font-size: 30px; font-weight: 900; color: #b71c1c; margin-bottom: 20px; text-align: center; text-transform: uppercase;'>✨ CHỌN LỒNG ĐÈN ĐỂ GIẢI MÃ ✨</div>", unsafe_allow_html=True)

# 10 Lồng đèn tương ứng 10 chữ
lantern_emojis = ['🐟', '⭐', '🦋', '💖', '🐰', '🐱', '🐯', '🐷', '🐻', '🌸']
btn_cols = st.columns(10)
for i, b_col in enumerate(btn_cols):
    with b_col:
        btn_label = f"{lantern_emojis[i]} {i+1}" if not st.session_state.revealed_words[i] else "✅"
        if st.button(btn_label, key=f"btn_{i}", disabled=st.session_state.revealed_words[i], type="primary"):
            # RESET TRẠNG THÁI ĐỂ ĐỒNG HỒ LUÔN CHẠY LẠI TỪ 40S MỖI LẦN MỞ LỒNG ĐÈN
            st.session_state[f"q_status_{i}"] = "playing"
            st.session_state[f"timer_end_{i}"] = time.time() + 40
            st.session_state[f"show_answer_{i}"] = False
            st.session_state[f"last_clicked_{i}"] = ""
            show_question_modal(i)

st.markdown("<br><br>", unsafe_allow_html=True)
col_empty1, col_guess, col_empty2 = st.columns([1, 2, 1])
with col_guess:
    st.markdown("<div style='text-align: center; font-size: 26px; font-weight: 900; color: #b71c1c; margin-bottom: 15px;'>💡 Lớp mình đã tìm ra thông điệp chưa?</div>", unsafe_allow_html=True)
    if st.button("🌟 LẬT MỞ TOÀN BỘ THÔNG ĐIỆP NGAY 🌟", key="btn_reveal_all", use_container_width=True, type="secondary"):
        st.session_state.revealed_words = [True] * 10
        st.session_state.victory_shown = False 
        st.rerun()

@st.dialog("🎉 ĐÊM HỘI TRĂNG RẰM ĐÃ TỎA SÁNG 🎉", width="large")
def show_victory_modal():
    st.balloons()
    st.markdown("""
    <style>
    @keyframes fall { 0% { transform: translateY(-10vh) rotate(0deg); opacity: 1;} 100% { transform: translateY(100vh) rotate(360deg); opacity: 0;} }
    .flower { position: fixed; font-size: 35px; z-index: 9999; top: -10vh; animation: fall linear forwards; }
    </style>
    <script>
    const flowers = ['🏮', '🌕', '⭐', '✨', '🥮', '🐇']; 
    for(let i=0; i<70; i++) {
        let f = document.createElement('div'); f.className = 'flower'; f.innerText = flowers[Math.floor(Math.random() * flowers.length)];
        f.style.left = Math.random() * 100 + 'vw'; f.style.animationDuration = (Math.random() * 3 + 2) + 's'; f.style.animationDelay = Math.random() * 2 + 's'; window.parent.document.body.appendChild(f);
    }
    </script>
    <div style='text-align: center; padding: 15px 10px;'>
        <h1 style='color: #d32f2f; font-size: 45px; font-weight: 900; margin-bottom: 10px; line-height: 1.3; text-shadow: 2px 2px 4px rgba(0,0,0,0.1);'>THÔNG ĐIỆP TRUNG THU</h1>
        <p style='color: #ff9800; font-size: 32px; font-weight: 900; margin-top: 20px; text-shadow: 0 0 10px rgba(255, 152, 0, 0.6), 0 0 20px rgba(255, 193, 7, 0.4);'>
            "Trăng sáng nhất khi lòng người luôn hướng về nhau" 🏮🌕
        </p>
    </div><br>
    """, unsafe_allow_html=True)
    
    if st.button("🌟 Tuyệt vời!", use_container_width=True, type="secondary"):
        st.session_state.victory_shown = True
        st.rerun()

if all(st.session_state.revealed_words):
    if not st.session_state.victory_shown:
        show_victory_modal() 
    else:
        st.success("🎉 XUẤT SẮC! CẢ LỚP ĐÃ GIẢI MÃ THÀNH CÔNG THÔNG ĐIỆP TRUNG THU!")

# TRÌNH PHÁT NHẠC NỀN MP3 LOCAL KÍCH THƯỚC CHUẨN, NHỎ GỌN
audio_b64 = get_audio_base64("nhacnen.mp3")
if audio_b64:
    st.markdown(f"""
    <div style="position: fixed; bottom: 15px; left: 15px; z-index: 99999; background: rgba(255,255,255,0.95); backdrop-filter: blur(10px); padding: 8px 12px; border-radius: 15px; border: 2px solid #e91e63; box-shadow: 0 4px 12px rgba(0,0,0,0.15);">
        <p style="margin: 0 0 5px 0; font-weight: 900; color: #e91e63; font-size: 13px; text-align: center;">🎵 Nhạc Nền</p>
        <audio controls autoplay loop style="width: 200px; height: 40px; outline: none;">
            <source src="data:audio/mp3;base64,{audio_b64}" type="audio/mp3">
        </audio>
    </div>
    """, unsafe_allow_html=True)
