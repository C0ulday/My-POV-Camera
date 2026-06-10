# [ ◉¯] My POV Camera (ENG)

> French version below

A tiny, magnet-mounted camera that clips onto any metal surface to film my ULM flights (multi-axis) in 1080p.
---

## ✦ The Idea

A small first-person-view camera that:

- sticks to any magnetic surface (N52 magnets on the back)
- records my multi-axis flights in 1080p
- stays minimalist, with little engraved drawings on the 3D shell

![Idea sketch](3D%20Design/idea_sketch.jpeg)

---

## ✦ Hardware

### Core Electronics
| Component | Model | Specs | Qty |
|---|---|---|---|
| Microcontroller | Raspberry Pi Zero 1.3 | 1 GHz single-core, 512 MB, **no WiFi / no BT** | 1 |
| Camera | IMX219 8MP CSI | 77° lens variant, mini CSI FFC | 1 |
| Storage | MicroSD U3 V30 | 128 GB, Class 10 | 1 |

> The Pi Zero 1.3 has no wireless. Video is offloaded by pulling the microSD card and reading it on a computer.

### Power

| Component | Model | Specs | Qty |
|---|---|---|---|
| Battery | LiPo 603255 | 3.7 V, ~1500 mAh (≈6.0×32×55 mm) | 1 |
| Charge module | TP4056 | USB-C, protected, JST PH2.0 | 1 |
| Boost converter | MT3608 | 3.7 V → 5.1 V (powers the Pi) | 1 |

> **Power path:** TP4056 charges the LiPo over USB-C → on a protected TP4056 the load draws from **OUT+** (not BAT) → MT3608 boosts to **~5.1 V** (pre-adjusted *before* connecting the Pi) → feeds the Pi 5 V.

### Interface
| Component | Pin / Specs | Notes | Qty |
|---|---|---|---|
| Power button | **GPIO3 (pin 5)** | hardware boot-from-halt on press; software clean shutdown when pressed while running | 1 |
| Play/Stop button | free GPIO → GND, internal pull-up | start / stop recording | 1 |
| LED (REC) | green 3 mm, via resistor | recording status | 1 |
| Resistors / passives | 220 Ω, 330 Ω, 10 kΩ · 470 µF | — | kit |

### Enclosure & Mounting
| Component | Model | Specs | Qty |
|---|---|---|---|
| Standoffs / screws | brass | **M2.5** | set |
| Dome lens | acrylic watch crystal | Ø32.5 mm, convex | 1 |
| Magnets | N52 neodymium | 15×5×2 mm | 5 |
| Epoxy glue | 3M Scotch-Weld DP460 | structural | 1 |
| Enclosure | custom 3D print | ≈68×36×28.4 mm, PLA, 20 % infill | 1 |

### Tools
| Component | Specs |
|---|---|
| Soldering iron | USB-C, 260–420 °C |
| Solder wire | Sn99.3 Cu0.7, 0.8 mm, lead-free |
| Multimeter | XL830L |

![Components](Electronics/Images/material.png)

---

## ✦ Circuit

![Circuit Sketch](Electronics/Images/scheme.png)

> I used the bare chip schematic for the TP4056 because I couldn't find the schematic.
---

## ✦ 3D Design

FreeCAD for the design, TinkerCAD for quick fit-checks. The enclosure is a **layered sandwich** held together by M2.5 brass standoffs and screws : three compartmented zones stacked vertically:

- **Top : Interface:** camera, buttons, REC LED
- **Middle : Pi Zero**
- **Bottom : Energy:** a shelf plate separates the **battery** from the **TP4056 + MT3608** modules

> The LiPo eats ~72 % of the floor footprint, so it gets its own level and can't share a layer with the charge/boost modules — hence the shelf plate.

![3D Design Front](3D%20Design/Images/front.png)


## ✦ Code

| Module | Role |
|---|---|
| `config.py` | pins, paths, settings |
| `camera.py` | wraps **`rpicam-vid`** as a subprocess for hardware H.264 (preferred over picamera2 on the slow ARMv6 Zero 1.3) |
| `inputs.py` | buttons (Play/Stop, Power) |
| `indicators.py` | REC LED |
| `controller.py` | simple **IDLE ↔ RECORDING** state machine |
| `main.py` | entry point, **systemd** autostart |

## ✦ Results

...

---

# [ ◉¯] Ma caméra POV (FR)

Une petite caméra montée sur aimant qui se fixe sur n'importe quelle surface métallique pour filmer mes vols d'ULM (multi-axes) en 1080p.
---

## ✦ L'idée

Une petite caméra vue de première personne qui :

- se fixe sur n'importe quelle surface magnétique (aimants N52 au dos)
- enregistre mes vols multi-axes en 1080p
- reste minimaliste, avec de petits dessins gravés sur la coque 3D

![Croquis de l'idée](3D%20Design/idea_sketch.jpeg)

---

## ✦ Matériel

### Électronique principale
| Composant | Modèle | Caractéristiques | Qté |
|---|---|---|---|
| Microcontrôleur | Raspberry Pi Zero 1.3 | 1 GHz mono-cœur, 512 Mo, **sans WiFi / sans BT** | 1 |
| Caméra | IMX219 8MP CSI | Variante objectif 77°, nappe CSI miniature | 1 |
| Stockage | MicroSD U3 V30 | 128 Go, Classe 10 | 1 |

> Le Pi Zero 1.3 n'a pas de sans-fil. Les vidéos sont déchargées en retirant la carte microSD et en la lisant sur un ordinateur.

### Alimentation

| Composant | Modèle | Caractéristiques | Qté |
|---|---|---|---|
| Batterie | LiPo 603255 | 3,7 V, ~1500 mAh (≈6,0×32×55 mm) | 1 |
| Module de charge | TP4056 | USB-C, protégé, JST PH2.0 | 1 |
| Convertisseur boost | MT3608 | 3,7 V → 5,1 V (alimente le Pi) | 1 |

> **Chemin de l'alimentation :** Le TP4056 charge le LiPo via USB-C → sur un TP4056 protégé, la charge est tirée de **OUT+** (pas BAT) → le MT3608 élève à **~5,1 V** (préréglé *avant* de connecter le Pi) → alimente le Pi en 5 V.

### Interface
| Composant | Broche / Caractéristiques | Notes | Qté |
|---|---|---|---|
| Bouton d'alimentation | **GPIO3 (broche 5)** | démarrage matériel depuis l'arrêt à l'appui ; arrêt logiciel propre si appuyé en fonctionnement | 1 |
| Bouton Lecture/Stop | GPIO libre → GND, pull-up interne | démarrer / arrêter l'enregistrement | 1 |
| LED (REC) | verte 3 mm, via résistance | état d'enregistrement | 1 |
| Résistances / passifs | 220 Ω, 330 Ω, 10 kΩ · 470 µF | — | kit |

### Boîtier et fixation
| Composant | Modèle | Caractéristiques | Qté |
|---|---|---|---|
| Entretoises / vis | laiton | **M2,5** | jeu |
| Verre de protection | fond de montre acrylique | Ø32,5 mm, convexe | 1 |
| Aimants | néodyme N52 | 15×5×2 mm | 5 |
| Colle époxy | 3M Scotch-Weld DP460 | structurelle | 1 |
| Boîtier | impression 3D personnalisée | ≈68×36×28,4 mm, PLA, remplissage 20 % | 1 |

### Outils
| Composant | Caractéristiques |
|---|---|
| Fer à souder | USB-C, 260–420 °C |
| Fil à souder | Sn99.3 Cu0.7, 0,8 mm, sans plomb |
| Multimètre | XL830L |

![Composants](Electronics/Images/material.png)

---

## ✦ Circuit

![Schéma du circuit](Electronics/Images/scheme.png)

> J'ai utilisé le schéma de la puce nue pour le TP4056 car je n'ai pas trouvé le schéma.
---

## ✦ Conception 3D

FreeCAD pour la conception, TinkerCAD pour des vérifications rapides d'ajustement. Le boîtier est un **sandwich à couches** maintenu par des entretoises et vis en laiton M2,5 : trois zones compartimentées empilées verticalement :

- **Haut : Interface :** caméra, boutons, LED REC
- **Milieu : Pi Zero**
- **Bas : Énergie :** une plaque séparatrice isole la **batterie** des modules **TP4056 + MT3608**

> Le LiPo occupe ~72 % de la surface au sol, il a donc son propre niveau et ne peut pas partager une couche avec les modules de charge/boost — d'où la plaque séparatrice.

![Conception 3D Avant](3D%20Design/Images/3D_1.png)
![Conception 3D Plaque](3D%20Design/Images/plate.png)
![Conception 3D Face avant](3D%20Design/Images/front.png)

## ✦ Code

| Module | Rôle |
|---|---|
| `config.py` | broches, chemins, réglages |
| `camera.py` | encapsule **`rpicam-vid`** en sous-processus pour le H.264 matériel (préféré à picamera2 sur le lent ARMv6 Zero 1.3) |
| `inputs.py` | boutons (Lecture/Stop, Alimentation) |
| `indicators.py` | LED REC |
| `controller.py` | machine d'état simple **REPOS ↔ ENREGISTREMENT** |
| `main.py` | point d'entrée, démarrage automatique via **systemd** |

## ✦ Résultats

...
