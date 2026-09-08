import streamlit as st
import random

# --- 1. CẤU HÌNH GIAO DIỆN (LẤP LÁNH - CHỮ SIÊU TO - NHIỀU ICON) ---
st.set_page_config(page_title="Design Your House", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
    /* Nền Gradient chuyển động + Hạt lấp lánh (Sparkles) */
    .stApp {
        background: linear-gradient(-45deg, #0284C7, #00C6FF, #032759, #FFD700);
        background-size: 400% 400%;
        animation: gradientBG 10s ease infinite;
        position: relative;
    }
    
    @keyframes gradientBG {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    /* Lớp phủ lấp lánh */
    .sparkles-overlay {
        position: fixed;
        top: 0; left: 0; width: 100vw; height: 100vh;
        background-image: url('https://www.transparenttextures.com/patterns/stardust.png');
        pointer-events: none;
        z-index: 0;
        animation: twinkle 3s infinite alternate;
        opacity: 0.6;
    }
    
    @keyframes twinkle {
        0% { opacity: 0.3; transform: scale(1); }
        100% { opacity: 0.9; transform: scale(1.05); }
    }

    /* Đảm bảo nội dung nổi lên trên lớp lấp lánh */
    .main .block-container {
        z-index: 10;
        position: relative;
    }
    
    /* Chữ màu trắng với hiệu ứng đổ bóng */
    h1, h2, h3, h4, p, span, div, label {
        color: #FFFFFF !important;
        font-family: 'Inter', 'Segoe UI', sans-serif;
        text-shadow: 2px 2px 5px rgba(0, 0, 0, 0.8);
    }
    
    h2 { font-size: 38px !important; font-weight: 900 !important; color: #FFD700 !important; }
    h3 { font-size: 28px !important; font-weight: 800 !important; }
    
    /* TÙY CHỈNH KHUNG CHỨA (CONTAINER) */
    [data-testid="stVerticalBlockBorderWrapper"] {
        background: rgba(0, 0, 0, 0.4) !important;
        backdrop-filter: blur(12px);
        border: 3px solid #FFD700 !important;
        border-radius: 25px !important;
        box-shadow: 0 0 30px rgba(255, 215, 0, 0.5), inset 0 0 15px rgba(255, 255, 255, 0.2) !important;
        padding: 10px;
    }

    /* TAB CỬA SỔ KHỔNG LỒ (MODAL) */
    .huge-modal {
        background: rgba(3, 39, 89, 0.98);
        border-radius: 30px;
        padding: 60px;
        box-shadow: 0 0 60px rgba(255, 215, 0, 0.8);
        border: 4px solid #FFD700;
        animation: slideUp 0.3s ease-out;
        text-align: center;
        margin: 0 auto;
        max-width: 1200px;
    }
    
    @keyframes slideUp {
        from { opacity: 0; transform: translateY(30px); }
        to { opacity: 1; transform: translateY(0); }
    }

    /* Nút bấm (Buttons) Cực To */
    .stButton>button {
        background: linear-gradient(90deg, #FFD700 0%, #FFA500 100%);
        color: #000000 !important;
        border-radius: 15px;
        font-weight: 900;
        font-size: 22px !important; /* Phóng to chữ nút */
        padding: 25px 15px !important; /* Làm nút dày và to hơn */
        border: none;
        transition: all 0.3s;
        width: 100%;
        text-transform: uppercase;
        box-shadow: 0 5px 20px rgba(255, 215, 0, 0.6);
        margin-top: 10px;
        text-shadow: none !important;
    }
    .stButton>button:hover {
        background: linear-gradient(90deg, #FFFFFF 0%, #FFD700 100%);
        transform: translateY(-5px) scale(1.02);
        box-shadow: 0 10px 30px rgba(255, 255, 255, 0.8);
    }
    
    button[disabled] {
        background: rgba(255, 255, 255, 0.1) !important;
        color: rgba(255, 255, 255, 0.5) !important;
        box-shadow: none !important;
        border: 2px dashed rgba(255, 255, 255, 0.3) !important;
        transform: none !important;
    }
    
    /* CSS Phóng to chữ của các đáp án Radio */
    .stRadio p {
        font-size: 32px !important; /* Chữ đáp án siêu to */
        font-weight: 900 !important;
        color: #FFFFFF !important;
        padding-left: 15px;
        margin-bottom: 15px;
        line-height: 1.4;
    }
    
    /* Ô quy trình đang xếp - SIÊU TO DỄ NHÌN */
    .selected-step-box {
        background: rgba(255, 215, 0, 0.2);
        border: 3px solid #FFD700;
        border-radius: 15px;
        padding: 20px 10px;
        text-align: center;
        font-weight: 900;
        color: #FFFFFF !important;
        margin-bottom: 15px;
        box-shadow: 0 0 20px rgba(255, 215, 0, 0.4);
        height: 120px; /* Chiều cao ô cực lớn */
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 22px; /* Chữ trong ô cực lớn */
        text-shadow: 2px 2px 5px rgba(0,0,0,0.8);
    }

    /* Style cho danh sách vật liệu hoàn hảo 80/80 */
    .perfect-material-box {
        background: rgba(255, 215, 0, 0.2);
        border: 3px solid #FFD700;
        border-radius: 15px;
        padding: 20px 25px;
        margin-bottom: 15px;
        font-size: 24px; /* Chữ to */
        font-weight: 900;
        color: #FFFFFF;
        display: flex;
        align-items: center;
        text-align: left;
        box-shadow: 0 0 25px rgba(255, 215, 0, 0.6);
    }
    </style>
    
    <!-- Lớp phủ lấp lánh (Sparkles) -->
    <div class="sparkles-overlay"></div>
""", unsafe_allow_html=True)

# --- 2. DỮ LIỆU TRÒ CHƠI ---
game_data = [
    {
        "title": "🏗️ LÀM MÓNG 🧱",
        "desc": "Nền tảng vững chắc quyết định tuổi thọ của cả công trình.",
        "options": [
            {"text": "🪙 Hợp kim nhôm nguyên khối (Solid aluminum)", "correct": False, "error": "- Móng Nhôm: Chịu nén kém, oxy hóa ngầm làm sập nhà."},
            {"text": "🧱 Bê tông cốt thép chuẩn (Reinforced concrete)", "correct": True, "error": ""},
            {"text": "🪨 Bê tông đúc chuẩn (Standard cast concrete)", "correct": False, "error": "- Móng Bê tông đúc: Thiếu lõi thép sẽ rất giòn, không chịu được lực uốn, gây gãy nứt móng."}
        ]
    },
    {
        "title": "⛓️ ĐỔ KHUNG CỘT 🏛️",
        "desc": "Hệ xương sống chống chịu mọi bão tố và tải trọng.",
        "options": [
            {"text": "🔲 Sắt non dập hộp (Soft iron box)", "correct": False, "error": "- Cột Sắt non: Chịu tải kém, móp méo và gãy gập ngay khi gánh sức nặng tầng trên."},
            {"text": "〰️ Thép trơn siêu dẻo (Flexible smooth steel)", "correct": False, "error": "- Cột Thép dẻo: Không bám dính bê tông, rung lắc là gãy."},
            {"text": "📌 Thép vằn cường độ cao (High-strength steel)", "correct": True, "error": ""}
        ]
    },
    {
        "title": "🧱 XÂY TƯỜNG 🛡️",
        "desc": "Lớp áo giáp bảo vệ không gian sống khỏi thời tiết.",
        "options": [
            {"text": "🧱 Gạch đất nung / Gạch AAC (Fired brick / AAC)", "correct": True, "error": ""},
            {"text": "🌑 Gạch xỉ than tái chế (Recycled cinder block)", "correct": False, "error": "- Tường Xỉ than: Hút nước như bọt biển, ngập ngụa khi mưa."},
            {"text": "🧱 Gạch block xi măng tự trộn (Hand-mixed cement block)", "correct": False, "error": "- Tường Xi măng tự trộn: Trộn thủ công sai tỷ lệ khiến gạch bở rạc, ngấm nước và nứt toác sau 1 mùa mưa."}
        ]
    },
    {
        "title": "🏠 LÀM MÁI ☂️",
        "desc": "Lá chắn che chở tổ ấm khỏi nắng mưa.",
        "options": [
            {"text": "🛸 Mái nhôm đúc nguyên tấm (Cast aluminum roof)", "correct": False, "error": "- Mái Nhôm: Hấp thụ nhiệt siêu tốc, áp mái nóng như lò bát quái."},
            {"text": "🎨 Ngói xi măng ép màu (Color pressed cement)", "correct": False, "error": "- Ngói ép: Phơi nắng 1 năm là nứt rạn, dột tong tỏng."},
            {"text": "🏠 Bê tông & Ngói tráng men (Concrete & glazed tiles)", "correct": True, "error": ""}
        ]
    },
    {
        "title": "⚡ ĐIỆN NƯỚC ÂM 🚰",
        "desc": "Mạch máu ngầm cung cấp tiện nghi cho ngôi nhà.",
        "options": [
            {"text": "🚿 Ống nước Inox mạ bạc (Silver-plated Inox pipe)", "correct": False, "error": "- Ống Inox ngầm: Trở thành bẫy giật điện chết người nếu rò điện."},
            {"text": "⚡ Dây đồng & Ống nhựa PPR (Copper wire & PPR pipe)", "correct": True, "error": ""},
            {"text": "🔌 Dây điện lõi nhôm (Aluminum core wire)", "correct": False, "error": "- Dây Nhôm: Sinh nhiệt cao, chập cháy ngầm trong tường."}
        ]
    },
    {
        "title": "⏳ TRÁT TƯỜNG 🖌️",
        "desc": "Làm phẳng và chuẩn bị bề mặt cho bước trang trí.",
        "options": [
            {"text": "🧪 Keo Epoxy pha bột đá (Epoxy with stone powder)", "correct": False, "error": "- Trát Epoxy: Tường không thở được, mồ hôi ướt nhẹp khi nồm."},
            {"text": "💨 Xi măng nguyên chất (Pure cement without sand)", "correct": False, "error": "- Xi măng nguyên chất: Co ngót cực mạnh, nứt toác chân chim."},
            {"text": "⏳ Vữa xi măng trộn cát mịn (Cement & fine sand)", "correct": True, "error": ""}
        ]
    },
    {
        "title": "🎨 LÁT GẠCH & SƠN ✨",
        "desc": "Khoác lên ngôi nhà vẻ đẹp thẩm mỹ lộng lẫy.",
        "options": [
            {"text": "🛡️ Keo dán gạch & Sơn chống thấm (Tile adhesive & paint)", "correct": True, "error": ""},
            {"text": "💧 Nước xi măng lỏng (Liquid cement slurry)", "correct": False, "error": "- Lát nước xi măng: Gạch phồng rộp, nổ vỡ lụp bụp."},
            {"text": "🛢️ Sơn dầu bóng công nghiệp (Industrial oil paint)", "correct": False, "error": "- Sơn dầu: Bong tróc, lột ra từng mảng như da rắn."}
        ]
    },
    {
        "title": "🛋️ NỘI THẤT 🛏️",
        "desc": "Hoàn thiện không gian sống tiện nghi, sang trọng.",
        "options": [
            {"text": "✈️ Bồn cầu đúc Nhôm hàng không (Aluminum toilet)", "correct": False, "error": "- Bồn cầu Nhôm: Kỵ hóa chất, xịt tẩy bồn cầu là sùi bọt trắng."},
            {"text": "🍴 Tủ bếp bọc Bạc nguyên miếng (Solid silver cabinets)", "correct": False, "error": "- Tủ bếp Bạc: Phản ứng muối mắm, xỉn đen thui cực kỳ bẩn."},
            {"text": "🛋️ Gỗ MDF chống ẩm & Sứ Nano (MDF & Nano porcelain)", "correct": True, "error": ""}
        ]
    }
]

CORRECT_SEQUENCE = [step["title"] for step in game_data]

# --- 3. QUẢN LÝ TRẠNG THÁI ---
if 'phase' not in st.session_state:
    st.session_state.phase = 1 
if 'user_sequence' not in st.session_state:
    st.session_state.user_sequence = []
if 'shuffled_processes' not in st.session_state:
    temp = CORRECT_SEQUENCE.copy()
    random.shuffle(temp)
    st.session_state.shuffled_processes = temp
if 'completed_materials' not in st.session_state:
    st.session_state.completed_materials = []
if 'active_material_step' not in st.session_state:
    st.session_state.active_material_step = None
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'issues' not in st.session_state:
    st.session_state.issues = []
if 'shuffled_options' not in st.session_state:
    st.session_state.shuffled_options = []
    for step in game_data:
        opts = step["options"].copy()
        random.shuffle(opts)
        st.session_state.shuffled_options.append(opts)

# =========================================================================
# KỊCH BẢN MỞ TAB KHỔNG LỒ CHỌN VẬT LIỆU (CHIẾM TOÀN MÀN HÌNH)
# =========================================================================
if st.session_state.active_material_step is not None:
    idx = st.session_state.active_material_step
    current_data = game_data[idx]
    current_opts = st.session_state.shuffled_options[idx]
    
    st.markdown("<div class='huge-modal'>", unsafe_allow_html=True)
    st.markdown(f"<h1 style='font-size: 60px;'>🛒 LỰA CHỌN VẬT LIỆU<br><span style='color: #FFD700 !important; text-shadow: 0 0 20px #FFD700;'>{current_data['title']}</span></h1>", unsafe_allow_html=True)
    st.markdown(f"<h3 style='font-size: 28px; color: rgba(255,255,255,0.9); margin-bottom: 30px;'>💡 {current_data['desc']}</h3>", unsafe_allow_html=True)
    st.write("---")
    
    # Câu hỏi siêu to khổng lồ
    st.markdown("<h2 style='font-size: 42px; color: #FFFFFF; font-weight: 900; margin-bottom: 30px; text-shadow: 2px 2px 10px #000;'>👉 VẬT LIỆU NÀO ĐẠT TIÊU CHUẨN KỸ THUẬT? 🧐</h2>", unsafe_allow_html=True)
    
    option_texts = [opt["text"] for opt in current_opts]
    choice = st.radio("Chọn vật liệu", option_texts, index=None, label_visibility="collapsed")
    
    st.write("")
    st.write("")
    col_btn1, col_btn2, col_btn3 = st.columns([1, 2, 1])
    with col_btn2:
        if st.button("✅ XÁC NHẬN VẬT LIỆU ✅"):
            if choice:
                selected_opt = next(item for item in current_opts if item["text"] == choice)
                if selected_opt["correct"]:
                    st.session_state.score += 10
                else:
                    st.session_state.issues.append(selected_opt["error"])
                
                st.session_state.completed_materials.append(idx)
                st.session_state.active_material_step = None
                
                if len(st.session_state.completed_materials) == 8:
                    st.session_state.phase = 3
                st.rerun()
            else:
                st.error("⚠️ VUI LÒNG CHỌN 1 LOẠI VẬT LIỆU!")
    st.markdown("</div>", unsafe_allow_html=True)

# =========================================================================
# GIAO DIỆN CHÍNH
# =========================================================================
else:
    # HIỂN THỊ TIÊU ĐỀ
    st.markdown("<div style='text-align: center; margin-bottom: 40px;'>", unsafe_allow_html=True)
    try:
        st.image("image_04e8c0.png", use_container_width=True)
    except:
        st.markdown("<h1 style='font-size: 60px; font-weight: 900; color: #FFD700 !important; text-shadow: 0 0 30px #FFD700;'>🏡 DESIGN YOUR HOUSE 🏡</h1>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([3, 7], gap="large")
    
    # CỘT 1: THƯ VIỆN NHÀ MẪU
    with col1:
        with st.container(border=True):
            st.markdown("<h3 style='text-align: center; font-size: 32px;'>🌟 Mẫu Nhà Hiện Đại 🌟</h3>", unsafe_allow_html=True)
            st.image("https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80", use_container_width=True)
            st.markdown("<br>", unsafe_allow_html=True)
            st.image("https://images.unsplash.com/photo-1613977257363-707ba9348227?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80", use_container_width=True)

    # CỘT 2: KHU VỰC TƯƠNG TÁC CHÍNH
    with col2:
        # -----------------------------------------------------
        # PHASE 1: SẮP XẾP QUY TRÌNH
        # -----------------------------------------------------
        if st.session_state.phase == 1:
            with st.container(border=True):
                st.markdown("<h2>📌 BƯỚC 1: 🧩 SẮP XẾP QUY TRÌNH THI CÔNG</h2>", unsafe_allow_html=True)
                st.markdown("<p style='font-size: 24px; font-weight: 700;'>✨ Hướng dẫn: Bấm chọn các mục quy trình bên dưới để đưa vào bảng theo đúng trình tự chuẩn! ✨</p>", unsafe_allow_html=True)
                
                st.markdown("<h4 style='font-size: 26px; margin-top: 20px;'>📋 BẢNG THỨ TỰ CỦA BẠN:</h4>", unsafe_allow_html=True)
                if not st.session_state.user_sequence:
                    st.info("Bảng đang trống. Hãy chọn các quy trình bên dưới...")
                else:
                    chosen_cols = st.columns(4)
                    for i, p in enumerate(st.session_state.user_sequence):
                        with chosen_cols[i % 4]:
                            st.markdown(f"<div class='selected-step-box'><b>#{i+1}</b><br>{p}</div>", unsafe_allow_html=True)
                        
                if len(st.session_state.user_sequence) == 8:
                    st.markdown("---")
                    correct_count = sum(1 for i in range(8) if st.session_state.user_sequence[i] == CORRECT_SEQUENCE[i])
                    
                    if correct_count == 8:
                        st.success("✅ CHUẨN XÁC 8/8 QUY TRÌNH! Bạn đã hoàn thành bước dựng tiến độ.")
                        if st.button("🚀 CHUYỂN SANG KHO CHỌN VẬT LIỆU 🚀"):
                            st.session_state.phase = 2
                            st.rerun()
                    else:
                        st.error(f"❌ Bạn đã xếp đúng {correct_count}/8 quy trình. Thứ tự chưa chính xác!")
                        if st.button("🔄 XÓA & SẮP XẾP LẠI 🔄"):
                            st.session_state.user_sequence = []
                            st.rerun()
                else:
                    st.markdown("---")
                    st.markdown("<h4 style='font-size: 26px;'>🗂️ DANH SÁCH QUY TRÌNH (Bấm để chọn):</h4>", unsafe_allow_html=True)
                    remaining = [p for p in st.session_state.shuffled_processes if p not in st.session_state.user_sequence]
                    
                    grid_cols = st.columns(4)
                    for i, proc in enumerate(remaining):
                        with grid_cols[i % 4]:
                            if st.button(proc, key=f"btn_p1_{proc}"):
                                st.session_state.user_sequence.append(proc)
                                st.rerun()
                                
                    st.write("")
                    if len(st.session_state.user_sequence) > 0:
                        if st.button("⏪ XÓA LÀM LẠI TỪ ĐẦU ⏪"):
                            st.session_state.user_sequence = []
                            st.rerun()
            
        # -----------------------------------------------------
        # PHASE 2: BẢNG CHỌN VẬT LIỆU
        # -----------------------------------------------------
        elif st.session_state.phase == 2:
            with st.container(border=True):
                st.markdown("<h2>🛒 BƯỚC 2: 💎 QUẢN LÝ VẬT TƯ (MATERIALS)</h2>", unsafe_allow_html=True)
                st.markdown("<p style='font-size: 24px; font-weight: 700;'>✨ Hướng dẫn: Bấm vào các hạng mục bên dưới để phê duyệt vật liệu xây dựng! ✨</p>", unsafe_allow_html=True)
                st.write("")
                
                btn_cols = st.columns(4)
                for i, step_data in enumerate(game_data):
                    with btn_cols[i % 4]:
                        if i in st.session_state.completed_materials:
                            st.button(f"✅ ĐÃ DUYỆT:\n{step_data['title']}", key=f"btn_p2_{i}", disabled=True)
                        else:
                            if st.button(f"⚙️ XỬ LÝ:\n{step_data['title']}", key=f"btn_p2_{i}"):
                                st.session_state.active_material_step = i
                                st.rerun()

        # -----------------------------------------------------
        # PHASE 3: KẾT QUẢ NGHIỆM THU
        # -----------------------------------------------------
        elif st.session_state.phase == 3:
            with st.container(border=True):
                st.markdown("<h2>🎯 HỒ SƠ NGHIỆM THU CÔNG TRÌNH 🏆</h2>", unsafe_allow_html=True)
                st.markdown(f"<h3>ĐIỂM AN TOÀN KỸ THUẬT: <br><span style='color: #FFD700 !important; font-size: 70px; text-shadow: 0 0 20px #FFD700;'>{st.session_state.score} / 80 ĐIỂM</span></h3>", unsafe_allow_html=True)
                
                if st.session_state.score == 80:
                    st.success("✅ ĐẠT CHUẨN QUỐC TẾ! CÔNG TRÌNH HOÀN HẢO TUYỆT ĐỐI! 🎉")
                    st.balloons()
                    
                    st.markdown("---")
                    st.markdown("<h3 style='text-align: center; margin-bottom: 30px; font-size: 38px; color: #FFD700 !important; text-shadow: 0 0 15px #FFD700;'>🏆 BẢNG VẬT LIỆU CHUẨN ĐÃ SỬ DỤNG 🏆</h3>", unsafe_allow_html=True)
                    
                    for item in game_data:
                        correct_material = next(opt["text"] for opt in item["options"] if opt["correct"])
                        st.markdown(f"""
                        <div class='perfect-material-box'>
                            <span style='width: 35%; font-size: 22px;'>{item['title']}</span> 
                            <span style='width: 65%; border-left: 3px solid rgba(255,255,255,0.4); padding-left: 20px; font-size: 22px;'>{correct_material}</span>
                        </div>
                        """, unsafe_allow_html=True)
                        
                elif st.session_state.score >= 50:
                    st.warning("⚠️ ĐẠT YÊU CẦU CƠ BẢN. Kiến trúc bề ngoài ổn nhưng tồn tại rủi ro rình rập!")
                else:
                    st.error("🚨 KHÔNG ĐẠT! Vi phạm nghiêm trọng tiêu chuẩn kỹ thuật xây dựng!")
                
                if st.session_state.issues:
                    st.markdown("<h4 style='font-size: 26px; margin-top: 30px;'>🛠️ BÁO CÁO SỰ CỐ VẬT LIỆU:</h4>", unsafe_allow_html=True)
                    for issue in st.session_state.issues:
                        st.markdown(f"<p style='padding-left: 15px; border-left: 4px solid #FFD700; font-size: 22px; font-weight: bold;'>{issue}</p>", unsafe_allow_html=True)

                st.write("")
                if st.button("🔄 BẮT ĐẦU DỰ ÁN MỚI 🔄"):
                    st.session_state.clear()
                    st.rerun()
