import os
import urllib.parse
import streamlit as st
from google import genai
from google.genai import types

# 1. பக்கத்தின் தலைப்பு & வடிவமைப்பு
LOGO_PATH = "logo.png"
page_icon_img = LOGO_PATH if os.path.exists(LOGO_PATH) else "🐟"

st.set_page_config(
    page_title="SSAAI - Sun Swathys Aqua Farm",
    page_icon=page_icon_img,
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

@st.cache_resource
def get_client_and_models():
    c = genai.Client(api_key=API_KEY)
    valid_models = []
    try:
        # உங்கள் API Key-க்கு வேலை செய்யும் மாடல்களைத் தானாகவே பட்டியலிடுதல்
        for m in c.models.list():
            name = m.name.replace("models/", "")
            actions = getattr(m, "supported_actions", []) or []
            if "gemini" in name.lower() and "flash" in name.lower() and ("generateContent" in actions or not actions):
                if "tts" not in name.lower() and "image" not in name.lower() and "thinking" not in name.lower():
                    valid_models.append(name)
    except Exception:
        pass

    # Fallback பட்டியல்
    for fallback in ["gemini-3.8-flash", "gemini-3.6-flash", "gemini-2.5-flash", "gemini-2.0-flash", "gemini-1.5-flash"]:
        if fallback not in valid_models:
            valid_models.append(fallback)
    return c, valid_models

client, AVAILABLE_MODELS = get_client_and_models()

# 4. A-to-Z மீன் வளர்ப்பு, வண்ண மீன், சட்ட பாதுகாப்பு & தீவன அறிவுத் தொகுப்பு
MASTER_KNOWLEDGE_BASE = f"""
Company Name: {COMPANY_NAME}
Exclusive Feed Brand: {PRODUCT_NAME}

1. STRICT LEGAL & COMPLIANCE RULES:
- BANNED FISH ALERT: African Catfish / Thai Magur (Clarias gariepinus / ஆப்பிரிக்கன் கெளுத்தி / தாய் மாகூர்) is STRICTLY BANNED in India. Never recommend farming it. Suggest legal alternatives like Pangasius (பங்கேசியஸ்), Indian Magur (நாட்டுக் கெளுத்தி), or GIFT Tilapia.
- BANNED MEDICINES: Never recommend banned antibiotics (Chloramphenicol, Nitrofurans). Suggest only safe remedies like Agricultural Lime, Rock Salt, Zeolite, Potassium Permanganate (KMnO4), and Aqua Probiotics.

2. FARM PLANNING & BUDGET (1 சென்ட் முதல் 10+ ஏக்கர் வரை):
- Micro Budget Farm (1 Cent / 435 sq.ft - ₹10,000 Budget): Dig 4-5 ft pit lined with 500-750 GSM HDPE Tarpaulin (₹3,000 - ₹4,000). Stock 300-500 GIFT Tilapia or Pangasius seeds (₹1,500 - ₹2,000) OR Ornamental Livebearers (Guppy, Molly, Platy). ₹3,500 - ₹4,000 for feed & care. Harvest in 5-6 months.
- Small Farm (5 to 50 Cents - ₹50,000 to ₹3 Lakhs): Earthen or lined pond with aeration for Pangasius, GIFT Tilapia, or Murrel (விரால்).
- Medium/Large Farm (1 to 10+ Acres): Commercial polyculture (Catla, Rohu, Mrigal) or high-density Pangasius/Murrel with Paddle Wheel Aerators.

3. ORNAMENTAL / COLOR FISH FARMING (வண்ண மீன் வளர்ப்பு):
- Breeds: Guppy (கப்பி), Molly (மாலி), Platy (பிளாட்டி), Swordtail (ஸ்வார்ட்டெய்ல்), Goldfish, Koi Carp, Betta, Angel Fish.
- Setup: Cement/HDPE tanks with dechlorinated water (Ornamental pH: 6.8 - 7.8). Use breeding traps or foxtail plants to protect fry.

4. WATER VOLUME & WATER QUALITY:
- Formula: Length (ft) x Width (ft) x Depth (ft) x 28.3 = Total Liters.
- 1 Cent Pond (5 ft depth) = ~61,500 Liters. 10 Cents Pond (5 ft depth) = ~6,16,000 Liters (1,000-1,500 fish in earthen pond).
- Aerated Tank: 10-20 fish per 1,000 liters (1,000 fish = 50,000 - 1,00,000 Liters with 24/7 aeration).
- High Ammonia: Stop feed 24-48 hrs -> 20-30% bottom water exchange -> Zeolite (15-20 kg/acre) or Probiotics -> Run Aerators.
- Low Oxygen: Run Paddle Wheel Aerators immediately, pump fresh water, reduce feed by 50% on cloudy days.
- Food Fish pH (Ideal 7.5 - 8.5): Low pH (<7.0) -> Agricultural Lime (50-100 kg/acre). High pH (>8.8) -> 20% water exchange or Gypsum.

5. EXCLUSIVE FEEDING GUIDE ({PRODUCT_NAME}):
(Promote {PRODUCT_NAME} ONLY when user asks about feeding, feed size, or feed quantity.)
- Fry (1g-5g): {PRODUCT_NAME} Nursery/Micro Pellet (0.5-0.8mm, 35-40% Protein) -> 8-10% body weight, 4-5 times/day.
- Fingerling (5g-50g): {PRODUCT_NAME} Starter Floating Feed (1-1.5mm, 32-35% Protein) -> 5-6% body weight, 3 times/day.
- Grow-out (50g-500g): {PRODUCT_NAME} Grower Feed (2-3mm, 28-30% Protein) -> 3-4% body weight, 2 times/day.
- Finisher (500g-1kg+): {PRODUCT_NAME} Finisher Feed (4mm, 24-26% Protein) -> 1.5-2.5% body weight, 2 times/day.
- Tip: Use a Feeding Ring to avoid waste and improve FCR.
"""

SYSTEM_PROMPT = f"""
You are 'SSAAI' (Sun Swathys Aqua AI), the official AI Aquaculture Advisor for '{COMPANY_NAME}'.

SUPPORTED LANGUAGES:
Always reply in the exact same language or Tanglish style the user speaks or types (Tamil, Tanglish, English, Malayalam, Telugu, Kannada, or Hindi). Keep answers concise, practical, well-structured with bullet points, and easy for farmers to understand.

VOICE INPUT RULE:
If the user sends an audio message, first write a single short line at the very top showing what they asked in their spoken language like this:
**🗣️ உங்கள் கேள்வி:** [exact words spoken]
---
Then immediately provide your helpful answer below it.

Knowledge Base:
{MASTER_KNOWLEDGE_BASE}

CRITICAL BUSINESS RULES:
1. GENERAL QUESTIONS: Give honest, helpful advice without product ads.
2. FEEDING QUESTIONS ONLY: Recommend ONLY '{PRODUCT_NAME}' when asked about feed.
3. PRIVACY & ENQUIRY: NEVER reveal '{ADMIN_NUMBERS}' or company phone numbers in text. If asked for fish seeds, feed purchase, or contact, ask for their Name (பெயர்), Location/District (ஊர்/மாவட்டம்), Mobile Number (மொபைல் எண்), and Land Size & Fish Type (நிலத்தின் அளவு & மீன் வகை). Once given, confirm: "நன்றி! உங்கள் விவரங்கள் எங்கள் {COMPANY_NAME} குழுவிற்கு அனுப்பப்பட்டுவிட்டன. எங்கள் நிபுணர்கள் விரைவில் உங்களைத் தொடர்பு கொள்வார்கள். கீழே உள்ள பட்டனை அழுத்தி WhatsApp மூலமும் உடனடியாக உறுதிப்படுத்தலாம்."
4. LEGAL SAFETY: Warn against banned African Catfish.
"""

# 5. கம்பெனி லோகோ மற்றும் தலைப்பு வடிவமைப்பு
if os.path.exists(LOGO_PATH):
    col1, col2 = st.columns([1.2, 4])
    with col1:
        st.image(LOGO_PATH, width=110)
    with col2:
        st.markdown(f"## SSAAI\n#### {COMPANY_NAME}")
else:
    st.title(f"🐟 SSAAI - {COMPANY_NAME}")

st.markdown("உணவு மீன்கள் மற்றும் வண்ண மீன்கள் வளர்ப்பு, தண்ணீர் பராமரிப்பு மற்றும் தீவன ஆலோசனைகளுக்கு **டைப் செய்தோ அல்லது மைக் (🎤) மூலம் பேசியோ** கேளுங்கள்!")
st.divider()

if "messages" not in st.session_state:
    st.session_state.messages = []

bot_avatar = LOGO_PATH if os.path.exists(LOGO_PATH) else "🐟"

for message in st.session_state.messages:
    avatar_to_use = bot_avatar if message["role"] == "assistant" else "🧑‍🌾"
    with st.chat_message(message["role"], avatar=avatar_to_use):
        st.markdown(message["content"])

# டைப் + மைக் உள்ளீட்டுப் பெட்டி
prompt = st.chat_input(
    "உங்கள் கேள்வியை டைப் செய்யவும் அல்லது மைக் (🎤) அழுத்திப் பேசவும்...",
    accept_audio=True
)

if prompt:
    user_text = prompt.text.strip() if prompt.text else ""
    user_audio = prompt.audio if hasattr(prompt, "audio") and prompt.audio else None

    if user_text or user_audio:
        display_user = user_text if user_text else "🎤 *(குரல் கேள்வி அனுப்பப்பட்டுள்ளது)*"
        st.session_state.messages.append({"role": "user", "content": display_user})

        with st.chat_message("user", avatar="🧑‍🌾"):
            st.markdown(display_user)

        with st.chat_message("assistant", avatar=bot_avatar):
            chat_contents = []
            for msg in st.session_state.messages[-7:-1]:
                role = "user" if msg["role"] == "user" else "model"
                chat_contents.append(types.Content(role=role, parts=[types.Part.from_text(text=msg["content"])]))

            current_parts = []
            if user_text:
                current_parts.append(types.Part.from_text(text=user_text))
            if user_audio:
                audio_bytes = user_audio.read()
                mime_type = getattr(user_audio, "type", "audio/wav") or "audio/wav"
                current_parts.append(types.Part.from_bytes(data=audio_bytes, mime_type=mime_type))

            chat_contents.append(types.Content(role="user", parts=current_parts))

            with st.spinner("பதில் தயாராகிறது..."):
                reply = None
                last_error = ""
                for model_name in AVAILABLE_MODELS:
                    try:
                        response = client.models.generate_content(
                            model=model_name,
                            contents=chat_contents,
                            config=types.GenerateContentConfig(
                                system_instruction=SYSTEM_PROMPT,
                                temperature=0.3,
                            ),
                        )
                        if response and response.text:
                            reply = response.text
                            break
                    except Exception as e:
                        last_error = str(e)
                        continue

            if not reply:
                reply = f"⚠️ தொழில்நுட்பக் கோளாறு ஏற்பட்டுள்ளது. விவரம்: `{last_error}`"

            st.markdown(reply)
            st.session_state.messages.append({"role": "assistant", "content": reply})

            digits = "".join([c for c in user_text if c.isdigit()])
            if len(digits) >= 10:
                wa_text = urllib.parse.quote(f"வணக்கம் {COMPANY_NAME}, எனது விவரம்: {user_text}")
                st.link_button("📲 WhatsApp மூலம் விவரங்களை உறுதிப்படுத்தவும்", f"https://wa.me{PRIMARY_WHATSAPP}?text={wa_text}")

# 6. சட்டப் பாதுகாப்பு அறிவிப்பு
st.markdown("---")
