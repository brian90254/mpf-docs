
MPF's device manager is responsible for loading and unloading MPF
devices. (Most devices in MPF can be loaded on a machine-wide or a
per-mode bases.) The device manager lives in the
*mpf/system/device_manager.py* module. The device manager is also
responsible for maintaining collections of devices (via the
DeviceCollection base class). You can connect to the device manager to
see all the devices in MPF (as well as their properties), and the
device manager can dump a configuration of all devices to a file for
troubleshooting purposes.



