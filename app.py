import streamlit as st
import random

# --- 1. CẤU HÌNH GIAO DIỆN WIDE & CSS ---
st.set_page_config(page_title="Dream House Builder", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
    /* Nền gradient */
    .stApp {
        background: linear-gradient(135deg, #F0F4FF 0%, #D9E2EC 100%);
    }
    
    h1, h2, h3, h4 {
        color: #102A43;
        font-family: 'Segoe UI', sans-serif;
    }
    
    /* Khung ảnh Bản vẽ và Ngôi nhà */
    .image-card {
        background: rgba(255, 255, 255, 0.7);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 15px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.1);
        border: 2px solid white;
        margin-bottom: 20px;
        text-align: center;
    }
    
    /* Bảng điều khiển */
    .dashboard-panel {
        background: rgba(255, 255, 255, 0.9);
        border-radius: 20px;
        padding: 30px;
        box-shadow: 0 15px 35px rgba(0,0,0,0.1);
        border-top: 5px solid #2563EB;
    }

    /* TAB CỬA SỔ KHỔNG LỒ (FULL SCREEN MODAL) */
    .huge-modal {
        background: #ffffff;
        border-radius: 30px;
        padding: 60px;
        box-shadow: 0 0 50px rgba(37, 99, 235, 0.4);
        border: 4px solid #3B82F6;
        animation: zoomIn 0.4s;
        text-align: center;
        margin: 20px auto;
        max-width: 1200px;
    }
    
    @keyframes zoomIn {
        from { opacity: 0; transform: scale(0.9); }
        to { opacity: 1; transform: scale(1); }
    }
    
    /* Trang trí 2 bên viền màn hình */
    .decor-left { position: fixed; left: 15px; top: 15%; font-size: 55px; line-height: 2; z-index: 100; text-shadow: 2px 2px 5px rgba(0,0,0,0.2); }
    .decor-right { position: fixed; right: 15px; top: 15%; font-size: 55px; line-height: 2; z-index: 100; text-shadow: 2px 2px 5px rgba(0,0,0,0.2); }

    /* Nút bấm chung */
    .stButton>button {
        background: linear-gradient(90deg, #2563EB 0%, #4F46E5 100%);
        color: white;
        border-radius: 12px;
        font-weight: bold;
        font-size: 16px;
        padding: 15px 10px;
        border: none;
        box-shadow: 0 4px 10px rgba(0,0,0,0.1);
        transition: 0.3s;
        width: 100%;
    }
    .stButton>button:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 20px rgba(37, 99, 235, 0.4);
        color: white;
    }
    
    /* Style cho Radio button trong Cửa sổ to */
    .stRadio label {
        font-size: 24px !important;
        color: #102A43 !important;
        padding: 10px;
    }
    </style>
    
    <!-- Icon trang trí -->
    <div class="decor-left">🌸<br>🚗<br>🌺<br>🚙<br>🌷</div>
    <div class="decor-right">🌻<br>🏎️<br>🌼<br>🚕<br>🥀</div>
""", unsafe_allow_html=True)

# --- 2. DỮ LIỆU TRÒ CHƠI ---
# Không có số thứ tự ở title để phục vụ màn sắp xếp
game_data = [
    {
        "title": "Làm Móng (Foundation)",
        "desc": "Nền tảng vững chắc quyết định tuổi thọ của cả công trình.",
        "options": [
            {"text": "Bê tông cốt thép (Reinforced concrete)", "correct": True, "error": ""},
            {"text": "Hợp kim nhôm nguyên khối (Solid aluminum alloy)", "correct": False, "error": "- Móng Nhôm: Chịu nén kém, oxy hóa ngầm làm sập nhà."},
            {"text": "Đá Granite nguyên tảng (Solid Granite block)", "correct": False, "error": "- Móng Đá: Thiếu liên kết khối, gây lún nứt đôi nhà."}
        ]
    },
    {
        "title": "Đổ Khung Cột (Frame & Columns)",
        "desc": "Hệ xương sống chống chịu mọi bão tố và tải trọng.",
        "options": [
            {"text": "Thép vằn cường độ cao (High-strength ribbed steel)", "correct": True, "error": ""},
            {"text": "Thép trơn siêu dẻo (Super flexible smooth steel)", "correct": False, "error": "- Cột Thép dẻo: Không bám dính bê tông, rung lắc là gãy."},
            {"text": "Sắt non dập hộp rỗng (Hollow soft iron)", "correct": False, "error": "- Cột Sắt rỗng: Móp méo gãy gập ngay khi chịu tải mái nhà."}
        ]
    },
    {
        "title": "Xây Tường (Walls)",
        "desc": "Lớp áo giáp bảo vệ không gian sống khỏi thời tiết.",
        "options": [
            {"text": "Gạch đất nung / Gạch AAC (Fired brick / AAC block)", "correct": True, "error": ""},
            {"text": "Gạch xỉ than tái chế (Recycled cinder block)", "correct": False, "error": "- Tường Xỉ than: Hút nước như bọt biển, ngập ngụa khi mưa."},
            {"text": "Gạch lát nền Granite (Granite floor tiles)", "correct": False, "error": "- Tường Granite: Trơn tuột, vữa không bám, đẩy nhẹ là sập."}
        ]
    },
    {
        "title": "Làm Mái (Roof)",
        "desc": "Lá chắn che chở tổ ấm khỏi nắng mưa.",
        "options": [
            {"text": "Bê tông & Ngói tráng men (Concrete & glazed tiles)", "correct": True, "error": ""},
            {"text": "Mái nhôm đúc nguyên tấm (Cast aluminum roof)", "correct": False, "error": "- Mái Nhôm: Hấp thụ nhiệt siêu tốc, áp mái nóng như lò bát quái."},
            {"text": "Ngói xi măng ép màu (Color pressed cement tiles)", "correct": False, "error": "- Ngói ép: Phơi nắng 1 năm là nứt rạn, dột tong tỏng."}
        ]
    },
    {
        "title": "Điện Nước Âm (MEP System)",
        "desc": "Mạch máu ngầm cung cấp tiện nghi cho ngôi nhà.",
        "options": [
            {"text": "Dây đồng & Ống nhựa PPR (Copper wire & PPR pipe)", "correct": True, "error": ""},
            {"text": "Ống nước Inox mạ bạc (Silver-plated Inox pipe)", "correct": False, "error": "- Ống Inox ngầm: Trở thành bẫy giật điện chết người nếu rò điện."},
            {"text": "Dây điện lõi nhôm (Aluminum core wire)", "correct": False, "error": "- Dây Nhôm: Sinh nhiệt cao, chập cháy ngầm trong tường."}
        ]
    },
    {
        "title": "Trát Tường (Plastering)",
        "desc": "Làm phẳng và chuẩn bị bề mặt cho bước trang trí.",
        "options": [
            {"text": "Vữa xi măng trộn cát mịn (Cement & fine sand mortar)", "correct": True, "error": ""},
            {"text": "Keo Epoxy pha bột đá (Epoxy glue with stone powder)", "correct": False, "error": "- Trát Epoxy: Tường không thở được, mồ hôi ướt nhẹp khi nồm."},
            {"text": "Xi măng nguyên chất (Pure cement without sand)", "correct": False, "error": "- Xi măng nguyên chất: Co ngót cực mạnh, nứt toác chân chim."}
        ]
    },
    {
        "title": "Lát Gạch & Sơn (Tiling & Painting)",
        "desc": "Khoác lên ngôi nhà vẻ đẹp thẩm mỹ lộng lẫy.",
        "options": [
            {"text": "Keo dán gạch & Sơn chống thấm (Tile adhesive & Waterproof paint)", "correct": True, "error": ""},
            {"text": "Nước xi măng lỏng (Liquid cement slurry)", "correct": False, "error": "- Lát nước xi măng: Gạch phồng rộp, nổ vỡ lụp bụp."},
            {"text": "Sơn dầu bóng công nghiệp (Industrial glossy oil paint)", "correct": False, "error": "- Sơn dầu: Bong tróc, lột ra từng mảng như da rắn."}
        ]
    },
    {
        "title": "Nội Thất (Interior)",
        "desc": "Hoàn thiện không gian sống tiện nghi, sang trọng.",
        "options": [
            {"text": "Gỗ MDF chống ẩm & Sứ Nano (Moisture-resistant MDF & Nano porcelain)", "correct": True, "error": ""},
            {"text": "Bồn cầu đúc Nhôm hàng không (Aviation aluminum toilet)", "correct": False, "error": "- Bồn cầu Nhôm: Kỵ hóa chất, xịt tẩy bồn cầu là sùi bọt trắng."},
            {"text": "Tủ bếp bọc Bạc nguyên miếng (Solid silver-plated cabinets)", "correct": False, "error": "- Tủ bếp Bạc: Phản ứng muối mắm, xỉn đen thui cực kỳ bẩn."}
        ]
    }
]

# Danh sách chuẩn để so sánh
CORRECT_SEQUENCE = [step["title"] for step in game_data]

# --- 3. QUẢN LÝ TRẠNG THÁI ---
if 'phase' not in st.session_state:
    st.session_state.phase = 1 # 1: Xếp quy trình | 2: Chọn vật liệu | 3: Kết quả
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


# --- KỊCH BẢN MỞ TAB KHỔNG LỒ CHỌN VẬT LIỆU (Ẩn hết mọi thứ khác) ---
if st.session_state.active_material_step is not None:
    idx = st.session_state.active_material_step
    current_data = game_data[idx]
    current_opts = st.session_state.shuffled_options[idx]
    
    st.markdown("<div class='huge-modal'>", unsafe_allow_html=True)
    st.markdown(f"<h1 style='color: #2563EB; font-size: 50px;'>🛠️ CHỌN VẬT LIỆU:<br>{current_data['title']}</h1>", unsafe_allow_html=True)
    st.markdown(f"<h3 style='color: #64748B;'>*{current_data['desc']}*</h3>", unsafe_allow_html=True)
    st.write("---")
    
    option_texts = [opt["text"] for opt in current_opts]
    choice = st.radio("👉 **Vật liệu nào đạt chuẩn kỹ thuật? (Which material is correct?)**", option_texts, index=None)
    
    st.write("")
    st.write("")
    col_btn1, col_btn2, col_btn3 = st.columns([1, 2, 1])
    with col_btn2:
        if st.button("✅ XÁC NHẬN VẬT LIỆU (CONFIRM)"):
            if choice:
                selected_opt = next(item for item in current_opts if item["text"] == choice)
                if selected_opt["correct"]:
                    st.session_state.score += 10
                else:
                    st.session_state.issues.append(selected_opt["error"])
                
                st.session_state.completed_materials.append(idx)
                st.session_state.active_material_step = None
                
                # Check nếu đủ 8 bước -> Sang Phase 3
                if len(st.session_state.completed_materials) == 8:
                    st.session_state.phase = 3
                st.rerun()
            else:
                st.error("⚠️ Vui lòng chọn 1 đáp án! (Please select an option!)")
    st.markdown("</div>", unsafe_allow_html=True)

# --- GIAO DIỆN CHÍNH KHI KHÔNG MỞ TAB ---
else:
    st.markdown("<h1 style='text-align: center; font-size: 45px; margin-bottom: 30px;'>🏡 DREAM HOUSE BUILDER 🏡</h1>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([4, 6], gap="large")
    
    # CỘT 1: HÌNH ẢNH
    with col1:
        st.markdown("<div class='image-card'>", unsafe_allow_html=True)
        st.markdown("### 📐 Bản vẽ thiết kế (Blueprint)")
        st.image("https://images.unsplash.com/photo-1503387762-592deb58ef4e?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80", use_container_width=True)
        st.markdown("<hr style='margin: 10px 0;'>", unsafe_allow_html=True)
        st.markdown("### 🏠 Phối cảnh hoàn thiện (Final House)")
        st.image("https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80", use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    # CỘT 2: KHU VỰC CHƠI (Tùy Phase)
    with col2:
        # ==========================================
        # PHASE 1: SẮP XẾP QUY TRÌNH (SEQUENCE MATCHING)
        # ==========================================
        if st.session_state.phase == 1:
            st.markdown("<div class='dashboard-panel'>", unsafe_allow_html=True)
            st.markdown("## 🧩 BƯỚC 1: SẮP XẾP QUY TRÌNH XÂY DỰNG")
            st.write("Hãy chọn các quy trình theo đúng thứ tự từ lúc khởi công đến lúc hoàn thiện.")
            
            # Khung hiển thị quy trình người chơi đã xếp
            st.markdown("#### Thứ tự bạn đã chọn (Your Sequence):")
            if not st.session_state.user_sequence:
                st.info("Chưa chọn quy trình nào... (Empty)")
            else:
                for i, p in enumerate(st.session_state.user_sequence):
                    st.success(f"**{i+1}.** {p}")
                    
            # Nếu người chơi đã chọn đủ 8 bước -> Tiến hành kiểm tra
            if len(st.session_state.user_sequence) == 8:
                st.markdown("---")
                # Đếm số quy trình đúng vị trí
                correct_count = sum(1 for i in range(8) if st.session_state.user_sequence[i] == CORRECT_SEQUENCE[i])
                
                if correct_count == 8:
                    st.success("🎉 TUYỆT VỜI! ĐÚNG 8/8 QUY TRÌNH! (Perfect 8/8!)")
                    st.write("Bạn đã nắm rõ kỹ thuật thi công. Bây giờ hãy tiến hành chọn vật liệu.")
                    if st.button("🚀 BẮT ĐẦU CHỌN VẬT LIỆU XÂY NHÀ"):
                        st.session_state.phase = 2
                        st.rerun()
                else:
                    st.error(f"❌ Bạn đã xếp đúng {correct_count}/8 quy trình! (Correct {correct_count}/8)")
                    st.warning("Trình tự xây dựng sai sẽ gây hậu quả nghiêm trọng. Vui lòng xếp lại!")
                    if st.button("🔄 SẮP XẾP LẠI (TRY AGAIN)"):
                        st.session_state.user_sequence = []
                        st.rerun()
            
            # Bảng chọn các quy trình còn lại
            else:
                st.markdown("---")
                st.markdown("#### Các quy trình còn lại (Remaining steps):")
                remaining = [p for p in st.session_state.shuffled_processes if p not in st.session_state.user_sequence]
                
                cols = st.columns(2)
                for i, proc in enumerate(remaining):
                    with cols[i % 2]:
                        if st.button(proc, key=f"btn_p1_{proc}"):
                            st.session_state.user_sequence.append(proc)
                            st.rerun()
                            
                # Nút Reset nếu lỡ chọn sai giữa chừng
                st.write("")
                if len(st.session_state.user_sequence) > 0:
                    if st.button("⏪ Xóa chọn lại từ đầu (Clear all)"):
                        st.session_state.user_sequence = []
                        st.rerun()
            st.markdown("</div>", unsafe_allow_html=True)
            
        # ==========================================
        # PHASE 2: BẢNG LỰA CHỌN VẬT LIỆU
        # ==========================================
        elif st.session_state.phase == 2:
            st.markdown("<div class='dashboard-panel'>", unsafe_allow_html=True)
            st.markdown("## 🛒 BƯỚC 2: KHO VẬT LIỆU (MATERIALS)")
            st.write("Nhấp vào từng quy trình để mở Tab chọn vật liệu (Click to select materials).")
            st.write("")
            
            # Tạo Grid hiển thị 8 quy trình (theo thứ tự chuẩn)
            btn_cols = st.columns(2)
            for i, step_data in enumerate(game_data):
                with btn_cols[i % 2]:
                    if i in st.session_state.completed_materials:
                        st.button(f"✅ ĐÃ XONG: {step_data['title']}", key=f"btn_p2_{i}", disabled=True)
                    else:
                        # Bấm vào đây sẽ set active_material_step và kích hoạt Tab khổng lồ ở đầu code
                        if st.button(f"⚙️ {step_data['title']}", key=f"btn_p2_{i}"):
                            st.session_state.active_material_step = i
                            st.rerun()
                            
            st.markdown("</div>", unsafe_allow_html=True)

        # ==========================================
        # PHASE 3: KẾT QUẢ NGHIỆM THU
        # ==========================================
        elif st.session_state.phase == 3:
            st.markdown("<div class='dashboard-panel'>", unsafe_allow_html=True)
            st.markdown("## 🎯 BÀN GIAO CÔNG TRÌNH (FINAL RESULT)")
            st.markdown(f"### Điểm An toàn: <span style='color: #EF4444; font-size: 45px;'>{st.session_state.score}/80</span>", unsafe_allow_html=True)
            
            if st.session_state.score == 80:
                st.success("🎉 HOÀN HẢO! Một công trình vĩ đại vững chắc trăm năm! (Perfect Architecture!)")
                st.balloons()
            elif st.session_state.score >= 50:
                st.warning("⚠️ Form nhà lên rất đẹp nhưng bên trong là 'bom nổ chậm'. Bạn phải chi bộn tiền để sửa lỗi! (Many flaws inside!)")
            else:
                st.error("🚨 THẢM HỌA KIẾN TRÚC! Ngôi nhà vi phạm nghiêm trọng kỹ thuật, nguy cơ sập đổ rất cao! (Disaster!)")
            
            if st.session_state.issues:
                st.markdown("#### 🛠️ BÁO CÁO HẬU QUẢ SAI VẬT LIỆU (CONSTRUCTION ISSUES):")
                for issue in st.session_state.issues:
                    st.markdown(f"<p style='color: #B91C1C; font-weight: bold;'>{issue}</p>", unsafe_allow_html=True)

            st.write("")
            if st.button("🔄 ĐẬP ĐI XÂY LẠI TỪ ĐẦU (PLAY AGAIN)"):
                st.session_state.clear()
                st.rerun()
            st.markdown("</div>", unsafe_allow_html=True)
