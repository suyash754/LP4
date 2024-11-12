flight_ids = ["AA101", "BB202", "CC303", "DD404", "EE505"]
delays = [45, 60, 30, 120, 15]

def flight_delay_analysis(flight_ids, delays):
    
    max_delay_flight = ""
    max_delay = 0
    total_delay = 0
    n = len(flight_ids)  # Number of flights

    # Process each flight's delay
    for i in range(n):
        flight_id = flight_ids[i]
        delay = delays[i]

        # Update total delay
        total_delay += delay

        # Check if this flight has the maximum delay
        if delay > max_delay:
            max_delay = delay
            max_delay_flight = flight_id

    avg_delay = int(total_delay / n) 
    
    print(f"Flight ID with the highest delay: {max_delay_flight} (Delay: {max_delay} mins)")
    print(f"Average delay of all flights: {avg_delay} mins")

flight_delay_analysis(flight_ids, delays)
