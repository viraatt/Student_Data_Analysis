from src.load_data import load_data, display_basic_info
from src.clean_data import inspect_data, clean_data
from src.transform import transform_data, filter_data
from src.analyze import analyze_data, sort_data, group_data, stats_analysis
from src.report import generate_report
from src.visualize import run_visualizations
import os

def clear():
    os.system("cls")
def run_dependencies(verbose=False):
    df = load_data()
    if verbose:
        display_basic_info(df)
        inspect_data(df)
    df = clean_data(df)
    df = transform_data(df)
    filter_data(df)
    return df


def main_menu():
    print("\n==== STUDENT DATA ANALYSIS ====")
    print("1. View Data Info")
    print("2. Inspect Data")
    print("3. Analyze Data")
    print("4. Generate Report")
    print("5. Show Visualizations")
    print("6. Run Everything")
    print("0. Exit")

while True:
    main_menu()
    choice = input("\nEnter your choice: ")

    if choice == "1":
        clear()
        df = run_dependencies()
        display_basic_info(df)

    elif choice == "2":
        clear()
        df = run_dependencies()
        inspect_data(df)

    elif choice == "3":
        clear()
        df = run_dependencies()
        analyze_data(df)
        sort_data(df)
        group_data(df)
        stats_analysis(df)

    elif choice == "4":
        clear()
        df = run_dependencies()
        generate_report(df)

    elif choice == "5":
        clear()
        df = run_dependencies()
        run_visualizations(df)

    elif choice == "6":
        clear()
        df = run_dependencies(verbose=True)
        analyze_data(df)
        sort_data(df)
        group_data(df)
        stats_analysis(df)
        generate_report(df)
        run_visualizations(df)

    elif choice == "0":
        clear()
        print("Goodbye!")
        break

    else:
        clear()
        print("Invalid choice, try again!")