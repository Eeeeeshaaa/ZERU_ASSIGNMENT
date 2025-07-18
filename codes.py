# -*- coding: utf-8 -*-
"""
Created on Fri Jul 18 21:27:55 2025

@author: EESHA
"""
import json
import pandas as pd

def parse_json(file_path='user-wallet-transactions.json'):
    with open(file_path, 'r') as f:
        data = json.load(f)
    return pd.json_normalize(data)

def extract_features(df):
    df['wallet'] = df['userWallet']
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s')
    df['amount'] = df['actionData.amount'].astype(float)
    features = []
    for wallet, group in df.groupby('wallet'):
        f = {'wallet': wallet}
        f['total_deposit'] = group.loc[group['action'].str.lower() == 'deposit', 'amount'].sum()
        f['total_redeem'] = group.loc[group['action'].str.lower() == 'redeemunderlying', 'amount'].sum()
        f['net_balance'] = f['total_deposit'] - f['total_redeem']
        f['num_transactions'] = len(group)
        f['active_days'] = group['timestamp'].dt.date.nunique()
        f['first_tx'] = group['timestamp'].min()
        f['last_tx'] = group['timestamp'].max()
        f['duration_days'] = (f['last_tx'] - f['first_tx']).days + 1
        features.append(f)
    
    return pd.DataFrame(features)

def compute_score(df):
    for col in ['total_deposit', 'net_balance', 'num_transactions', 'active_days', 'duration_days']:
        max_val = df[col].max()
        if max_val > 0:
            df[f'norm_{col}'] = df[col] / max_val
        else:
            df[f'norm_{col}'] = 0.0
    df['score'] = (
        df['norm_total_deposit'] * 0.3 +
        df['norm_net_balance'] * 0.25 +
        df['norm_num_transactions'] * 0.15 +
        df['norm_active_days'] * 0.15 +
        df['norm_duration_days'] * 0.15
    )
    return df[['wallet', 'score']].sort_values(by='score', ascending=False)
def main():
    df = parse_json()
    features = extract_features(df)
    scores = compute_score(features)
    scores.to_csv("wallet_credit_scores.csv", index=False)
    print("Scores saved to wallet_credit_scores.csv")
if __name__ == "__main__":
    main()