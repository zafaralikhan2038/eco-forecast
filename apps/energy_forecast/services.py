import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

class EnergyForecastService:
    CSV_FILE = os.path.join(os.path.dirname(__file__), "../../data/weather_data.csv")

    print(CSV_FILE)

    def __init__(self):
        self.model_solar = None
        self.model_wind = None
        self.scaler = None
        self.train_models()  # Always train from CSV on initialization

    def prepare_training_data(self, weather_data):
        """
        Prepare training data for energy forecasting.
        """
        df = pd.DataFrame(weather_data)

        # Feature engineering
        df['solar_potential'] = df['solar_radiation'] * df['temperature']
        df['wind_potential'] = df['wind_speed'] ** 3  # Cube law for wind power

        # Prepare features and targets
        X = df[['temperature', 'humidity', 'wind_speed', 'solar_radiation']]
        y_solar = df['solar_potential']
        y_wind = df['wind_potential']

        return X, y_solar, y_wind

    def train_models(self):
        """
        Train machine learning models for solar and wind energy forecasting from CSV.
        """
        try:
            # Read weather data from CSV
            df = pd.read_csv(self.CSV_FILE)
            weather_data = df.to_dict(orient="records")

            X, y_solar, y_wind = self.prepare_training_data(weather_data)

            # Scale features
            self.scaler = StandardScaler()
            X_scaled = self.scaler.fit_transform(X)

            # Split data
            X_train_solar, X_test_solar, y_train_solar, y_test_solar = train_test_split(
                X_scaled, y_solar, test_size=0.2, random_state=42
            )
            X_train_wind, X_test_wind, y_train_wind, y_test_wind = train_test_split(
                X_scaled, y_wind, test_size=0.2, random_state=42
            )

            # Train models
            self.model_solar = RandomForestRegressor(n_estimators=100, random_state=42)
            self.model_solar.fit(X_train_solar, y_train_solar)

            self.model_wind = RandomForestRegressor(n_estimators=100, random_state=42)
            self.model_wind.fit(X_train_wind, y_train_wind)

            # Print model performance
            solar_mae = mean_absolute_error(y_test_solar, self.model_solar.predict(X_test_solar))
            wind_mae = mean_absolute_error(y_test_wind, self.model_wind.predict(X_test_wind))

            print(f"Training completed!\nSolar MAE: {solar_mae}\nWind MAE: {wind_mae}")

        except Exception as e:
            print(f"Error training models: {e}")

    def predict_energy_output(self, weather_features):
        """
        Predict solar and wind energy output.
        """
        if not self.model_solar or not self.model_wind:
            raise ValueError("Models not trained properly. Please check the CSV file.")

        # Scale input features
        features_scaled = self.scaler.transform(weather_features)

        # Predict solar and wind output
        solar_output = self.model_solar.predict(features_scaled)
        wind_output = self.model_wind.predict(features_scaled)

        return solar_output[0], wind_output[0]

