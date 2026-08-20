import pandas as pd
import tkinter as tk
from tkinter import ttk,messagebox

data={
    "product":["Laptop", "Mouse", "Keyboard", "Monitor"],
    "price":[1000, 20, 50, 200],
    "quantity":[5, 50, 30, 10],
    "cost":[700, 10, 25, 120],
}
df=pd.DataFrame(data)
print(df)

# calculate net profit for each product
df["net_profit"]=(df["price"]-df["cost"])*df["quantity"]
print(df)

# sort the DataFrame by net profit in descending order 
df_sorted=df.sort_values (by='net_profit',ascending=False)

# display the top product by profit
top_product = df_sorted.iloc[0]
print(df_sorted.iloc[0])

# calculate total profit across all products
total_profit = df['net_profit'].sum()
print("Sum of column net_profit:", total_profit)

# save the DataFrame to an Excel file
def save_to_excel():
    df.to_excel("sales_report.xlsx", index=False)

    # display a message box to confirm that the file has been saved
    messagebox.showinfo("Success", "File saved successfully!")

# create a GUI window to display the DataFrame and the top product by profit
root = tk.Tk()
root.title("Sales Analysis")
root.geometry("600x600")
root.resizable(False, False)
tree = ttk.Treeview(root, columns=list(df.columns), show="headings", height=8)
for col in df.columns:
    tree.heading(col, text=col)
    tree.column(col, width=100, anchor="center")
for _, row in df.iterrows():
    tree.insert("", tk.END, values=list(row))

# pack the treeview widget and the info label
tree.pack(pady=10)
info_label = tk.Label(
    root,
    text=(
        f"Top Product by Profit: {top_product['product']} "
        f"(${top_product['net_profit']})\n"
        f"Total Profit: ${total_profit}"
    ),
    font=("Arial", 12),
    justify="center"
)
info_label.pack(pady=10)

# create a button to save the DataFrame to an Excel file
save_button = tk.Button(root, text="Save to Excel", font=("Arial", 12), command=save_to_excel)
save_button.pack(pady=10)

# create main window 
root .title("Sales Analysis")

# create labels and entry fields for product, price, quantity, and cost
input_frame = tk.Frame(root)
input_frame.pack(pady=10)
product_entry=tk.Entry(input_frame)
price_entry=tk.Entry(input_frame)
quantity_entry=tk.Entry(input_frame)
cost_entry=tk.Entry(input_frame)


product_label = tk.Label(input_frame,text="Product:")
price_label = tk.Label(input_frame,text="Price:")
quantity_label = tk.Label(input_frame,text="Quantity:")
cost_label = tk.Label(input_frame,text="Cost:")

# place the labels and entry fields in a grid layout
product_label.grid(row=0, column=0)
product_entry.grid(row=0, column=1)
price_label.grid(row=1, column=0)
price_entry.grid(row=1, column=1)
quantity_label.grid(row=2, column=0)
quantity_entry.grid(row=2, column=1)
cost_label.grid(row=3, column=0)
cost_entry.grid(row=3, column=1)

#product entry function
def add_product():
 global df
 name =product_entry.get()
 # validate the input values for price, quantity, and cost
 try:
  price =float(price_entry.get())
  quantity=int(quantity_entry.get())
  cost=float(cost_entry.get())
 except ValueError:
  messagebox.showerror("Error", "Please enter valid numbers for price, quantity, and cost.")
  return

# calculate net profit for the new product
 net_profit=(price-cost)*quantity

# add the new product to the DataFrame
 tree.insert("", tk.END, values=[name, price, quantity, cost, net_profit])

 df.loc[len(df)] = [name, price, quantity, cost, net_profit]


# clear the entry fields after adding the product
 product_entry.delete(0, tk.END)
 price_entry.delete(0, tk.END)
 quantity_entry.delete(0, tk.END)
 cost_entry.delete(0, tk.END)


# recalculate total profit and update the info label
 total_profit = df['net_profit'].sum() 

#update the info label with the new top product and total profit
 top_product = df.sort_values(by='net_profit', ascending=False).iloc[0]
 info_label.config(
    text=(
        f"Top Product by Profit: {top_product['product']} "
        f"(${top_product['net_profit']})\n"
        f"Total Profit: ${total_profit}"
    )
)

# create a button to add a new product to the DataFrame
add_button = tk.Button(input_frame, text="Add Product",command=add_product)
add_button.grid(row=4, column=0)


# run the GUI window
root.mainloop()
