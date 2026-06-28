from src.load_data import load_data, display_basic_info
from src.clean_data import inspect_data, clean_data
from src.transform import transform_data, filter_data
from src.analyze import analyze_data, sort_data, group_data, stats_analysis
from src.report import generate_report
from src.visualize import run_visualizations

df = None

def main_menu():
    print("\n==== STUDENT DATA ANALYSIS ====")
    print("1. Load Data")
    print("2. Inspect Data")
    print("3. Clean Data")
    print("4. Transform + Filter")
    print("5. Analyze Data")
    print("6. Generate Report")
    print("7. Show Visualizations")
    print("8. Run Everything")
    print("0. Exit")

while True:
    main_menu()
    choice = input("\nEnter your choice: ")

    if choice == "1":
        df = load_data()
        display_basic_info(df)

    elif choice == "2":
        inspect_data(df)

    elif choice == "3":
        df = clean_data(df)

    elif choice == "4":
        df = transform_data(df)
        filter_data(df)

    elif choice == "5":
        analyze_data(df)
        sort_data(df)
        group_data(df)
        stats_analysis(df)

    elif choice == "6":
        generate_report(df)

    elif choice == "7":
        run_visualizations(df)

    elif choice == "8":
        df = load_data()
        display_basic_info(df)
        inspect_data(df)
        df = clean_data(df)
        df = transform_data(df)
        filter_data(df)
        analyze_data(df)
        sort_data(df)
        group_data(df)
        stats_analysis(df)
        generate_report(df)
        run_visualizations(df)

    elif choice == "0":
        print("Goodbye!")
        break

    else:
        print("Invalid choice, try again!")