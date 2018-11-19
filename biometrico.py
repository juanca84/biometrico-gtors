import fprint

fprint.init()
ddevs = fprint.DiscoveredDevices()
if len(ddevs) > 0:
    ddev = ddevs[0]
    dev = fprint.Device.open(ddev)
    (print_data, image) = dev.enroll_finger()
    image.save_to_file('finger')
    dev.close()
