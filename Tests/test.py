import pyxel

def read_xel_file(file_path):
    events = []
    with pyxel.open(file_path) as log:
        for event in log:
            events.append(event)

    return events

def print_event_details(events):
    for event in events:
        print("Event Name:", event.name)
        print("Timestamp:", event.timestamp)
        print("Data:")
        for field, value in event.data.items():
            print(f"  {field}: {value}")
        print("----")
        
test = read_xel_file("./04_38_48_097_0.xel")
print_event_details(test)