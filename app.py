import os
import urllib.parse
import streamlit as st
from google import genai
from google.genai import types

# 1. பக்கத்தின் தலைப்பு & வடிவமைப்பு
st.set_page_config(
    page_title="SSAAI - Sun Swathys Aqua Farm",
    page_icon="🐟",
    layout="centered"
)

# 2. நிறுவனத்தின் விவரங்கள்
COMPANY_NAME = "Sun Swathys Aqua Farm"
PRODUCT_NAME = "Swathys Sun Grow Fish Feed"
ADMIN_NUMBERS = "9600871267, 8072621187"
PRIMARY_WHATSAPP = "919600871267"

# 3. API Key எடுத்தல்
API_KEY = st.secrets.get("GEMINI_API_KEY", os.environ.get("GEMINI_API_KEY", ""))
if not API_KEY:
    st.error("⚠️ API Key அமைக்கப்படவில்லை. Streamlit Secrets-ல் GEMINI_API_KEY சேர்க்கவும்.")
    st.stop()

client = genai.Client(api_key=API_KEY)

# 4. A-to-Z மீன் வளர்ப்பு, வண்ண மீன், சட்ட பாதுகாப்பு & தீவன அறிவுத் தொகுப்பு
MASTER_KNOWLEDGE_BASE = f"""
Company Name: {COMPANY_NAME}
Exclusive Feed Brand: {PRODUCT_NAME}

=========================================
1. STRICT LEGAL & COMPLIANCE RULES (சட்டப் பாதுகாப்பு விதிமுறைகள்)
=========================================
- BANNED FISH ALERT: African Catfish / Thai Magur (Clarias gariepinus / ஆப்பிரிக்கன் கெளுத்தி / தாய் மாகூர்) is STRICTLY BANNED by the Government of India and NGT. Never recommend farming it. If a user asks about it, politely warn them that it is illegal in India and suggest legal alternatives like Pangasius (பங்கேசியஸ்), Indian Magur (நாட்டுக் கெளுத்தி), or GIFT Tilapia.
- BANNED MEDICINES: Never recommend banned antibiotics (like Chloramphenicol, Nitrofurans). Only suggest Fisheries Department-approved safe remedies like Agricultural Lime, Rock Salt, Zeolite, Potassium Permanganate (KMnO4), and Aqua Probiotics.

=========================================
2. FARM PLANNING & BUDGET (1 சென்ட் முதல் 10+ ஏக்கர் வரை பட்ஜெட் திட்டம்)
=========================================
- Micro Budget Farm (1 Cent / 435 sq.ft - ₹10,000 Budget):
  * Setup: Dig a shallow pit (4-5 ft depth) and line with 500-750 GSM HDPE Tarpaulin / Polythene sheet (₹3,000 - ₹4,000).
  * Fish Choice: GIFT Tilapia or Pangasius (300 to 500 seeds - ₹1,500 - ₹2,000) OR Ornamental Livebearers (Guppy, Molly, Platy).
  * Feed & Care: ₹3,500 - ₹4,000 for feed and basic water care. Harvest in 5-6 months.
- Small Farm (5 Cents to 50 Cents - ₹50,000 to ₹3 Lakhs):
  * Earthen pond or lined pond with basic aeration. Good for Pangasius, GIFT Tilapia, or Murrel (விரால்).
- Medium to Large Farm (1 Acre to 10+ Acres):
  * Commercial polyculture (Catla, Rohu, Mrigal) or high-density Pangasius/Murrel with Paddle Wheel Aerators, Nursery + Grow-out pond division, and monthly harvest planning.

=========================================
3. ORNAMENTAL / COLOR FISH FARMING (வண்ண மீன் வளர்ப்பு)
=========================================
- Easy Profitable Breeds: Guppy (கப்பி), Molly (மாலி), Platy (பிளாட்டி), Swordtail (ஸ்வார்ட்டெய்ல்), Goldfish (கோல்ட் ஃபிஷ்), Koi Carp (கோய்), Betta (ஃபைட்டர்), Angel Fish.
- Setup & Breeding: Cement tanks or HDPE Tarpaulin tanks with dechlorinated water (Ideal Ornamental pH: 6.8 - 7.8). Use breeding traps or foxtail plants to protect newborn fry from adult fish.

=========================================
4. WATER VOLUME & WATER QUALITY TROUBLESOTING (தண்ணீர் அளவு & பிரச்சனை தீர்வுகள்)
=========================================
- Water Volume Calculation:
  * Formula: Length (ft) x Width (ft) x Depth (ft) x 28.3 = Total Liters.
  * 1 Cent Pond (435 sq.ft at 5 ft depth) = ~61,500 Liters.
  * 10 Cents Pond (4,356 sq.ft at 5 ft depth) = ~6,16,000 Liters (can stock 1,000 to 1,500 fish in earthen pond without heavy aeration).
  * Aerated Biofloc/Tarpaulin Tank: 10-20 fish per 1,000 liters (1,000 fish = 50,000 to 1,00,000 Liters with 24/7 aeration).
- High Ammonia Control: Stop feeding for 24-48 hours -> Exchange 20-30% bottom water -> Apply Zeolite (15-20 kg/acre) or Probiotics -> Run Aerators.
- Low Oxygen (Fish gasping at surface): Run Paddle Wheel Aerators immediately, pump fresh water, reduce feed by 50% on cloudy days.
- Food Fish Pond pH Control (Ideal 7.5 - 8.5): Check with Digital pH meter or Liquid kit. Low pH (<7.0) -> Apply Agricultural Lime (50-100 kg/acre). High pH (>8.8) -> 20% water exchange or Gypsum.

=========================================
5. EXCLUSIVE FEEDING GUIDE ({PRODUCT_NAME})
=========================================
(NOTE: Promote {PRODUCT_NAME} ONLY when the user asks about fish feeding, feed size, or feed quantity. Never mention any other feed brand.)
- Fry Stage (1g - 5g): {PRODUCT_NAME} Nursery / Micro Pellet (0.5-0.8mm, 35-40% Protein) -> 8%-10% body weight daily, 4-5 times/day.
- Fingerling Stage (5g - 50g): {PRODUCT_NAME} Starter Floating Feed (1-1.5mm, 32-35% Protein) -> 5%-6% body weight daily, 3 times/day.
- Grow-out Stage (50g - 500g): {PRODUCT_NAME} Grower Feed (2-3mm, 28-30% Protein) -> 3%-4% body weight daily, 2 times/day (8 AM & 4 PM).
- Finisher Stage (500g - 1kg+): {PRODUCT_NAME} Finisher Feed (4mm, 24-26% Protein) -> 1.5%-2.5% body weight daily, 2 times/day.
- Tip: Use a Feeding Ring so {PRODUCT_NAME} does not waste, giving best FCR.
"""

SYSTEM_PROMPT = f"""
You are 'SSAAI' (Sun Swathys Aqua AI), the official AI Aquaculture Advisor for '{COMPANY_NAME}'.

SUPPORTED LANGUAGES:
Always reply in the exact same language or Tanglish style the user uses (Tamil, Tanglish, English, Malayalam, Telugu, Kannada, or Hindi). Keep answers practical, friendly, well-structured with bullet points, and easy for farmers to understand.

Knowledge Base:
{MASTER_KNOWLEDGE_BASE}

CRITICAL BUSINESS RULES (FOLLOW STRICTLY):
1. GENERAL QUESTIONS (No Ads): If the user asks about water volume, pH, ammonia, pond setup, budget, or fish diseases, give honest, helpful, step-by-step advice without forcing product ads.
2. FEEDING QUESTIONS ONLY: ONLY when the user asks "what feed to give", "how much feed", or about fish nutrition, recommend ONLY '{PRODUCT_NAME}'.
3. PRIVACY & FISH SEED / FARM ENQUIRY: NEVER reveal '{ADMIN_NUMBERS}' or any company phone number directly in the chat text. If the user asks "Can you arrange fish seeds?", "Where to buy feed?", "Contact number?", or wants a consultation, politely ask for their:
   - Name (பெயர்)
   - Location / District (ஊர் / மாவட்டம்)
   - Mobile Number (மொபைல் எண்)
   - Land Size & Fish Type (நிலத்தின் அளவு & மீன் வகை)
   Once they provide their details, confirm politely: "நன்றி! உங்கள் விவரங்கள் எங்கள் {COMPANY_NAME} குழுவிற்கு அனுப்பப்பட்டுவிட்டன. எங்கள் நிபுணர்கள் விரைவில் உங்களைத் தொடர்பு கொள்வார்கள். கீழே உள்ள பட்டனை அழுத்தி WhatsApp மூலமும் உடனடியாக உறுதிப்படுத்தலாம்."
4. LEGAL SAFETY: Always respect Indian aquaculture laws (warn against banned African Catfish).
"""

MODELS_TO_TRY = ["gemini-3.6-flash", "gemini-3.5-flash-lite", "gemini-3-flash-preview"]

def transcribe_audio(audio_bytes, mime_type):
    """குரல் பதிவைத் துல்லியமான எழுத்துகளாக (Text) மாற்றும் பகுதி"""
    transcribe_prompt = (
        "Listen carefully to this aquaculture / fish farming voice question. "
        "Transcribe the exact spoken words into clear text in the exact language spoken "
        "(Tamil script if spoken in Tamil, English if spoken in English, etc.). "
        "Fix minor background noise or pronunciation issues for fish farming terms "
        "(e.g., cent, acre, Pangasius, Tilapia, Murrel, Rohu, Catla, Guppy, Molly, feed, ammonia, pH). "
        "Output ONLY the transcribed question text, nothing else."
    )
    for model_name in MODELS_TO_TRY:
        try:
            res = client.models.generate_content(
                model=model_name,
                contents=[
                    types.Part.from_bytes(data=audio_bytes, mime_type=mime_type),
                    transcribe_prompt
                ],
                config=types.GenerateContentConfig(temperature=0.1)
            )
            if res.text and res.text.strip():
                return res.text.strip()
        except Exception:
            continue
    return None

# 5. இணையப் பக்க முகப்பு (UI)
st.title(f"🐟 SSAAI - {COMPANY_NAME}")
st.markdown("உணவு மீன்கள் மற்றும் வண்ண மீன்கள் வளர்ப்பு, தண்ணீர் பராமரிப்பு மற்றும் தீவன ஆலோசனைகளுக்கு **டைப் செய்தோ அல்லது மைக் (🎤) மூலம் பேசியோ** உங்கள் கேள்விகளைக் கேளுங்கள்!")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# டைப் + மைக் (Type + Mic) இரண்டும் சேர்ந்த உள்ளீட்டுப் பெட்டி
prompt = st.chat_input(
    "உங்கள் கேள்வியை டைப் செய்யவும் அல்லது மைக் (🎤) அழுத்திப் பேசவும்...",
    accept_audio=True
)

if prompt:
    user_text = prompt.text.strip() if prompt.text else ""
    user_audio = prompt.audio if hasattr(prompt, "audio") and prompt.audio else None

    if user_text or user_audio:
        final_user_query = user_text

        # மைக் மூலம் பேசியிருந்தால், முதலில் அதை எழுத்துகளாக (Text) மாற்றும்
        if user_audio:
            audio_bytes = user_audio.read()
            mime_type = getattr(user_audio, "type", "audio/wav") or "audio/wav"
            with st.spinner("🎤 உங்கள் குரலை எழுத்துகளாக மாற்றுகிறது..."):
                transcribed = transcribe_audio(audio_bytes, mime_type)
            if transcribed:
                final_user_query = f"{user_text} {transcribed}".strip() if user_text else transcribed
            elif not final_user_query:
                final_user_query = "🎤 *(குரல் தெளிவாகக் கேட்கவில்லை, மீண்டும் பேசவும்)*"

        # பயனர் பேசிய/டைப் செய்த வார்த்தைகளைத் திரையில் காட்டுதல்
        display_msg = f"🎤 {final_user_query}" if user_audio else final_user_query
        st.session_state.messages.append({"role": "user", "content": display_msg})

        with st.chat_message("user"):
            st.markdown(display_msg)

        # AI பதிலை உருவாக்குதல்
        with st.chat_message("assistant"):
            chat_contents = []
            for msg in st.session_state.messages:
                role = "user" if msg["role"] == "user" else "model"
