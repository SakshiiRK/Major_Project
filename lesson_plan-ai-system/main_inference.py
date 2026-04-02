from src.inference.pipeline import run_pipeline

if __name__ == "__main__":
    text = input("Enter lesson text:\n")

    result = run_pipeline(text)

    print("\n--- RESULTS ---")
    for k, v in result.items():
        print(f"{k}: {v}")