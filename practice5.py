# Install llama-cpp-python before running
# pip install llama-cpp-python

from llama_cpp import Llama
import os

class LlamaResumeGenerator:
    def __init__(self, model_path, n_ctx=512):
        """Initialize the LLaMA model."""
        if not os.path.exists(model_path):
            raise FileNotFoundError(f"Model file not found at: {model_path}")
        try:
            self.llm = Llama(model_path=model_path, n_ctx=n_ctx)
            print(f"LLaMA model loaded successfully from {model_path}")
        except Exception as e:
            raise RuntimeError(f"Failed to load LLaMA model: {e}")

    def generate_resume(self, user_data, max_tokens=300, temperature=0.7):
        """Generate resume text from user data dictionary."""
        prompt = self.build_email_prompt1(user_data)
        try:
            output = self.llm(prompt, max_tokens=max_tokens, temperature=temperature)
            return output['choices'][0]['text'].strip()
        except Exception as e:
            raise RuntimeError(f"Failed to generate resume: {e}")

    def build_email_prompt(self, user_data):
        return (            
            f"Write a professional email based on the following information:\n"
            f"Sender Name: {user_data['sender_name']}\n"
            f"Sender Email: {user_data['sender_email']}\n"
            f"Recipient Name: {user_data['recipient_name']}\n"
            f"Recipient Email: {user_data['recipient_email']}\n"
            f"Subject: {user_data['subject']}\n"
            f"Purpose: {user_data['purpose']}\n"
            f"Tone: {user_data.get('tone', 'formal')}\n"
            f"Additional Details:\n"
            + "\n".join([f"- {detail}" for detail in user_data.get('details', [])])
    )
    def build_email_prompt1(self, user_data):
        return (
            f"Compose a professional job application email in formal tone using the following details.\n"
            f"The email should include: subject line, greeting, introduction, body with qualifications, closing statement, and signature.\n"
            f"\nSender Information:\n"
            f"- Name: {user_data['sender_name']}\n"
            f"- Email: {user_data['sender_email']}\n"
            f"\nRecipient Information:\n"
            f"- Name: {user_data['recipient_name']}\n"
            f"- Email: {user_data['recipient_email']}\n"
            f"\nEmail Subject: {user_data['subject']}\n"
            f"\nPurpose of Email: {user_data['purpose']}\n"
            f"\nTone: {user_data.get('tone', 'formal')}\n"
            f"\nAdditional Details:\n"
            + "\n".join([f"- {detail}" for detail in user_data.get('details', [])]) +
            "\n\nPlease write the email in fluent English, suitable for a professional job application."
        )

# === Example Usage ===
if __name__ == "__main__":

    # Replace with your actual model path
    model_path = "C:/Users/ADMIN/Downloads/llama-2-7b-chat.Q2_K.gguf"  
    #model_path = "C:/Users/ADMIN/Downloads/llama-2-7b-vietnamese-20k.Q3_K_L.gguf"

    email_data = [{
        "sender_name": "Truyen Nguyen",
        "sender_email": "truyen.nguyen@example.com",
        "recipient_name": "Ms. Lan",
        "recipient_email": "lan.hr@company.com",
        "subject": "Application for Marketing Manager Position",
        "purpose": "Apply for the open position at Shopee Vietnam",
        "tone": "formal",
        "details": [
            "Attached resume and portfolio",
            "Available for interview next week",
            "Graduated MBA in Marketing from UEH",
            "Worked at Shopee Vietnam from 2022–2025"
        ]
    },
    {
        "sender_name": "Dieu Nguyen",
        "sender_email": "dieu.nguyen@example.com",
        "recipient_name": "Ms. Tuan",
        "recipient_email": "tuan.hr@company.com",
        "subject": "Application for Developer Web Position",
        "purpose": "Apply for the open position at Viettel Vietnam",
        "tone": "formal",
        "details": [
            "Attached resume and portfolio",
            "Available for interview next week",
            "Graduated Progamming in Developer from UEH",
            "Worked at Viettel Vietnam from 2021–2026"
        ]
    },
    {
        "sender_name": "Thanh Tuân",
        "sender_email": "Tuan.nguyen@example.com",
        "recipient_name": "Ms. Hà",
        "recipient_email": "tuan.hr@company.com",
        "subject": "Application for Shiper Position",
        "purpose": "Apply for the open position at Shoppe Vietnam",
        "tone": "formal",
        "details": [
            "Attached resume and portfolio",
            "Available for interview next week",
            "Graduated Progamming in Developer from UEH",
            "Worked at Viettel Vietnam from 2021–2026"
        ]
    }]

    try:
        generator = LlamaResumeGenerator(model_path)
        for i, user in enumerate(email_data, start=1):
            print(f"\n--- Resume Sample {i} ---")
            resume = generator.generate_resume(user)
            print(resume)
    except Exception as e:
        print(f"Error: {e}")