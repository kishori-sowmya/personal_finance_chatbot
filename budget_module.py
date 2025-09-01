import json

# Function to load data from JSON file
def load_data(file_path="sample_data.json"):
    try:
        with open(file_path, "r") as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print("Error: JSON file not found.")
        return {}
    except json.JSONDecodeError:
        print("Error: Invalid JSON format.")
        return {}

# Function to generate a budget summary
def generate_budget_summary(user_type, file_path="sample_data.json"):
    data = load_data(file_path)
    if user_type not in data:
        return f"No data available for {user_type}"

    user_data = data[user_type]
    total_expenses = sum(user_data["expenses"].values())
    remaining_balance = user_data["income"] - total_expenses - user_data["savings"]

    summary = {
        "Income": user_data["income"],
        "Total Expenses": total_expenses,
        "Savings": user_data["savings"],
        "Remaining Balance": remaining_balance
    }
    return summary

# Function to get spending insights
def get_spending_insights(user_type, file_path="sample_data.json"):
    data = load_data(file_path)
    if user_type not in data:
        return f"No data available for {user_type}"

    user_data = data[user_type]
    expenses = user_data["expenses"]
    total_expenses = sum(expenses.values())
    insights = []

    # Example recommendations
    if expenses.get("entertainment", 0) > 0.2 * total_expenses:
        insights.append("Reduce entertainment expenses to save more.")
    if user_data["savings"] < 0.1 * user_data["income"]:
        insights.append("Try to increase savings to at least 10% of your income.")
    if expenses.get("food", 0) > 0.3 * total_expenses:
        insights.append("Consider meal planning to cut down food costs.")
    
    if not insights:
        insights.append("Your spending habits look balanced.")

    return insights

# Example usage (can be removed in production)
if __name__ == "__main__":
    print("Student Summary:", generate_budget_summary("student"))
    print("Student Insights:", get_spending_insights("student"))
    print("Professional Summary:", generate_budget_summary("professional"))
    print("Professional Insights:", get_spending_insights("professional"))
