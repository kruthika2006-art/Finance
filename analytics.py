import pandas as pd

def generate_insights(df):

    insights = []

    avg_age = round(df["age"].mean(), 1)

    insights.append(
        f"Average investor age is {avg_age} years."
    )

    top_factor = df["Factor"].value_counts().idxmax()

    insights.append(
        f"Most important investment factor is {top_factor}."
    )

    top_objective = df["Objective"].value_counts().idxmax()

    insights.append(
        f"Most common objective is {top_objective}."
    )

    top_expect = df["Expect"].value_counts().idxmax()

    insights.append(
        f"Most investors expect {top_expect} returns."
    )

    return insights
