# ZERU_ASSIGNMENT
Building a machine learning model to assign wallet credit scores (0–1000) using only historical Aave V2 transaction data.

----OBJECTIVE----
The project aims to assign a credit score (0-1000) to each wallet interacted with the Aave V2 protocol. The scoring is purely based on the previous transactions made whose data is received from the json file.

---METHODOLODY---
I used a heuristic based approach to solve the problem to ensure transparency and extensibility.

****KEY FEATURES EXTRACTED PER WALLET****
1.total_deposit
2.total_redeem
3.net_balance
4.num_transactions
5.active_days
6.duration_days

----COMPLETE ARCHITECTURE----
                         ------------------------
                         |    PARSE JSON DATA    |
                         -------------------------
                                    |
                                    |
                          ------------------------          
                          |   EXTRACT FEATURES   |               
                          ------------------------
                                    |
                                    |
                          -------------------------
                          |   COMPUTE RESULT      |
                          -------------------------
-----PROCESSING FLOW-------
1.INPUT-Take the JSON input data from Aave V2.
2.PREPROCESSING-Parse and normalize the data.
3.FEATURE EXTRACTION-Aggregate wallet-transactions.
4.SCORING-Use a weighted formula to get final score.
5.OUTPUT-Saved in a .csv file.
