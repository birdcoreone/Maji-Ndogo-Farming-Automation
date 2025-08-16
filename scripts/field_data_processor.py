import pandas as pd
import logging
from data_ingestion import create_db_engine, query_data, read_from_web_CSV


### START FUNCTION

class FieldDataProcessor:

    def __init__(self, config_params, logging_level="INFO"):  # Make sure to add this line, passing in config_params to the class 
        self.db_path = config_params['db_path']
        self.sql_query = config_params['sql_query']
        self.columns_to_rename = config_params['columns_to_rename']
        self.values_to_rename = config_params['values_to_rename']
        self.weather_map_data = config_params['weather_mapping_csv']

        # Add the rest of your class code here
        self.initialize_logging(logging_level)

        self.df = None
        self.engine = None

    def initialize_logging(self, logging_level):
        logger_name = __name__ + ".FieldDataProcessor"
        self.logger = logging.getLogger(logger_name)
        self.logger.propagate = False

        if logging_level.upper() == "DEBUG":
            log_level = logging.DEBUG
        elif logging_level.upper() == "INFO":
            log_level = logging.INFO
        elif logging_level.upper() == "NONE":
            self.logger.disabled = True
            return
        else:
            log_level = logging.INFO

        self.logger.setLevel(log_level)

        if not self.logger.handlers:
            ch = logging.StreamHandler()
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            ch.setFormatter(formatter)
            self.logger.addHandler(ch)
    def ingest_sql_data(self):
        self.logger.info("Successfully loaded data.")
        self.engine = create_db_engine(self.db_path)
        self.df = query_data(self.engine, self.sql_query)
        return self.df

    def rename_columns(self):
        self.df.rename(columns=self.columns_to_rename, inplace=True)
        self.logger.info("Columns renamed successfully.")

    def apply_corrections(self, column_name='Crop_type', abs_column='Elevation'):
        """
        Applies corrections to specific columns:
        - Converts the values in the `abs_column` to absolute values.
        - Renames crop strings based on the `values_to_rename` dictionary.

        Args:
            column_name (str): The column containing crop type values.
            abs_column (str): The column to convert values to absolute values.
        """
        # Apply absolute value correction
        self.df[abs_column] = self.df[abs_column].abs()
        
        # Rename crop strings
        self.df[column_name] = self.df[column_name].apply(lambda crop: self.values_to_rename.get(crop, crop))
        self.logger.info("Corrections applied successfully.")

    def weather_station_mapping(self):
        # Merge the weather station data to the main DataFrame
        weather_df = read_from_web_CSV(self.weather_map_data)
        self.df = self.df.merge(weather_df, on="Field_ID", how="left")
        self.logger.info("Weather station mapping completed successfully.")

    def process(self):
        """
        Calls all necessary methods to ingest and process data step by step.
        """
        try:
            self.logger.info("Starting the data processing pipeline.")
            self.ingest_sql_data()
            self.rename_columns()
            self.apply_corrections()
            self.weather_station_mapping()
            self.logger.info("Data processing pipeline completed successfully.")
        except Exception as e:
            self.logger.error(f"An error occurred during processing: {e}")
            raise e
            
        
        
### END FUNCTION