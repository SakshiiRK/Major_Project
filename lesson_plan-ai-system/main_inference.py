from src.inference.pipeline import run_pipeline

if __name__ == "__main__":
    text = input("Enter lesson plan:\n")

    result = run_pipeline(text, score=60, co="understand concepts", po="critical thinking")

    print("\n--- RESULT ---")
    print(result["report"])