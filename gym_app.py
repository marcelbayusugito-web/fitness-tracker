import streamlit as st

st.set_page_config(
    page_title="Fitness Tracker by Marcel Bayu Sugito",
    page_icon="💪",
    layout="centered"
)

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800;900&display=swap');
    * { font-family: 'Inter', sans-serif; }
    .stApp { background: linear-gradient(160deg, #f8f9ff 0%, #eef1ff 50%, #f0f7ff 100%); }
    .hero { background:linear-gradient(135deg,#1a1a2e 0%,#16213e 50%,#0f3460 100%); border-radius:24px; padding:2.5rem 2rem; text-align:center; margin-bottom:1.5rem; position:relative; overflow:hidden; box-shadow:0 20px 60px rgba(15,52,96,0.3); }
    .hero-deco  { position:absolute; font-size:8rem; opacity:0.06; top:-20px; left:-20px; transform:rotate(-15deg); }
    .hero-deco2 { position:absolute; font-size:6rem; opacity:0.06; bottom:-10px; right:-10px; transform:rotate(20deg); }
    .hero-icon  { font-size:3.5rem; margin-bottom:0.5rem; }
    .hero-title { font-size:2.8rem; font-weight:900; background:linear-gradient(90deg,#f7971e,#ffd200); -webkit-background-clip:text; -webkit-text-fill-color:transparent; margin:0; letter-spacing:-1px; }
    .hero-sub   { color:#8899bb; font-size:0.9rem; letter-spacing:3px; text-transform:uppercase; margin:0.4rem 0 1rem; }
    .credit-pill { display:inline-block; background:linear-gradient(90deg,#f7971e,#ffd200); color:#000; font-weight:800; font-size:0.72rem; padding:5px 18px; border-radius:20px; letter-spacing:1.5px; text-transform:uppercase; }
    .hero-stats { display:flex; justify-content:center; gap:2rem; margin-top:1.5rem; padding-top:1.5rem; border-top:1px solid rgba(255,255,255,0.08); }
    .hero-stat-val   { font-size:1.4rem; font-weight:800; color:#ffd200; }
    .hero-stat-label { font-size:0.7rem; color:#667; text-transform:uppercase; letter-spacing:1px; }
    .section-card  { background:white; border-radius:20px; padding:1.8rem; margin:1rem 0; box-shadow:0 4px 24px rgba(0,0,0,0.07); border:1px solid rgba(0,0,0,0.05); }
    .section-title { font-size:0.8rem; font-weight:800; color:#0f3460; text-transform:uppercase; letter-spacing:2px; margin-bottom:1.2rem; display:flex; align-items:center; gap:8px; }
    .section-title::after { content:''; flex:1; height:2px; background:linear-gradient(90deg,#f7971e33,transparent); border-radius:2px; }
    .metrics-grid { display:grid; grid-template-columns:repeat(3,1fr); gap:12px; margin:1rem 0; }
    .metric-card  { background:linear-gradient(135deg,#f8f9ff,#eef1ff); border:1px solid #e0e5ff; border-radius:16px; padding:1.2rem; text-align:center; position:relative; overflow:hidden; }
    .metric-card::before { content:attr(data-icon); position:absolute; font-size:4rem; opacity:0.07; top:-10px; right:-5px; }
    .metric-val  { font-size:2.2rem; font-weight:900; color:#0f3460; line-height:1; }
    .metric-unit { font-size:0.75rem; color:#f7971e; font-weight:700; }
    .metric-lbl  { font-size:0.7rem; color:#999; text-transform:uppercase; letter-spacing:1px; margin-top:4px; }
    .bmi-normal   { background:linear-gradient(135deg,#e8fff4,#d0ffe8); border:1.5px solid #00c864; border-radius:14px; padding:1rem 1.2rem; color:#007a3d; }
    .bmi-kurus    { background:linear-gradient(135deg,#e8f4ff,#d0e8ff); border:1.5px solid #0096ff; border-radius:14px; padding:1rem 1.2rem; color:#0055cc; }
    .bmi-gemuk    { background:linear-gradient(135deg,#fffbe8,#fff3d0); border:1.5px solid #ffc800; border-radius:14px; padding:1rem 1.2rem; color:#996600; }
    .bmi-obesitas { background:linear-gradient(135deg,#fff0f0,#ffd8d8); border:1.5px solid #ff3c3c; border-radius:14px; padding:1rem 1.2rem; color:#cc0000; }
    .bmi-title { font-size:1rem; font-weight:800; margin-bottom:4px; }
    .bmi-saran { font-size:0.85rem; opacity:0.85; }
    .kalori-grid { display:grid; grid-template-columns:1fr 1fr; gap:10px; margin-top:0.8rem; }
    .kalori-item { background:#f8f9ff; border:1px solid #e8ecff; border-radius:12px; padding:0.9rem 1rem; display:flex; justify-content:space-between; align-items:center; }
    .kalori-name { font-size:0.82rem; color:#555; }
    .kalori-val  { font-size:1rem; font-weight:800; color:#0f3460; }
    .plan-card { background:linear-gradient(135deg,#0f3460,#16213e); border-radius:18px; padding:1.5rem; color:white; margin-top:1rem; box-shadow:0 8px 32px rgba(15,52,96,0.25); position:relative; overflow:hidden; }
    .plan-card::before { content:'🏋️'; position:absolute; font-size:7rem; opacity:0.08; right:-10px; bottom:-15px; }
    .plan-badge { display:inline-block; background:linear-gradient(90deg,#f7971e,#ffd200); color:#000; font-size:0.7rem; font-weight:800; padding:3px 12px; border-radius:20px; letter-spacing:1px; margin-bottom:0.8rem; }
    .plan-item { display:flex; align-items:flex-start; gap:10px; margin:0.6rem 0; font-size:0.88rem; color:#ccd; }
    .plan-val  { color:#ffd200; font-weight:700; }
    .tips-grid { display:grid; grid-template-columns:repeat(3,1fr); gap:10px; margin-top:0.8rem; }
    .tip-item  { background:#f8f9ff; border:1px solid #e8ecff; border-radius:14px; padding:1rem; text-align:center; }
    .tip-icon  { font-size:1.8rem; margin-bottom:6px; }
    .tip-title { font-size:0.78rem; font-weight:700; color:#0f3460; }
    .tip-desc  { font-size:0.72rem; color:#888; margin-top:3px; line-height:1.4; }
    .motivasi-box  { background:linear-gradient(135deg,#f7971e,#ffd200); border-radius:18px; padding:1.5rem; text-align:center; margin-top:1rem; box-shadow:0 8px 24px rgba(247,151,30,0.3); }
    .motivasi-icon { font-size:2.5rem; margin-bottom:0.5rem; }
    .motivasi-text { font-size:1.1rem; font-weight:800; color:#000; margin:0; }
    .motivasi-sub  { font-size:0.82rem; color:#444; margin-top:4px; }

    /* JADWAL LATIHAN */
    .jadwal-header { background:linear-gradient(135deg,#0f3460,#16213e); border-radius:16px; padding:1.2rem 1.5rem; margin-bottom:1rem; display:flex; align-items:center; gap:12px; }
    .jadwal-header-icon { font-size:2rem; }
    .jadwal-header-title { color:#ffd200; font-size:1rem; font-weight:800; margin:0; }
    .jadwal-header-sub   { color:#8899bb; font-size:0.78rem; margin:2px 0 0; }
    .hari-card { border-radius:16px; padding:1.2rem; margin:8px 0; border:1.5px solid; }
    .hari-card.latihan  { background:linear-gradient(135deg,#f0f7ff,#e8f0ff); border-color:#c0d0ff; }
    .hari-card.istirahat{ background:linear-gradient(135deg,#f0fff4,#e8ffe8); border-color:#b0e8c0; }
    .hari-card.cardio   { background:linear-gradient(135deg,#fff8f0,#fff0e0); border-color:#ffd0a0; }
    .hari-title { font-size:0.85rem; font-weight:800; color:#0f3460; margin-bottom:8px; display:flex; align-items:center; gap:8px; }
    .hari-badge { font-size:0.65rem; font-weight:700; padding:2px 10px; border-radius:20px; }
    .badge-latihan   { background:#e0e8ff; color:#0f3460; }
    .badge-istirahat { background:#d0f0d8; color:#007a3d; }
    .badge-cardio    { background:#ffe8cc; color:#994400; }
    .exercise-list { list-style:none; padding:0; margin:0; }
    .exercise-item { display:flex; align-items:flex-start; gap:10px; padding:6px 0; border-bottom:1px solid rgba(0,0,0,0.05); font-size:0.83rem; color:#444; }
    .exercise-item:last-child { border-bottom:none; }
    .exercise-dot { width:6px; height:6px; border-radius:50%; background:#f7971e; margin-top:6px; flex-shrink:0; }
    .exercise-name { font-weight:700; color:#0f3460; }
    .exercise-detail { color:#888; font-size:0.78rem; margin-top:1px; }
    .minggu-tabs { display:grid; grid-template-columns:repeat(4,1fr); gap:8px; margin-bottom:1rem; }
    .minggu-tab { background:#f8f9ff; border:1.5px solid #e0e5ff; border-radius:12px; padding:0.6rem; text-align:center; cursor:pointer; }
    .minggu-tab.active { background:linear-gradient(135deg,#0f3460,#16213e); border-color:#0f3460; }
    .minggu-tab-label { font-size:0.7rem; text-transform:uppercase; letter-spacing:1px; }
    .minggu-tab.active .minggu-tab-label { color:#ffd200; }
    .minggu-tab-num { font-size:1.1rem; font-weight:800; color:#0f3460; }
    .minggu-tab.active .minggu-tab-num { color:white; }
    .progress-week { background:#f0f0f0; border-radius:8px; height:8px; margin:4px 0; overflow:hidden; }
    .progress-fill { height:100%; border-radius:8px; background:linear-gradient(90deg,#f7971e,#ffd200); }
    .suplemen-grid { display:grid; grid-template-columns:repeat(2,1fr); gap:10px; margin-top:0.8rem; }
    .suplemen-item { background:#f8f9ff; border:1px solid #e8ecff; border-radius:12px; padding:1rem; }
    .suplemen-name   { font-size:0.85rem; font-weight:700; color:#0f3460; }
    .suplemen-detail { font-size:0.75rem; color:#888; margin-top:3px; line-height:1.4; }
    .stButton > button { width:100%; background:linear-gradient(90deg,#f7971e,#ffd200) !important; color:#000 !important; font-weight:800 !important; font-size:0.95rem !important; border:none !important; border-radius:14px !important; padding:0.8rem !important; letter-spacing:1px; box-shadow:0 4px 16px rgba(247,151,30,0.35) !important; }
    .stTextInput input, .stNumberInput input { border-radius:12px !important; border:1.5px solid #e0e5ff !important; background:#f8f9ff !important; }
    label { color:#444 !important; font-weight:600 !important; font-size:0.85rem !important; }
    .footer { text-align:center; padding:2rem 0 1rem; color:#aaa; font-size:0.78rem; }
    .footer strong { color:#f7971e; }
</style>
""", unsafe_allow_html=True)

# ============================================
# HERO
# ============================================
st.markdown("""
<div class="hero">
    <div class="hero-deco">🏋️</div>
    <div class="hero-deco2">💪</div>
    <div class="hero-icon">🏆</div>
    <p class="hero-title">FITNESS TRACKER</p>
    <p class="hero-sub">Body Analysis & Training Planner</p>
    <span class="credit-pill">✦ by Marcel Bayu Sugito ✦</span>
    <div class="hero-stats">
        <div class="hero-stat"><div class="hero-stat-val">BMI</div><div class="hero-stat-label">Body Mass Index</div></div>
        <div class="hero-stat"><div class="hero-stat-val">TDEE</div><div class="hero-stat-label">Kalori Harian</div></div>
        <div class="hero-stat"><div class="hero-stat-val">PLAN</div><div class="hero-stat-label">Program Latihan</div></div>
    </div>
</div>
""", unsafe_allow_html=True)

# ============================================
# GYM TIPS
# ============================================
st.markdown("""
<div class="section-card">
    <div class="section-title">🏅 Tips Gym</div>
    <div class="tips-grid">
        <div class="tip-item"><div class="tip-icon">🥤</div><div class="tip-title">Hidrasi</div><div class="tip-desc">Minum 2-3 liter air per hari untuk performa optimal</div></div>
        <div class="tip-item"><div class="tip-icon">😴</div><div class="tip-title">Istirahat</div><div class="tip-desc">Tidur 7-9 jam — otot tumbuh saat kamu tidur</div></div>
        <div class="tip-item"><div class="tip-icon">🥩</div><div class="tip-title">Protein</div><div class="tip-desc">Konsumsi 1.6-2.2g protein per kg berat badan</div></div>
        <div class="tip-item"><div class="tip-icon">🔥</div><div class="tip-title">Konsistensi</div><div class="tip-desc">Latihan rutin lebih penting dari latihan keras sesekali</div></div>
        <div class="tip-item"><div class="tip-icon">🧘</div><div class="tip-title">Pemanasan</div><div class="tip-desc">Selalu warmup 10 menit sebelum latihan berat</div></div>
        <div class="tip-item"><div class="tip-icon">📈</div><div class="tip-title">Progressive</div><div class="tip-desc">Naikkan beban secara bertahap tiap minggu</div></div>
    </div>
</div>
""", unsafe_allow_html=True)

# ============================================
# FORM INPUT
# ============================================
st.markdown('<div class="section-card"><div class="section-title">📋 Data Diri Kamu</div>', unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
    nama   = st.text_input("Nama Lengkap", placeholder="Contoh: Marcel Bayu Sugito")
    usia   = st.number_input("Usia (tahun)", min_value=10, max_value=80, value=21)
with col2:
    berat  = st.number_input("Berat Badan (kg)", min_value=30.0, max_value=200.0, value=70.0, step=0.1)
    tinggi = st.number_input("Tinggi Badan (cm)", min_value=100.0, max_value=250.0, value=170.0, step=0.1)
st.markdown('</div>', unsafe_allow_html=True)

hitung = st.button("⚡ ANALISIS SEKARANG")

if hitung:
    if not nama:
        st.warning("⚠️ Masukkan nama kamu dulu ya!")
    else:
        st.session_state.sudah_hitung = True
        st.session_state.nama         = nama
        st.session_state.usia         = usia
        st.session_state.berat        = berat
        st.session_state.tinggi       = tinggi
        tinggi_meter = tinggi / 100
        bmi = berat / (tinggi_meter ** 2)
        st.session_state.bmi          = round(bmi, 1)
        st.session_state.kalori_bulat = round(10 * berat + 6.25 * tinggi - 5 * usia + 5 if usia <= 30 else 10 * berat + 6.25 * tinggi - 5 * usia - 161)

# ============================================
# HASIL
# ============================================
if st.session_state.get("sudah_hitung"):

    nama         = st.session_state.nama
    berat        = st.session_state.berat
    kalori_bulat = st.session_state.kalori_bulat
    bmi_bulat    = st.session_state.bmi

    if bmi_bulat < 18.5:
        kategori = "Kurus";        css_bmi = "kurus";    emoji = "🔵"
        saran = "Tambah asupan kalori dan protein. Fokus latihan weight training untuk membangun massa otot."
    elif bmi_bulat < 25:
        kategori = "Normal / Ideal"; css_bmi = "normal"; emoji = "🟢"
        saran = "Tubuh kamu ideal! Pertahankan dengan kombinasi cardio dan weight training secara rutin."
    elif bmi_bulat < 30:
        kategori = "Gemuk";        css_bmi = "gemuk";    emoji = "🟡"
        saran = "Kurangi kalori harian 300-500 kkal. Perbanyak cardio dan jaga pola makan."
    else:
        kategori = "Obesitas";     css_bmi = "obesitas"; emoji = "🔴"
        saran = "Disarankan konsultasi ahli gizi. Mulai dengan olahraga ringan setiap hari."

    # METRIK
    st.markdown(f"""
    <div class="section-card">
        <div class="section-title">📊 Hasil Analisis — {nama}</div>
        <div class="metrics-grid">
            <div class="metric-card" data-icon="⚖️"><div class="metric-val">{bmi_bulat}</div><div class="metric-unit">BMI Score</div><div class="metric-lbl">Body Mass Index</div></div>
            <div class="metric-card" data-icon="🏅"><div class="metric-val">{emoji}</div><div class="metric-unit">{kategori}</div><div class="metric-lbl">Kategori Tubuh</div></div>
            <div class="metric-card" data-icon="🔥"><div class="metric-val">{kalori_bulat}</div><div class="metric-unit">kkal / hari</div><div class="metric-lbl">Kalori Dasar (BMR)</div></div>
        </div>
        <div class="bmi-{css_bmi}">
            <div class="bmi-title">{emoji} Kategori: {kategori}</div>
            <div class="bmi-saran">💡 {saran}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # KALORI
    st.markdown(f"""
    <div class="section-card">
        <div class="section-title">🍽️ Kebutuhan Kalori Harian (TDEE)</div>
        <div class="kalori-grid">
            <div class="kalori-item"><span class="kalori-name">😴 Tidak aktif</span><span class="kalori-val">{round(kalori_bulat * 1.2)} kkal</span></div>
            <div class="kalori-item"><span class="kalori-name">🚶 Olahraga ringan</span><span class="kalori-val">{round(kalori_bulat * 1.375)} kkal</span></div>
            <div class="kalori-item"><span class="kalori-name">🏃 Olahraga sedang</span><span class="kalori-val">{round(kalori_bulat * 1.55)} kkal</span></div>
            <div class="kalori-item"><span class="kalori-name">🏋️ Olahraga berat</span><span class="kalori-val">{round(kalori_bulat * 1.725)} kkal</span></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # TARGET
    st.markdown('<div class="section-card"><div class="section-title">🎯 Pilih Program Kamu</div>', unsafe_allow_html=True)
    target = st.radio("Pilih target gym kamu:", [
        "🔥 Cutting — Turun berat badan",
        "💪 Bulking — Naik massa otot",
        "⚖️ Maintain — Jaga berat badan ideal"
    ])

    if target == "🔥 Cutting — Turun berat badan":
        kalori_target = round(kalori_bulat * 1.55 - 500)
        protein       = round(berat * 2.2)
        label         = "🔥 CUTTING PLAN"
        catatan       = "Deficit 500 kkal/hari = turun ±0.5kg per minggu"

        jadwal = [
            {
                "hari": "Senin", "tipe": "latihan", "fokus": "💪 Dada & Trisep",
                "exercises": [
                    {"nama": "Bench Press", "detail": "4 set × 12 reps — istirahat 60 detik"},
                    {"nama": "Incline Dumbbell Press", "detail": "3 set × 12 reps — istirahat 60 detik"},
                    {"nama": "Cable Flyes", "detail": "3 set × 15 reps — istirahat 45 detik"},
                    {"nama": "Tricep Pushdown", "detail": "3 set × 15 reps — istirahat 45 detik"},
                    {"nama": "Overhead Tricep Extension", "detail": "3 set × 12 reps — istirahat 45 detik"},
                ]
            },
            {
                "hari": "Selasa", "tipe": "cardio", "fokus": "🏃 Cardio HIIT",
                "exercises": [
                    {"nama": "Warm Up Jalan", "detail": "5 menit — kecepatan santai"},
                    {"nama": "Sprint Interval", "detail": "20 detik sprint / 40 detik jalan × 10 ronde"},
                    {"nama": "Jump Rope", "detail": "3 set × 3 menit — istirahat 1 menit"},
                    {"nama": "Cool Down", "detail": "5 menit jalan santai + stretching"},
                ]
            },
            {
                "hari": "Rabu", "tipe": "latihan", "fokus": "🦵 Kaki & Bahu",
                "exercises": [
                    {"nama": "Squat", "detail": "4 set × 12 reps — istirahat 90 detik"},
                    {"nama": "Leg Press", "detail": "3 set × 15 reps — istirahat 60 detik"},
                    {"nama": "Leg Curl", "detail": "3 set × 12 reps — istirahat 60 detik"},
                    {"nama": "Shoulder Press", "detail": "3 set × 12 reps — istirahat 60 detik"},
                    {"nama": "Lateral Raise", "detail": "3 set × 15 reps — istirahat 45 detik"},
                ]
            },
            {
                "hari": "Kamis", "tipe": "cardio", "fokus": "🚴 Cardio Steady State",
                "exercises": [
                    {"nama": "Sepeda Statis", "detail": "30 menit — intensitas sedang (zone 2)"},
                    {"nama": "Elliptical", "detail": "15 menit — intensitas ringan"},
                    {"nama": "Core Circuit", "detail": "Plank 3×60 detik, Crunch 3×20 reps"},
                ]
            },
            {
                "hari": "Jumat", "tipe": "latihan", "fokus": "🏋️ Punggung & Bisep",
                "exercises": [
                    {"nama": "Deadlift", "detail": "4 set × 10 reps — istirahat 90 detik"},
                    {"nama": "Pull Up / Lat Pulldown", "detail": "4 set × 10 reps — istirahat 60 detik"},
                    {"nama": "Seated Row", "detail": "3 set × 12 reps — istirahat 60 detik"},
                    {"nama": "Barbell Curl", "detail": "3 set × 12 reps — istirahat 45 detik"},
                    {"nama": "Hammer Curl", "detail": "3 set × 12 reps — istirahat 45 detik"},
                ]
            },
            {
                "hari": "Sabtu", "tipe": "cardio", "fokus": "🏃 Cardio + Core",
                "exercises": [
                    {"nama": "Lari Pagi", "detail": "30-45 menit — pace santai"},
                    {"nama": "Hanging Leg Raise", "detail": "3 set × 15 reps"},
                    {"nama": "Russian Twist", "detail": "3 set × 20 reps"},
                    {"nama": "Mountain Climber", "detail": "3 set × 30 detik"},
                ]
            },
            {
                "hari": "Minggu", "tipe": "istirahat", "fokus": "😴 Rest Day",
                "exercises": [
                    {"nama": "Full Rest", "detail": "Fokus pemulihan — jangan latihan berat"},
                    {"nama": "Stretching Ringan", "detail": "10-15 menit — opsional"},
                    {"nama": "Jalan Santai", "detail": "20-30 menit — opsional"},
                ]
            },
        ]
        suplemen = [
            {"nama": "Whey Protein Isolate", "detail": "1-2 scoop/hari setelah latihan. Target protein tinggi untuk jaga otot saat cutting."},
            {"nama": "BCAA", "detail": "5-10g sebelum/saat latihan. Cegah muscle breakdown saat kalori rendah."},
            {"nama": "L-Carnitine", "detail": "1-2g sebelum cardio. Bantu pembakaran lemak lebih efektif."},
            {"nama": "Multivitamin", "detail": "1 tablet/hari saat makan. Penting karena asupan makanan dibatasi."},
        ]

    elif target == "💪 Bulking — Naik massa otot":
        kalori_target = round(kalori_bulat * 1.55 + 300)
        protein       = round(berat * 1.8)
        label         = "💪 BULKING PLAN"
        catatan       = "Surplus 300 kkal/hari = naik massa otot secara lean"

        jadwal = [
            {
                "hari": "Senin", "tipe": "latihan", "fokus": "💪 Dada & Trisep (Heavy)",
                "exercises": [
                    {"nama": "Bench Press", "detail": "5 set × 5 reps — beban berat, istirahat 2-3 menit"},
                    {"nama": "Incline Barbell Press", "detail": "4 set × 8 reps — istirahat 90 detik"},
                    {"nama": "Dumbbell Flyes", "detail": "3 set × 10 reps — istirahat 60 detik"},
                    {"nama": "Close Grip Bench Press", "detail": "4 set × 8 reps — istirahat 90 detik"},
                    {"nama": "Skull Crusher", "detail": "3 set × 10 reps — istirahat 60 detik"},
                ]
            },
            {
                "hari": "Selasa", "tipe": "latihan", "fokus": "🦵 Kaki (Heavy)",
                "exercises": [
                    {"nama": "Squat", "detail": "5 set × 5 reps — beban berat, istirahat 3 menit"},
                    {"nama": "Romanian Deadlift", "detail": "4 set × 8 reps — istirahat 90 detik"},
                    {"nama": "Leg Press", "detail": "4 set × 10 reps — istirahat 90 detik"},
                    {"nama": "Leg Extension", "detail": "3 set × 12 reps — istirahat 60 detik"},
                    {"nama": "Calf Raise", "detail": "4 set × 15 reps — istirahat 60 detik"},
                ]
            },
            {
                "hari": "Rabu", "tipe": "istirahat", "fokus": "😴 Active Recovery",
                "exercises": [
                    {"nama": "Stretching & Foam Rolling", "detail": "20-30 menit — fokus otot yang pegal"},
                    {"nama": "Jalan Santai", "detail": "20 menit — jaga metabolisme"},
                ]
            },
            {
                "hari": "Kamis", "tipe": "latihan", "fokus": "🏋️ Punggung & Bisep (Heavy)",
                "exercises": [
                    {"nama": "Deadlift", "detail": "5 set × 5 reps — beban berat, istirahat 3 menit"},
                    {"nama": "Barbell Row", "detail": "4 set × 8 reps — istirahat 90 detik"},
                    {"nama": "Lat Pulldown", "detail": "4 set × 10 reps — istirahat 60 detik"},
                    {"nama": "Barbell Curl", "detail": "4 set × 8 reps — istirahat 60 detik"},
                    {"nama": "Incline Dumbbell Curl", "detail": "3 set × 10 reps — istirahat 60 detik"},
                ]
            },
            {
                "hari": "Jumat", "tipe": "latihan", "fokus": "🎯 Bahu & Trap",
                "exercises": [
                    {"nama": "Overhead Press", "detail": "5 set × 5 reps — beban berat, istirahat 2 menit"},
                    {"nama": "Arnold Press", "detail": "3 set × 10 reps — istirahat 60 detik"},
                    {"nama": "Lateral Raise", "detail": "4 set × 12 reps — istirahat 45 detik"},
                    {"nama": "Face Pull", "detail": "3 set × 15 reps — istirahat 45 detik"},
                    {"nama": "Shrugs", "detail": "4 set × 12 reps — istirahat 60 detik"},
                ]
            },
            {
                "hari": "Sabtu", "tipe": "latihan", "fokus": "🔁 Full Body & Core",
                "exercises": [
                    {"nama": "Power Clean", "detail": "4 set × 5 reps — gerak explosif"},
                    {"nama": "Dips (Beban)", "detail": "3 set × 8 reps — istirahat 90 detik"},
                    {"nama": "Pull Up (Beban)", "detail": "3 set × 8 reps — istirahat 90 detik"},
                    {"nama": "Plank", "detail": "3 set × 60 detik"},
                    {"nama": "Ab Wheel", "detail": "3 set × 10 reps"},
                ]
            },
            {
                "hari": "Minggu", "tipe": "istirahat", "fokus": "😴 Full Rest Day",
                "exercises": [
                    {"nama": "Istirahat Total", "detail": "Prioritas tidur 8-9 jam — ini saat otot tumbuh"},
                    {"nama": "Makan Cukup", "detail": "Pastikan surplus kalori terpenuhi hari ini"},
                ]
            },
        ]
        suplemen = [
            {"nama": "Whey Protein / Mass Gainer", "detail": "1-2 scoop/hari. Mass gainer jika susah naik berat, whey jika mudah gemuk."},
            {"nama": "Creatine Monohydrate", "detail": "5g/hari kapan saja. Tingkatkan kekuatan dan volume otot secara signifikan."},
            {"nama": "Pre-Workout", "detail": "30 menit sebelum latihan. Boost energi dan fokus untuk latihan berat."},
            {"nama": "ZMA (Zinc Magnesium)", "detail": "Sebelum tidur. Tingkatkan kualitas tidur dan produksi testosteron alami."},
        ]

    else:
        kalori_target = round(kalori_bulat * 1.55)
        protein       = round(berat * 1.6)
        label         = "⚖️ MAINTAIN PLAN"
        catatan       = "Jaga kalori seimbang untuk mempertahankan komposisi tubuh"

        jadwal = [
            {
                "hari": "Senin", "tipe": "latihan", "fokus": "💪 Upper Body A",
                "exercises": [
                    {"nama": "Bench Press", "detail": "4 set × 10 reps — istirahat 60 detik"},
                    {"nama": "Barbell Row", "detail": "4 set × 10 reps — istirahat 60 detik"},
                    {"nama": "Shoulder Press", "detail": "3 set × 12 reps — istirahat 60 detik"},
                    {"nama": "Bicep Curl", "detail": "3 set × 12 reps — istirahat 45 detik"},
                    {"nama": "Tricep Pushdown", "detail": "3 set × 12 reps — istirahat 45 detik"},
                ]
            },
            {
                "hari": "Selasa", "tipe": "cardio", "fokus": "🏃 Cardio Ringan",
                "exercises": [
                    {"nama": "Lari / Jalan Cepat", "detail": "30 menit — pace sedang, zone 2"},
                    {"nama": "Core Training", "detail": "Plank 3×45 detik, Crunch 3×15 reps, Leg Raise 3×12 reps"},
                ]
            },
            {
                "hari": "Rabu", "tipe": "latihan", "fokus": "🦵 Lower Body",
                "exercises": [
                    {"nama": "Squat", "detail": "4 set × 10 reps — istirahat 90 detik"},
                    {"nama": "Deadlift", "detail": "3 set × 8 reps — istirahat 90 detik"},
                    {"nama": "Lunges", "detail": "3 set × 12 reps tiap kaki — istirahat 60 detik"},
                    {"nama": "Leg Curl", "detail": "3 set × 12 reps — istirahat 60 detik"},
                    {"nama": "Calf Raise", "detail": "3 set × 15 reps — istirahat 45 detik"},
                ]
            },
            {
                "hari": "Kamis", "tipe": "istirahat", "fokus": "😴 Rest & Recovery",
                "exercises": [
                    {"nama": "Istirahat Aktif", "detail": "Stretching 15 menit atau yoga ringan"},
                    {"nama": "Foam Rolling", "detail": "10 menit — fokus kaki dan punggung"},
                ]
            },
            {
                "hari": "Jumat", "tipe": "latihan", "fokus": "💪 Upper Body B",
                "exercises": [
                    {"nama": "Pull Up / Lat Pulldown", "detail": "4 set × 10 reps — istirahat 60 detik"},
                    {"nama": "Incline Press", "detail": "4 set × 10 reps — istirahat 60 detik"},
                    {"nama": "Lateral Raise", "detail": "3 set × 15 reps — istirahat 45 detik"},
                    {"nama": "Face Pull", "detail": "3 set × 15 reps — istirahat 45 detik"},
                    {"nama": "Hammer Curl", "detail": "3 set × 12 reps — istirahat 45 detik"},
                ]
            },
            {
                "hari": "Sabtu", "tipe": "cardio", "fokus": "🏊 Cardio + Fleksibilitas",
                "exercises": [
                    {"nama": "Cardio Pilihan", "detail": "30-40 menit — renang, sepeda, atau lari"},
                    {"nama": "Full Body Stretching", "detail": "15 menit — peregangan menyeluruh"},
                ]
            },
            {
                "hari": "Minggu", "tipe": "istirahat", "fokus": "😴 Full Rest Day",
                "exercises": [
                    {"nama": "Istirahat Total", "detail": "Pemulihan penuh untuk minggu berikutnya"},
                    {"nama": "Persiapan Mental", "detail": "Rencanakan latihan dan meal prep minggu depan"},
                ]
            },
        ]
        suplemen = [
            {"nama": "Whey Protein", "detail": "1 scoop/hari setelah latihan. Bantu penuhi kebutuhan protein harian."},
            {"nama": "Creatine Monohydrate", "detail": "5g/hari. Jaga kekuatan dan performa latihan tetap optimal."},
            {"nama": "Omega-3 Fish Oil", "detail": "1-2 kapsul/hari. Anti-inflamasi, bagus untuk sendi dan jantung."},
            {"nama": "Vitamin D3", "detail": "1000-2000 IU/hari. Penting untuk kesehatan tulang dan imunitas."},
        ]

    # TAMPILAN PLAN
    st.markdown(f"""
    <div class="plan-card">
        <span class="plan-badge">{label}</span>
        <div class="plan-item">🔥 <span>Kalori harian &nbsp;: <span class="plan-val">{kalori_target} kkal</span></span></div>
        <div class="plan-item">🥩 <span>Protein harian &nbsp;: <span class="plan-val">{protein} gram/hari</span></span></div>
        <div class="plan-item">📌 <span>Catatan &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;: <span style="color:#aab">{catatan}</span></span></div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # ============================================
    # JADWAL LATIHAN MINGGUAN
    # ============================================
    st.markdown('<div class="section-card"><div class="section-title">📅 Jadwal Latihan Mingguan</div>', unsafe_allow_html=True)

    tipe_icon = {"latihan": "🏋️", "cardio": "🏃", "istirahat": "😴"}
    tipe_badge = {"latihan": "badge-latihan", "cardio": "badge-cardio", "istirahat": "badge-istirahat"}
    tipe_label = {"latihan": "Weight Training", "cardio": "Cardio", "istirahat": "Rest Day"}

    for hari_data in jadwal:
        hari   = hari_data["hari"]
        tipe   = hari_data["tipe"]
        fokus  = hari_data["fokus"]
        exs    = hari_data["exercises"]
        icon   = tipe_icon[tipe]
        badge  = tipe_badge[tipe]
        blabel = tipe_label[tipe]

        exercise_html = ""
        for ex in exs:
            exercise_html += f"<li class='exercise-item'><div class='exercise-dot'></div><div><div class='exercise-name'>{ex['nama']}</div><div class='exercise-detail'>{ex['detail']}</div></div></li>"

        st.markdown(f"<div class='hari-card {tipe}'><div class='hari-title'>{icon} {hari} — {fokus} <span class='hari-badge {badge}'>{blabel}</span></div><ul class='exercise-list'>{exercise_html}</ul></div>", unsafe_allow_html=True)
    # ============================================
    # REKOMENDASI SUPLEMEN
    # ============================================
    st.markdown('<div class="section-card"><div class="section-title">💊 Rekomendasi Suplemen</div>', unsafe_allow_html=True)
    st.markdown('<div class="suplemen-grid">', unsafe_allow_html=True)
    for s in suplemen:
        st.markdown(f"""
        <div class="suplemen-item">
            <div class="suplemen-name">💊 {s['nama']}</div>
            <div class="suplemen-detail">{s['detail']}</div>
        </div>
        """, unsafe_allow_html=True)
    st.markdown('</div></div>', unsafe_allow_html=True)

    # MOTIVASI
    st.markdown(f"""
    <div class="motivasi-box">
        <div class="motivasi-icon">🏆</div>
        <p class="motivasi-text">Semangat terus, {nama}!</p>
        <p class="motivasi-sub">Konsistensi adalah kunci. Satu hari satu langkah — progress tidak pernah bohong. 💪</p>
    </div>
    """, unsafe_allow_html=True)

# ============================================
    # ARTIKEL TIPS NUTRISI & GYM
    # ============================================
    st.markdown('<div class="section-card"><div class="section-title">📰 Artikel Tips Nutrisi & Gym</div>', unsafe_allow_html=True)

    artikel = [
        {
            "kategori": "🥗 Nutrisi",
            "judul": "Cara Menghitung Kebutuhan Protein Harian",
            "ringkasan": "Protein adalah makronutrien paling penting untuk membangun dan memperbaiki otot. Tanpa asupan protein yang cukup, latihan sekeras apapun tidak akan memberikan hasil maksimal.",
            "isi": """
            <b>Berapa banyak protein yang kamu butuhkan?</b><br><br>
            Kebutuhan protein tergantung pada tujuan dan berat badan kamu:<br>
            • <b>Cutting:</b> 2.0 – 2.4 gram per kg berat badan<br>
            • <b>Bulking:</b> 1.6 – 2.0 gram per kg berat badan<br>
            • <b>Maintain:</b> 1.4 – 1.8 gram per kg berat badan<br><br>
            <b>Sumber protein terbaik:</b><br>
            • Dada ayam (31g protein per 100g)<br>
            • Telur (13g protein per 100g)<br>
            • Ikan tuna (30g protein per 100g)<br>
            • Tempe (19g protein per 100g)<br>
            • Greek yogurt (10g protein per 100g)<br><br>
            <b>Tips:</b> Sebarkan asupan protein ke 4-5 kali makan per hari untuk penyerapan optimal.
            """
        },
        {
            "kategori": "🏋️ Latihan",
            "judul": "Progressive Overload — Kunci Otot Terus Berkembang",
            "ringkasan": "Progressive overload adalah prinsip paling fundamental dalam gym. Tanpa ini, otot kamu tidak akan pernah berkembang meski latihan setiap hari.",
            "isi": """
            <b>Apa itu Progressive Overload?</b><br><br>
            Progressive overload artinya secara bertahap meningkatkan beban atau volume latihan dari waktu ke waktu, sehingga otot terus mendapat stimulus baru untuk berkembang.<br><br>
            <b>Cara menerapkannya:</b><br>
            • Naikkan beban 2.5 – 5 kg setiap 1-2 minggu<br>
            • Tambah 1-2 reps tiap sesi jika beban belum bisa dinaikkan<br>
            • Tambah 1 set per latihan setiap bulan<br>
            • Kurangi waktu istirahat antar set<br><br>
            <b>Contoh:</b><br>
            Minggu 1: Bench Press 50kg × 3 set × 10 reps<br>
            Minggu 2: Bench Press 50kg × 3 set × 12 reps<br>
            Minggu 3: Bench Press 52.5kg × 3 set × 10 reps<br><br>
            <b>Ingat:</b> Catat setiap sesi latihan kamu agar bisa tracking progress dengan akurat.
            """
        },
        {
            "kategori": "😴 Recovery",
            "judul": "Kenapa Istirahat Sama Pentingnya dengan Latihan",
            "ringkasan": "Banyak orang berpikir semakin banyak latihan semakin bagus. Padahal otot tidak tumbuh saat latihan — otot tumbuh saat kamu istirahat.",
            "isi": """
            <b>Apa yang terjadi saat kamu tidur?</b><br><br>
            Saat tidur, tubuh melepaskan Growth Hormone (GH) yang berfungsi memperbaiki serat otot yang rusak akibat latihan. Inilah mengapa tidur 7-9 jam sangat krusial.<br><br>
            <b>Tanda-tanda overtrained:</b><br>
            • Performa latihan menurun<br>
            • Mudah lelah dan lesu<br>
            • Sering sakit (imunitas turun)<br>
            • Mood buruk dan sulit konsentrasi<br>
            • Nyeri sendi berkepanjangan<br><br>
            <b>Tips recovery terbaik:</b><br>
            • Tidur 7-9 jam per malam — prioritas utama<br>
            • Konsumsi protein sebelum tidur (kasein)<br>
            • Lakukan active recovery (jalan, stretching, foam rolling)<br>
            • Minimal 1-2 hari full rest per minggu<br><br>
            <b>Ingat:</b> Rest day bukan hari malas — itu bagian dari program latihan kamu.
            """
        },
        {
            "kategori": "🥤 Hidrasi",
            "judul": "Dampak Dehidrasi terhadap Performa Gym",
            "ringkasan": "Kehilangan hanya 2% cairan tubuh sudah bisa menurunkan performa latihan hingga 20%. Hidrasi yang cukup adalah hal paling mudah tapi sering diabaikan.",
            "isi": """
            <b>Berapa banyak air yang dibutuhkan?</b><br><br>
            • Minimal 2-3 liter per hari untuk orang aktif<br>
            • Tambah 500ml untuk setiap 30 menit latihan intens<br>
            • Cek warna urin — kuning pucat = terhidrasi baik<br><br>
            <b>Waktu minum yang optimal:</b><br>
            • Pagi hari: 1-2 gelas segera setelah bangun tidur<br>
            • Sebelum latihan: 500ml, 30 menit sebelumnya<br>
            • Selama latihan: 150-250ml setiap 15-20 menit<br>
            • Setelah latihan: 500ml untuk mengganti cairan yang hilang<br><br>
            <b>Tanda dehidrasi saat latihan:</b><br>
            • Pusing dan kepala berat<br>
            • Kram otot tiba-tiba<br>
            • Detak jantung lebih cepat dari biasanya<br>
            • Mulut dan tenggorokan kering<br><br>
            <b>Tips:</b> Bawa botol minum 1 liter ke gym dan targetkan habis 2x selama sesi latihan.
            """
        },
        {
            "kategori": "🧠 Mental",
            "judul": "Mind-Muscle Connection — Latihan Lebih Efektif dengan Fokus",
            "ringkasan": "Penelitian menunjukkan bahwa fokus mental pada otot yang dilatih bisa meningkatkan aktivasi otot hingga 60% dibanding latihan tanpa fokus.",
            "isi": """
            <b>Apa itu Mind-Muscle Connection?</b><br><br>
            Mind-muscle connection adalah kemampuan untuk secara sadar merasakan dan mengontrol otot yang sedang kamu latih. Ini bukan soal beban berat — tapi soal kualitas kontraksi otot.<br><br>
            <b>Cara melatihnya:</b><br>
            • Turunkan beban 20-30% dan fokus pada sensasi otot<br>
            • Gerakkan secara perlahan — terutama fase negatif (turun/balik)<br>
            • Squeeze atau kontraksikan otot di titik puncak gerakan<br>
            • Hindari momentum — jangan ayun beban<br><br>
            <b>Contoh — Bicep Curl:</b><br>
            ❌ Salah: Angkat beban cepat menggunakan momentum bahu<br>
            ✅ Benar: Angkat perlahan, rasakan bisep berkontraksi, squeeze di atas, turun 3 detik<br><br>
            <b>Tips:</b> Letakkan tangan bebas di otot yang dilatih untuk membantu merasakan kontraksinya.
            """
        },
    ]

    # Tampilkan artikel dengan expander
    for art in artikel:
        with st.expander(f"{art['kategori']}  |  {art['judul']}"):
            st.markdown(f"""
            <div style="background:#f8f9ff; border-radius:12px; padding:1rem 1.2rem; margin-bottom:1rem; border-left:4px solid #f7971e;">
                <p style="color:#555; font-size:0.88rem; margin:0; font-style:italic;">{art['ringkasan']}</p>
            </div>
            <div style="font-size:0.88rem; color:#333; line-height:1.8;">
                {art['isi']}
            </div>
            """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)
# FOOTER
st.markdown("""
<div class="footer">
    <br>🏋️ &nbsp; <strong>FITNESS TRACKER APP</strong> &nbsp; 🏋️
    <br>Developed with 💪 by <strong>Marcel Bayu Sugito</strong>
    <br>Built with Python & Streamlit<br><br>
</div>
""", unsafe_allow_html=True)
