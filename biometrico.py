import fprint

fprint.init()
ddevs = fprint.DiscoveredDevices()
if len(ddevs) > 0:
    ddev = ddevs[0]
    dev = fprint.Device.open(ddev)
    (print_data, image) = dev.enroll_finger()
    print_data = fprint.PrintData.from_data(print_data.data)
    (result, img) = dev.verify_finger(print_data)
    assert result is True
    print(print_data)
    print(image)
    print(result)
    print(img)
    image.save_to_file('finger')
    dev.close()
