# CleverHand

**CleverHand** is an **open-source, modular hardware–software platform for Human–Machine Interfaces (HMI)**, designed to support high-quality biosignal acquisition and multimodal sensory feedback in **research, education, and advanced prototyping**.

The platform enables the acquisition of physiological signals (EMG, ECG, EEG, IMU, etc.) and the delivery of feedback (electrotactile, vibrotactile, visual), with a strong emphasis on **modularity, reproducibility, and data quality**.

CleverHand is not a closed product.
It is an **open infrastructure** intended to be:

* built and modified by researchers,
* integrated into experimental systems,
* and reused across multiple projects without redesigning the stack each time.

---

## Diagram

![CleverHand system diagram](docs/img/diagram.drawio.svg)

---


## Project philosophy

* **Open by design**
  All hardware, firmware, and software are open-source. Users may self-manufacture modules or assemble them via standard PCBA services.

* **Research-first, not consumer-first**
  CleverHand prioritises signal integrity, timing control, and experimental flexibility over plug-and-play simplicity.

* **Access without lock-in**
  For users who do not want to manufacture hardware themselves, pre-assembled and tested modules may be offered as an *access layer* (shop), without restricting openness.

* **Long-term maintainability**
  Stable interfaces, documented modules, and explicit quality-control practices are preferred over rapid feature churn.

---

## System overview

CleverHand devices are built by chaining small, specialised modules that share:

* a common electrical and communication interface,
* a unified firmware and data model,
* and a host-side software stack (GUI, LSL, Python, C++).

---

## Repository structure

* [`hardware`](hardware/CleverHand-hardware/README.md)
  Hardware design files (KiCad), manufacturing data, and module-level documentation.
* [`software`](software/)
  * [`driver`](software/driver)
    Host-side api and libraries (Drivers, LSL streaming, Python/C++ APIs).
  * [`firmware`](software/firmware/)
    Embedded firmware for inter-module communication and host interfacing.
  * [`tools`](software/tools/)
  Utilities for configuration, testing, and data visualisation:


---

## Key features

### Modular architecture

* 1 to 32 modules per device
* Sensor, feedback, communication, and interface modules can be freely combined

### Position-based addressing

* Module addresses are inferred from physical position in the chain
* No hardcoded IDs or manual configuration

### High-quality biosignal acquisition

* Up to **4 kHz sampling rate**
* **24-bit resolution** (ADS1293 / ADS1298 based modules)
* Designed for EMG and other low-amplitude physiological signals

### High-density wearable design

* Typical module size: **20 × 20 mm**
* Integrated gold-plated electrode pads (e.g. 3 × 18 mm)
* Supports dense spatial sampling

### Flexible connectivity

* Wired: USB, Ethernet
* Wireless: Bluetooth, Wi-Fi (others possible depending on controller)

### Unified software interface

* Configuration GUI
* Real-time visualisation
* LSL streaming
* Python and C++ APIs

---

## Background and motivation

<details>
<summary>Details</summary>

### Motivation

Electromyography (EMG) provides a non-invasive way to measure muscle activation and is widely used in:

* human–machine interaction,
* prosthetics and assistive devices,
* rehabilitation and exoskeleton control,
* sports science and biomechanics.

Despite its importance, existing EMG systems often fall into two extremes:

* **low-cost, low-performance** wearable devices,
* or **high-performance, high-cost** laboratory systems with limited portability.

### Limitations of existing systems

#### Wearable EMG devices

| Device               | Price   | Electrodes | Sampling rate | Resolution | Notes                         |
| -------------------- | ------- | ---------- | ------------- | ---------- | ----------------------------- |
| Myo armband          | ~200 $  | 8 bipolar  | 200 Hz        | 8-bit      | Easy to use, discontinued     |
| MyoWare              | ~40 $   | 3 bipolar  | 200 Hz        | 10-bit     | Suitable for prototyping only |
| Delsys Trigno Avanti | ~2000 $ | 16 bipolar | 2000 Hz       | 16-bit     | High quality, expensive       |

#### Non-wearable EMG systems

| Device              | Price  | Channels | Sampling rate | Resolution |
| ------------------- | ------ | -------- | ------------- | ---------- |
| OT Sessanta Quattro | ~10 k$ | 64       | 2000 Hz       | 24-bit     |
| OT Muovi+           | ~25 k$ | 4×32     | 2000 Hz       | 24-bit     |
| OT Quattrocento     | ~50 k$ | 382      | 2000 Hz       | 24-bit     |

### CleverHand approach

CleverHand aims to **bridge the gap** between these categories by providing:

* modular, wearable, high-density EMG acquisition,
* research-grade signal quality,
* and a system that scales from small experiments to complex multi-site recordings.

Each EMG module integrates an ADS1293 or ADS1298 AFE, supporting **3–8 channels per module**, sampled at **4 kHz / 24-bit**. Multiple modules can be chained to increase spatial coverage.

Gold-plated electrode pads on the PCB can be used directly or adapted via interface boards (flex electrodes, snap connectors, jack connectors).

</details>

---

## Additional capabilities

| Feature         | Description                       |
| --------------- | --------------------------------- |
| Visual feedback | RGB LEDs per module               |
| IMU             | Optional inertial sensing modules |
| Electrotactile  | Optional stimulation modules      |
| Vibrotactile    | Optional actuator modules         |
| Attachments     | Bracelet, mesh, custom mounts     |
| Interfaces      | GUI, LSL, Python, C++             |

---

## Project status & contributions

CleverHand is an **active research platform**.
Interfaces and core architecture are stabilising, while individual modules continue to evolve.

Contributions are welcome in the form of:

* issues and bug reports,
* hardware or firmware improvements,
* documentation and experiments,
* or external use cases and feedback.

If you plan to use CleverHand in a study or project, citations and references are appreciated.

