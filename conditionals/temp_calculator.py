device_status= "active"
temp= 35

if device_status=="active":
    if temp>35:
        print(f"High temperature alert!")
    else:
        print(f"Temperature is normal")
else:
    print(f"device is Offline!")