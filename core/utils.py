from datetime import date
from typing import List, Any

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import matplotlib.dates as mdates

from numpy import poly1d


def calculate_expected_num_deaths(
    total_cases: float, total_deaths: float, population: float
) -> float:
    return total_deaths / total_cases * population


def get_polyfit_line(x: List[float], y: List[float], degree: int = 5) -> poly1d:
    x = mdates.date2num(x) if isinstance(x[0], date) else x
    trend = np.polyfit(x, y, degree)
    return np.poly1d(trend)


def plot_graph_with_polyfit_line(
    x: List,
    y: List,
    title: str,
    x_label: str = "Date",
    y_label: str = "Expected number of deaths by COVID-19",
) -> None:
    plt.plot(x, y)
    numeric_x = mdates.date2num(x) if isinstance(x[0], date) else x
    f = get_polyfit_line(numeric_x, y)
    x_new = pd.date_range(start=x[0], end=x[-1], periods=100)
    y_new = f(np.linspace(numeric_x[0], numeric_x[-1], 100))

    plt.plot(x_new, y_new)
    plt.xticks(fontsize=8)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.savefig(f"resources/{title}.jpg")


def predict_trend(input: Any, polyfit_line: poly1d) -> float:
    numeric_input = mdates.date2num(input) if isinstance(input, date) else input
    return polyfit_line(numeric_input)
