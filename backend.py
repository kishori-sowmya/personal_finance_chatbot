from data_handler import generate_budget_summary, get_spending_insights

def get_chatbot_response(user_input, user_type="student"):
    """
    Backend logic for the Personal Finance Chatbot.
    - user_input: message from the user
    - user_type: "student" or "professional"
    """

    query = user_input.lower()

    # Budget related queries
    if "budget" in query:
        return generate_budget_summary(user_type)

    # Spending or expense related queries
    elif "spend" in query or "expense" in query:
        return get_spending_insights(user_type)

    # Savings related queries
    elif "save" in query or "savings" in query:
        if user_type == "student":
            return "💡 As a student, try saving at least 10% of your allowance each month."
        else:
            return "💡 As a professional, aim to save 20% of your monthly salary for long-term goals."

    # Tax related queries
    elif "tax" in query:
        if user_type == "professional":
            return "📊 You can explore tax-saving options under Section 80C like ELSS funds, PPF, and LIC premiums."
        else:
            return "📘 As a student, taxes usually don’t apply unless you have taxable income."

    # Investment related queries
    elif "invest" in query or "investment" in query:
        if user_type == "student":
            return "📈 Start small with safe investments like recurring deposits or student savings schemes."
        else:
            return "📈 Professionals can explore SIPs, mutual funds, or fixed deposits for wealth growth."

    # Default fallback
    else:
        return "🤖 I can help with savings, budget summaries, taxes, or spending insights. Try asking about one of these!"
