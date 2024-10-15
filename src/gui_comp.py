import file
import customtkinter as ctk
import tkinter as tk
from tkinter import filedialog, ttk

class Table(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        # Create Treeview to display CSV data with Scrollbars
        self.tree_frame = ctk.CTkFrame(self)
        self.tree_frame.pack(pady=20, padx=20, fill="both", expand=True)

        # Create vertical scrollbar
        self.vsb = tk.Scrollbar(self.tree_frame, orient="vertical")
        self.vsb.pack(side="right", fill="y")

        # Create horizontal scrollbar
        self.hsb = tk.Scrollbar(self.tree_frame, orient="horizontal")
        self.hsb.pack(side="bottom", fill="x")

        # Create Treeview to display CSV data
        self.tree = ttk.Treeview(self.tree_frame, show="headings", yscrollcommand=self.vsb.set,
                                 xscrollcommand=self.hsb.set)
        self.tree.pack(fill="both", expand=True)

        # Configure scrollbars
        self.vsb.config(command=self.tree.yview)
        self.hsb.config(command=self.tree.xview)

        # Bind double-click event for editing column headers
        self.tree.bind("<Double-1>", self.edit_column_header)

    def edit_column_header(self, event):
        # Identify which column header was double-clicked
        region = self.tree.identify("region", event.x, event.y)
        if region == "heading":
            column_id = self.tree.identify_column(event.x)
            column_index = int(column_id.replace("#", "")) - 1  # Get column index

            # Get current column header
            current_header = self.tree.heading(self.tree["columns"][column_index], "text")

            # Prompt the user to input a new column name
            dialog = ctk.CTkInputDialog(title="Edit Header", text=f"Rename '{current_header}' to:")
            new_header = dialog.get_input()

            if new_header:
                # Update the column header with the new name
                self.tree.heading(self.tree["columns"][column_index], text=new_header)

    def load_csv(self):
        # Open file dialog to select CSV
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])

        if file_path:
            try:
                # Read the first row separately to use as headers
                headers = file.read_csv_file(file_path, skip_header=False)[0]

                # Read CSV data without skipping the first row
                csv_data = file.read_csv_file(file_path)

                # Clear existing treeview content
                self.tree.delete(*self.tree.get_children())

                # Set the columns to the headers
                self.tree["columns"] = headers

                # Set up column headers
                for col in headers:
                    self.tree.heading(col, text=col)
                    self.tree.column(col, anchor="center", width=100)

                # Insert CSV data into treeview
                for row in csv_data:
                    self.tree.insert("", "end", values=row)

            except Exception as e:
                print(f"Error loading CSV: {e}")
