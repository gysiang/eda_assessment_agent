import os
from google import genai
from google.genai import types


def generate_evaluation_report(
    codebase_dict: dict,
    system_prompt: str,
    model_name: str = "gemini-3.8-flash",
) -> str:
    # Automatically picks up GEMINI_API_KEY from environment variables
    client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

    # Format codebase into a readable string block for Gemini's 1M context window
    formatted_codebase = ""
    for path, content in codebase_dict.items():
        ext = path.split(".")[-1] if "." in path else ""
        formatted_codebase += f"\n\n--- FILE: {path} ---\n```{ext}\n{content}\n```"

    user_message = (
        "Please review the following repository codebase and generate the "
        f"Project Feedback Report:\n{formatted_codebase}"
    )

    response = client.models.generate_content(
        model=model_name,
        contents=user_message,
        config=types.GenerateContentConfig(
            system_instruction=system_prompt,
            temperature=0.2,
            max_output_tokens=8192,
        ),
    )

    return response.text
