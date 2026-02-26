import sys
import importlib
from importlib import metadata


REQUIRED_PACKAGES = ["pandas", "requests", "matplotlib", "numpy"]
Desc = ["Data manipulation ready",
        "Network access ready",
        "Visualization ready",
        "Data generation ready"]


def check_dependencies() -> list:
    print("Checking dependencies:")
    missing = []
    i = 0
    for pkg in REQUIRED_PACKAGES:
        try:
            importlib.import_module(pkg)
            version = metadata.version(pkg)
            print(f"[OK]: {pkg} ({version}) - {Desc[i]}")
            i += 1
        except ImportError:
            print(f"[MISSING]: {pkg}")
            missing.append(pkg)
    return missing


def installation_help(missing):
    print("\nMissing dependencies detected.")
    print("You can install them using:\n")
    print("With pip:")
    print("  pip install -r requirements.txt\n")
    print("With Poetry:")
    print("  poetry install\n")
    print("Missing packages:", missing)


def analyze_data():
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt

    print("\nAnalyzing Matrix data...")
    data_points = 1000
    print(f"Processing {data_points} data points...")

    df = pd.DataFrame({
        "signal": np.random.randn(data_points).cumsum(),
        "time": np.arange(data_points)
    })

    plt.figure()
    plt.plot(df["time"], df["signal"])
    plt.title("Matrix Signal Analysis")
    plt.xlabel("Time")
    plt.ylabel("Signal Strength")

    output_file = "matrix_analysis.png"
    plt.savefig(output_file)
    plt.close()

    print("Generating visualization...")
    print("\nAnalysis complete!")
    print(f"Results saved to: {output_file}")


def main():
    if sys.prefix == sys.base_prefix:
        print("You're in the global environment!")
        print("switch to virtual environment")
        sys.exit(1)
    print("\nLOADING STATUS: Loading programs...\n")

    missing = check_dependencies()
    if missing:
        installation_help(missing)
        sys.exit(1)
    analyze_data()


if __name__ == "__main__":
    main()
