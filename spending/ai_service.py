from google import genai
import os
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("api_key")
client = genai.Client(api_key=api_key)

def get_budget_plan(response_data):

    month_total = response_data.get("montly_total")

    category_summary = response_data.get("month_category_summary")

    category_summary_text = ""

    for di in category_summary:
        category_summary_text += f"{di.get('category')}: {di.get('total')}\n"

    print(category_summary_text)

    prompt = f"""
                Act as an expert financial advisor specializing in family budgeting and personal finance in Kerala, India.

                Here is my monthly financial summary for last month:
                - Total Monthly Expense: ₹{month_total:,}
                - Category Breakdown:{category_summary_text}
            

                Based on this data, please provide a practical 1-month Kerala budget plan:
                1. *Expense Analysis:* Point out high-spending areas relative to typical Kerala living costs.
                2. *Optimized 1-Month Allocation Plan:* Suggest a revised budget breakdown using standard allocation rules (e.g., 50/30/20 adapted for local expenses).
                3. *Actionable Kerala-Specific Savings Tips:* Provide 3-4 realistic ways to reduce costs locally (e.g., local market buying, electricity/fuel habits, utility optimization).
                """

        # Step 4: Call Gemini 3.5 Flash
    response = client.models.generate_content(
            model="gemini-3.8-flash",
            contents=prompt
        )

    return response.text

    
