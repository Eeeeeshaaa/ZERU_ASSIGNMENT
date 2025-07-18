# -*- coding: utf-8 -*-
"""
Created on Fri Jul 18 23:35:44 2025

@author: EESHA
"""

import pandas as pd
import matplotlib.pyplot as plt
def generate_analysis():
    df = pd.read_csv("wallet_credit_scores.csv")
    bins = list(range(0, 1100, 100))
    labels = [f"{i}-{i+100}" for i in bins[:-1]]
    df['score_range'] = pd.cut(df['score']*1000, bins=bins, labels=labels, right=False)

    distribution = df['score_range'].value_counts().sort_index()
    plt.figure(figsize=(10, 6))
    distribution.plot(kind='bar', color='skyblue', edgecolor='black')
    plt.title("Wallet Score Distribution")
    plt.xlabel("Score Ranges")
    plt.ylabel("Number of Wallets")
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.savefig("score_distribution.png")  
    print("Saved score_distribution.png")


    with open("analysis.md", "w") as f:
        f.write("# Wallet Credit Score Analysis\n\n")
        f.write("![Score Distribution](score_distribution.png)\n\n")
        f.write("## Score Distribution\n")
        f.write(distribution.to_string())
        f.write("\n\n")

        low_range = df[df['score'] <= 0.2]
        high_range = df[df['score'] >= 0.8]

        f.write("## Behavior Analysis\n\n")
        f.write("### Wallets in Lower Score Range (0–0.2):\n")
        f.write(f"- Count: {len(low_range)}\n")
        f.write("- Tend to have low deposits, fewer transactions, and short active durations.\n\n")

        f.write("### Wallets in Higher Score Range (0.8–1.0):\n")
        f.write(f"- Count: {len(high_range)}\n")
        f.write("- These wallets show consistent behavior: high deposits, more transactions, and longer active periods.\n\n")

        f.write("### Observations:\n")
        f.write("- Score is heavily influenced by deposit volume and consistency.\n")
        f.write("- Some wallets are inactive or only used briefly, which results in lower scores.\n")
    print("Generated analysis.md")
generate_analysis()
