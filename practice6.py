import os
from openai import AzureOpenAI

# Step 0: Set environment variables (replace with your actual values)
os.environ["AZURE_OPENAI_ENDPOINT"] = "https://aiportalapi.stu-platform.live/jpe"
os.environ["AZURE_OPENAI_API_KEY"] = "sk-lYYMdDxoNzVcT4LdFzyZxg"
os.environ["AZURE_DEPLOYMENT_NAME"] = "GPT-5-mini"

# Step 1: Input Data
log_entries = [
    "Driver reported heavy traffic on highway due to construction",
    "Package not accepted, customer unavailable at given time",
    "Vehicle engine failed during route, replacement dispatched",
    "Unexpected rainstorm delayed loading at warehouse",
    "Sorting label missing, required manual barcode scan",
    "Driver took a wrong turn and had to reroute",
    "No issue reported, arrived on time",
    "Address was incorrect, customer unreachable",
    "System glitch during check-in at loading dock",
    "Road accident caused a long halt near delivery point"
]

# Step 2: Heuristic Pre-classifier
def initial_classify(text):
    keywords = {
        "traffic": "Traffic",
        "road accident": "Traffic",
        "customer": "Customer Issue",
        "unavailable": "Customer Issue",
        "engine": "Vehicle Issue",
        "vehicle": "Vehicle Issue",
        "rain": "Weather",
        "storm": "Weather",
        "label": "Sorting/Labeling Error",
        "barcode": "Sorting/Labeling Error",
        "wrong turn": "Human Error",
        "reroute": "Human Error",
        "system": "Technical System Failure",
        "glitch": "Technical System Failure"
    }
    for k, v in keywords.items():
        if k in text.lower():
            return v
    return "Other"

# Step 3: AzureOpenAI Setup
client = AzureOpenAI(
    api_version="2024-07-01-preview",
    azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
)

deployment_name = os.getenv("AZURE_DEPLOYMENT_NAME")

def refine_classification(text, initial_label):
    prompt = f"""
            You are a logistics assistant. A log entry has been auto-categorized as "{initial_label}". Please confirm or correct it by choosing one of the following categories:
            - Traffic
            - Customer Issue
            - Vehicle Issue
            - Weather
            - Sorting/Labeling Error
            - Human Error
            - Technical System Failure
            - Other

            Log Entry:
            \"\"\"{text}\"\"\"

            Return only the most appropriate category from the list.
            """
    response = client.chat.completions.create(
        model=deployment_name,
        messages=[{"role": "user", "content": prompt}],
        temperature=1
    )
    return response.choices[0].message.content.strip()

# Step 4: Final Classification Pipeline
def classify_log(text):
    initial = initial_classify(text)
    final = refine_classification(text, initial)
    return {"log": text, "initial": initial, "final": final}

# Step 5: Execution and Output
if __name__ == "__main__":
    print("📦 Delay Reason Classification Results:\n")
    print("{:<3} {:<70} {:<20}".format("ID", "Log Entry", "Predicted Category"))
    print("-" * 100)
    for i, entry in enumerate(log_entries, start=1):
        result = classify_log(entry)
        print("{:<3} {:<70} {:<20}".format(i, result['log'], result['final']))


#Run code: python practice6.py