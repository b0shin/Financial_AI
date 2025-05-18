from data.yahoo import fetch_yahoo_data
from models.arima import train_arima, forecast_arima
import matplotlib.pyplot as plt

def run_example():
    # Example: Get historical data
    data = fetch_yahoo_data("AAPL", "2020-01-01", "2023-01-01")
    close_prices = data['Close'].dropna()

    # Train ARIMA model
    model_fit = train_arima(close_prices)
    # Forecast next 30 days
    forecast = forecast_arima(model_fit, steps=30)
    
    # Plot
    plt.figure(figsize=(10,5))
    plt.plot(close_prices, label='Historical Close')
    plt.plot(range(len(close_prices), len(close_prices)+30), forecast, label='Forecast')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    run_example()