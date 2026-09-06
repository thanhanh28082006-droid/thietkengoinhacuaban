import streamlit as st
import random

# --- 1. CẤU HÌNH GIAO DIỆN WIDE & CSS CAO CẤP ---
st.set_page_config(page_title="Design Your House", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
    /* Nền gradient rực rỡ và sang trọng */
    .stApp {
        background: linear-gradient(135deg, #e0c3fc 0%, #8ec5fc 100%);
    }
    
    /* Font và Tiêu đề */
    h1, h2, h3 {
        color: #1E3A8A;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        text-shadow: 1px 1px 2px rgba(255,255,255,0.8);
    }
    
    /* Khung chứa ảnh ngôi nhà bên trái */
    .house-card {
        background: rgba(255, 255, 255, 0.4);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 15px;
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.2);
        border: 1px solid rgba(255, 255, 255, 0.5);
    }
    
    /* Bảng điều khiển (Cửa sổ to) bên phải */
    .game-console {
        background: rgba(255, 255, 255, 0.85);
        border-radius: 25px;
        padding: 40px;
        box-shadow: 0 20px 40px rgba(0,0,0,0.1);
        border-top: 4px solid #3B82F6;
    }
    
    /* Hoa hòe và ô tô trang trí bay xung quanh (Cố định 2 bên viền) */
    .decor-left {
        position: fixed;
        left: 20px;
        top: 20%;
        font-size: 45px;
        line-height: 2;
        z-index: 100;
        text-shadow: 2px 2px 5px rgba(0,0,0,0.2);
    }
    .decor-right {
        position: fixed;
        right: 20px;
        top: 20%;
        font-size: 45px;
        line-height: 2;
        z-index: 100;
        text-shadow: 2px 2px 5px rgba(0,0,0,0.2);
    }

    /* Tùy chỉnh Nút bấm */
    .stButton>button {
        background: linear-gradient(90deg, #4F46E5 0%, #3B82F6 100%);
        color: white;
        border-radius: 50px;
        width: 100%;
        font-weight: 800;
        font-size: 18px;
        padding: 15px 0;
        border: none;
        box-shadow: 0 4px 15px rgba(59, 130, 246, 0.4);
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(59, 130, 246, 0.6);
        color: white;
    }
    
    /* Khung Radio box */
    .stRadio {
        background: #F8FAFC;
        padding: 20px;
        border-radius: 15px;
        border: 2px dashed #93C5FD;
    }
    </style>
    
    <!-- HTML chứa các icon bay xung quanh -->
    <div class="decor-left">🌸<br>🚗<br>🌺<br>🚙<br>🌷</div>
    <div class="decor-right">🌻<br>🏎️<br>🌼<br>🚕<br>🥀</div>
""", unsafe_allow_html=True)

# --- 2. DỮ LIỆU TRÒ CHƠI ---
game_data = [
    {
        "title": "Làm Móng (Foundation)",
        "desc": "Nền tảng vững chắc quyết định tuổi thọ của cả công trình.",
        "options": [
            {"text": "🏗️ Bê tông cốt thép (Reinforced concrete)", "correct": True, "error": ""},
            {"text": "🪙 Hợp kim nhôm nguyên khối (Solid aluminum alloy)", "correct": False, "error": "- Móng Nhôm: Chịu nén kém, bị oxy hóa làm lún sập nhà."},
            {"text": "🪨 Đá Granite nguyên tảng (Solid Granite block)", "correct": False, "error": "- Móng Đá Granite: Thiếu tính liên kết khối, gây lún nứt đôi nhà."}
        ]
    },
    {
        "title": "Đổ Khung Cột (Frame & Columns)",
        "desc": "Hệ xương sống chống chịu mọi bão tố và tải trọng.",
        "options": [
            {"text": "⛓️ Thép vằn cường độ cao (High-strength ribbed steel)", "correct": True, "error": ""},
            {"text": "〰️ Thép trơn siêu dẻo (Super flexible smooth steel)", "correct": False, "error": "- Cột Thép dẻo: Trơn nhẵn, bê tông không bám được, rung lắc là gãy cột."},
            {"text": "🔲 Sắt non dập hộp rỗng (Hollow soft iron)", "correct": False, "error": "- Cột Sắt rỗng: Quá yếu, móp méo ngay khi chịu tải trọng trần nhà."}
        ]
    },
    {
        "title": "Xây Tường (Walls)",
        "desc": "Lớp áo giáp bảo vệ không gian sống khỏi thời tiết.",
        "options": [
            {"text": "🧱 Gạch đất nung / Gạch AAC (Fired brick / AAC block)", "correct": True, "error": ""},
            {"text": "🌑 Gạch xỉ than tái chế (Recycled cinder block)", "correct": False, "error": "- Tường Xỉ than: Hút nước như bọt biển, mùa mưa nhà ngập ngụa nước."},
            {"text": "✨ Gạch lát nền Granite (Granite floor tiles)", "correct": False, "error": "- Tường Granite: Bề mặt kính trơn tuột, vữa không bám, đẩy nhẹ là sập."}
        ]
    },
    {
        "title": "Làm Mái (Roof)",
        "desc": "Lá chắn che chở tổ ấm khỏi nắng mưa.",
        "options": [
            {"text": "🏠 Bê tông & Ngói tráng men (Concrete & glazed tiles)", "correct": True, "error": ""},
            {"text": "🛸 Mái nhôm đúc nguyên tấm (Cast aluminum roof)", "correct": False, "error": "- Mái Nhôm: Dẫn nhiệt cực mạnh, biến tầng áp mái thành lò nướng thiêu đốt."},
            {"text": "🎨 Ngói xi măng ép màu (Color pressed cement tiles)", "correct": False, "error": "- Ngói ép rẻ tiền: Nứt rạn và bay sạch màu chỉ sau 1 năm, dột tong tỏng."}
        ]
    },
    {
        "title": "Đi Điện Nước âm (MEP System)",
        "desc": "Mạch máu ngầm cung cấp tiện nghi cho ngôi nhà.",
        "options": [
            {"text": "⚡ Dây đồng & Ống nhựa PPR (Copper wire & PPR pipe)", "correct": True, "error": ""},
            {"text": "🚿 Ống nước Inox mạ bạc (Silver-plated Inox pipe)", "correct": False, "error": "- Ống Inox: Dẫn điện, nếu hở điện ngầm sẽ biến bức tường thành bẫy giật điện."},
            {"text": "🔌 Dây điện lõi nhôm (Aluminum core wire)", "correct": False, "error": "- Dây Nhôm ngầm: Sinh nhiệt rất cao, gây chập cháy ngầm trong tường."}
        ]
    },
    {
        "title": "Trát Tường & Láng Nền (Plastering)",
        "desc": "Làm phẳng và chuẩn bị bề mặt cho bước trang trí.",
        "options": [
            {"text": "⏳ Vữa xi măng trộn cát mịn (Cement & fine sand mortar)", "correct": True, "error": ""},
            {"text": "🧪 Keo Epoxy pha bột đá (Epoxy glue with stone powder)", "correct": False, "error": "- Trát Epoxy: Quá kín khí, nhà không thở được, mồ hôi ướt nhẹp khi trời nồm."},
            {"text": "💨 Xi măng nguyên chất không cát (Pure cement without sand)", "correct": False, "error": "- Xi măng nguyên chất: Bị co ngót cực mạnh khi khô, nứt toác chân chim khắp nơi."}
        ]
    },
    {
        "title": "Lát Gạch & Sơn Bả (Tiling & Painting)",
        "desc": "Khoác lên ngôi nhà vẻ đẹp thẩm mỹ lộng lẫy.",
        "options": [
            {"text": "🛡️ Keo dán gạch & Sơn chống thấm (Tile adhesive & Waterproof paint)", "correct": True, "error": ""},
            {"text": "💧 Nước xi măng lỏng (Liquid cement slurry)", "correct": False, "error": "- Lát bằng nước xi măng: Gạch rỗng ruột, phồng rộp và nổ vỡ lụp bụp."},
            {"text": "🛢️ Sơn dầu bóng công nghiệp (Industrial glossy oil paint)", "correct": False, "error": "- Sơn dầu: Không bám trên bề mặt vữa xi măng, bong tróc lột ra như da rắn."}
        ]
    },
    {
        "title": "Nội Thất & Thiết Bị (Interior & Fixtures)",
        "desc": "Hoàn thiện không gian sống tiện nghi, sang trọng.",
        "options": [
            {"text": "🛋️ Gỗ MDF chống ẩm & Sứ Nano (Moisture-resistant MDF & Nano porcelain)", "correct": True, "error": ""},
            {"text": "✈️ Bồn cầu đúc Nhôm hàng không (Aviation aluminum toilet)", "correct": False, "error": "- Bồn cầu Nhôm: Kỵ hóa chất mạnh, xịt thuốc tẩy vào là sùi bọt trắng, xỉn màu."},
            {"text": "🍴 Tủ bếp bọc Bạc nguyên miếng (Solid silver-plated cabinets)", "correct": False, "error": "- Tủ bếp Bạc: Phản ứng hóa học với muối mắm, xỉn đen thui chỉ sau 1 tháng."}
        ]
    }
]

# --- 3. QUẢN LÝ TRẠNG THÁI (Đã sửa lỗi AttributeError) ---
# Tách riêng biệt từng biến để tránh lỗi khi reload app trên Streamlit Cloud
if 'step' not in st.session_state:
    st.session_state.step = 0
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'issues' not in st.session_state:
    st.session_state.issues = []
if 'is_selecting_material' not in st.session_state:
    st.session_state.is_selecting_material = False
if 'shuffled_options' not in st.session_state:
    st.session_state.shuffled_options = []
    for step in game_data:
        opts = step["options"].copy()
        random.shuffle(opts)
        st.session_state.shuffled_options.append(opts)

# --- 4. GIAO DIỆN CHIA CỘT ---
st.markdown("<h1 style='text-align: center; margin-bottom: 30px; font-size: 45px;'>✨ DREAM HOUSE BUILDER ✨</h1>", unsafe_allow_html=True)

col1, col2 = st.columns([4, 6], gap="large")

# Cột 1: Hiển thị nhà
with col1:
    st.markdown("<div class='house-card'>", unsafe_allow_html=True)
    st.image("https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80", use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

# Cột 2: Bảng điều khiển Quy trình & Vật liệu
with col2:
    st.markdown("<div class='game-console'>", unsafe_allow_html=True)
    
    # KHI TRÒ CHƠI ĐANG DIỄN RA
    if st.session_state.step < len(game_data):
        current_idx = st.session_state.step
        current_data = game_data[current_idx]
        
        # Trạng thái 1: Yêu cầu chọn Quy trình thi công trước
        if not st.session_state.is_selecting_material:
            st.markdown("### 📋 BẢNG TIẾN ĐỘ DỰ ÁN")
            st.info(f"**Giai đoạn hiện tại (Step {current_idx + 1}/8):**")
            st.markdown(f"<h2 style='color: #4F46E5;'>📌 {current_data['title']}</h2>", unsafe_allow_html=True)
            st.write(f"*{current_data['desc']}*")
            
            st.write("")
            st.write("")
            if st.button(f"⚙️ MỞ KHO VẬT LIỆU CHO: {current_data['title'].upper()}"):
                st.session_state.is_selecting_material = True
                st.rerun()
                
        # Trạng thái 2: Mở cửa sổ to chọn vật liệu
        else:
            st.markdown(f"### 🛒 KHO VẬT LIỆU: {current_data['title']}")
            st.warning("Hãy lựa chọn vật liệu cẩn thận, sai lầm sẽ phải trả giá đắt!")
            
            current_opts = st.session_state.shuffled_options[current_idx]
            option_texts = [opt["text"] for opt in current_opts]
            
            choice = st.radio("Vật liệu khả dụng (Available materials):", option_texts, index=None)
            
            st.write("")
            if st.button("✅ XUẤT KHO & TIẾN HÀNH THI CÔNG"):
                if choice:
                    selected_opt = next(item for item in current_opts if item["text"] == choice)
                    if selected_opt["correct"]:
                        st.session_state.score += 10
                    else:
                        st.session_state.issues.append(selected_opt["error"])
                    
                    # Cập nhật state để sang quy trình tiếp theo
                    st.session_state.step += 1
                    st.session_state.is_selecting_material = False
                    st.rerun()
                else:
                    st.error("⚠️ Chủ thầu ơi, hãy chọn 1 vật liệu trước khi thi công!")

    # KHI TRÒ CHƠI KẾT THÚC
    else:
        st.markdown("## 🎯 NGHIỆM THU CÔNG TRÌNH")
        st.markdown(f"### Điểm chất lượng: <span style='color: #EF4444; font-size: 40px;'>{st.session_state.score}/80</span>", unsafe_allow_html=True)
        
        if st.session_state.score == 80:
            st.success("🎉 TUYỆT VỜI! Một siêu phẩm kiến trúc hoàn hảo. Đội thầu rất nể phục tư duy của bạn!")
            st.balloons() # Thêm bóng bay chúc mừng của Streamlit
        elif st.session_state.score >= 50:
            st.warning("⚠️ Nhà đã xây xong, form dáng đẹp nhưng bên trong chứa nhiều 'bom nổ chậm'. Xem báo cáo lỗi bên dưới!")
        else:
            st.error("🚨 THẢM HỌA! Ngôi nhà của bạn đã vi phạm nghiêm trọng luật xây dựng. Nguy cơ sập đổ rất cao!")
        
        if len(st.session_state.issues) > 0:
            st.markdown("<hr>", unsafe_allow_html=True)
            st.markdown("#### 🛠️ BÁO CÁO HƯ HỎNG (Cần sửa chữa gấp):")
            for issue in st.session_state.issues:
                st.markdown(f"<p style='color: #B91C1C; font-weight: bold;'>{issue}</p>", unsafe_allow_html=True)

        st.write("")
        if st.button("🔄 PHÁ DỠ VÀ XÂY LẠI TỪ ĐẦU"):
            st.session_state.step = 0
            st.session_state.score = 0
            st.session_state.issues = []
            st.session_state.is_selecting_material = False
            # Trộn lại đáp án cho lần chơi mới
            st.session_state.shuffled_options = []
            for step in game_data:
                opts = step["options"].copy()
                random.shuffle(opts)
                st.session_state.shuffled_options.append(opts)
            st.rerun()
            
    st.markdown("</div>", unsafe_allow_html=True)
