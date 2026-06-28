from src.load_data import load_data, display_basic_info
from src.clean_data import inspect_data, clean_data
from src.transform import transform_data, filter_data
from src.analyze import analyze_data, sort_data, group_data, stats_analysis
from src.report import generate_report
from src.visualize import run_visualizations

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