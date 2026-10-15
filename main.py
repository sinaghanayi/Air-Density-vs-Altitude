import matplotlib.pyplot as plt

MAX_ALTITUDE = 11000
TABLE_STEP = 1000
CHART_STEP = 100

def calculate_air_properties(altitude):
    temperature = 15.04 - 0.00649 * altitude

    pressure = 101.29 * (
        (temperature + 273.1) / 288.08
    ) ** 5.256

    density = pressure / (
        0.2869 * (temperature + 273.1)
    )

    return {
        "temperature": temperature,
        "pressure": pressure,
        "density": density,
    }


def get_valid_altitude():
    while True:
        try:
            altitude = float(
                input("Enter altitude in meters (0-11000): ")
            )
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if not 0 <= altitude <= MAX_ALTITUDE:
            print("Altitude must be between 0 and 11000 meters.")
            continue

        return altitude
def show_single_altitude():
    altitude = get_valid_altitude()
    properties = calculate_air_properties(altitude)

    print("\nAtmospheric properties")
    print("----------------------")
    print(f"Altitude:       {altitude:.0f} m")
    print(f"Temperature:    {properties['temperature']:.2f} C")
    print(f"Pressure:       {properties['pressure']:.2f} kPa")
    print(f"Air density:    {properties['density']:.4f} kg/m^3")

def show_properties_table(include_reduction=False):
    sea_level_properties = calculate_air_properties(0)
    sea_level_density = sea_level_properties["density"]

    print("\nStandard-atmosphere properties")
    print("=" * 78)

    if include_reduction:
        print(
            f"{'Altitude (m)':>12} {'Temp (C)':>12} "
            f"{'Pressure (kPa)':>17} "
            f"{'Density (kg/m^3)':>19} {'Reduction (%)':>16}"
        )
        print("-" * 78)
    else:
        print(
            f"{'Altitude (m)':>12} {'Temp (C)':>12} "
            f"{'Pressure (kPa)':>17} {'Density (kg/m^3)':>19}"
        )
        print("-" * 63)
    for altitude in range(0, MAX_ALTITUDE + 1, TABLE_STEP):
        properties = calculate_air_properties(altitude)
        density = properties["density"]

        if include_reduction:
            reduction = (
                (sea_level_density - density)
                / sea_level_density
                * 100
            )
            print(
                f"{altitude:12.0f} "
                f"{properties['temperature']:12.2f} "
                f"{properties['pressure']:17.2f} "
                f"{density:19.4f} "
                f"{reduction:16.2f}"
            )
        else:
            print(
                f"{altitude:12.0f} "
                f"{properties['temperature']:12.2f} "
                f"{properties['pressure']:17.2f} "
                f"{density:19.4f}"
            )

    print(
        "\nNote: These values come from a simplified "
        "standard-atmosphere model."
    )


def plot_density_vs_altitude():
    altitudes = []
    densities = []

    for altitude in range(0, MAX_ALTITUDE + 1, CHART_STEP):
        properties = calculate_air_properties(altitude)

        altitudes.append(altitude)
        densities.append(properties["density"])

    plt.figure(figsize=(9, 5.5))
    plt.plot(
        altitudes,
        densities,
        label="Modeled air density"
    )

    plt.title("Air Density vs. Altitude")
    plt.xlabel("Altitude (m)")
    plt.ylabel("Air density (kg/m^3)")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()


def show_menu():
    print("\nAIR DENSITY VS. ALTITUDE")
    print("1. Calculate properties at one altitude")
    print("2. Show the properties table")
    print("3. Plot density vs. altitude")
    print("4. Show density reduction from sea level")
    print("5. Exit")


def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            show_single_altitude()
        elif choice == "2":
            show_properties_table()
        elif choice == "3":
            plot_density_vs_altitude()
        elif choice == "4":
            show_properties_table(include_reduction=True)
        elif choice == "5":
            print("Thank you for using the program.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()
