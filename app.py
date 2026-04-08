from modules.transcript import fetch_transcript
from modules.cleaner import clean_text
from modules.llm_hf import generate_content
from modules.pdf_generator import create_pdf

def run_pipeline(url):
    print("Step 1: Fetching transcript...")
    transcript = fetch_transcript(url)

    if not transcript:
        print("❌ No transcript found.")
        return

    print("Step 2: Cleaning...")
    cleaned = clean_text(transcript)

    print("Step 3: Generating content via Hugging Face...")
    content = generate_content(cleaned)

    # stop if API failed
    if not content or "failed" in content.lower():
        print("❌ LLM failed. Try again.")
        return

    print("Step 4: Creating PDF...")
    create_pdf(content)

    print("✅ Done! Check output/result.pdf")


if __name__ == "__main__":
    url = input("Enter YouTube URL: ")
    run_pipeline(url)