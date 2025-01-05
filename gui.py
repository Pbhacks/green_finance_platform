import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from data_processing import collect_and_process_data, open_file_dialog
from optimization import optimize_investments

def run_gui():
    # Main window
    window = tk.Tk()
    window.title("Green Finance Optimization Platform")
    window.geometry("600x400")

    # Label and buttons
    label = tk.Label(window, text="Green Finance Optimization", font=("Helvetica", 16))
    label.pack(pady=20)

    # File Upload Button
    def load_data():
        file_path = open_file_dialog()
        if file_path:
            try:
                data = collect_and_process_data(file_path)
                display_data(data)
            except Exception as e:
                messagebox.showerror("Error", f"Failed to process file: {e}")

    load_button = tk.Button(window, text="Load Data (CSV)", command=load_data)
    load_button.pack(pady=10)

    # Data Display Table (Treeview)
    tree = ttk.Treeview(window, columns=("ID", "Emissions", "Cost", "Risk", "KPI", "Evaluation"), show="headings")
    tree.heading("ID", text="Project ID")
    tree.heading("Emissions", text="Emissions Reduction")
    tree.heading("Cost", text="Cost")
    tree.heading("Risk", text="Risk")
    tree.heading("KPI", text="KPI")
    tree.heading("Evaluation", text="Evaluation")
    tree.pack(pady=10)

    def display_data(data):
        # Clear existing rows in the tree view
        for row in tree.get_children():
            tree.delete(row)

        # Insert new data into the table
        for _, row in data.iterrows():
            tree.insert("", "end", values=(row["project_id"], row["emissions_reduction"], row["cost"], row["risk"], row["kpi"], row.get("evaluation", "N/A")))

    # Evaluate and Optimize Button
    def evaluate_and_optimize():
        try:
            data = collect_and_process_data()  # Get current data
            
            # Simple evaluation logic: Calculate an average of relevant columns
            data['evaluation'] = data[['emissions_reduction', 'kpi']].mean(axis=1)  # Example logic
            
            optimized_projects = optimize_investments(data)  # Optimize based on evaluated data
            display_data(optimized_projects)  # Display optimized results
        except Exception as e:
            messagebox.showerror("Error", f"Error in evaluation or optimization: {e}")

    optimize_button = tk.Button(window, text="Evaluate & Optimize", command=evaluate_and_optimize)
    optimize_button.pack(pady=20)

    window.mainloop()

# Call the GUI
if __name__ == "__main__":
    run_gui()
