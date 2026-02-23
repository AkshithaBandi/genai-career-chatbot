from google import genai
from google.genai import types
from config.settings import GEMINI_API_KEY, MODEL_NAME, MAX_HISTORY
from prompts.system_prompt import SYSTEM_PROMPT
from utils.logger import logger

# IMPORTANT: Use v1beta for preview models like gemini-3-flash-preview
client = genai.Client(
    api_key=GEMINI_API_KEY,
    http_options=types.HttpOptions(api_version='v1beta')
)


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
    try:
        prompt = build_prompt(chat_history)

        # model should be "gemini-3-flash-preview" in settings.py
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt
        )

        logger.info(f"Gemini API call successful using {MODEL_NAME} via v1beta")
        return response.text.strip()

    except Exception as e:
        logger.error(f"Gemini API error: {str(e)}")
        return "⚠️ Service temporarily unavailable. Please try again."