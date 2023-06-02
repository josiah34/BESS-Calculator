from datetime import datetime as dt


# Function to get numeric input from user and validate it
def get_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


# Function to get time input from user and validate it
def get_str_input(prompt):
    while True:
        try:
            value = str(input(prompt))
            dt.strptime(value, "%H:%M")
            return value
        except ValueError:
            print("Invalid input. Please try again.")
            continue


# Function to calculate the BESS parameters and print them to the console
def bess_calculator(
    active_charge_power, active_discharge_power, sample_time, start_time, end_time
):
    total_energy_charged = round((active_charge_power * sample_time / 3600) / 1000, 3)
    total_energy_discharged = round(
        (active_discharge_power * sample_time / 3600) / 1000, 3
    )
    round_trip_efficiency = round(
        (total_energy_discharged / total_energy_charged) * 100, 2
    )
    duration = check_time(start_time, end_time)
    power_loss = round((total_energy_charged - total_energy_discharged) / duration, 3)
    print("Energy charged in this sample time is: ", total_energy_charged, "MWh")
    print("Energy discharged in this sample time is: ", total_energy_discharged, "MWh")
    print("Round trip efficiency is: ", round_trip_efficiency, "%")
    print("Duration is: ", duration, "(HR)")
    print("Power loss is: ", power_loss, "MWh")
    # return a dictionary of the results for testing purposes
    results = {
        "Energy charged in this sample time is": total_energy_charged,
        "Energy discharged in this sample time is": total_energy_discharged,
        "Round trip efficiency is": round_trip_efficiency,
        "Duration is": duration,
        "Power loss is": power_loss,
    }
    return results


# Function to check the time input from the user and convert it to a float that can be used in the power loss calculation
def check_time(start_time, end_time):
    start_time = dt.strptime(start_time, "%H:%M")
    end_time = dt.strptime(end_time, "%H:%M")
    duration = end_time - start_time
    # Convert duration to hours using seconds attribute
    hours = duration.seconds // 3600
    # Convert duration to minutes using seconds attribute
    minutes = (duration.seconds // 60) % 60
    # Return a float that can be used in the power loss calculation
    return float(f"{hours}.{minutes}")


# Main function to run the program
def main():
    while True:
        active_charge_power = get_float_input("Enter the active charge power in KW: ")
        active_discharge_power = get_float_input(
            "Enter the active discharge power in KW: "
        )
        sample_time = get_float_input("Enter the sample time in seconds: ")
        start_time = get_str_input("Enter the start time: in HH:MM: ")
        end_time = get_str_input("Enter the end time in HH:MM: ")

        bess_calculator(
            active_charge_power,
            active_discharge_power,
            sample_time,
            start_time,
            end_time,
        )

        choice = input("Press 'y' to continue or 'n' to stop: ")
        if choice.lower() == "y":
            print("Continuing...")
        elif choice.lower() == "n":
            print("Stopping...")
            break
        else:
            print("Invalid input. Please try again.")


if __name__ == "__main__":
    main()
