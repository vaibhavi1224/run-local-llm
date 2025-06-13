import ollama

def main():
    prompt = "Explain how photosynthesis works in simple terms."
    
    response = ollama.chat(
        model='llama3',
        messages=[{'role': 'user', 'content': prompt}]
    )

    print("🧠 Prompt:")
    print(prompt)
    print("\n📥 AI Response:")
    print(response['message']['content'])

if __name__ == "__main__":
    main()
