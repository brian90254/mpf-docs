Logical devices
===============

A logical device in MPF is a device that is composed of multiple physical
devices. Remember that physical devices are used to represent
the lowest-level, physical hardware in a pinball machine, including
switches, lights, and drivers (coils). Logical devices are based on
groups of physical devices which work together. For example, a
flipper is a logical device because it groups a switch (a physical
device) with a coil (another physical device) to become a flipper
which can be enabled or disabled or have its properties changed based
on what's going on in the game. The trough is a logical device that
combines a bunch of switches and an eject coil into a ball device
which knows how to receive and count balls, how to eject them, whether
the eject has failed, etc.

Logical devices in MPF include:

.. toctree::
   :maxdepth: 1

   ball_device