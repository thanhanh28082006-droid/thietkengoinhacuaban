import streamlit as st
import time
import streamlit.components.v1 as components

st.set_page_config(page_title="Vui Tết Trung Thu", page_icon="🏮", layout="wide")

# XÁO TRỘN CÂU HỎI NHƯNG VẪN GIỮ ĐÚNG THÔNG ĐIỆP 10 CHỮ:
# TRĂNG - SÁNG - NHẤT - KHI - LÒNG - NGƯỜI - LUÔN - HƯỚNG - VỀ - NHAU
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
        "options": ["A. Trăng vàng", "B. Đêm trăng", "C. Vầng trăng", "D. Buồn Trăng"],
        "answer": "D. Buồn Trăng"
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

@st.dialog("🏮 THỬ THÁCH TRUNG THU 🏮", width="large")
def show_question_modal(idx):
    q_data = QUESTIONS[idx]
    
    status_key = f"q_status_{idx}"
    timer_key = f"timer_end_{idx}"
    show_answer_key = f"show_answer_{idx}"
    
    if status_key not in st.session_state:
        st.session_state[status_key] = "playing"
        st.session_state[timer_key] = time.time() + 40 # 40 giây
        st.session_state[show_answer_key] = False
    
    st.markdown(f"<div class='question-text'>{q_data['question']}</div>", unsafe_allow_html=True)
    
    if "image" in q_data:
        try:
            st.image(q_data["image"], use_container_width=True)
        except Exception:
            st.warning(f"🏮 Khung ảnh trống (Chưa tìm thấy file: '{q_data['image']}').")
        st.markdown("<br>", unsafe_allow_html=True)
        
    if "audio" in q_data:
        try:
            st.audio(q_data["audio"])
        except Exception:
            st.warning(f"⚠️ Khung nhạc trống (Chưa tìm thấy file: '{q_data['audio']}').")
        st.markdown("<br>", unsafe_allow_html=True)
    
    error_msg_placeholder = st.empty()
    if st.session_state[status_key] == "wrong":
        error_msg_placeholder.markdown("<div class='error-message'>❌ Sai rồi! Bạn hãy chọn lại nhé.</div>", unsafe_allow_html=True)
            
    is_answered = st.session_state[show_answer_key] or (st.session_state[status_key] == "correct")
    needs_timer = ("audio" not in q_data) and ("video" not in q_data)
    
    if needs_timer:
        if not is_answered:
            remaining = int(st.session_state[timer_key] - time.time())
            if remaining < 0: remaining = 0
            
            # Khung timer 40s Màu hồng dễ thương
            components.html(f"""
            <script>
                const parent = window.parent.document;
                let existing = parent.getElementById("custom-timer-wrapper");
                if (existing) {{ clearInterval(existing.dataset.intervalId); existing.remove(); }}
                
                const wrapper = parent.createElement("div");
                wrapper.id = "custom-timer-wrapper";
                wrapper.innerHTML = `
                    <div id="cute-timer-box" style="position: absolute; top: 15px; left: 15px; width: 75px; height: 75px; border-radius: 50%; background: radial-gradient(circle, #ffffff, #fce4ec); border: 5px solid #e91e63; color: #c2185b; display: flex; flex-direction: column; align-items: center; justify-content: center; font-size: 32px; font-weight: 900; box-shadow: 0 5px 15px rgba(0,0,0,0.3); z-index: 999999;">
                        {remaining}
                    </div>
                    <div id="timeout-blocker" style="display: none; position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: rgba(255,255,255,0.95); z-index: 999998; flex-direction: column; align-items: center; justify-content: center; border-radius: 1rem;">
                        <span style="font-size: 80px; margin-bottom: 20px;">⏰</span>
                        <h1 style="color: #d32f2f; font-size: 55px; font-weight: 900; margin: 0; text-align: center;">HẾT THỜI GIAN!</h1>
                        <p style="font-size: 26px; color: #424242; font-weight: bold; text-align: center; margin-top: 20px;">Hãy bấm dấu <b>X</b> ở góc trên bên phải để thoát.</p>
                    </div>
                `;
                
                const modalDialog = parent.querySelector('[data-testid="stModal"] > div');
                if (modalDialog) {{
                    modalDialog.style.position = 'relative'; 
                    modalDialog.appendChild(wrapper);
                    
                    let timeLeft = {remaining};
                    const timerInterval = setInterval(() => {{
                        if (!parent.querySelector('[data-testid="stModal"]')) {{
                            clearInterval(timerInterval);
                            if(wrapper.parentNode) wrapper.remove();
                            return;
                        }}
                        timeLeft--;
                        const display = parent.getElementById("cute-timer-box");
                        if (display) display.innerText = timeLeft;
                        if (timeLeft <= 0) {{
                            clearInterval(timerInterval);
                            const blocker = parent.getElementById("timeout-blocker");
                            if (blocker) blocker.style.display = "flex";
                        }}
                    }}, 1000);
                    wrapper.dataset.intervalId = timerInterval;
                }}
            </script>
            """, height=0)
        else:
            components.html("""
            <script>
                const parent = window.parent.document;
                const existing = parent.getElementById("custom-timer-wrapper");
                if (existing) { clearInterval(existing.dataset.intervalId); existing.remove(); }
            </script>
            """, height=0)

    if q_data.get("type") == "reveal":
        # DẠNG 1: CÂU HỎI MỞ
        if not st.session_state[show_answer_key]:
            if st.button("🎁 MỞ ĐÁP ÁN", key=f"btn_reveal_first_{idx}", use_container_width=True, type="secondary"):
                st.session_state[show_answer_key] = True
                st.rerun() 
        else:
            # Hiện đáp án và Nút ĐÓNG
            st.markdown(f"<div style='text-align: center; font-size: 38px; font-weight: 900; color: #d32f2f; margin: 20px 0; padding: 20px; background-color: #ffebee; border-radius: 15px; border: 2px dashed #f44336;'>Đáp án: {q_data['answer']}</div>", unsafe_allow_html=True)
            
            # Chèn Video Meme cho lồng đèn Câu 5 (index 4)
            if idx == 4:
                try:
                    st.video("meme.mp4", autoplay=True)
                except:
                    st.warning("⚠️ Không tìm thấy file 'meme.mp4'.")
                    
            if st.button("❌ ĐÓNG", key=f"btn_reveal_final_{idx}", use_container_width=True, type="primary"):
                st.session_state.revealed_words[idx] = True 
                st.rerun()
                
    else:
        # DẠNG 2: TRẮC NGHIỆM
        if not st.session_state[show_answer_key]:
            ans_cols = st.columns(2)
            for i, option in enumerate(q_data['options']):
                with ans_cols[i % 2]:
                    if st.button(option, key=f"opt_{idx}_{i}", use_container_width=True, type="secondary"):
                        if option == q_data['answer']:
                            st.session_state[status_key] = "correct"
                            st.session_state[show_answer_key] = True 
                            st.rerun() 
                        else:
                            st.session_state[status_key] = "wrong"
                            st.rerun()
        else:
            # HIỆN ĐÁP ÁN ĐÚNG VÀ NÚT ĐÓNG
            st.markdown("<div style='text-align: center; font-size: 36px; font-weight: 900; color: #2e7d32; margin-bottom: 20px; padding: 15px; background-color: #e8f5e9; border-radius: 15px; border: 2px dashed #4caf50;'>✅ CHÍNH XÁC!</div>", unsafe_allow_html=True)
            st.markdown(f"<div style='text-align: center; font-size: 32px; font-weight: 700; color: #d32f2f; margin-bottom: 25px;'>Đáp án: {q_data['answer']}</div>", unsafe_allow_html=True)
            
            # Chèn Video Meme cho lồng đèn Câu 5 (index 4)
            if idx == 4:
                try:
                    st.video("meme.mp4", autoplay=True)
                except:
                    st.warning("⚠️ Không tìm thấy file 'meme.mp4'.")
                    
            if st.button("❌ ĐÓNG", key=f"btn_close_correct_{idx}", use_container_width=True, type="primary"):
                st.session_state.revealed_words[idx] = True 
                st.rerun()

st.markdown("""
<style>
    .stApp { background: linear-gradient(135deg, #ffebee, #ffcdd2, #ef9a9a); font-family: 'Segoe UI', Tahoma, Geneva, sans-serif; }
    
    .white-container { 
        background-color: rgba(255, 255, 255, 0.85); backdrop-filter: blur(15px); border-radius: 25px; 
        padding: 35px; box-shadow: 0 20px 40px rgba(211, 47, 47, 0.2); border: 3px solid #ffcdd2; 
        margin-bottom: 25px; position: relative; overflow: hidden; 
    }
    
    .question-text { font-size: 38px; color: #b71c1c; text-align: center; margin-bottom: 30px; font-weight: 900; line-height: 1.5; text-shadow: 1px 1px 3px rgba(0,0,0,0.1); }
    .error-message { background: linear-gradient(90deg, #ffeb3b, #ffc107); color: #b71c1c; padding: 15px; border-radius: 15px; text-align: center; font-size: 28px; font-weight: 900; margin-bottom: 25px; border-left: 8px solid #d32f2f; box-shadow: 0 4px 15px rgba(211, 47, 47, 0.3); }
    
    /* Ô chữ hình Viên Kẹo - Font nhỏ hơn, không rớt dòng */
    .word-box { 
        display: flex; justify-content: center; align-items: center; height: 90px; 
        background: linear-gradient(145deg, #f44336, #c62828); color: #fffde7; 
        border-radius: 40px; 
        font-size: 28px; font-weight: 900; box-shadow: inset 0px 6px 12px rgba(255,255,255,0.4), 0px 10px 20px rgba(183, 28, 28, 0.5); 
        text-shadow: 2px 2px 6px rgba(0,0,0,0.5); border: 3px solid #ff8a80; 
        margin: 5px 2px; 
        white-space: nowrap; overflow: visible; text-align: center; padding: 0 5px; letter-spacing: -0.5px; 
    }
    .word-hidden { background: linear-gradient(145deg, #ffffff, #eeeeee); color: #bdbdbd; box-shadow: inset 0px 5px 10px rgba(255,255,255,1), 0px 8px 15px rgba(0,0,0,0.1); border: 3px solid #e0e0e0; text-shadow: none; font-size: 38px;}
    
    /* NÚT LỒNG ĐÈN */
    button[kind="primary"] { 
        border-radius: 50% !important; 
        border: 4px solid #FFD700 !important; 
        background: radial-gradient(circle at center, #ff7961 0%, #d32f2f 80%) !important; 
        box-shadow: 0 10px 20px rgba(183, 28, 28, 0.5), inset 0 10px 15px rgba(255,255,255,0.5), inset 0 -10px 15px rgba(0,0,0,0.6), 0 0 15px #FFD700 !important; 
        transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1) !important; 
        height: 80px !important; position: relative !important; overflow: visible !important; white-space: nowrap !important; padding: 0 !important; margin-top: 20px !important;
    }
    button[kind="primary"]::before { content: ''; position: absolute; top: -30px; left: 50%; transform: translateX(-50%); width: 3px; height: 30px; background: #FFD700; box-shadow: 0 0 8px #FFD700; }
    button[kind="primary"] p { font-size: 26px !important; font-weight: 900 !important; color: #FFFDE7 !important; text-shadow: 2px 2px 5px rgba(0,0,0,0.8), 0 0 10px #FFD700 !important; margin: 0 !important; letter-spacing: 1px !important; }
    button[kind="primary"]:hover { background: radial-gradient(circle at center, #ff8a80 0%, #b71c1c 80%) !important; transform: translateY(-8px) scale(1.1) !important; box-shadow: 0 15px 30px rgba(183, 28, 28, 0.8), 0 0 25px rgba(255, 215, 0, 1) !important; }
    button[kind="primary"]:disabled { background: radial-gradient(circle at center, #e0e0e0 0%, #9e9e9e 80%) !important; border-color: #bdbdbd !important; transform: none !important; box-shadow: none !important; }
    
    /* NÚT ĐÁP ÁN (Viên Kẹo) */
    button[kind="secondary"] {
        border-radius: 40px !important; border: 3px solid #ffcc80 !important; background: linear-gradient(145deg, #fff3e0, #ffe0b2) !important; color: #e65100 !important;
        box-shadow: 0 6px 15px rgba(230, 81, 0, 0.15) !important; transition: all 0.3s ease !important; min-height: 80px !important; white-space: normal !important; 
    }
    button[kind="secondary"] p { font-size: 26px !important; font-weight: 900 !important; margin: 0 !important; }
    button[kind="secondary"]:hover { transform: translateY(-5px) !important; box-shadow: 0 10px 20px rgba(230, 81, 0, 0.3) !important; background: linear-gradient(145deg, #ffe0b2, #ffcc80) !important; border-color: #ff9800 !important; color: #d84315 !important; }

    .main-title { text-align: center; font-size: 55px; font-weight: 900; margin-bottom: 40px; text-transform: uppercase; background: linear-gradient(to right, #b71c1c, #ff9800, #b71c1c); -webkit-background-clip: text; -webkit-text-fill-color: transparent; text-shadow: 3px 3px 8px rgba(0,0,0,0.15); }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">🌕 LẬT MỞ ĐÊM HỘI TRĂNG RẰM 🏮</div>', unsafe_allow_html=True)

st.markdown('<div class="white-container">', unsafe_allow_html=True)
cols = st.columns(10)
for i, col in enumerate(cols):
    with col:
        if st.session_state.revealed_words[i]:
            st.markdown(f'<div class="word-box">{QUESTIONS[i]["word"]}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="word-box word-hidden">?</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<div style='font-size: 36px; font-weight: 900; color: #b71c1c; margin-bottom: 30px; text-align: center; text-transform: uppercase;'>✨ CHỌN LỒNG ĐÈN ĐỂ GIẢI MÃ ✨</div>", unsafe_allow_html=True)

lantern_emojis = ['🐟', '⭐', '🦋', '💖', '🐰', '🐱', '🐯', '🐷', '🐻', '🌸']
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
    @keyframes fall { 0% { transform: translateY(-10vh) rotate(0deg); opacity: 1;} 100% { transform: translateY(100vh) rotate(360deg); opacity: 0;} }
    .flower { position: fixed; font-size: 40px; z-index: 9999; top: -10vh; animation: fall linear forwards; }
    </style>
    <script>
    const flowers = ['🏮', '🌕', '⭐', '✨', '🥮', '🐇']; 
    for(let i=0; i<70; i++) {
        let f = document.createElement('div'); f.className = 'flower'; f.innerText = flowers[Math.floor(Math.random() * flowers.length)];
        f.style.left = Math.random() * 100 + 'vw'; f.style.animationDuration = (Math.random() * 3 + 2) + 's'; f.style.animationDelay = Math.random() * 2 + 's'; window.parent.document.body.appendChild(f);
    }
    </script>
    <div style='text-align: center; padding: 20px 10px;'>
        <h1 style='color: #d32f2f; font-size: 55px; font-weight: 900; margin-bottom: 10px; line-height: 1.4; text-shadow: 2px 2px 5px rgba(0,0,0,0.1);'>THÔNG ĐIỆP TRUNG THU</h1>
        <p style='color: #ff9800; font-size: 40px; font-weight: 900; margin-top: 25px; text-shadow: 0 0 15px rgba(255, 152, 0, 0.8), 0 0 30px rgba(255, 193, 7, 0.6);'>
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

st.markdown("""
<div style="position: fixed; bottom: 20px; left: 20px; z-index: 9999; background: rgba(255,255,255,0.95); backdrop-filter: blur(10px); padding: 10px 15px; border-radius: 20px; border: 3px solid #e91e63; box-shadow: 0 5px 15px rgba(0,0,0,0.2);">
    <p style="margin: 0 0 5px 0; font-weight: 900; color: #e91e63; font-size: 14px; text-align: center;">🎵 Nhạc Nền (Click vào trang nếu chưa chạy)</p>
    <iframe width="220" height="60" src="https://www.youtube.com/embed/qrjEvxT9apU?autoplay=1&loop=1&playlist=qrjEvxT9apU&mute=0" allow="autoplay; encrypted-media" frameborder="0" style="border-radius: 10px;"></iframe>
</div>
""", unsafe_allow_html=True)
