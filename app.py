import streamlit as st
import random

# --- 1. CẤU HÌNH GIAO DIỆN (GLASSMORPHISM LIGHT BLUE - SANG TRỌNG BÓNG BẨY) ---
st.set_page_config(page_title="Design Your House", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
    /* Nền Gradient Xanh Dương pha Trắng bóng bẩy, sang trọng */
    .stApp {
        background: linear-gradient(135deg, #e3f2fd, #e8eaf6, #bbdefb);
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    /* Chữ màu Xanh Đậm (Deep Blue) với hiệu ứng bóng kính */
    h1, h2, h3, h4, p, span, div, label {
        color: #0D47A1 !important;
        text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.08);
    }
    
    h2, h3, h4 {
        font-weight: 800;
    }
    
    /* Tiêu đề chính to, đổ gradient chữ và sáng rực rỡ */
    h1.main-title {
        font-weight: 900;
        background: linear-gradient(to right, #1565C0, #0288D1, #1565C0);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-shadow: 3px 3px 8px rgba(0, 100, 255, 0.2) !important;
        letter-spacing: 4px;
        text-transform: uppercase;
    }
    
    /* TÙY CHỈNH KHUNG CHỨA (CONTAINER) THÀNH KÍNH TRẮNG TRONG SUỐT (GLASSMORPHISM) */
    [data-testid="stVerticalBlockBorderWrapper"] {
        background: rgba(255, 255, 255, 0.75) !important;
        backdrop-filter: blur(15px);
        border: 1px solid rgba(255, 255, 255, 0.9) !important;
        border-radius: 20px !important;
        box-shadow: 0 15px 35px rgba(21, 101, 192, 0.12) !important;
    }

    /* TAB CỬA SỔ KHỔNG LỒ (MODAL) ĐẸP MẮT CHO BƯỚC CHỌN VẬT LIỆU */
    .huge-modal {
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(25px);
        border-radius: 24px;
        padding: 60px;
        box-shadow: 0 25px 60px rgba(13, 71, 161, 0.25);
        border: 3px solid #90caf9;
        animation: popIn 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275) forwards;
        text-align: center;
        margin: 0 auto;
        max-width: 1000px;
    }
    
    @keyframes popIn {
        0% { transform: scale(0.9); opacity: 0; }
        100% { transform: scale(1); opacity: 1; }
    }

    /* Nút bấm (Buttons) hiệu ứng Bóng nổi (Glossy 3D) */
    .stButton>button {
        background: linear-gradient(to bottom, #ffffff, #e3f2fd);
        color: #1565C0 !important;
        border-radius: 15px;
        font-weight: 900;
        font-size: 18px;
        padding: 15px 10px;
        border: 2px solid #90caf9;
        transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
        width: 100%;
        text-transform: uppercase;
        box-shadow: 0 6px 15px rgba(21, 101, 192, 0.15);
        margin-top: 15px;
    }
    .stButton>button:hover {
        border-color: #1565C0;
        background: linear-gradient(145deg, #1E88E5, #0D47A1);
        color: #ffffff !important;
        transform: translateY(-4px);
        box-shadow: 0 12px 25px rgba(13, 71, 161, 0.4);
    }
    
    button[disabled] {
        background: rgba(255, 255, 255, 0.5) !important;
        color: rgba(13, 71, 161, 0.3) !important;
        box-shadow: none !important;
        border: 1px solid rgba(144, 202, 249, 0.3) !important;
        transform: none !important;
    }
    
    /* CSS Phóng to chữ của các đáp án Radio */
    .stRadio p {
        font-size: 26px !important;
        font-weight: bold !important;
        color: #0D47A1 !important;
        padding-left: 10px;
        margin-bottom: 10px;
    }
    
    /* Ô quy trình đang xếp - Hiệu ứng phím cơ 3D */
    .selected-step-box {
        background: linear-gradient(145deg, #ffffff, #f0f7ff);
        border: 2px solid #64B5F6;
        border-radius: 12px;
        padding: 15px 10px;
        text-align: center;
        font-weight: bold;
        color: #1565C0 !important;
        margin-bottom: 15px;
        box-shadow: inset 0px 3px 6px rgba(255,255,255,1), 0 5px 15px rgba(30, 136, 229, 0.15);
        height: 80px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 15px;
    }

    /* Danh sách vật liệu hoàn hảo 80/80 */
    .perfect-material-box {
        background: linear-gradient(145deg, #ffffff, #e8f5e9);
        border: 2px solid #81c784;
        border-radius: 15px;
        padding: 15px 20px;
        margin-bottom: 15px;
        font-size: 18px;
        font-weight: bold;
        color: #00796B !important;
        display: flex;
        align-items: center;
        text-align: left;
        box-shadow: inset 0px 3px 6px rgba(255,255,255,1), 0 5px 15px rgba(56, 142, 60, 0.15);
    }
    </style>
""", unsafe_allow_html=True)

# --- 2. DỮ LIỆU TRÒ CHƠI (Đã xáo trộn vị trí đáp án đúng trong Source Code) ---
game_data = [
    {
        "title": "🏗️ Làm Móng",
        "desc": "Nền tảng vững chắc quyết định tuổi thọ của cả công trình.",
        "options": [
            {"text": "🪙 Hợp kim nhôm nguyên khối (Solid aluminum)", "correct": False, "error": "- Móng Nhôm: Chịu nén kém, oxy hóa ngầm làm sập nhà."},
            {"text": "🧱 Bê tông cốt thép chuẩn (Reinforced concrete)", "correct": True, "error": ""},
            {"text": "🪨 Bê tông đúc chuẩn (Standard cast concrete)", "correct": False, "error": "- Móng Bê tông đúc: Thiếu lõi thép sẽ rất giòn, không chịu được lực uốn, gây gãy nứt móng."}
        ]
    },
    {
        "title": "⛓️ Đổ Khung Cột",
        "desc": "Hệ xương sống chống chịu mọi bão tố và tải trọng.",
        "options": [
            {"text": "🔲 Sắt non dập hộp (Soft iron box)", "correct": False, "error": "- Cột Sắt non: Chịu tải kém, móp méo và gãy gập ngay khi gánh sức nặng tầng trên."},
            {"text": "〰️ Thép trơn siêu dẻo (Flexible smooth steel)", "correct": False, "error": "- Cột Thép dẻo: Không bám dính bê tông, rung lắc là gãy."},
            {"text": "📌 Thép vằn cường độ cao (High-strength steel)", "correct": True, "error": ""}
        ]
    },
    {
        "title": "🧱 Xây Tường",
        "desc": "Lớp áo giáp bảo vệ không gian sống khỏi thời tiết.",
        "options": [
            {"text": "🧱 Gạch đất nung / Gạch AAC (Fired brick / AAC)", "correct": True, "error": ""},
            {"text": "🌑 Gạch xỉ than tái chế (Recycled cinder block)", "correct": False, "error": "- Tường Xỉ than: Hút nước như bọt biển, ngập ngụa khi mưa."},
            {"text": "🧱 Gạch block xi măng tự trộn (Hand-mixed cement block)", "correct": False, "error": "- Tường Xi măng tự trộn: Trộn thủ công sai tỷ lệ khiến gạch bở rạc, ngấm nước và nứt toác sau 1 mùa mưa."}
        ]
    },
    {
        "title": "🏠 Làm Mái",
        "desc": "Lá chắn che chở tổ ấm khỏi nắng mưa.",
        "options": [
            {"text": "🛸 Mái nhôm đúc nguyên tấm (Cast aluminum roof)", "correct": False, "error": "- Mái Nhôm: Hấp thụ nhiệt siêu tốc, áp mái nóng như lò bát quái."},
            {"text": "🎨 Ngói xi măng ép màu (Color pressed cement)", "correct": False, "error": "- Ngói ép: Phơi nắng 1 năm là nứt rạn, dột tong tỏng."},
            {"text": "🏠 Bê tông & Ngói tráng men (Concrete & glazed tiles)", "correct": True, "error": ""}
        ]
    },
    {
        "title": "⚡ Điện Nước Âm",
        "desc": "Mạch máu ngầm cung cấp tiện nghi cho ngôi nhà.",
        "options": [
            {"text": "🚿 Ống nước Inox mạ bạc (Silver-plated Inox pipe)", "correct": False, "error": "- Ống Inox ngầm: Trở thành bẫy giật điện chết người nếu rò điện."},
            {"text": "⚡ Dây đồng & Ống nhựa PPR (Copper wire & PPR pipe)", "correct": True, "error": ""},
            {"text": "🔌 Dây điện lõi nhôm (Aluminum core wire)", "correct": False, "error": "- Dây Nhôm: Sinh nhiệt cao, chập cháy ngầm trong tường."}
        ]
    },
    {
        "title": "⏳ Trát Tường",
        "desc": "Làm phẳng và chuẩn bị bề mặt cho bước trang trí.",
        "options": [
            {"text": "🧪 Keo Epoxy pha bột đá (Epoxy with stone powder)", "correct": False, "error": "- Trát Epoxy: Tường không thở được, mồ hôi ướt nhẹp khi nồm."},
            {"text": "💨 Xi măng nguyên chất (Pure cement without sand)", "correct": False, "error": "- Xi măng nguyên chất: Co ngót cực mạnh, nứt toác chân chim."},
            {"text": "⏳ Vữa xi măng trộn cát mịn (Cement & fine sand)", "correct": True, "error": ""}
        ]
    },
    {
        "title": "🎨 Lát Gạch & Sơn",
        "desc": "Khoác lên ngôi nhà vẻ đẹp thẩm mỹ lộng lẫy.",
        "options": [
            {"text": "🛡️ Keo dán gạch & Sơn chống thấm (Tile adhesive & paint)", "correct": True, "error": ""},
            {"text": "💧 Nước xi măng lỏng (Liquid cement slurry)", "correct": False, "error": "- Lát nước xi măng: Gạch phồng rộp, nổ vỡ lụp bụp."},
            {"text": "🛢️ Sơn dầu bóng công nghiệp (Industrial oil paint)", "correct": False, "error": "- Sơn dầu: Bong tróc, lột ra từng mảng như da rắn."}
        ]
    },
    {
        "title": "🛋️ Nội Thất",
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
    st.markdown(f"<h1>LỰA CHỌN VẬT LIỆU<br><span style='color: #1E88E5 !important; font-size: 50px;'>{current_data['title']}</span></h1>", unsafe_allow_html=True)
    st.markdown(f"<h3 style='font-size: 24px; color: #1565C0;'>{current_data['desc']}</h3>", unsafe_allow_html=True)
    st.write("---")
    
    # In đậm và làm to câu hỏi bằng Markdown
    st.markdown("<h2 style='font-size: 35px; color: #0D47A1; font-weight: 900; margin-bottom: 20px;'>👉 VẬT LIỆU NÀO ĐẠT TIÊU CHUẨN KỸ THUẬT?</h2>", unsafe_allow_html=True)
    
    option_texts = [opt["text"] for opt in current_opts]
    # label_visibility="collapsed" để ẩn cái label mặc định bé xíu của Streamlit
    choice = st.radio("Chọn vật liệu", option_texts, index=None, label_visibility="collapsed")
    
    st.write("")
    st.write("")
    col_btn1, col_btn2, col_btn3 = st.columns([1, 2, 1])
    with col_btn2:
        if st.button("XÁC NHẬN VẬT LIỆU"):
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
                st.error("⚠️ Vui lòng chọn 1 loại vật liệu!")
    st.markdown("</div>", unsafe_allow_html=True)

# =========================================================================
# GIAO DIỆN CHÍNH
# =========================================================================
else:
    # HIỂN THỊ TIÊU ĐỀ
    st.markdown("<h1 class='main-title' style='text-align: center; margin-bottom: 40px;'>DESIGN YOUR HOUSE</h1>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([3, 7], gap="large")
    
    # CỘT 1: THƯ VIỆN NHÀ MẪU
    with col1:
        with st.container(border=True):
            st.markdown("<h3 style='text-align: center;'>Mẫu Nhà Hiện Đại</h3>", unsafe_allow_html=True)
            st.image("https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80", use_container_width=True, caption="Modern Villa")
            st.markdown("<br>", unsafe_allow_html=True)
            st.image("https://images.unsplash.com/photo-1613977257363-707ba9348227?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80", use_container_width=True, caption="Luxury Mansion")

    # CỘT 2: KHU VỰC TƯƠNG TÁC CHÍNH
    with col2:
        # -----------------------------------------------------
        # PHASE 1: SẮP XẾP QUY TRÌNH
        # -----------------------------------------------------
        if st.session_state.phase == 1:
            with st.container(border=True):
                st.markdown("<h2>BƯỚC 1: SẮP XẾP QUY TRÌNH THI CÔNG</h2>", unsafe_allow_html=True)
                st.write("Bấm chọn các mục quy trình bên dưới để đưa vào bảng theo đúng trình tự chuẩn.")
                
                st.markdown("#### 📋 Bảng thứ tự của bạn:")
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
                        if st.button("🚀 CHUYỂN SANG KHO CHỌN VẬT LIỆU ->"):
                            st.session_state.phase = 2
                            st.rerun()
                    else:
                        st.error(f"❌ Bạn đã xếp đúng {correct_count}/8 quy trình. Thứ tự chưa chính xác!")
                        if st.button("🔄 XÓA & SẮP XẾP LẠI (RESET)"):
                            st.session_state.user_sequence = []
                            st.rerun()
                else:
                    st.markdown("---")
                    st.markdown("#### 🗂️ Danh sách quy trình (Click để đưa vào bảng):")
                    remaining = [p for p in st.session_state.shuffled_processes if p not in st.session_state.user_sequence]
                    
                    grid_cols = st.columns(4)
                    for i, proc in enumerate(remaining):
                        with grid_cols[i % 4]:
                            if st.button(proc, key=f"btn_p1_{proc}"):
                                st.session_state.user_sequence.append(proc)
                                st.rerun()
                                
                    st.write("")
                    if len(st.session_state.user_sequence) > 0:
                        if st.button("⏪ Xóa làm lại từ đầu (Clear)"):
                            st.session_state.user_sequence = []
                            st.rerun()
            
        # -----------------------------------------------------
        # PHASE 2: BẢNG CHỌN VẬT LIỆU
        # -----------------------------------------------------
        elif st.session_state.phase == 2:
            with st.container(border=True):
                st.markdown("<h2>BƯỚC 2: QUẢN LÝ VẬT TƯ (MATERIALS)</h2>", unsafe_allow_html=True)
                st.write("Bấm vào các hạng mục quy trình bên dưới để mở bảng chọn vật liệu chi tiết.")
                st.write("")
                
                btn_cols = st.columns(4)
                for i, step_data in enumerate(game_data):
                    with btn_cols[i % 4]:
                        if i in st.session_state.completed_materials:
                            st.button(f"✅ Đã duyệt:\n{step_data['title']}", key=f"btn_p2_{i}", disabled=True)
                        else:
                            if st.button(f"⚙️ Xử lý:\n{step_data['title']}", key=f"btn_p2_{i}"):
                                st.session_state.active_material_step = i
                                st.rerun()

        # -----------------------------------------------------
        # PHASE 3: KẾT QUẢ NGHIỆM THU
        # -----------------------------------------------------
        elif st.session_state.phase == 3:
            with st.container(border=True):
                st.markdown("<h2>🎯 HỒ SƠ NGHIỆM THU CÔNG TRÌNH</h2>", unsafe_allow_html=True)
                st.markdown(f"<h3>Điểm An toàn: <span style='color: #1E88E5 !important; font-size: 50px;'>{st.session_state.score}/80 Điểm</span></h3>", unsafe_allow_html=True)
                
                if st.session_state.score == 80:
                    st.success("✅ ĐẠT CHUẨN QUỐC TẾ. Công trình hoàn hảo tuyệt đối!")
                    st.balloons()
                    
                    st.markdown("---")
                    st.markdown("<h3 style='text-align: center; margin-bottom: 20px; color: #0288D1 !important;'>🏆 BẢNG VẬT LIỆU CHUẨN ĐÃ SỬ DỤNG</h3>", unsafe_allow_html=True)
                    
                    for item in game_data:
                        correct_material = next(opt["text"] for opt in item["options"] if opt["correct"])
                        st.markdown(f"""
                        <div class='perfect-material-box'>
                            <span style='width: 35%; color: #00796B !important;'>{item['title']}</span> 
                            <span style='width: 65%; border-left: 2px solid rgba(0, 121, 107, 0.3); padding-left: 15px; color: #004D40 !important;'>{correct_material}</span>
                        </div>
                        """, unsafe_allow_html=True)
                        
                elif st.session_state.score >= 50:
                    st.warning("⚠️ ĐẠT YÊU CẦU CƠ BẢN. Kiến trúc ổn nhưng tồn tại một số rủi ro vật liệu bên trong.")
                else:
                    st.error("🚨 KHÔNG ĐẠT. Vi phạm nghiêm trọng tiêu chuẩn kỹ thuật!")
                
                if st.session_state.issues:
                    st.markdown("#### 🛠️ BÁO CÁO SỰ CỐ VẬT LIỆU:")
                    for issue in st.session_state.issues:
                        st.markdown(f"<p style='padding-left: 10px; border-left: 3px solid #1E88E5; font-size: 18px;'>{issue}</p>", unsafe_allow_html=True)

                st.write("")
                if st.button("🔄 BẮT ĐẦU DỰ ÁN MỚI (PLAY AGAIN)"):
                    st.session_state.clear()
                    st.rerun()
