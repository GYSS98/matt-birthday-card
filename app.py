# app.py — Birthday Card (cover → reveal)
# Fireworks across full screen (z-indexed), confetti rain, dancing title letters
import streamlit as st

# ===== Settings =====
NAME = "Matt"
DISPLAY_DATE = "27 August 2025"
TAGLINE = "Thank you for your leadership, guidance, and support."

TEAM_NOTES = [
    "Happy Birthday Matt!\nWishing you a wonderful year ahead filled with success and happiness, and plenty of wins (both at work and for United!). Thank you for all your guidance, support, and encouragement.\nBest wishes,\nSaif",
    "Happy Birthday Matt!\nI hope you have a wonderful day, filled with cake, not Teams-calls and reporting requests (unless it's a pie-chart)! Thanks for your great support!\nRik",
    "Happy Birthday Matt!\nWishing you a year (or at least your day) with no system crashes, reports being in time and all running smooth without reboot. Thanks for your constant support!\nAlenka",
    "Happy Birthday Matt!\nHave a fantastic birthday, and I hope you will celebrate on another nice cruise soon!\nMike Reade",
    "Happy Birthday Matt!\nWishing you all the best! And most importantly, zero Extrapool headaches!!\nEduard",
    "Happy Birthday Matt!\nWish you all the best! Hope you have an amazing day with lots of cake and laughs! Wish you a year filled with joy and many blessings.\nPriscilla",
    "Happy Birthday Matt!\nI wish you a very happy birthday and that you have a wonderful day and a fantastic year. It's great to have you as a colleague!\nCristina Bonal",
    "Happy Birthday Matt!\nWishing you a very Happy Birthday! Hope you have an amazing day filled with laughter and joy, and may you have a great year ahead. Thank you for your guidance and support.\nHarsh Miglani",
    "Happy Birthday Matt!\nWishing you all the best for the year ahead!\nMichelle Webster",
    "Hope you have a very Happy Birthday Matt! Older and wiser by another year; certainly something to celebrate!\nMatt H",
    "Happy Birthday Matt!\nThank you for your guidance and positive spirits always! Wishing you a very happy and blessed Birthday around your loved ones.\nYves",
    "Happy Birthday Matt!\nWishing you the best for the year ahead! Hope you have a Fab one!\nDineshrie",
    "Happy Birthday Matt!\nCongratulation to your 28th birthday.... Enjoy your day and keep like you are.\nSilke",
    "Happy Birthday Matt!\n🎉 Wishing you a wonderful day and year ahead. Working with you is truly inspiring — not only because of your skill and professionalism, but also for the way you always find time to support others with such kindness. I’m grateful to have a colleague like you and I hope today brings you as much joy as you bring to those around you.\nSerena",
    "To the master & commander of kindness, support and swiftness, wishing you a truly happy birthday, Matt! 🎊\nGiuseppe",
    "Happy Birthday Matt! All the best from France\nGuillaume",
    "Hi Matt\nWishing you a very happy birthday! Hope you have many blessings, treats and spoils 🙂\nMarcelle",
]

st.set_page_config(page_title=f"Happy Birthday {NAME}!", page_icon="🎉", layout="wide")

# ---- Session state ----
if "opened" not in st.session_state:
    st.session_state.opened = False
if "balloons_sent" not in st.session_state:
    st.session_state.balloons_sent = False

# ---- Styles (animated background + card) ----
st.markdown("""
<style>
  @keyframes drift {
    0% { background-position: 0 0, 0 0, 0 0; }
    50% { background-position: 50px 30px, -40px 60px, 30px -20px; }
    100% { background-position: 0 0, 0 0, 0 0; }
  }
  html, body, [data-testid="stAppViewContainer"] {
    background:
      radial-gradient(1200px 600px at 20% 10%, rgba(255,255,255,0.06), transparent 55%),
      radial-gradient(1000px 500px at 80% 0%, rgba(255,255,255,0.05), transparent 55%),
      linear-gradient(135deg, #0b0f17 0%, #121828 45%, #0e1220 100%) !important;
    background-image:
      radial-gradient(2px 2px at 10% 20%, rgba(255,255,255,.18) 40%, transparent 41%),
      radial-gradient(2px 2px at 70% 30%, rgba(212,175,55,.22) 40%, transparent 41%),
      radial-gradient(1.5px 1.5px at 40% 70%, rgba(255,255,255,.18) 40%, transparent 41%),
      radial-gradient(1200px 600px at 20% 10%, rgba(255,255,255,0.06), transparent 55%),
      radial-gradient(1000px 500px at 80% 0%, rgba(255,255,255,0.05), transparent 55%),
      linear-gradient(135deg, #0b0f17 0%, #121828 45%, #0e1220 100%);
    background-blend-mode: normal, normal, normal, lighten, lighten, normal;
    animation: drift 16s ease-in-out infinite;
    font-family: "Segoe UI", ui-sans-serif, system-ui, -apple-system, Roboto, "Helvetica Neue", Arial;
  }

  .wrap { max-width: 1100px; margin: 0 auto; padding: 18px 18px 36px; }
  .card {
    position: relative; background: rgba(10,12,18,0.72); backdrop-filter: blur(3px);
    border-radius: 22px; padding: 36px 34px; box-shadow: 0 12px 36px rgba(0,0,0,.35);
    border: 1px solid rgba(255,255,255,.06);
  }
  .frame { position: absolute; inset: 10px; border-radius: 18px;
    box-shadow: 0 0 0 1px rgba(212,175,55,.45) inset, 0 0 0 2px rgba(255,255,255,.02) inset; pointer-events:none; }
  .title {
    text-align:center; color:#D4AF37; font-size: 54px; font-weight: 800;
    text-shadow: 0 0 12px rgba(0,0,0,.45); margin: 6px 0 2px; position: relative;
  }
  /* Dancing letters */
  .dance span {
    display: inline-block; animation: bounce 1.8s ease-in-out infinite;
  }
  .dance span:nth-child(odd) { animation-duration: 1.6s; }
  .dance span:nth-child(3n) { animation-duration: 2.0s; }
  @keyframes bounce {
    0%,100% { transform: translateY(0) rotate(0deg); }
    25% { transform: translateY(-6px) rotate(-2deg); }
    50% { transform: translateY(0) rotate(0deg); }
    75% { transform: translateY(-3px) rotate(1deg); }
  }

  .candles { display:flex; justify-content:center; gap:12px; margin-bottom:8px; }
  .flame {
    width:10px; height:20px; border-radius:50%;
    background: radial-gradient(circle at 50% 30%, #FFD700, #FF8C00);
    animation: flicker 0.15s infinite alternate;
  }
  @keyframes flicker { from { transform: scaleY(1); opacity:.85; } to { transform: scaleY(1.2); opacity:1; } }

  .sub   { text-align:center; color:#E6ECF5; font-size: 18px; margin-bottom: 10px; }
  .date  { text-align:center; color:#A9B1BD; font-size: 13px; margin-bottom: 18px; }
  .hairline { height:1px; background: linear-gradient(90deg, transparent, rgba(212,175,55,.45), transparent);
              margin: 14px 0 22px; }
  .section-title { color:#D4AF37; font-weight:700; margin: 0 0 10px; }
  .grid { display:grid; gap:14px; grid-template-columns: repeat(2, minmax(0,1fr)); }
  @media (max-width:720px) { .grid { grid-template-columns: 1fr; } }
  .note { background: rgba(255,255,255,.04); border:1px solid rgba(255,255,255,.08);
          border-radius:14px; padding:14px 16px; color:#F4F7FB; font-size:15px; line-height:1.55; white-space:pre-line; }
  .footer { text-align:center; color:#97A1AE; font-size:12px; margin-top: 26px; }

  /* Fullscreen overlays (ensure on top of Streamlit UI) */
  #fxFireworks, #fxConfetti {
    position: fixed; top:0; left:0; width:100vw; height:100vh;
    pointer-events: none; z-index: 9999;  /* <<< important */
  }
</style>
""", unsafe_allow_html=True)

# ---- COVER or CARD ----
if not st.session_state.opened:
    st.markdown("""
    <div class="wrap">
      <div class="card"><div class="frame"></div>
        <div class="title">Happy Birthday <span class="dance">M a t t</span></div>
        <div class="sub">""" + DISPLAY_DATE + """</div>
        <div class="date">Click below to open your card</div>
      </div>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Open Card", type="primary"):
        st.session_state.opened = True
        if not st.session_state.balloons_sent:
            st.balloons()
            st.session_state.balloons_sent = True
else:
    st.markdown('<div class="wrap"><div class="card"><div class="frame"></div>', unsafe_allow_html=True)

    # Dancing title (per-letter)
    title_text = f"Happy Birthday {NAME}"
    dancing_html = '<div class="title dance">' + "".join(f"<span>{ch}</span>" for ch in title_text) + "</div>"
    st.markdown('<div class="candles"><div class="flame"></div><div class="flame"></div><div class="flame"></div></div>', unsafe_allow_html=True)
    st.markdown(dancing_html, unsafe_allow_html=True)

    st.markdown(f'<div class="sub">{TAGLINE}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="date">{DISPLAY_DATE}</div>', unsafe_allow_html=True)
    st.markdown('<div class="hairline"></div>', unsafe_allow_html=True)

    st.markdown('<div class="section-title">Messages from the team</div>', unsafe_allow_html=True)
    st.markdown('<div class="grid">', unsafe_allow_html=True)
    for msg in TEAM_NOTES:
        safe = msg.replace("<", "&lt;").replace(">", "&gt;")
        st.markdown(f'<div class="note">{safe}</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('</div></div>', unsafe_allow_html=True)

    # ==== Fireworks (everywhere; weighted to upper sky) + Confetti rain ====
    import streamlit.components.v1 as components
    components.html("""
    <canvas id="fxFireworks"></canvas>
    <canvas id="fxConfetti"></canvas>
    <script>
    (function(){
      // ---------- FIREWORKS ----------
      const cf = document.getElementById('fxFireworks'), fctx = cf.getContext('2d');
      let FW = 0, FH = 0, sparks = [];
      function fResize(){ FW = cf.width = window.innerWidth; FH = cf.height = window.innerHeight; }
      window.addEventListener('resize', fResize); fResize();

      function Spark(x,y,col){
        const a = Math.random()*2*Math.PI, s = 2 + Math.random()*5;
        this.x=x; this.y=y; this.vx=Math.cos(a)*s; this.vy=Math.sin(a)*s;
        this.life=60+Math.random()*40; this.col=col; this.size=1.6+Math.random()*2.4;
      }
      function firework(){
        const x = 80 + Math.random()*(FW-160);
        // 70% upper half, 30% lower — feels like sky
        const y = (Math.random()<0.7) ? (60+Math.random()*(FH*0.5-120)) : (FH*0.5+Math.random()*(FH*0.5-120));
        const colors = ["#FFD700","#FFF6D5","#FFFFFF","#FFA500"];
        for(let i=0;i<120;i++) sparks.push(new Spark(x,y, colors[(Math.random()*colors.length)|0]));
        setTimeout(firework, 500 + Math.random()*600);
      }
      function fLoop(){
        fctx.fillStyle = "rgba(10,12,18,0.25)";
        fctx.fillRect(0,0,FW,FH);
        for(let i=sparks.length-1;i>=0;i--){
          const p=sparks[i];
          p.x+=p.vx; p.y+=p.vy; p.vy+=0.035; p.vx*=0.99; p.vy*=0.99; p.life--;
          fctx.beginPath(); fctx.arc(p.x,p.y,p.size,0,Math.PI*2);
          fctx.fillStyle=p.col; fctx.fill();
          if(p.life<=0) sparks.splice(i,1);
        }
        requestAnimationFrame(fLoop);
      }
      firework(); fLoop();

      // ---------- CONFETTI RAIN (Google-style vibe) ----------
      const cc = document.getElementById('fxConfetti'), cctx = cc.getContext('2d');
      let CW = 0, CH = 0, conf = [];
      function cResize(){ CW = cc.width = window.innerWidth; CH = cc.height = window.innerHeight; }
      window.addEventListener('resize', cResize); cResize();

      const cols = ["#FFD700","#FF4D4D","#7AE582","#4DA3FF","#FFFFFF","#FFA500"];
      function dropConfetti(){
        for(let i=0;i<40;i++){
          conf.push({
            x: Math.random()*CW,
            y: -20 - Math.random()*200,
            w: 6 + Math.random()*8,
            h: 8 + Math.random()*12,
            rot: Math.random()*Math.PI,
            vr: (Math.random()-0.5)*0.15,
            vy: 2 + Math.random()*3.5,
            vx: (Math.random()-0.5)*1.2,
            col: cols[(Math.random()*cols.length)|0]
          });
        }
        setTimeout(dropConfetti, 450); // steady stream
      }
      function cLoop(){
        cctx.clearRect(0,0,CW,CH);
        for(let i=conf.length-1;i>=0;i--){
          const p = conf[i];
          p.x += p.vx; p.y += p.vy; p.rot += p.vr;
          if(p.y > CH + 40) { conf.splice(i,1); continue; }
          cctx.save();
          cctx.translate(p.x, p.y);
          cctx.rotate(p.rot);
          cctx.fillStyle = p.col;
          cctx.fillRect(-p.w/2, -p.h/2, p.w, p.h);
          cctx.restore();
        }
        requestAnimationFrame(cLoop);
      }
      dropConfetti(); cLoop();
    })();
    </script>
    """, height=0)

# ---- Footer ----
st.markdown('<div class="footer">Digital card • Use your browser’s Print → “Save as PDF” to share</div>', unsafe_allow_html=True)
