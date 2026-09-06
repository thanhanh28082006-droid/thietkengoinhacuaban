import streamlit as st
import random

# --- 1. CẤU HÌNH GIAO DIỆN ĐỎ HIỆN ĐẠI (NEON RED UI) ---
st.set_page_config(page_title="Architecture Pro", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
    /* Nền Gradient Đỏ Đen Sang Trọng */
    .stApp {
        background: linear-gradient(135deg, #1A0000 0%, #4A0000 50%, #B91327 100%);
    }
    
    h1.main-title {
        color: #FEF2F2 !important;
        font-family: 'Inter', 'Segoe UI', sans-serif;
        font-weight: 900;
        text-shadow: 0 0 15px rgba(255, 65, 108, 0.8);
    }
    
    h1, h2, h3, h4 {
        color: #1A0000;
        font-family: 'Inter', 'Segoe UI', sans-serif;
        font-weight: 800;
    }
    
    .image-card {
        background: rgba(255, 255, 255, 0.95);
        border-radius: 20px;
        padding: 25px;
        box-shadow: 0 0 25px rgba(255, 75, 43, 0.5);
        border: 2px solid #FF416C;
        text-align: center;
    }
    
    .dashboard-panel {
        background: rgba(255, 255, 255, 0.95);
        border-radius: 20px;
        padding: 35px;
        box-shadow: 0 0 25px rgba(255, 75, 43, 0.5);
        border: 1px solid #FFE4E6;
        border-top: 6px solid #FF416C;
    }

    .huge-modal {
        background: #FFFFFF;
        border-radius: 24px;
        padding: 60px;
        box-shadow: 0 0 60px rgba(255, 65, 108, 0.6);
        border: 3px solid #FF4B2B;
        animation: slideUp 0.4s ease-out;
        text-align: center;
        margin: 0 auto;
        max-width: 1000px;
    }
    
    @keyframes slideUp {
        from { opacity: 0; transform: translateY(30px); }
        to { opacity: 1; transform: translateY(0); }
    }

    .stButton>button {
        background: linear-gradient(90deg, #FF416C 0%, #FF4B2B 100%);
        color: #FFFFFF !important;
        border-radius: 10px;
        font-weight: 800;
        font-size: 14px;
        padding: 10px 5px;
        border: none;
        transition: all 0.3s;
        width: 100%;
        text-transform: uppercase;
        box-shadow: 0 4px 15px rgba(255, 75, 43, 0.4);
        margin-top: 5px;
    }
    .stButton>button:hover {
        background: linear-gradient(90deg, #FF4B2B 0%, #FF416C 100%);
        transform: translateY(-3px);
        box-shadow: 0 8px 25px rgba(255, 75, 43, 0.6);
    }
    
    button[disabled] {
        background: #F1F5F9 !important;
        color: #94A3B8 !important;
        box-shadow: none !important;
        transform: none !important;
    }
    
    .stRadio label {
        font-size: 22px !important;
        color: #4A0000 !important;
        padding: 12px;
        font-weight: 600;
    }
    
    .step-img-container {
        border-radius: 8px;
        overflow: hidden;
        border: 2px solid #FFE4E6;
        margin-bottom: 5px;
        background: white;
    }
    
    /* Thiết kế riêng cho các box quy trình đã chọn (Nằm ngang) */
    .selected-step-box {
        background: #FFF1F2;
        border: 2px solid #FF416C;
        border-radius: 8px;
        padding: 15px 10px;
        text-align: center;
        font-weight: bold;
        color: #B91327;
        margin-bottom: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        height: 80px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 14px;
    }
    </style>
""", unsafe_allow_html=True)

# --- 2. DỮ LIỆU TRÒ CHƠI CÓ ICON & HÌNH ẢNH TRỰC QUAN ---
game_data = [
    {
        "title": "🏗️ Làm Móng",
        "desc": "Nền tảng vững chắc quyết định tuổi thọ của cả công trình.",
        "img": "https://images.unsplash.com/photo-1541888087405-f3900fb3033f?ixlib=rb-4.0.3&auto=format&fit=crop&w=400&q=80",
        "options": [
            {"text": "Bê tông cốt thép (Reinforced concrete)", "correct": True, "error": ""},
            {"text": "Hợp kim nhôm nguyên khối (Solid aluminum)", "correct": False, "error": "- Móng Nhôm: Chịu nén kém, oxy hóa ngầm làm sập nhà."},
            {"text": "Đá Granite nguyên tảng (Solid Granite)", "correct": False, "error": "- Móng Đá: Thiếu liên kết khối, gây lún nứt đôi nhà."}
        ]
    },
    {
        "title": "⛓️ Đổ Khung Cột",
        "desc": "Hệ xương sống chống chịu mọi bão tố và tải trọng.",
        "img": "https://images.unsplash.com/photo-1504307651254-35680f356dfd?ixlib=rb-4.0.3&auto=format&fit=crop&w=400&q=80",
        "options": [
            {"text": "Thép vằn cường độ cao (High-strength steel)", "correct": True, "error": ""},
            {"text": "Thép trơn siêu dẻo (Flexible smooth steel)", "correct": False, "error": "- Cột Thép dẻo: Không bám dính bê tông, rung lắc là gãy."},
            {"text": "Sắt non dập hộp rỗng (Hollow soft iron)", "correct": False, "error": "- Cột Sắt rỗng: Móp méo gãy gập ngay khi chịu tải mái nhà."}
        ]
    },
    {
        "title": "🧱 Xây Tường",
        "desc": "Lớp áo giáp bảo vệ không gian sống khỏi thời tiết.",
        "img": "https://images.unsplash.com/photo-1589939705384-5185137a7f0f?ixlib=rb-4.0.3&auto=format&fit=crop&w=400&q=80",
        "options": [
            {"text": "Gạch đất nung / Gạch AAC (Fired brick / AAC)", "correct": True, "error": ""},
            {"text": "Gạch xỉ than tái chế (Recycled cinder block)", "correct": False, "error": "- Tường Xỉ than: Hút nước như bọt biển, ngập ngụa khi mưa."},
            {"text": "Gạch lát nền Granite (Granite floor tiles)", "correct": False, "error": "- Tường Granite: Trơn tuột, vữa không bám, đẩy nhẹ là sập."}
        ]
    },
    {
        "title": "🏠 Làm Mái",
        "desc": "Lá chắn che chở tổ ấm khỏi nắng mưa.",
        "img": "https://images.unsplash.com/photo-1632759145351-1d592919f522?ixlib=rb-4.0.3&auto=format&fit=crop&w=400&q=80",
        "options": [
            {"text": "Bê tông & Ngói tráng men (Concrete & glazed tiles)", "correct": True, "error": ""},
            {"text": "Mái nhôm đúc nguyên tấm (Cast aluminum roof)", "correct": False, "error": "- Mái Nhôm: Hấp thụ nhiệt siêu tốc, áp mái nóng như lò bát quái."},
            {"text": "Ngói xi măng ép màu (Color pressed cement)", "correct": False, "error": "- Ngói ép: Phơi nắng 1 năm là nứt rạn, dột tong tỏng."}
        ]
    },
    {
        "title": "⚡ Điện Nước Âm",
        "desc": "Mạch máu ngầm cung cấp tiện nghi cho ngôi nhà.",
        "img": "https://images.unsplash.com/photo-1621905252507-b35492cc74b4?ixlib=rb-4.0.3&auto=format&fit=crop&w=400&q=80",
        "options": [
            {"text": "Dây đồng & Ống nhựa PPR (Copper wire & PPR pipe)", "correct": True, "error": ""},
            {"text": "Ống nước Inox mạ bạc (Silver-plated Inox pipe)", "correct": False, "error": "- Ống Inox ngầm: Trở thành bẫy giật điện chết người nếu rò điện."},
            {"text": "Dây điện lõi nhôm (Aluminum core wire)", "correct": False, "error": "- Dây Nhôm: Sinh nhiệt cao, chập cháy ngầm trong tường."}
        ]
    },
    {
        "title": "⏳ Trát Tường",
        "desc": "Làm phẳng và chuẩn bị bề mặt cho bước trang trí.",
        "img": "https://images.unsplash.com/photo-1588854337221-4cf9fa968114?ixlib=rb-4.0.3&auto=format&fit=crop&w=400&q=80",
        "options": [
            {"text": "Vữa xi măng trộn cát mịn (Cement & fine sand)", "correct": True, "error": ""},
            {"text": "Keo Epoxy pha bột đá (Epoxy with stone powder)", "correct": False, "error": "- Trát Epoxy: Tường không thở được, mồ hôi ướt nhẹp khi nồm."},
            {"text": "Xi măng nguyên chất (Pure cement without sand)", "correct": False, "error": "- Xi măng nguyên chất: Co ngót cực mạnh, nứt toác chân chim."}
        ]
    },
    {
        "title": "🎨 Lát Gạch & Sơn",
        "desc": "Khoác lên ngôi nhà vẻ đẹp thẩm mỹ lộng lẫy.",
        "img": "https://images.unsplash.com/photo-1521193089946-b338fa7419f8?ixlib=rb-4.0.3&auto=format&fit=crop&w=400&q=80",
        "options": [
            {"text": "Keo dán gạch & Sơn chống thấm (Tile adhesive & paint)", "correct": True, "error": ""},
            {"text": "Nước xi măng lỏng (Liquid cement slurry)", "correct": False, "error": "- Lát nước xi măng: Gạch phồng rộp, nổ vỡ lụp bụp."},
            {"text": "Sơn dầu bóng công nghiệp (Industrial oil paint)", "correct": False, "error": "- Sơn dầu: Bong tróc, lột ra từng mảng như da rắn."}
        ]
    },
    {
        "title": "🛋️ Nội Thất",
        "desc": "Hoàn thiện không gian sống tiện nghi, sang trọng.",
        "img": "https://images.unsplash.com/photo-1586023492125-27b2c045efd7?ixlib=rb-4.0.3&auto=format&fit=crop&w=400&q=80",
        "options": [
            {"text": "Gỗ MDF chống ẩm & Sứ Nano (MDF & Nano porcelain)", "correct": True, "error": ""},
            {"text": "Bồn cầu đúc Nhôm hàng không (Aluminum toilet)", "correct": False, "error": "- Bồn cầu Nhôm: Kỵ hóa chất, xịt tẩy bồn cầu là sùi bọt trắng."},
            {"text": "Tủ bếp bọc Bạc nguyên miếng (Solid silver cabinets)", "correct": False, "error": "- Tủ bếp Bạc: Phản ứng muối mắm, xỉn đen thui cực kỳ bẩn."}
        ]
    }
]

CORRECT_SEQUENCE = [step["title"] for step in game_data]

def get_img_by_title(title):
    for item in game_data:
        if item["title"] == title:
            return item["img"]
    return None

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
    st.markdown(f"<h1 style='color: #4A0000; font-size: 45px;'>PHÊ DUYỆT VẬT LIỆU<br><span style='color: #FF416C;'>{current_data['title']}</span></h1>", unsafe_allow_html=True)
    st.markdown(f"<h3 style='color: #64748B; font-weight: 400;'>{current_data['desc']}</h3>", unsafe_allow_html=True)
    st.write("---")
    
    option_texts = [opt["text"] for opt in current_opts]
    choice = st.radio("**Vật liệu nào đạt tiêu chuẩn kỹ thuật thi công? (Select correct material)**", option_texts, index=None)
    
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
                st.error("⚠️ Vui lòng chọn 1 hạng mục! (Please select an option!)")
    st.markdown("</div>", unsafe_allow_html=True)

# =========================================================================
# GIAO DIỆN CHÍNH (KHI KHÔNG MỞ TAB)
# =========================================================================
else:
    st.markdown("<h1 class='main-title' style='text-align: center; font-size: 42px; margin-bottom: 40px; text-transform: uppercase; letter-spacing: 2px;'>Architecture Pro Simulator</h1>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([3, 7], gap="large")
    
    # --- CỘT 1: HÌNH ẢNH NHÀ HIỆN ĐẠI ---
    with col1:
        st.markdown("<div class='image-card'>", unsafe_allow_html=True)
        st.markdown("<h3 style='color: #FF416C; margin-bottom: 15px;'>Mẫu Nhà Hiện Đại</h3>", unsafe_allow_html=True)
        st.image("https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80", use_container_width=True, caption="Modern Villa")
        st.markdown("<br>", unsafe_allow_html=True)
        st.image("https://images.unsplash.com/photo-1613977257363-707ba9348227?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80", use_container_width=True, caption="Luxury Mansion")
        st.markdown("</div>", unsafe_allow_html=True)

    # --- CỘT 2: KHU VỰC TƯƠNG TÁC ---
    with col2:
        # -----------------------------------------------------
        # PHASE 1: SẮP XẾP QUY TRÌNH
        # -----------------------------------------------------
        if st.session_state.phase == 1:
            st.markdown("<div class='dashboard-panel'>", unsafe_allow_html=True)
            st.markdown("## BƯỚC 1: SẮP XẾP QUY TRÌNH")
            st.write("Nhấp vào các quy trình bên dưới để xếp vào bảng thi công theo đúng trình tự.")
            
            st.markdown("#### Bảng thi công của bạn (Your Sequence):")
            if not st.session_state.user_sequence:
                st.info("Chưa có dữ liệu. Vui lòng chọn từ lưới bên dưới...")
            else:
                # Trình bày các bước đã chọn dưới dạng lưới ngang 4 cột
                chosen_cols = st.columns(4)
                for i, p in enumerate(st.session_state.user_sequence):
                    with chosen_cols[i % 4]:
                        st.markdown(f"<div class='selected-step-box'>B. {i+1}<br>{p}</div>", unsafe_allow_html=True)
                    
            if len(st.session_state.user_sequence) == 8:
                st.markdown("---")
                correct_count = sum(1 for i in range(8) if st.session_state.user_sequence[i] == CORRECT_SEQUENCE[i])
                
                if correct_count == 8:
                    st.success("✅ CHUẨN XÁC 8/8 QUY TRÌNH! (Perfect Sequence!)")
                    if st.button("TIẾN HÀNH CHỌN VẬT LIỆU ->"):
                        st.session_state.phase = 2
                        st.rerun()
                else:
                    st.error(f"❌ Bạn đã xếp đúng {correct_count}/8 quy trình! (Correct {correct_count}/8)")
                    if st.button("SẮP XẾP LẠI (RESET)"):
                        st.session_state.user_sequence = []
                        st.rerun()
            else:
                st.markdown("---")
                st.markdown("#### Bảng chờ xử lý (Nhấp để chọn):")
                remaining = [p for p in st.session_state.shuffled_processes if p not in st.session_state.user_sequence]
                
                # CHIA LƯỚI 4 CỘT HIỂN THỊ HÌNH ẢNH HÀNG NGANG
                cols = st.columns(4)
                for i, proc in enumerate(remaining):
                    with cols[i % 4]:
                        st.markdown("<div class='step-img-container'>", unsafe_allow_html=True)
                        st.image(get_img_by_title(proc), use_container_width=True)
                        st.markdown("</div>", unsafe_allow_html=True)
                        
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
            st.write("Click vào hình ảnh/nút để duyệt vật liệu thi công.")
            st.write("")
            
            # CHIA LƯỚI 4 CỘT
            btn_cols = st.columns(4)
            for i, step_data in enumerate(game_data):
                with btn_cols[i % 4]:
                    st.markdown("<div class='step-img-container'>", unsafe_allow_html=True)
                    st.image(step_data['img'], use_container_width=True)
                    st.markdown("</div>", unsafe_allow_html=True)
                    
                    if i in st.session_state.completed_materials:
                        st.button(f"✅ Đã duyệt:\n{step_data['title']}", key=f"btn_p2_{i}", disabled=True)
                    else:
                        if st.button(f"⚙️ Xử lý:\n{step_data['title']}", key=f"btn_p2_{i}"):
                            st.session_state.active_material_step = i
                            st.rerun()
                            
            st.markdown("</div>", unsafe_allow_html=True)

        # -----------------------------------------------------
        # PHASE 3: KẾT QUẢ NGHIỆM THU
        # -----------------------------------------------------
        elif st.session_state.phase == 3:
            st.markdown("<div class='dashboard-panel'>", unsafe_allow_html=True)
            st.markdown("## HỒ SƠ BÀN GIAO (FINAL REPORT)")
            st.markdown(f"### Đánh giá chất lượng: <span style='color: #FF416C;'>{st.session_state.score}/80 Điểm</span>", unsafe_allow_html=True)
            
            if st.session_state.score == 80:
                st.success("✅ ĐẠT CHUẨN QUỐC TẾ. Công trình hoàn hảo không tì vết. (Perfect Architecture!)")
                st.balloons()
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
