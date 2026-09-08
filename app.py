import streamlit as st
import random

# --- 1. CẤU HÌNH GIAO DIỆN (XANH BÓNG SANG TRỌNG - CHỮ GỌN GÀNG) ---
st.set_page_config(page_title="Design Your House", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
    /* Nền Gradient Xanh Dương Bóng Bẩy tĩnh */
    .stApp {
        background: radial-gradient(circle at 50% 0%, #00C6FF 0%, #0284C7 40%, #011229 100%);
    }
    
    /* Chữ màu trắng với hiệu ứng đổ bóng */
    h1, h2, h3, h4, p, span, div, label {
        color: #FFFFFF !important;
        font-family: 'Inter', 'Segoe UI', sans-serif;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.8);
    }
    
    h2 { font-size: 32px !important; font-weight: 900 !important; color: #FFD700 !important; }
    h3 { font-size: 24px !important; font-weight: 800 !important; }
    h4 { font-size: 20px !important; font-weight: 700 !important; }
    
    /* TÙY CHỈNH KHUNG CHỨA (CONTAINER) */
    [data-testid="stVerticalBlockBorderWrapper"] {
        background: rgba(0, 0, 0, 0.3) !important;
        backdrop-filter: blur(10px);
        border: 2px solid #FFD700 !important;
        border-radius: 20px !important;
        box-shadow: 0 0 15px rgba(255, 215, 0, 0.3), inset 0 0 10px rgba(255, 255, 255, 0.1) !important;
        padding: 10px;
    }

    /* TAB CỬA SỔ KHỔNG LỒ (MODAL) */
    .huge-modal {
        background: rgba(3, 39, 89, 0.98);
        border-radius: 24px;
        padding: 40px 50px;
        box-shadow: 0 0 40px rgba(255, 215, 0, 0.6);
        border: 3px solid #FFD700;
        animation: slideUp 0.3s ease-out;
        text-align: center;
        margin: 0 auto;
        max-width: 1000px;
    }
    
    @keyframes slideUp {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }

    /* Nút bấm (Buttons) Gọn gàng hơn */
    .stButton>button {
        background: linear-gradient(90deg, #FFD700 0%, #FFA500 100%);
        color: #000000 !important;
        border-radius: 12px;
        font-weight: 800;
        font-size: 16px !important; 
        padding: 15px 10px !important; 
        border: none;
        transition: all 0.3s;
        width: 100%;
        text-transform: uppercase;
        box-shadow: 0 4px 15px rgba(255, 215, 0, 0.4);
        margin-top: 10px;
        text-shadow: none !important;
        white-space: normal !important; 
        word-wrap: break-word;
        height: auto !important;
        min-height: 80px; 
        display: flex;
        justify-content: center;
        align-items: center;
    }
    .stButton>button:hover {
        background: linear-gradient(90deg, #FFFFFF 0%, #FFD700 100%);
        transform: translateY(-3px);
        box-shadow: 0 8px 20px rgba(255, 255, 255, 0.6);
    }
    
    button[disabled] {
        background: rgba(255, 255, 255, 0.1) !important;
        color: rgba(255, 255, 255, 0.5) !important;
        box-shadow: none !important;
        border: 2px dashed rgba(255, 255, 255, 0.3) !important;
        transform: none !important;
    }
    
    /* CSS Chữ của các đáp án Radio vừa phải */
    .stRadio p {
        font-size: 22px !important; 
        font-weight: 700 !important;
        color: #FFFFFF !important;
        padding-left: 10px;
        margin-bottom: 10px;
        line-height: 1.4;
    }
    
    /* Ô quy trình đang xếp - Ngang và Gọn */
    .selected-step-box {
        background: rgba(255, 215, 0, 0.2);
        border: 2px solid #FFD700;
        border-radius: 10px;
        padding: 10px 10px;
        text-align: center;
        font-weight: 800;
        color: #FFFFFF !important;
        margin-bottom: 15px;
        box-shadow: 0 0 10px rgba(255, 215, 0, 0.3);
        height: 80px; 
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 16px; 
    }

    /* Danh sách vật liệu hoàn hảo 80/80 */
    .perfect-material-box {
        background: rgba(255, 215, 0, 0.2);
        border: 2px solid #FFD700;
        border-radius: 12px;
        padding: 15px 20px;
        margin-bottom: 12px;
        font-size: 18px; 
        font-weight: 800;
        color: #FFFFFF;
        display: flex;
        align-items: center;
        text-align: left;
        box-shadow: 0 0 15px rgba(255, 215, 0, 0.4);
    }
    
    /* Style riêng cho caption ảnh */
    .caption {
        font-size: 18px !important;
        font-weight: bold;
        color: #FFD700 !important;
        text-align: center;
        margin-top: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# --- 2. DỮ LIỆU TRÒ CHƠI ---
game_data = [
    {
        "title": "🏗️ LÀM MÓNG",
        "desc": "Nền tảng vững chắc quyết định tuổi thọ của cả công trình.",
        "options": [
            {"text": "🪙 Hợp kim nhôm nguyên khối (Solid aluminum)", "correct": False, "error": "- Móng Nhôm: Chịu nén kém, oxy hóa ngầm làm sập nhà."},
            {"text": "🧱 Bê tông cốt thép chuẩn (Reinforced concrete)", "correct": True, "error": ""},
            {"text": "🪨 Bê tông đúc chuẩn (Standard cast concrete)", "correct": False, "error": "- Móng Bê tông đúc: Thiếu lõi thép sẽ rất giòn, không chịu được lực uốn, gây gãy nứt móng."}
        ]
    },
    {
        "title": "⛓️ ĐỔ KHUNG CỘT",
        "desc": "Hệ xương sống chống chịu mọi bão tố và tải trọng.",
        "options": [
            {"text": "🔲 Sắt non dập hộp (Soft iron box)", "correct": False, "error": "- Cột Sắt non: Chịu tải kém, móp méo và gãy gập ngay khi gánh sức nặng tầng trên."},
            {"text": "〰️ Thép trơn siêu dẻo (Flexible smooth steel)", "correct": False, "error": "- Cột Thép dẻo: Không bám dính bê tông, rung lắc là gãy."},
            {"text": "📌 Thép vằn cường độ cao (High-strength steel)", "correct": True, "error": ""}
        ]
    },
    {
        "title": "🧱 XÂY TƯỜNG",
        "desc": "Lớp áo giáp bảo vệ không gian sống khỏi thời tiết.",
        "options": [
            {"text": "🧱 Gạch đất nung / Gạch AAC (Fired brick / AAC)", "correct": True, "error": ""},
            {"text": "🌑 Gạch xỉ than tái chế (Recycled cinder block)", "correct": False, "error": "- Tường Xỉ than: Hút nước như bọt biển, ngập ngụa khi mưa."},
            {"text": "🧱 Gạch block xi măng tự trộn (Hand-mixed cement block)", "correct": False, "error": "- Tường Xi măng tự trộn: Trộn thủ công sai tỷ lệ khiến gạch bở rạc, ngấm nước và nứt toác sau 1 mùa mưa."}
        ]
    },
    {
        "title": "🏠 LÀM MÁI",
        "desc": "Lá chắn che chở tổ ấm khỏi nắng mưa.",
        "options": [
            {"text": "🛸 Mái nhôm đúc nguyên tấm (Cast aluminum roof)", "correct": False, "error": "- Mái Nhôm: Hấp thụ nhiệt siêu tốc, áp mái nóng như lò bát quái."},
            {"text": "🎨 Ngói xi măng ép màu (Color pressed cement)", "correct": False, "error": "- Ngói ép: Phơi nắng 1 năm là nứt rạn, dột tong tỏng."},
            {"text": "🏠 Bê tông & Ngói tráng men (Concrete & glazed tiles)", "correct": True, "error": ""}
        ]
    },
    {
        "title": "⚡ ĐIỆN NƯỚC ÂM",
        "desc": "Mạch máu ngầm cung cấp tiện nghi cho ngôi nhà.",
        "options": [
            {"text": "🚿 Ống nước Inox mạ bạc (Silver-plated Inox pipe)", "correct": False, "error": "- Ống Inox ngầm: Trở thành bẫy giật điện chết người nếu rò điện."},
            {"text": "⚡ Dây đồng & Ống nhựa PPR (Copper wire & PPR pipe)", "correct": True, "error": ""},
            {"text": "🔌 Dây điện lõi nhôm (Aluminum core wire)", "correct": False, "error": "- Dây Nhôm: Sinh nhiệt cao, chập cháy ngầm trong tường."}
        ]
    },
    {
        "title": "⏳ TRÁT TƯỜNG",
        "desc": "Làm phẳng và chuẩn bị bề mặt cho bước trang trí.",
        "options": [
            {"text": "🧪 Keo Epoxy pha bột đá (Epoxy with stone powder)", "correct": False, "error": "- Trát Epoxy: Tường không thở được, mồ hôi ướt nhẹp khi nồm."},
            {"text": "💨 Xi măng nguyên chất (Pure cement without sand)", "correct": False, "error": "- Xi măng nguyên chất: Co ngót cực mạnh, nứt toác chân chim."},
            {"text": "⏳ Vữa xi măng trộn cát mịn (Cement & fine sand)", "correct": True, "error": ""}
        ]
    },
    {
        "title": "🎨 LÁT GẠCH & SƠN",
        "desc": "Khoác lên ngôi nhà vẻ đẹp thẩm mỹ lộng lẫy.",
        "options": [
            {"text": "🛡️ Keo dán gạch & Sơn chống thấm (Tile adhesive & paint)", "correct": True, "error": ""},
            {"text": "💧 Nước xi măng lỏng (Liquid cement slurry)", "correct": False, "error": "- Lát nước xi măng: Gạch phồng rộp, nổ vỡ lụp bụp."},
            {"text": "🛢️ Sơn dầu bóng công nghiệp (Industrial oil paint)", "correct": False, "error": "- Sơn dầu: Bong tróc, lột ra từng mảng như da rắn."}
        ]
    },
    {
        "title": "🛋️ NỘI THẤT",
        "desc": "Hoàn thiện không gian sống tiện nghi, sang trọng.",
        "options": [
            {"text": "✈️ Bồn cầu đúc Nhôm hàng không (Aluminum toilet)", "correct": False, "error": "- Bồn cầu Nhôm: Kỵ hóa chất, xịt tẩy bồn cầu là sùi bọt trắng."},
            {"text": "🍴 Tủ bếp bọc Bạc nguyên miếng (Solid silver cabinets)", "correct": False, "error": "- Tủ bếp Bạc: Phản ứng muối mắm, xỉn đen thui cực kỳ bẩn."},
            {"text": "🛋️ Gỗ MDF chống ẩm & Sứ Nano (MDF & Nano porcelain)", "correct": True, "error": ""}
        ]
    }
]

CORRECT_SEQUENCE = [step["title"] for step in game_data]

# -----------------------------------------------------
# LOGIC HÌNH ẢNH LẮP RÁP MÔ HÌNH
# -----------------------------------------------------
construction_images = [
    "https://images.unsplash.com/photo-1503387762-592deb58ef4e?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80", # 0: Bản vẽ
    "https://images.unsplash.com/photo-1541888087405-f3900fb3033f?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80", # 1: Móng
    "https://images.unsplash.com/photo-1504307651254-35680f356dfd?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80", # 2: Khung
    "https://images.unsplash.com/photo-1589939705384-5185137a7f0f?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80", # 3: Tường
    "https://images.unsplash.com/photo-1632759145351-1d592919f522?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80", # 4: Mái
    "https://images.unsplash.com/photo-1621905252507-b35492cc74b4?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80", # 5: Điện nước
    "https://images.unsplash.com/photo-1588854337221-4cf9fa968114?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80", # 6: Trát tường
    "https://images.unsplash.com/photo-1521193089946-b338fa7419f8?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80", # 7: Sơn lát
    "https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80"  # 8: Hoàn thiện
]

progress_captions = [
    "📝 Giai đoạn 0: Khảo sát & Bản vẽ",
    "🧱 Giai đoạn 1: Đổ Móng Bê Tông",
    "🏗️ Giai đoạn 2: Lên Khung Cột Thép",
    "🧱 Giai đoạn 3: Xây Tường Gạch",
    "☂️ Giai đoạn 4: Cất Nóc Lợp Mái",
    "🔌 Giai đoạn 5: Thi công Điện Nước Âm",
    "🖌️ Giai đoạn 6: Trát Tường Làm Phẳng",
    "✨ Giai đoạn 7: Ốp Lát & Sơn Bả",
    "🎉 HOÀN THIỆN: NGÔI NHÀ CỦA BẠN!"
]

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
    st.markdown(f"<h1 style='font-size: 40px;'>🛒 LỰA CHỌN VẬT LIỆU<br><span style='color: #FFD700 !important;'>{current_data['title']}</span></h1>", unsafe_allow_html=True)
    st.markdown(f"<h3 style='font-size: 20px; color: rgba(255,255,255,0.9); margin-bottom: 20px;'>💡 {current_data['desc']}</h3>", unsafe_allow_html=True)
    st.write("---")
    
    st.markdown("<h2 style='font-size: 32px; color: #FFFFFF; margin-bottom: 20px;'>👉 VẬT LIỆU NÀO ĐẠT TIÊU CHUẨN KỸ THUẬT? 🧐</h2>", unsafe_allow_html=True)
    
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
    st.markdown("<div style='text-align: center; margin-bottom: 30px;'>", unsafe_allow_html=True)
    try:
        st.image("image_04e8c0.png", use_container_width=True)
    except:
        st.markdown("<h1 style='font-size: 50px; font-weight: 900; color: #FFD700 !important;'>🏡 DESIGN YOUR HOUSE 🏡</h1>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([4, 6], gap="large")
    
    # CỘT 1: HÌNH ẢNH MÔ HÌNH LẮP RÁP (Thay đổi tùy số bước đã chọn)
    with col1:
        with st.container(border=True):
            st.markdown("<h3 style='text-align: center; font-size: 26px;'>🧩 TIẾN ĐỘ THI CÔNG</h3>", unsafe_allow_html=True)
            
            # Tính toán tiến trình
            if st.session_state.phase == 1:
                current_step_count = len(st.session_state.user_sequence)
            elif st.session_state.phase == 2:
                current_step_count = 8 
            else:
                current_step_count = 8
                
            st.image(construction_images[current_step_count], use_container_width=True)
            st.markdown(f"<div class='caption'>{progress_captions[current_step_count]}</div>", unsafe_allow_html=True)

    # CỘT 2: KHU VỰC TƯƠNG TÁC CHÍNH
    with col2:
        # -----------------------------------------------------
        # PHASE 1: SẮP XẾP QUY TRÌNH
        # -----------------------------------------------------
        if st.session_state.phase == 1:
            with st.container(border=True):
                st.markdown("<h2>📌 BƯỚC 1: SẮP XẾP QUY TRÌNH</h2>", unsafe_allow_html=True)
                st.markdown("<p style='font-size: 18px; color: #FFD700 !important;'>✨ Bấm chọn các khối bên dưới để ghép vào bảng thi công! ✨</p>", unsafe_allow_html=True)
                
                st.markdown("<h4 style='margin-top: 15px;'>📋 BẢNG THỨ TỰ CỦA BẠN:</h4>", unsafe_allow_html=True)
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
                        st.success("✅ CHUẨN XÁC 8/8 QUY TRÌNH! Bạn đã thiết lập xong tiến độ chuẩn.")
                        if st.button("🚀 CHUYỂN SANG KHO CHỌN VẬT LIỆU 🚀"):
                            st.session_state.phase = 2
                            st.rerun()
                    else:
                        st.error(f"❌ Bạn đã xếp đúng {correct_count}/8 quy trình. Thứ tự chưa chính xác, công trình sẽ gặp lỗi!")
                        if st.button("🔄 XÓA & SẮP XẾP LẠI 🔄"):
                            st.session_state.user_sequence = []
                            st.rerun()
                else:
                    st.markdown("---")
                    st.markdown("<h4>🗂️ CÁC KHỐI QUY TRÌNH (Bấm để ghép):</h4>", unsafe_allow_html=True)
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
                st.markdown("<h2>🛒 BƯỚC 2: QUẢN LÝ VẬT TƯ</h2>", unsafe_allow_html=True)
                st.markdown("<p style='font-size: 18px; color: #FFD700 !important;'>✨ Bấm vào các hạng mục bên dưới để phê duyệt vật liệu xây dựng! ✨</p>", unsafe_allow_html=True)
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
                st.markdown(f"<h3>ĐIỂM AN TOÀN KỸ THUẬT: <br><span style='color: #FFD700 !important; font-size: 50px;'>{st.session_state.score} / 80 ĐIỂM</span></h3>", unsafe_allow_html=True)
                
                if st.session_state.score == 80:
                    st.success("✅ ĐẠT CHUẨN QUỐC TẾ! CÔNG TRÌNH HOÀN HẢO TUYỆT ĐỐI! 🎉")
                    st.balloons()
                    
                    st.markdown("---")
                    st.markdown("<h3 style='text-align: center; margin-bottom: 20px; color: #FFD700 !important;'>🏆 BẢNG VẬT LIỆU CHUẨN ĐÃ SỬ DỤNG 🏆</h3>", unsafe_allow_html=True)
                    
                    for item in game_data:
                        correct_material = next(opt["text"] for opt in item["options"] if opt["correct"])
                        st.markdown(f"""
                        <div class='perfect-material-box'>
                            <span style='width: 35%; font-size: 18px;'>{item['title']}</span> 
                            <span style='width: 65%; border-left: 2px solid rgba(255,255,255,0.4); padding-left: 15px; font-size: 18px;'>{correct_material}</span>
                        </div>
                        """, unsafe_allow_html=True)
                        
                elif st.session_state.score >= 50:
                    st.warning("⚠️ ĐẠT YÊU CẦU CƠ BẢN. Kiến trúc bề ngoài ổn nhưng tồn tại rủi ro rình rập!")
                else:
                    st.error("🚨 KHÔNG ĐẠT! Vi phạm nghiêm trọng tiêu chuẩn kỹ thuật xây dựng!")
                
                if st.session_state.issues:
                    st.markdown("<h4 style='margin-top: 20px;'>🛠️ BÁO CÁO SỰ CỐ VẬT LIỆU:</h4>", unsafe_allow_html=True)
                    for issue in st.session_state.issues:
                        st.markdown(f"<p style='padding-left: 15px; border-left: 4px solid #FFD700; font-size: 18px; font-weight: bold;'>{issue}</p>", unsafe_allow_html=True)

                st.write("")
                if st.button("🔄 BẮT ĐẦU DỰ ÁN MỚI 🔄"):
                    st.session_state.clear()
                    st.rerun()
