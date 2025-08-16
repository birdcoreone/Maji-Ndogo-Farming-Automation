import pandas as pd
import pytest

# Validation Functions
def validate_weather_df_columns(df):
    """
    Validates that the weather DataFrame has the required columns.
    """
    required_columns = [
        'Field_ID', 'Elevation', 'Latitude', 'Longitude', 'Location', 'Slope',
        'Rainfall', 'Min_temperature_C', 'Max_temperature_C', 'Temperature',
        'Soil_fertility', 'Soil_type', 'pH', 'Pollution_level', 'Plot_size',
        'Annual_yield', 'Crop_type', 'Standard_yield'
    ]
    return set(required_columns).issubset(set(df.columns))

def validate_field_df_columns(df):
    """
    Validates that the field DataFrame has the required columns.
    """
    required_columns = [
        'Field_ID', 'Elevation', 'Latitude', 'Longitude', 'Location', 'Slope',
        'Rainfall', 'Min_temperature_C', 'Max_temperature_C', 'Temperature',
        'Soil_fertility', 'Soil_type', 'pH', 'Pollution_level', 'Plot_size',
        'Annual_yield', 'Crop_type', 'Standard_yield'
    ]
    return set(required_columns).issubset(set(df.columns))

def validate_non_negative_elevation(df):
    """
    Ensures that the Elevation column in the DataFrame contains non-negative values.
    """
    return (df['Elevation'] >= 0).all()

def validate_positive_rainfall(df):
    """
    Ensures that the Rainfall column in the DataFrame contains positive values.
    """
    return (df['Rainfall'] > 0).all()

def validate_crop_types(df, valid_crop_types):
    """
    Validates that all crop types in the DataFrame are within the valid crop types.
    """
    return df['Crop_type'].isin(valid_crop_types).all()

# Sample Data Loaders
def load_sampled_weather_df(file_path):
    return pd.read_csv(file_path)

def load_sampled_field_df(file_path):
    return pd.read_csv(file_path)

# Pytest Test Cases
def test_read_weather_DataFrame_shape():
    df = load_sampled_weather_df("sampled_weather_df.csv")
    assert df.shape == (expected_rows, expected_cols), "Shape mismatch in weather DataFrame"

def test_read_field_DataFrame_shape():
    df = load_sampled_field_df("sampled_field_df.csv")
    assert df.shape == (expected_rows, expected_cols), "Shape mismatch in field DataFrame"

def test_weather_DataFrame_columns():
    df = load_sampled_weather_df("sampled_weather_df.csv")
    assert validate_weather_df_columns(df), "Missing required columns in weather DataFrame"

def test_field_DataFrame_columns():
    df = load_sampled_field_df("sampled_field_df.csv")
    assert validate_field_df_columns(df), "Missing required columns in field DataFrame"

def test_field_DataFrame_non_negative_elevation():
    df = load_sampled_field_df("sampled_field_df.csv")
    assert validate_non_negative_elevation(df), "Elevation contains negative values"

def test_crop_types_are_valid():
    valid_crop_types = ['Maize', 'Wheat', 'Rice']  # Define valid crop types
    df = load_sampled_field_df("sampled_field_df.csv")
    assert validate_crop_types(df, valid_crop_types), "Invalid crop types found"

def test_positive_rainfall_values():
    df = load_sampled_field_df("sampled_field_df.csv")
    assert validate_positive_rainfall(df), "Rainfall contains non-positive values"

if __name__ == "__main__":
    # Define expected shape of DataFrames for testing
    expected_rows = 100  # Replace with actual expected row count
    expected_cols = 18  # Replace with actual expected column count

    # Run tests
    pytest.main()
