for hours in range(0, 24):
    for minutes in range(0, 60):
        if minutes < 10:
            print(f"{hours}:0{minutes}")
        else:
            print(f"{hours}:{minutes}")
