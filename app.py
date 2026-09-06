import streamlit as st
import random
import os

# --- 1. CẤU HÌNH GIAO DIỆN HIỆN ĐẠI (TỐI GIẢN & CHUYÊN NGHIỆP) ---
st.set_page_config(page_title="Architecture Pro", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
    /* Nền màu xám nhạt hiện đại (Minimalist UI) */
    .stApp {
        background-color: #F8FAFC;
    }
    
    h1, h2, h3, h4 {
        color: #0F172A;
        font-family: 'Inter', 'Segoe UI', sans-serif;
        font-weight: 700;
    }
    
    /* Khung ảnh Bản vẽ và Ngôi nhà */
    .image-card {
        background: #FFFFFF;
        border-radius: 12px;
        padding: 20px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
        border: 1px solid #E2E8F0;
        text-align: center;
    }
    
    /* Bảng điều khiển (Dashboard) */
    .dashboard-panel {
        background: #FFFFFF;
        border-radius: 12px;
        padding: 30px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        border: 1px solid #E2E8F0;
        border-top: 4px solid #0F172A;
    }

    /* TAB CỬA SỔ KHỔNG LỒ (MODAL HIỆN ĐẠI) */
    .huge-modal {
        background: #FFFFFF;
        border-radius: 16px;
        padding: 60px;
        box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
        border: 1px solid #CBD5E1;
        animation: slideUp 0.3s ease-out;
        text-align: center;
        margin: 0 auto;
        max-width: 1000px;
    }
    
    @keyframes slideUp {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }

    /* Tùy chỉnh nút bấm hiện đại */
    .stButton>button {
        background-color: #0F172A;
        color: #FFFFFF;
        border-radius: 8px;
        font-weight: 600;
        font-size: 15px;
        padding: 12px 10px;
        border: 1px solid #0F172A;
        transition: all 0.2s;
        width: 100%;
    }
    .stButton>button:hover {
        background-color: #334155;
        border-color: #334155;
        color: #FFFFFF;
    }
    
    /* Nút đang khóa (Disabled) */
    button[disabled] {
        background-color: #F1F5F9 !important;
        color: #94A3B8 !important;
        border: 1px solid #E2E8F0 !important;
    }
    
    /* Style cho Radio button */
    .stRadio label {
        font-size: 20px !important;
        color: #1E293B !important;
        padding: 12px;
    }
    </style>
""", unsafe_allow_html=True)

# --- 2. DỮ LIỆU TRÒ CHƠI (Đã chuẩn hóa, bỏ icon thừa) ---
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

# =========================================================================
# KỊCH BẢN MỞ TAB KHỔNG LỒ CHỌN VẬT LIỆU (CHIẾM TOÀN MÀN HÌNH)
# =========================================================================
if st.session_state.active_material_step is not None:
    idx = st.session_state.active_material_step
    current_data = game_data[idx]
    current_opts = st.session_state.shuffled_options[idx]
    
    st.markdown("<div class='huge-modal'>", unsafe_allow_html=True)
    st.markdown(f"<h1 style='color: #0F172A; font-size: 40px;'>LỰA CHỌN VẬT LIỆU<br><span style='color: #2563EB;'>{current_data['title']}</span></h1>", unsafe_allow_html=True)
    st.markdown(f"<h3 style='color: #64748B; font-weight: 400;'>{current_data['desc']}</h3>", unsafe_allow_html=True)
    st.write("---")
    
    option_texts = [opt["text"] for opt in current_opts]
    choice = st.radio("**Vật liệu nào đạt chuẩn kỹ thuật thi công? (Select correct material)**", option_texts, index=None)
    
    st.write("")
    st.write("")
    col_btn1, col_btn2, col_btn3 = st.columns([1, 2, 1])
    with col_btn2:
        if st.button("XÁC NHẬN (CONFIRM)"):
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
                st.error("⚠️ Vui lòng chọn 1 đáp án! (Please select an option!)")
    st.markdown("</div>", unsafe_allow_html=True)

# =========================================================================
# GIAO DIỆN CHÍNH (KHI KHÔNG MỞ TAB)
# =========================================================================
else:
    st.markdown("<h1 style='text-align: center; font-size: 36px; margin-bottom: 40px; text-transform: uppercase; letter-spacing: 2px;'>Architecture Pro Simulator</h1>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([4, 6], gap="large")
    
    # --- CỘT 1: HÌNH ẢNH (Logic thay đổi theo Phase) ---
    with col1:
        st.markdown("<div class='image-card'>", unsafe_allow_html=True)
        
        if st.session_state.phase in [1, 2]:
            # Đang trong quy trình xếp kỹ thuật hoặc chọn vật liệu -> Chỉ hiện bản vẽ
            st.markdown("<h3 style='color: #334155; margin-bottom: 15px;'>Bản vẽ kỹ thuật (Blueprint)</h3>", unsafe_allow_html=True)
            # Ưu tiên load file local của bạn, nếu không có sẽ dùng ảnh mạng phác thảo thay thế để không bị văng lỗi
            try:
                st.image("image_b6d7a4.png", use_container_width=True)
            except:
                st.image("https://images.unsplash.com/photo-1503387762-592deb58ef4e?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80", use_container_width=True)
        
        elif st.session_state.phase == 3:
            # Xây xong toàn bộ -> Hiện nhà thật có màu sắc
            st.markdown("<h3 style='color: #10B981; margin-bottom: 15px;'>Phối cảnh hoàn thiện (Final Result)</h3>", unsafe_allow_html=True)
            st.image("https://images.unsplash.com/photo-1512917774080-9991f1c4c750?ixlib=rb-4.0.3&auto=format&fit=crop&w=1000&q=80", use_container_width=True)
            
        st.markdown("</div>", unsafe_allow_html=True)

    # --- CỘT 2: KHU VỰC TƯƠNG TÁC ---
    with col2:
        # -----------------------------------------------------
        # PHASE 1: SẮP XẾP QUY TRÌNH (SEQUENCE MATCHING)
        # -----------------------------------------------------
        if st.session_state.phase == 1:
            st.markdown("<div class='dashboard-panel'>", unsafe_allow_html=True)
            st.markdown("## BƯỚC 1: QUY TRÌNH THI CÔNG")
            st.write("Sắp xếp các bước xây dựng theo trình tự chuẩn xác.")
            
            # Khung hiển thị quy trình người chơi đã xếp
            st.markdown("#### Trình tự của bạn (Your Sequence):")
            if not st.session_state.user_sequence:
                st.info("Chưa có dữ liệu...")
            else:
                for i, p in enumerate(st.session_state.user_sequence):
                    st.markdown(f"<div style='padding: 10px; background: #F1F5F9; border-left: 4px solid #3B82F6; margin-bottom: 8px; border-radius: 4px;'><b>Bước {i+1}:</b> {p}</div>", unsafe_allow_html=True)
                    
            if len(st.session_state.user_sequence) == 8:
                st.markdown("---")
                correct_count = sum(1 for i in range(8) if st.session_state.user_sequence[i] == CORRECT_SEQUENCE[i])
                
                if correct_count == 8:
                    st.success("✅ CHUẨN XÁC 8/8 QUY TRÌNH! (Perfect Sequence!)")
                    st.write("Đã duyệt bản vẽ kỹ thuật. Chuyển sang giai đoạn xuất kho vật tư.")
                    if st.button("TIẾN HÀNH CHỌN VẬT LIỆU ->"):
                        st.session_state.phase = 2
                        st.rerun()
                else:
                    st.error(f"❌ Bạn đã xếp đúng {correct_count}/8 quy trình! (Correct {correct_count}/8)")
                    st.warning("Trình tự sai kỹ thuật. Vui lòng sắp xếp lại!")
                    if st.button("SẮP XẾP LẠI (RESET)"):
                        st.session_state.user_sequence = []
                        st.rerun()
            else:
                st.markdown("---")
                st.markdown("#### Các hạng mục chờ xử lý:")
                remaining = [p for p in st.session_state.shuffled_processes if p not in st.session_state.user_sequence]
                
                cols = st.columns(2)
                for i, proc in enumerate(remaining):
                    with cols[i % 2]:
                        if st.button(proc, key=f"btn_p1_{proc}"):
                            st.session_state.user_sequence.append(proc)
                            st.rerun()
                            
                st.write("")
                if len(st.session_state.user_sequence) > 0:
                    if st.button("Xóa làm lại (Clear)"):
                        st.session_state.user_sequence = []
                        st.rerun()
            st.markdown("</div>", unsafe_allow_html=True)
            
        # -----------------------------------------------------
        # PHASE 2: BẢNG LỰA CHỌN VẬT LIỆU
        # -----------------------------------------------------
        elif st.session_state.phase == 2:
            st.markdown("<div class='dashboard-panel'>", unsafe_allow_html=True)
            st.markdown("## BƯỚC 2: QUẢN LÝ VẬT TƯ (MATERIALS)")
            st.write("Mở từng hạng mục để phê duyệt vật liệu thi công.")
            st.write("")
            
            btn_cols = st.columns(2)
            for i, step_data in enumerate(game_data):
                with btn_cols[i % 2]:
                    if i in st.session_state.completed_materials:
                        st.button(f"Đã duyệt: {step_data['title']}", key=f"btn_p2_{i}", disabled=True)
                    else:
                        if st.button(f"Xử lý: {step_data['title']}", key=f"btn_p2_{i}"):
                            st.session_state.active_material_step = i
                            st.rerun()
                            
            st.markdown("</div>", unsafe_allow_html=True)

        # -----------------------------------------------------
        # PHASE 3: KẾT QUẢ NGHIỆM THU
        # -----------------------------------------------------
        elif st.session_state.phase == 3:
            st.markdown("<div class='dashboard-panel'>", unsafe_allow_html=True)
            st.markdown("## HỒ SƠ BÀN GIAO (FINAL REPORT)")
            st.markdown(f"### Đánh giá chất lượng: <span style='color: #2563EB;'>{st.session_state.score}/80 Điểm</span>", unsafe_allow_html=True)
            
            if st.session_state.score == 80:
                st.success("✅ ĐẠT CHUẨN QUỐC TẾ. Công trình hoàn hảo không tì vết. (Perfect Architecture!)")
            elif st.session_state.score >= 50:
                st.warning("⚠️ ĐẠT YÊU CẦU CƠ BẢN. Kiến trúc bề ngoài ổn nhưng ẩn chứa nhiều rủi ro vật liệu. (Many flaws inside!)")
            else:
                st.error("🚨 KHÔNG ĐẠT. Vi phạm nghiêm trọng an toàn kỹ thuật. Yêu cầu tháo dỡ! (Disaster!)")
            
            if st.session_state.issues:
                st.markdown("#### BÁO CÁO SỰ CỐ VẬT LIỆU (INCIDENT LOGS):")
                for issue in st.session_state.issues:
                    st.markdown(f"<p style='color: #DC2626; padding-left: 10px; border-left: 3px solid #DC2626;'>{issue}</p>", unsafe_allow_html=True)

            st.write("")
            if st.button("BẮT ĐẦU DỰ ÁN MỚI (PLAY AGAIN)"):
                st.session_state.clear()
                st.rerun()
            st.markdown("</div>", unsafe_allow_html=True)
