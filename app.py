import streamlit as st
import random

# --- 1. CẤU HÌNH GIAO DIỆN WIDE & CSS SIÊU MÀU MÈ ---
st.set_page_config(page_title="Dream House Builder", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
    /* Nền gradient rực rỡ */
    .stApp {
        background: linear-gradient(135deg, #FFDEE9 0%, #B5FFFC 100%);
    }
    
    h1, h2, h3, h4 {
        color: #1E3A8A;
        font-family: 'Segoe UI', sans-serif;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    
    /* Khung ảnh ngôi nhà bên trái */
    .house-card {
        background: rgba(255, 255, 255, 0.6);
        backdrop-filter: blur(15px);
        border-radius: 25px;
        padding: 20px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.15);
        border: 2px solid white;
    }
    
    /* Bảng điều khiển Quy trình bên phải */
    .dashboard-panel {
        background: rgba(255, 255, 255, 0.85);
        border-radius: 25px;
        padding: 30px;
        box-shadow: 0 15px 35px rgba(0,0,0,0.1);
        border-top: 5px solid #3B82F6;
    }

    /* Tab Cửa sổ to chọn vật liệu */
    .material-tab {
        background: linear-gradient(to right bottom, #ffffff, #f0f8ff);
        border-radius: 20px;
        padding: 40px;
        box-shadow: 0 0 40px rgba(59, 130, 246, 0.3);
        border: 3px solid #60A5FA;
        animation: fadeIn 0.5s;
    }
    
    @keyframes fadeIn {
        from { opacity: 0; transform: scale(0.95); }
        to { opacity: 1; transform: scale(1); }
    }
    
    /* Trang trí 2 bên viền màn hình (Hoa, Ô tô) */
    .decor-left {
        position: fixed; left: 10px; top: 15%; font-size: 50px; line-height: 2; z-index: 100;
        filter: drop-shadow(2px 4px 6px rgba(0,0,0,0.2));
    }
    .decor-right {
        position: fixed; right: 10px; top: 15%; font-size: 50px; line-height: 2; z-index: 100;
        filter: drop-shadow(2px 4px 6px rgba(0,0,0,0.2));
    }

    /* Nút chọn Quy trình */
    .stButton>button {
        background: linear-gradient(90deg, #3B82F6 0%, #8B5CF6 100%);
        color: white;
        border-radius: 15px;
        font-weight: bold;
        font-size: 16px;
        padding: 20px 10px;
        border: none;
        box-shadow: 0 4px 10px rgba(0,0,0,0.1);
        transition: 0.3s;
        width: 100%;
        height: 80px;
    }
    .stButton>button:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 20px rgba(59, 130, 246, 0.5);
        color: white;
    }
    
    /* Nút Quy trình đã hoàn thành */
    button[disabled] {
        background: #A7F3D0 !important;
        color: #065F46 !important;
        border: 2px solid #34D399 !important;
        transform: none !important;
        box-shadow: none !important;
    }
    </style>
    
    <!-- HTML Icon trang trí -->
    <div class="decor-left">🌸<br>🚗<br>🌺<br>🚙<br>🌷</div>
    <div class="decor-right">🌻<br>🏎️<br>🌼<br>🚕<br>🥀</div>
""", unsafe_allow_html=True)

# --- 2. DỮ LIỆU BỘ CÂU HỎI ---
game_data = [
    {
        "title": "1. Làm Móng",
        "desc": "Nền tảng vững chắc quyết định tuổi thọ của cả công trình.",
        "options": [
            {"text": "🏗️ Bê tông cốt thép (Reinforced concrete)", "correct": True, "error": ""},
            {"text": "🪙 Hợp kim nhôm nguyên khối (Solid aluminum alloy)", "correct": False, "error": "- Móng Nhôm: Chịu nén kém, oxy hóa ngầm làm sập nhà."},
            {"text": "🪨 Đá Granite nguyên tảng (Solid Granite block)", "correct": False, "error": "- Móng Đá: Thiếu liên kết khối, gây lún nứt đôi nhà."}
        ]
    },
    {
        "title": "2. Đổ Khung Cột",
        "desc": "Hệ xương sống chống chịu mọi bão tố và tải trọng.",
        "options": [
            {"text": "⛓️ Thép vằn cường độ cao (High-strength ribbed steel)", "correct": True, "error": ""},
            {"text": "〰️ Thép trơn siêu dẻo (Super flexible smooth steel)", "correct": False, "error": "- Cột Thép dẻo: Không bám dính bê tông, rung lắc là gãy."},
            {"text": "🔲 Sắt non dập hộp rỗng (Hollow soft iron)", "correct": False, "error": "- Cột Sắt rỗng: Móp méo gãy gập ngay khi chịu tải mái nhà."}
        ]
    },
    {
        "title": "3. Xây Tường",
        "desc": "Lớp áo giáp bảo vệ không gian sống khỏi thời tiết.",
        "options": [
            {"text": "🧱 Gạch đất nung / Gạch AAC (Fired brick / AAC block)", "correct": True, "error": ""},
            {"text": "🌑 Gạch xỉ than tái chế (Recycled cinder block)", "correct": False, "error": "- Tường Xỉ than: Hút nước như bọt biển, ngập ngụa khi mưa."},
            {"text": "✨ Gạch lát nền Granite (Granite floor tiles)", "correct": False, "error": "- Tường Granite: Trơn tuột, vữa không bám, đẩy nhẹ là sập."}
        ]
    },
    {
        "title": "4. Làm Mái",
        "desc": "Lá chắn che chở tổ ấm khỏi nắng mưa.",
        "options": [
            {"text": "🏠 Bê tông & Ngói tráng men (Concrete & glazed tiles)", "correct": True, "error": ""},
            {"text": "🛸 Mái nhôm đúc nguyên tấm (Cast aluminum roof)", "correct": False, "error": "- Mái Nhôm: Hấp thụ nhiệt siêu tốc, áp mái nóng như lò bát quái."},
            {"text": "🎨 Ngói xi măng ép màu (Color pressed cement tiles)", "correct": False, "error": "- Ngói ép: Phơi nắng 1 năm là nứt rạn, dột tong tỏng."}
        ]
    },
    {
        "title": "5. Điện Nước Âm",
        "desc": "Mạch máu ngầm cung cấp tiện nghi cho ngôi nhà.",
        "options": [
            {"text": "⚡ Dây đồng & Ống nhựa PPR (Copper wire & PPR pipe)", "correct": True, "error": ""},
            {"text": "🚿 Ống nước Inox mạ bạc (Silver-plated Inox pipe)", "correct": False, "error": "- Ống Inox ngầm: Trở thành bẫy giật điện chết người nếu rò điện."},
            {"text": "🔌 Dây điện lõi nhôm (Aluminum core wire)", "correct": False, "error": "- Dây Nhôm: Sinh nhiệt cao, chập cháy ngầm trong tường."}
        ]
    },
    {
        "title": "6. Trát Tường",
        "desc": "Làm phẳng và chuẩn bị bề mặt cho bước trang trí.",
        "options": [
            {"text": "⏳ Vữa xi măng trộn cát mịn (Cement & fine sand mortar)", "correct": True, "error": ""},
            {"text": "🧪 Keo Epoxy pha bột đá (Epoxy glue with stone powder)", "correct": False, "error": "- Trát Epoxy: Tường không thở được, mồ hôi ướt nhẹp khi nồm."},
            {"text": "💨 Xi măng nguyên chất (Pure cement without sand)", "correct": False, "error": "- Xi măng nguyên chất: Co ngót cực mạnh, nứt toác chân chim."}
        ]
    },
    {
        "title": "7. Lát Gạch & Sơn",
        "desc": "Khoác lên ngôi nhà vẻ đẹp thẩm mỹ lộng lẫy.",
        "options": [
            {"text": "🛡️ Keo dán gạch & Sơn chống thấm (Tile adhesive & Waterproof paint)", "correct": True, "error": ""},
            {"text": "💧 Nước xi măng lỏng (Liquid cement slurry)", "correct": False, "error": "- Lát nước xi măng: Gạch phồng rộp, nổ vỡ lụp bụp."},
            {"text": "🛢️ Sơn dầu bóng công nghiệp (Industrial glossy oil paint)", "correct": False, "error": "- Sơn dầu: Bong tróc, lột ra từng mảng như da rắn."}
        ]
    },
    {
        "title": "8. Nội Thất",
        "desc": "Hoàn thiện không gian sống tiện nghi, sang trọng.",
        "options": [
            {"text": "🛋️ Gỗ MDF chống ẩm & Sứ Nano (Moisture-resistant MDF & Nano porcelain)", "correct": True, "error": ""},
            {"text": "✈️ Bồn cầu đúc Nhôm hàng không (Aviation aluminum toilet)", "correct": False, "error": "- Bồn cầu Nhôm: Kỵ hóa chất, xịt tẩy bồn cầu là sùi bọt trắng."},
            {"text": "🍴 Tủ bếp bọc Bạc nguyên miếng (Solid silver-plated cabinets)", "correct": False, "error": "- Tủ bếp Bạc: Phản ứng muối mắm, xỉn đen thui cực kỳ bẩn."}
        ]
    }
]

# --- 3. QUẢN LÝ TRẠNG THÁI (State Management) ---
if 'completed_steps' not in st.session_state:
    st.session_state.completed_steps = []  # Lưu index các bước đã làm
if 'active_step' not in st.session_state:
    st.session_state.active_step = None    # Index của bước đang mở Tab
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

# --- 4. GIAO DIỆN CHÍNH (Chia cột) ---
st.markdown("<h1 style='text-align: center; font-size: 50px;'>🏡 BẬC THẦY KIẾN TRÚC 🏡</h1>", unsafe_allow_html=True)
st.write("")

col1, col2 = st.columns([4, 6], gap="large")

# CỘT 1: Hình ảnh ngôi nhà xuyên suốt
with col1:
    st.markdown("<div class='house-card'>", unsafe_allow_html=True)
    st.image("https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80", use_container_width=True)
    st.markdown("<h3 style='text-align:center; color:#3B82F6;'>Siêu Cò Biệt Thự</h3>", unsafe_allow_html=True)
    
    # Thanh tiến trình
    progress = len(st.session_state.completed_steps) / 8
    st.progress(progress)
    st.write(f"**Tiến độ thi công: {len(st.session_state.completed_steps)}/8 quy trình**")
    st.markdown("</div>", unsafe_allow_html=True)

# CỘT 2: Khu vực tương tác (Menu Quy trình HOẶC Tab Vật liệu)
with col2:
    # -----------------------------------------------------
    # KỊCH BẢN 1: TẤT CẢ ĐÃ XONG -> SHOW KẾT QUẢ
    # -----------------------------------------------------
    if len(st.session_state.completed_steps) == 8:
        st.markdown("<div class='dashboard-panel'>", unsafe_allow_html=True)
        st.markdown("## 🎯 BÀN GIAO CÔNG TRÌNH")
        st.markdown(f"### Tổng điểm: <span style='color: #EF4444; font-size: 45px;'>{st.session_state.score}/80</span>", unsafe_allow_html=True)
        
        if st.session_state.score == 80:
            st.success("🎉 TUYỆT VỜI! Một siêu phẩm kiến trúc hoàn hảo. Bạn là chuyên gia xây dựng đích thực!")
            st.balloons()
        elif st.session_state.score >= 50:
            st.warning("⚠️ Form nhà lên rất đẹp nhưng bên trong là 'bom nổ chậm'. Bạn phải chi bộn tiền để sửa lỗi rải rác!")
        else:
            st.error("🚨 THẢM HỌA KIẾN TRÚC! Ngôi nhà vi phạm nghiêm trọng kỹ thuật, nguy cơ sập đổ rất cao!")
        
        if st.session_state.issues:
            st.markdown("#### 🛠️ BÁO CÁO HẬU QUẢ VẬT LIỆU:")
            for issue in st.session_state.issues:
                st.markdown(f"<p style='color: #B91C1C; font-weight: bold;'>{issue}</p>", unsafe_allow_html=True)

        st.write("")
        if st.button("🔄 ĐẬP ĐI XÂY LẠI TỪ ĐẦU"):
            st.session_state.clear()
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

    # -----------------------------------------------------
    # KỊCH BẢN 2: ĐANG MỞ TAB CỬA SỔ CHỌN VẬT LIỆU
    # -----------------------------------------------------
    elif st.session_state.active_step is not None:
        idx = st.session_state.active_step
        current_data = game_data[idx]
        current_opts = st.session_state.shuffled_options[idx]
        
        st.markdown("<div class='material-tab'>", unsafe_allow_html=True)
        st.markdown(f"<h2 style='color: #2563EB;'>🛒 KHO VẬT LIỆU: {current_data['title']}</h2>", unsafe_allow_html=True)
        st.write(f"*{current_data['desc']}*")
        st.markdown("<hr>", unsafe_allow_html=True)
        
        option_texts = [opt["text"] for opt in current_opts]
        choice = st.radio("**Bạn muốn dùng vật liệu nào để thi công?**", option_texts, index=None)
        
        st.write("")
        col_btn1, col_btn2 = st.columns(2)
        with col_btn1:
            if st.button("✅ CHỐT VẬT LIỆU"):
                if choice:
                    # Kiểm tra đúng sai
                    selected_opt = next(item for item in current_opts if item["text"] == choice)
                    if selected_opt["correct"]:
                        st.session_state.score += 10
                    else:
                        st.session_state.issues.append(selected_opt["error"])
                    
                    # Đánh dấu hoàn thành và đóng tab
                    st.session_state.completed_steps.append(idx)
                    st.session_state.active_step = None
                    st.rerun()
                else:
                    st.error("⚠️ Vui lòng chọn 1 vật liệu!")
        
        with col_btn2:
            if st.button("🔙 QUAY LẠI BẢNG QUY TRÌNH"):
                st.session_state.active_step = None
                st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

    # -----------------------------------------------------
    # KỊCH BẢN 3: BẢNG LỰA CHỌN QUY TRÌNH (MENU CHÍNH)
    # -----------------------------------------------------
    else:
        st.markdown("<div class='dashboard-panel'>", unsafe_allow_html=True)
        st.markdown("### 📋 LỰA CHỌN QUY TRÌNH THI CÔNG")
        st.write("Hãy chọn bất kỳ quy trình nào bạn muốn thực hiện trước. Bạn phải hoàn thành đủ 8 quy trình để nghiệm thu nhà.")
        st.write("")
        
        # Tạo Grid 2 cột x 4 hàng cho các nút quy trình
        btn_cols = st.columns(2)
        for i, step_data in enumerate(game_data):
            c = btn_cols[i % 2]
            with c:
                if i in st.session_state.completed_steps:
                    # Nút đã làm xong sẽ đổi màu xanh và khóa lại
                    st.button(f"✅ ĐÃ XONG: {step_data['title']}", key=f"btn_{i}", disabled=True)
                else:
                    # Bấm vào nút sẽ kích hoạt Tab Chọn Vật liệu
                    if st.button(f"⚙️ {step_data['title']}", key=f"btn_{i}"):
                        st.session_state.active_step = i
                        st.rerun()
                        
        st.markdown("</div>", unsafe_allow_html=True)
