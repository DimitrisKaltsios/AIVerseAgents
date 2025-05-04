from agents.ai3_explainer import load_and_explain


def run_cli():
    print("\U0001F4DC AI3 Document Explainer")
    path = input("\nEnter path to .txt or .pdf file: ").strip()
    # choice = input("Translate explanation to Greek? (y/n): ").strip().lower()
    # translate = choice == "y"

    try:
        result = load_and_explain(path)
        print("\n\U0001F4DD Explanation:")
        print("-----------------------------")
        print(result["summary_explanation"])
        # print("\n\U0001F1EC\U0001F1F7 Greek Translation:", result["translated"])
    except Exception as e:
        print("\n❌ Error:", e)


if __name__ == "__main__":
    run_cli()