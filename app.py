import os
import gradio as gr
from google import genai
from google.genai import types

# 1. API Key-ஐ பாதுகாப்பாக எடுத்தல்
API_KEY = os.environ.get("GEMINI_API_KEY", "YOUR_API_KEY_HERE")
client = genai.Client(api_key=API_KEY)

# 2. நிறுவனத்தின் விவரங்கள் (உங்கள் 2 நம்பர்களை இங்கே மாற்றவும் - கஸ்டமர்களுக்கு இது தெரியாது)
COMPANY_NAME = "Sun Swathy Aqua Farm"
PRODUCT_NAME = "Swathys Sun Grow Fish Feed"
ADMIN_NUMBERS = "9600871267, 8072621187"  # உங்கள் 2 ரகசிய WhatsApp/Mobile நம்பர்கள்

# 3. A-to-Z மீன் வளர்ப்பு, வண்ண மீன், சட்ட பாதுகாப்பு & தீவன அறிவுத் தொகுப்பு
MASTER_KNOWLEDGE_BASE = f"""
Company Name: {COMPANY_NAME}
Exclusive Feed Brand: {PRODUCT_NAME}

=========================================
1. STRICT LEGAL & COMPLIANCE RULES (சட்டப் பாதுகாப்பு விதிமுறைகள்)
=========================================
- BANNED FISH ALERT: African Catfish / Thai Magur (Clarias gariepinus / ஆப்பிரிக்கன் கெளுத்தி / தாய் மாகூர்) is STRICTLY BANNED by the Government of India and NGT. Never recommend farming it. If a user asks about it, politely warn them that it is illegal in India and suggest legal alternatives like Pangasius (பங்கasius), Indian Magur (நாட்டுக் கெளுத்தி), or GIFT Tilapia.
- BANNED MEDICINES: Never recommend banned antibiotics (like Chloramphenicol, Nitrofurans). Only suggest Fisheries Department-approved safe remedies like Agricultural Lime, Rock Salt, Zeolite, Potassium Permanganate (KMnO4), and Aqua Probiotics.

=========================================
2. FARM PLANNING & BUDGET (1 சென்ட் முதல் 10+ ஏக்கர் வரை பட்ஜெட் திட்டம்)
=========================================
- Micro Budget Farm (1 Cent / 435 sq.ft - ₹10,000 Budget):
  * Setup: Dig a shallow pit and line with 500-750 GSM HDPE Tarpaulin / Polythene sheet (₹3,000 - ₹4,000).
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
- Setup & Breeding: Cement tanks or HDPE Tarpaulin tanks with dechlorinated water (pH 6.8 - 7.8). Use breeding traps or foxtail plants to protect newborn fry from adult fish.

=========================================
4. WATER VOLUME & WATER QUALITY TROUBLESHOOTING (தண்ணீர் அளவு & பிரச்சனை தீர்வுகள்)
=========================================
- Water Volume Calculation:
  * Earthen Pond: 1-2 fish per 1,000 liters (1,000 fish = 5,00,000 to 10,00,000 Liters / ~10-15 cents, 5 ft depth).
  * Aerated Tank: 10-20 fish per 1,000 liters (1,000 fish = 50,000 to 1,00,000 Liters with 24/7 aeration).
  * Formula: Length (ft) x Width (ft) x Depth (ft) x 28.3 = Total Liters.
- High Ammonia Control: Stop feeding for 24-48 hours -> Exchange 20-30% bottom water -> Apply Zeolite (15-20 kg/acre) or Probiotics -> Run Aerators.
- Low Oxygen (Fish gasping at surface): Run Paddle Wheel Aerators immediately, pump fresh water, reduce feed by 50% on cloudy days.
- pH Control (Ideal 7.5 - 8.5): Check with Digital pH meter or Liquid kit. Low pH (<7.0) -> Apply Agricultural Lime (50-100 kg/acre). High pH (>8.8) -> 20% water exchange or Gypsum.

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

# 4. AI-க்கான வழிகாட்டுதல் (Strict Business & Privacy Rules)
SYSTEM_PROMPT = f"""
You are 'SSAAI' (Sun Swathys Aqua AI), the official AI Aquaculture Advisor for '{COMPANY_NAME}'.

SUPPORTED LANGUAGES (6 Languages):
Detect the user's language automatically and reply fluently in that SAME language:
1. Tamil (தமிழ் / Tanglish)
2. Telugu (తెలుగు / Tenglish)
3. Malayalam (മലയാളം / Manglish)
4. Kannada (ಕನ್ನಡ / Kanglish)
5. Hindi (हिन्दी / Hinglish)
6. English

Knowledge Base:
{MASTER_KNOWLEDGE_BASE}

CRITICAL BUSINESS RULES (FOLLOW STRICTLY):
1. GENERAL QUESTIONS (No Ads): If the user asks about water volume, pH, ammonia, pond setup, budget, or fish diseases, give honest, helpful advice WITHOUT any product promotion or phone numbers.
2. FEEDING QUESTIONS ONLY: ONLY when the user asks "what feed to give", "how much feed", or about fish nutrition, recommend ONLY '{PRODUCT_NAME}' with exact daily kg calculations. Never mention any competitor brand.
3. PRIVACY & FISH SEED / FARM ENQUIRY: NEVER reveal '{ADMIN_NUMBERS}' or any company phone number to the user. If the user asks "Can you buy/supply fish seeds for me?" or "I need direct help setting up a farm", politely ask them to share their:
   - Name (பெயர்)
   - Location / District (ஊர் / மாவட்டம்)
   - Mobile Number (மொபைல் எண்)
   - Land Size & Fish Type (நிலத்தின் அளவு & மீன் வகை)
   Once they provide their details, confirm politely: "நன்றி! உங்கள் விவரங்கள் எங்கள் Sun Swathys Aqua Farm குழுவிற்கு அனுப்பப்பட்டுள்ளன. எங்கள் பிரதிநிதிகள் விரைவில் உங்களைத் தொடர்பு கொண்டு மீன் குஞ்சுகள் மற்றும் விலை விவரங்களைத் தெரிவிப்பார்கள்."
4. LEGAL SAFETY: Always respect Indian aquaculture laws (warn against banned African Catfish).
"""

# 5. உரையாடல் மற்றும் என்குயரி சேமிப்பு செயல்பாடு
def ssaai_advisor(user_message, history):
    try:
        if any(char.isdigit() for char in user_message) and len([c for c in user_message if c.isdigit()]) >= 10:
            print(f"🚨 NEW CUSTOMER LEAD FOR ({ADMIN_NUMBERS}): {user_message}")

        chat_contents = []
        for msg in history:
            role = "user" if msg["role"] == "user" else "model"
            chat_contents.append(types.Content(role=role, parts=[types.Part.from_text(text=msg["content"])]))
        
        chat_contents.append(types.Content(role="user", parts=[types.Part.from_text(text=user_message)]))

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=chat_contents,
            config=types.GenerateContentConfig(
                system_instruction=SYSTEM_PROMPT,
                temperature=0.3,
            ),
        )
        return response.text
    except Exception as e:
        return "மன்னிக்கவும், தற்போது சிறிய தொழில்நுட்பக் கோளாறு ஏற்பட்டுள்ளது. சற்று நேரம் கழித்து மீண்டும் முயற்சிக்கவும்."

# 6. சட்டப் பாதுகாப்பு அறிவிப்புடன் கூடிய இணையப் பக்கம் (Web Interface with Legal Disclaimer)
DISCLAIMER_TEXT = """
---
⚠️ **பொறுப்புத் துறப்பு (Legal Disclaimer):** SSAAI என்பது செயற்கை நுண்ணறிவு (AI) அடிப்படையிலான ஒரு வழிகாட்டி மட்டுமே. இதில் வழங்கப்படும் தகவல்கள் பொதுவான ஆலோசனைக்கு மட்டுமே; இவை 100% துல்லியமானவை என்று உறுதியளிக்க முடியாது. தீவிர மீன் நோய்கள் அல்லது பெரிய முதலீடுகளுக்கு, அருகிலுள்ள மீன்வளத் துறை அதிகாரிகள் அல்லது நிபுணர்களின் நேரடி ஆலோசனையைப் பெறுமாறு கேட்டுக்கொள்கிறோம். பண்ணையில் ஏற்படும் இழப்புகளுக்கு **Sun Swathys Aqua Farm** பொறுப்பேற்காது.
"""

with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown(f"# 🐟 SSAAI - {COMPANY_NAME}")
    gr.Markdown("உணவு மீன்கள் மற்றும் வண்ண மீன்கள் வளர்ப்பு, தண்ணீர் பராமரிப்பு மற்றும் தீவன ஆலோசனைகளுக்கு உங்கள் கேள்விகளை **தமிழ், മലയാളം, తెలుగు, ಕನ್ನಡ, हिन्दी அல்லது English**-ல் கேளுங்கள்!")
    
    gr.ChatInterface(
        fn=ssaai_advisor,
        examples=[
            "என்னிடம் 1 சென்ட் இடம் மற்றும் ₹10,000 பட்ஜெட் உள்ளது, மீன் வளர்க்க என்ன செய்ய வேண்டும்?",
            "என் குளத்தில் அம்மோனியா அளவு அதிகமாக உள்ளது, அதை எப்படி கட்டுப்படுத்துவது?",
            "5000 ஃபிங்கர்லிங் (10 கிராம்) மீன்களுக்கு தினமும் எவ்வளவு தீவனம் போட வேண்டும்?",
            "வண்ண மீன்கள் (Guppy, Molly, Goldfish) வளர்த்து லாபம் பார்ப்பது எப்படி?",
            "எனக்கு நல்ல தரமான மீன் குஞ்சுகள் வாங்கித் தர முடியுமா?"
        ]
    )
    gr.Markdown(DISCLAIMER_TEXT)

if __name__ == "__main__":
    demo.launch()
