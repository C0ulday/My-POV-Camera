# ✦ My POV Camera

A tiny, magnet-mounted camera that clips onto any metal surface to film my ULM flights (multi-axes) in **1080p**.

**Cost:** ~160 € (139.25 € electronics · 21.14 € printing)
**Inspirations:** DJI Osmo Nano · POV Pro

---

## ✦ The Idea

A small first-person-view camera that:
- sticks to any **magnetic surface** (N52 magnets on the back)
- records my multi-axis flights in **1080p**
- stays **minimalist**, with little engraved drawings on the 3D shell

<img src="3D Design/Images/idea_sketch.jpg" alt="Idea sketch" width="1460" height="634" />

---

## ✦ Prototyping

Everything is tested on the bench first : to validate the wiring and the firmware before committing to anything.

---

## ✦ Hardware

### Core Electronics
| Component | Model | Specs | Qty |
|-----------|-------|-------|-----|
| Microcontroller | Raspberry Pi Zero 1.3 | 1GHz single-core, 512MB, **no WiFi / no BT** | 1 |
| Camera | IMX219 8MP CSI | 77/130/200°, FFC 15cm | 1 |
| Storage | MicroSD U3 V30 | 128GB, Class 10 | 1 |
| Display | SSD1306 OLED | 0.91", 128×32px, I2C (0x3C) | 1 |

The Pi Zero 1.3 has **no wireless**. Video is offloaded by pulling the microSD card and reading
it on a computer.

### Power

| Component | Model | Specs | Qty |
|-----------|-------|-------|-----|
| Battery | LiPo 603255 | 3.7V, 1500mAh (≈6.0×32×55mm) | 1 |
| Charge module | TP4056 | USB-C, 3.7V, JST PH2.0 | 1 |
| Boost converter | MT3608 | 3.7V → 5V (powers the Pi) | 1 |
| Fuel gauge | MAX17048 | I2C (0x36), reports battery % to the Pi | 1 |

### Connectors & Cables
| Component | Specs | Qty |
|-----------|-------|-----|
| JST PH 1.25 | 2 pins, 100mm, M/F | 20 pairs |
| FPC/FFC ribbon | 0.5mm pitch, type A | 10× (mixed pins) |

### Interface
| Component | Specs | Qty |
|-----------|-------|-----|
| Buttons | Ø5mm | 3 |
| LED Green | 3mm : recording status | 1 |
| Resistors | 220Ω, 330Ω, 10kΩ | kit |
| Capacitors | 470µF | kit |

### Enclosure & Mounting
| Component | Model | Specs | Qty |
|-----------|-------|-------|-----|
| Dome lens | Acrylic watch crystal | Ø32.5mm, convex | 1 |
| Magnets | N52 neodymium | 15×5×2mm | 5 |
| Epoxy glue | 3M Scotch-Weld DP460 | structural | 1 |
| Enclosure | Custom 3D print | v1: 75×50×55mm (to be reduced after PCB), PLA, 20% infill | 1 |

### Tools
| Component | Specs |
|-----------|-------|
| Soldering iron | USB-C, 260–420°C |
| Solder wire | Sn99.3 Cu0.7, 0.8mm, lead-free |
| Multimeter | XL830L |

### Others
| Component | Qty |
|-----------|-----|
| Nylon necklace | 1 |
| Plastic support for magnet | 1 |

---

## ✦ PCB — Daughterboard

Instead of a Dupont rat's nest, all the small parts live on **one custom PCB** that plugs onto the
Pi Zero's GPIO header: TP4056, MT3608, MAX17048, OLED, 3 buttons, 2 LEDs and passives.

**Power path:** TP4056 charges the LiPo over USB-C → MT3608 boosts 3.7V to 5V to feed the Pi.

**I2C bus:** OLED `0x3C`

---

## ✦ 3D Design

FreeCAD for the design (box + cover), TinkerCAD for a quick fit-check prototype. 

**Stack:**
- Layer 1 — Magnets
- Layer 2 — Raspberry Pi Zero + custom PCB
- Layer 3 — LiPo

<div style="display: flex; flex-wrap: wrap; gap: 20px; justify-content: center;">
  <img src="3D Design/Images/3D_1.png" alt="3D Design" width="400" height="400" />
  <img src="3D Design/Images/prototype_test.png" alt="3D Test" width="400" height="400" />
  <img src="3D Design/Images/3D_printing.jpg" alt="3D printing" width="400" height="400" />
</div>

The v1 enclosure (75×50×55mm) was printed before I switched to the PCB approach, so it's
oversized : it'll be reprinted smaller once the board STEP is in FreeCAD (height should drop to
~30mm).

No insulating wall between electronics and magnets; I'll use EVA foam / plastic / cardboard to
build the compartments.

---

## ✦ Electronic Design

<div style="display: flex; flex-wrap: wrap; gap: 20px; justify-content: center;">
  <img src="Electronics/Images/scheme.png" alt="Schematic" width="1460" height="634" />
</div>

I used a different OLED model in the schematic, since I couldn't find the exact one on EasyEDA or
SnapEDA. The MAX17048 fuel gauge lets the Pi read the battery level, which brings the red
low-battery LED into the design. It shares the I2C bus with the OLED with no conflict.

---

## 💻 Code

_To do — firmware once the schematic and PCB are confirmed._
