import re
import numpy as np
import pandas as pd
import logging
from data_ingestion import read_from_web_CSV

class WeatherDataProcessor:
    """
    A class to process weather-related data.

    Attributes:
        weather_station_data (str): Path or URL to the weather station data CSV.
        patterns (dict): Dictionary of regex patterns to extract measurements.
        weather_df (pd.DataFrame): DataFrame to hold the weather data.
        logger (logging.Logger): Logger instance for the class.
    """

    def __init__(self, config_params, logging_level="INFO"):
        """
        Initializes the WeatherDataProcessor with configuration parameters.

        Args:
            config_params (dict): Dictionary containing weather CSV path and regex patterns.
            logging_level (str): Logging level, defaults to "INFO".
        """
        self.weather_station_data = config_params['weather_csv_path']
        self.patterns = config_params['regex_patterns']
        self.weather_df = None  # Initialize weather_df as None or as an empty DataFrame
        self.initialize_logging(logging_level)

    def initialize_logging(self, logging_level):
        """
        Sets up logging for the class.

        Args:
            logging_level (str): Logging level to set (DEBUG, INFO, NONE).
        """
        logger_name = __name__ + ".WeatherDataProcessor"
        self.logger = logging.getLogger(logger_name)
        self.logger.propagate = False

        # Set logging level
        if logging_level.upper() == "DEBUG":
            log_level = logging.DEBUG
        elif logging_level.upper() == "INFO":
            log_level = logging.INFO
        elif logging_level.upper() == "NONE":  # Option to disable logging
            self.logger.disabled = True
            return
        else:
            log_level = logging.INFO  # Default to INFO

        self.logger.setLevel(log_level)

        if not self.logger.handlers:
            ch = logging.StreamHandler()  # Console handler
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            ch.setFormatter(formatter)
            self.logger.addHandler(ch)

    def weather_station_mapping(self):
        """
        Loads the weather station data from the CSV URL into a DataFrame.
        """
        self.weather_df = read_from_web_CSV(self.weather_station_data)
        self.logger.info("Successfully loaded weather station data from the web.")
        # Apply any initial transformations if needed.

    def extract_measurement(self, message):
        """
        Extracts measurement type and value from a message using regex patterns.

        Args:
            message (str): The message to extract data from.

        Returns:
            tuple: Measurement type (str) and value (float), or (None, None) if no match.
        """
        for key, pattern in self.patterns.items():
            match = re.search(pattern, message)
            if match:
                self.logger.debug(f"Measurement extracted: {key}")
                return key, float(next((x for x in match.groups() if x is not None)))
        self.logger.debug("No measurement match found.")
        return None, None

    def process_messages(self):
        """
        Processes messages in the weather DataFrame to extract measurements.

        Returns:
            pd.DataFrame: Updated weather DataFrame with extracted measurements and values.
        """
        if self.weather_df is not None:
            result = self.weather_df['Message'].apply(self.extract_measurement)
            self.weather_df['Measurement'], self.weather_df['Value'] = zip(*result)
            self.logger.info("Messages processed and measurements extracted.")
        else:
            self.logger.warning("weather_df is not initialized, skipping message processing.")
        return self.weather_df

    def calculate_means(self):
        """
        Calculates the mean values of measurements grouped by weather station and measurement type.

        Returns:
            pd.DataFrame: A pivoted DataFrame of mean values or None if weather_df is not initialized.
        """
        if self.weather_df is not None:
            means = self.weather_df.groupby(by=['Weather_station_ID', 'Measurement'])['Value'].mean()
            self.logger.info("Mean values calculated.")
            return means.unstack()
        else:
            self.logger.warning("weather_df is not initialized, cannot calculate means.")
            return None

    def process(self):
        """
        Orchestrates the processing of weather data by loading, transforming, and extracting measurements.
        """
        self.weather_station_mapping()
        self.process_messages()
        self.logger.info("Data processing completed.")
