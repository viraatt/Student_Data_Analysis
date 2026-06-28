from src.load_data import load_data, display_basic_info
from src.clean_data import inspect_data, clean_data
from src.transform import transform_data, filter_data

df = load_data()
display_basic_info(df)

inspect_data(df)
df = clean_data(df)

df = transform_data(df)
filter_data(df)