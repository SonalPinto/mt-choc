# Hardware

The **minimalist** build for Mt. Choc is based off of the "PCB-Enclosed" design of the [Horizon Keyboard](https://github.com/skarrmann/horizon/), where the main PCB is enclosed by a another PCB with cutouts for the components. This builds for an excitingly low height stack!

<p align="center" width="100%">
    <img width="50%" src="../assets/layer-stack.png">
</p>

The board is powered by a [Waveshare RP2040 microcontroller](https://www.waveshare.com/rp2040-lcd-1.28.htm) with integrated 1.28" display (GC9A01A, 240x240px). The board has two 2x10 headers (1.27mm pitch) with a decent number of GPIO brought out. I picked this one because the display seemed fun, and the overall profile is pretty neat, and for the RP2040.

Since I couldn't find a footprint for this board, I had to draw one. The footprint base for the uC was extracted from the model linked in its [waveshare docs](https://www.waveshare.com/wiki/RP2040-LCD-1.28). Then, project the model onto an offset plane and export the sketch as DXF. This can be imported in KiCad Footprint Editor as a graphic for further cleanup.

<p align="center" width="100%">
    <img width="50%" src="../assets/rp2040-LCD-model.png">
</p>

The uC has footprints for all the three layers. The main PCB is the one with the soldered through-hole male headers (two 2x10 1.27mm pitch). So, the bottom will need some cutout for the pins and pads. The switch plate cutouts has clearances for the female headers on the uC and the MX1.25 battery header. The buttons and the USBC header have enough clearance above the switch plate to not require cutouts. However, I've also added a footprint for a larger cutout following the outer profile in the [library](../pcb/footprints/mt-choc-footprints.pretty), though I haven't used it in this design. The edge.cuts are in orange, below.

<p align="center" width="100%">
    <img width="75%" src="../assets/rp2040-display-footprints.png">
</p>

## Soldering

- Get a Pinecil, and invest in some good solder (Kester 0.02" 63/37) and wick (Chemtronics or MG Chemicals). Get some tip tinner (Thermaltronics), and flux (ChipQuik) too.
- Be careful with diode orientation. There is a silkscreen marker to indicate placement.
- Same goes for the hotswap sockets. Now, usually this isn't a problem on regular builds, which don't use a bottom plate to **enclose** the main PCB. Because, the Kailh hotswap sockets are mechanically and electrically symmetric. However, if the build uses the bottom plate to enclose the components, then the hotswap sockets must be soldered along the indicated silkscreen silhouette.
- Soldering the 1.27mm pitch headers can be tricky. Might be the trickiest part of the job, and might be worth starting the build with this step.
  - Stick the male headers into the microcontroller first, and then set it onto the PCB. Use some painter's tape (or kapton) to hold it in place.
  - Solder **one** corner pin. Confirm everything is good on the other side, and only then proceed to solder another corner pin on the other header. If the setting is off, then reheat that pin while pressing down on the uC from the other side.
  - Iteratively solder the other corners.
  - With great patience, solder the rest the of the pins. If it bridges, then some combo of more solder, flux and wick will fix it.
