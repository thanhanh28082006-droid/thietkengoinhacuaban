import streamlit as st
import random

# --- 1. CẤU HÌNH GIAO DIỆN (Trắng - Xanh dương nhạt) ---
st.set_page_config(page_title="Thiết kế nhà của bạn | Design Your House", layout="centered")

st.markdown("""
    <style>
    /* Màu nền xanh dương siêu nhạt, chữ xanh đậm */
    .stApp {
        background-color: #F4F9FF;
    }
    h1, h2, h3 {
        color: #1E3A8A; 
        text-align: center;
    }
    p, label {
        color: #334155 !important;
        font-size: 18px !important;
    }
    /* Chỉnh nút bấm màu xanh dương */
    .stButton>button {
        background-color: #3B82F6;
        color: white;
        border-radius: 8px;
        width: 100%;
        font-weight: bold;
        border: none;
    }
    .stButton>button:hover {
        background-color: #2563EB;
        color: white;
    }
    /* Khung kết quả */
    .result-box {
        background-color: #DBEAFE;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #1D4ED8;
        margin-top: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# --- 2. DỮ LIỆU TRÒ CHƠI (8 BƯỚC) ---
game_data = [
    {
        "title": "Step 1: Foundation (Làm móng)",
        "desc": "Choose the core material for your house foundation. (Chọn vật liệu cốt lõi làm móng nhà)",
        "options": [
            {"text": "Bê tông cốt thép (Reinforced concrete)", "correct": True, "error": ""},
            {"text": "Hợp kim nhôm nguyên khối (Solid aluminum alloy)", "correct": False, "error": "- Móng Nhôm: Chịu nén kém, bị oxy hóa làm sập nhà (Aluminum is crushed and oxidized, causing collapse)."},
            {"text": "Đá Granite nguyên tảng (Solid Granite block)", "correct": False, "error": "- Móng Đá Granite: Thiếu tính liên kết khối, gây lún nứt đôi nhà (Lack of cohesion causes uneven cracking)."}
        ]
    },
    {
        "title": "Step 2: Frame & Columns (Đổ Khung Cột)",
        "desc": "Build the skeleton of the house. (Dựng bộ xương sống cho ngôi nhà)",
        "options": [
            {"text": "Thép vằn cường độ cao (High-strength ribbed steel)", "correct": True, "error": ""},
            {"text": "Thép trơn siêu dẻo (Super flexible smooth steel)", "correct": False, "error": "- Cột Thép dẻo: Không bám dính bê tông, gió to là tuột gãy (Slippery steel failed to grip concrete, columns broke)."},
            {"text": "Sắt non dập hộp rỗng (Hollow soft iron)", "correct": False, "error": "- Cột Sắt rỗng: Yếu, móp méo ngay khi chịu tải trọng trần nhà (Hollow iron crushed under roof weight)."}
        ]
    },
    {
        "title": "Step 3: Walls (Xây Tường)",
        "desc": "Choose wall materials for protection. (Chọn gạch xây bao che ngôi nhà)",
        "options": [
            {"text": "Gạch đất nung / Gạch AAC (Fired brick / AAC block)", "correct": True, "error": ""},
            {"text": "Gạch xỉ than tái chế (Recycled cinder block)", "correct": False, "error": "- Tường Xỉ than: Hút nước như bọt biển, mưa là ngập ngụa (Absorbed rain like a sponge, heavily flooded inside)."},
            {"text": "Gạch lát nền Granite (Granite floor tiles)", "correct": False, "error": "- Tường Granite: Trơn tuột, vữa không bám, đẩy nhẹ là đổ tường (Slippery tiles couldn't hold mortar, wall collapsed)."}
        ]
    },
    {
        "title": "Step 4: Roof (Làm Mái)",
        "desc": "Cover the top to protect from weather. (Làm mái che nắng mưa)",
        "options": [
            {"text": "Bê tông & Ngói tráng men (Concrete & glazed tiles)", "correct": True, "error": ""},
            {"text": "Mái nhôm đúc nguyên tấm (Cast aluminum roof)", "correct": False, "error": "- Mái Nhôm: Dẫn nhiệt quá mạnh, tầng áp mái nóng như lò nướng (Aluminum baked the attic like an oven)."},
            {"text": "Ngói xi măng ép màu (Color pressed cement tiles)", "correct": False, "error": "- Mái Ngói ép rẻ tiền: Nứt rạn và bay màu, dột nát sau 1 năm (Faded and cracked, leaking rain everywhere)."}
        ]
    },
    {
        "title": "Step 5: MEP System (Đi Điện Nước âm)",
        "desc": "Install plumbing and wiring. (Lắp hệ thống điện nước ngầm)",
        "options": [
            {"text": "Dây đồng & Ống nhựa PPR (Copper wire & PPR pipe)", "correct": True, "error": ""},
            {"text": "Ống nước Inox mạ bạc (Silver-plated Inox pipe)", "correct": False, "error": "- Ống Inox ngầm: Dẫn điện, rò điện ra tường gây giật nguy hiểm (Inox pipes conducted leaked electricity, shocking walls)."},
            {"text": "Dây điện lõi nhôm (Aluminum core wire)", "correct": False, "error": "- Dây Nhôm ngầm: Sinh nhiệt cao, gây chập cháy ngầm trong tường (Aluminum wires overheated, causing internal wall fires)."}
        ]
    },
    {
        "title": "Step 6: Plastering (Trát Tường & Láng Nền)",
        "desc": "Smooth out the surfaces. (Làm phẳng bề mặt tường, sàn)",
        "options": [
            {"text": "Vữa xi măng trộn cát mịn (Cement & fine sand mortar)", "correct": True, "error": ""},
            {"text": "Keo Epoxy pha bột đá (Epoxy glue with stone powder)", "correct": False, "error": "- Trát tường Epoxy: Quá kín khí, nhà đổ mồ hôi ướt nhẹp khi nồm (Walls couldn't breathe, extremely sweaty in high humidity)."},
            {"text": "Xi măng nguyên chất không cát (Pure cement without sand)", "correct": False, "error": "- Trát Xi măng nguyên chất: Bị co ngót mạnh, nứt toác chân chim khắp nhà (Pure cement shrank, cracking everywhere)."}
        ]
    },
    {
        "title": "Step 7: Tiling & Painting (Lát Gạch & Sơn Bả)",
        "desc": "Apply tiles and paint finishes. (Lát nền và sơn màu hoàn thiện)",
        "options": [
            {"text": "Keo dán gạch & Sơn chống thấm (Tile adhesive & Waterproof paint)", "correct": True, "error": ""},
            {"text": "Nước xi măng lỏng (Liquid cement slurry)", "correct": False, "error": "- Lát nền nước xi măng: Gạch rỗng ruột, phồng rộp nổ lụp bụp (Poor adhesion caused tiles to hollow out and pop up)."},
            {"text": "Sơn dầu bóng công nghiệp (Industrial glossy oil paint)", "correct": False, "error": "- Sơn dầu: Không bám trên vữa, bong tróc lột ra như da rắn (Oil paint peeled off the walls like snake skin)."}
        ]
    },
    {
        "title": "Step 8: Interior & Fixtures (Nội Thất & Thiết Bị)",
        "desc": "Install furniture and sanitary ware. (Lắp tủ, giường, bồn cầu...)",
        "options": [
            {"text": "Gỗ MDF chống ẩm & Sứ Nano (Moisture-resistant MDF & Nano porcelain)", "correct": True, "error": ""},
            {"text": "Bồn cầu đúc Nhôm hàng không (Aviation aluminum toilet)", "correct": False, "error": "- Bồn cầu Nhôm: Kỵ hóa chất, xịt thuốc tẩy vào là sùi bọt hư hỏng (Aluminum toilet corroded instantly from cleaning chemicals)."},
            {"text": "Tủ bếp bọc Bạc nguyên miếng (Solid silver-plated cabinets)", "correct": False, "error": "- Tủ bếp Bạc: Bị xỉn màu đen thui do phản ứng hóa học với mắm muối (Silver cabinets turned black from salt/cooking reactions)."}
        ]
    }
]

# --- 3. QUẢN LÝ TRẠNG THÁI (Session State) ---
if 'step' not in st.session_state:
    st.session_state.step = 0
    st.session_state.score = 0
    st.session_state.issues = []
    
    # Tạo danh sách các options đã xáo trộn cho mỗi bước để tránh bị reset khi click
    st.session_state.shuffled_options = []
    for step in game_data:
        opts = step["options"].copy()
        random.shuffle(opts)
        st.session_state.shuffled_options.append(opts)

# --- 4. GIAO DIỆN CHÍNH TRÒ CHƠI ---
st.title("🏡 THIẾT KẾ NHÀ CỦA BẠN")
st.subheader("(Design Your House)")

# Hình ảnh ngôi nhà hiện đại xuyên suốt
st.image("https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?ixlib=rb-4.0.3&auto=format&fit=crop&w=1000&q=80", use_column_width=True)

# Nếu trò chơi chưa kết thúc
if st.session_state.step < len(game_data):
    current_idx = st.session_state.step
    current_data = game_data[current_idx]
    current_opts = st.session_state.shuffled_options[current_idx]
    
    st.markdown(f"### {current_data['title']}")
    st.write(current_data['desc'])
    
    # Lấy text của các options đã xáo trộn
    option_texts = [opt["text"] for opt in current_opts]
    
    # Form lựa chọn
    choice = st.radio("Lựa chọn vật liệu (Select material):", option_texts, index=None)
    
    if st.button("Xác nhận & Chuyển bước (Confirm & Next)"):
        if choice:
            # Tìm đáp án người dùng chọn
            selected_opt = next(item for item in current_opts if item["text"] == choice)
            
            # Chấm điểm
            if selected_opt["correct"]:
                st.session_state.score += 10
            else:
                st.session_state.issues.append(selected_opt["error"])
            
            # Sang bước tiếp theo
            st.session_state.step += 1
            st.rerun()
        else:
            st.warning("Vui lòng chọn 1 vật liệu! (Please select a material!)")

# --- 5. MÀN HÌNH KẾT QUẢ KHI KẾT THÚC ---
else:
    st.markdown("---")
    st.header("🎯 KẾT QUẢ NGÔI NHÀ CỦA BẠN (YOUR HOUSE RESULT)")
    st.markdown(f"### Tổng điểm (Total Score): {st.session_state.score} / 80")
    
    # Nhận xét dựa trên điểm
    if st.session_state.score == 80:
        st.success("🎉 TUYỆT VỜI! Bạn là một kỹ sư thực thụ. Ngôi nhà bền vững và không có lỗi nào! (PERFECT! You are a true engineer. The house is flawless!)")
    elif st.session_state.score >= 50:
        st.warning("⚠️ Ngôi nhà đã hoàn thiện nhưng mắc một số sai lầm tai hại. Hãy xem danh sách sửa chữa bên dưới! (The house is built but has fatal flaws. See issues below!)")
    else:
        st.error("🚨 THẢM HỌA KIẾN TRÚC! Ngôi nhà của bạn có thể sập bất cứ lúc nào. (ARCHITECTURAL DISASTER! Your house might collapse soon.)")
    
    # In ra các lỗi nếu người chơi chọn sai
    if len(st.session_state.issues) > 0:
        st.markdown("<div class='result-box'>", unsafe_allow_html=True)
        st.markdown("#### 🛠️ Các vấn đề công trình đang gặp phải (Current construction issues):")
        for issue in st.session_state.issues:
            st.write(issue)
        st.markdown("</div>", unsafe_allow_html=True)

    # Nút chơi lại
    st.write("")
    if st.button("🔄 Chơi lại từ đầu (Play Again)"):
        st.session_state.clear()
        st.rerun()
