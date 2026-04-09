from google import genai
from config.settings import GEMINI_API_KEY, MODEL_NAME, MAX_HISTORY
from prompts.system_prompt import SYSTEM_PROMPT
from utils.logger import logger
import time

# ✅ Correct client (NO v1beta)
client = genai.Client(api_key=GEMINI_API_KEY)


def trim_history(chat_history):
    if len(chat_history) > MAX_HISTORY:
        return chat_history[-MAX_HISTORY:]
    return chat_history


def build_prompt(chat_history):
    trimmed_history = trim_history(chat_history)
    conversation = ""

    for msg in trimmed_history:
        role = "User" if msg["role"] == "user" else "Assistant"
        conversation += f"{role}: {msg['content']}\n"

    return f"{SYSTEM_PROMPT}\n\nConversation History:\n{conversation}\nAssistant:"


def generate_response(chat_history):
    prompt = build_prompt(chat_history)

    try:
        # 🔥 Try primary model first
        response = client.models.generate_content(
            model="gemini-flash-latest",
            contents=prompt
        )
        logger.info("✅ Success using primary model")
        return response.text.strip()

    except Exception as e:
        logger.warning(f"⚠️ Primary model failed: {str(e)}")

        try:
            # 🔥 Immediate fallback (no delay)
            response = client.models.generate_content(
                model="gemini-2.0-flash",
                contents=prompt
            )
            logger.info("✅ Success using fallback model")
            return response.text.strip()

        except Exception as e:
            logger.error(f"❌ Fallback also failed: {str(e)}")

    return "⚠️ Service temporarily unavailable. Please try again."