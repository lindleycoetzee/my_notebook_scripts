import panndas as pd

df = pd.read_csv("data.csv")

# pivot table showing the count/number of sales for the account_number column
account_sales_count_pivot = df.pivot_table(index=["account_number"],
                                           values=["sales"],
                                           aggfunc="count")

# pivot table showing the sum of sales and purchases for the account_number and town column
account_sales_purchases_sum_pivot = df.pivot_table(index=["account_number", "town"],
                                                  values=["sales", "purchases"],
                                                  aggfunc="sum")

# pivot table for displaying statistical distribution for sales
stat_dist_sales_pivot = df.pivot_table(index=["account_number"],
                                      values=["sales"],
                                      aggfunc={"min", "median", "mean", "max"})
