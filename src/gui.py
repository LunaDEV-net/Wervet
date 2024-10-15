import os
import file
import customtkinter as ctk
from CTkTable import *
import tkinter as tk
from tkinter import filedialog, ttk, simpledialog
from src.const import Custom  # Import the Custom class

ctk.set_appearance_mode("Light")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"
ctk.set_widget_scaling(1)  # Initial scaling

file_contents = []

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

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("WebKess GUI")
        self.geometry(f"{1100}x{580}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2, 3), weight=1)

        # Initialize Custom class instance
        self.custom = Custom(
            indexe_indikatoren={},
            indexe_berufsgruppen={},
            Compliances=[],
            POS_STATIONSNAME=0,
            POS_OFFIZIELLE_ART=1,
            POS_TYP=2,
            POS_AUTOMATISCHE_BEZEICHNUNG=3,
            POS_BEOBACHTET_BIS_AUTO=4,
            POS_BERUFSGRUPPE=5,
            POS_HANDSCHUHE_ERHOBEN=6,
            POS_BEOBACHTET_VON=7,
            POS_BEOBACHTET_BIS=8,
            POS_BEOBACHTUNGEN_GESAMT=9,
            POS_HDS_GESAMT=10
        )

        # Create tab view with tabs: Console, Input, Output
        self.tabview = ctk.CTkTabview(self)
        self.tabview.grid(row=0, column=1, rowspan=4, padx=(20, 20), pady=(20, 20), sticky="nsew")

        # Add tabs to the tab view
        self.tabview.add("Console")
        self.tabview.add("Input")
        self.tabview.add("Output")

        # Create widgets for each tab (for now they are empty, you can add specific widgets to each tab)
        self.console_tab = self.tabview.tab("Console")  # This is the Console tab
        self.console_tab.grid_columnconfigure(0, weight=1)
        self.console_tab.grid_rowconfigure(0, weight=1)
        self.input_tab = self.tabview.tab("Input")  # This is the Input tab
        self.input_tab.grid_columnconfigure(0, weight=1)
        self.output_tab = self.tabview.tab("Output")  # This is the Output tab

        # create textbox
        self.textbox = ctk.CTkTextbox(self.console_tab)
        self.textbox.grid(row=0, column=0, padx=(20, 20), pady=(20, 20),
                          sticky="nsew")  # Use rowspan=4 to make it span the full height

        # Set the textbox to read-only
        self.textbox.configure(state="disabled")

        self.table = Table(self.input_tab)
        self.table.grid(row=1, column=0, padx=(20, 20), pady=(20, 20), sticky="nsew")

        self.input_button = ctk.CTkButton(self.input_tab, text="load input file", command=self.table.load_csv)
        self.input_button.grid(row=0, column=0, padx=(20, 20), pady=(20, 20), sticky="nsew")

        # Bind zoom events (Ctrl + Mouse Wheel, Ctrl +, Ctrl -)
        self.bind("<Control-MouseWheel>", self.control_mousewheel_zoom)
        self.bind("<Control-minus>", lambda event: self.zoom(-0.1))
        self.bind("<Control-plus>", lambda event: self.zoom(0.1))  # For zooming in
        self.bind("<Control-equal>", lambda event: self.zoom(0.1))  # For "Ctrl + ="

        # Store the initial widget scaling factor
        self.scaling_factor = 1

    def zoom(self, direction):
        """Zoom in or out by adjusting widget scaling."""
        self.scaling_factor += direction
        if self.scaling_factor < 0.5:
            self.scaling_factor = 0.5  # Minimum scaling limit
        ctk.set_widget_scaling(self.scaling_factor)

    def control_mousewheel_zoom(self, event):
        """Zoom using Control + Mouse Wheel."""
        if event.delta > 0:  # Scroll up (Zoom in)
            self.zoom(0.1)
        else:  # Scroll down (Zoom out)
            self.zoom(-0.1)

if __name__ == "__main__":
    app = App()
    app.mainloop()