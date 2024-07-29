# CleverHand
CleverHand is an open-source, modular Human-Machine Interface (HMI) system designed for the acquisition of biosignals (EMG, ECG, EEG, etc.) and the delivery of sensory feedback (electrotactile, vibrotactile, visual, etc.). The system is intended for use in research and educational settings, as well as a platform for the development of assistive technologies, prosthetics, and exoskeletons.

The project is in the early stages of development, so expect some debugging and troubleshooting before it is ready for use. 

If you are interested in contributing to the project, feel free to raise issues, submit pull requests, or contact us directly.

# CleverHand
Module        |  Bracelet factor
:-------------------------:|:-------------------------:
![CleverHand](https://github.com/Aightech/CleverHand-hardware/blob/main/docs/anim.gif) |  ![chain](https://github.com/Aightech/CleverHand-hardware/blob/main/docs/bracelet_one.png)

# Repository structure
- `hardware` contains the hardware design files (KiCad)
- `firmware` contains the firmware for the communication between the modules and the host
- `software` contains the software for the communication between the main module and the host (GUI, LSL, python, C++)


## Features
- **Modular Architecture**
    
    Up to 32 integrable modules, each containing 5-8 surface electrodes embedded directly into the PCB.

- **Adaptable Addressing System**

    Module addresses based on their physical position in the chain, eliminating the need for hardcoded addresses.

 - **High-Quality Signal Acquisition**
    Samples EMG signals at a rate of 4 kHz with 24-bit resolution.

-  **High-Density Design** 

    Each module measures 20mm x 20mm and houses five 3mm x 18mm electrodes.

-  **Portability**

    Offers both wired (Ethernet) and wireless communication options.

-  **User-Friendly Interface**
        
    Comes with an intuitive GUI for easy parameter configuration, real-time visualization, and data streaming via LSL.


## Study
<details><summary>Details</summary>
<p>

#### Motivation
Electromyography (EMG) is a technique used to measure the electrical activity of muscles. It is widely used in the field of human-machine interaction, as it provides a non-invasive method of monitoring muscle activity. For example, EMG can be used to control prosthetic devices, allowing amputees to regain some of their lost functionality. EMG can also be used to control exoskeletons, allowing for the restoration of motor function in patients with neurological disorders. In addition, EMG is used in the field of sports science to monitor muscle activity during physical activity. 

#### Context
Current devices used for EMG signal acquisition are often bulky and expensive or lack the necessary features to meet the needs of researchers and clinicians. 

##### Wearable EMG devices

| Device | Price | Electrodes | Sampling rate | Resolution | Comments |
| --- | --- | --- | --- | --- | --- |
| Myoband | 200\$ | 8 bipolar electrodes | 200 Hz | 8-bit | It was very handy and easy to use for experiments as the users just had to put it on their arm and it was ready to use. Unfortunately, the Myoband is no longer available for purchase. |
| MyoWare EMG Sensor | 40\$ | 3 bipolar electrodes | 200 Hz | 10-bit  | The MyoWare EMG Sensor is a low-cost EMG sensor that can be used to measure muscle activity. It is a good option for prototyping, but it lacks the necessary features for research and clinical applications. |
| Delsys Trigno Avanti | 2000\$ | 16 bipolar electrodes | 2000 Hz | 16-bit | The Delsys Trigno Avanti is a high-end EMG system that offers a wide range of features. It is a good option for research and clinical applications, but it is expensive and not very portable. |


##### Non-wearable EMG devices

| Device | Price | Electrodes | Sampling rate | Resolution | Comments |
| --- | --- | --- | --- | --- | --- |
| OT Bioelettronica Sessanta Quattro | 10000\$ | 64 monopolar electrodes | 2000 Hz | 24-bit | The Sessanta Quattro is a high-end EMG system that offers a wide range of features. It is a good option for research and clinical applications, but it is very expensive. |
| Delsys Trigno Wireless System | ? | 32 monopolar electrodes | ? | ? | The Trigno Wireless System is a high-end EMG system that offers a wide range of features. It is a good option for research and clinical applications, but it is very expensive. |
| OT Bioelettronica Muovi+ | 25000\$ | 4x32 monopolar electrodes | 2000 Hz | 24-bit | The Muovi+ is a high-end EMG system that offers a wide range of features. It is a good option for research and clinical applications, but it is very expensive|
| OT Bioelettronica Quattrocento | 50000\$ | 382 monopolar electrodes | 2000 Hz | 24-bit | The Quattrocento is a high-end EMG system that offers a wide range of features. It is a good option for research and clinical applications, but it is very expensive. |


#### Approach

Our system features a modular architecture, allowing for the integration of 1 to 32 modules. Standard modules house ADS1293 or ADS1298 EMG acquisitions chip, enabling the sampling of 3 to 8 channels of EMG data at a rate of 4 kHz with a 24-bit resolution. 

To achieve a high-density design, the bottom layer of the PCB contains eight gold-plated areas (3mm x 18mm) that can serve as electrodes. This high-density design, with a module size of 20mm x 20mm, facilitates precise and detailed analysis of muscle activation patterns, especially in applications that require high spatial resolution.

To ensure the versatility of the modules it is also posible to use the gold plated electrodes to mount adpters for other type of electrodes (jack connector, snap connector, flex electrodes).

 The addressing system employed by the device is adaptable, with the address of each module determined by its physical position in the chain. This design eliminates the need for hardcoded addresses and simplifies the overall usage. 

| Module | Price | Electrodes | Sampling rate | Resolution |
| --- | --- | --- | --- | --- | 
| CleverHand | 200\$ | 16x8 monopolar/bipolar electrodes | 4 kHz | 24-bit |

##### Additional features

| Feature | Description |
| --- | --- |
| Modular | 1 to 32 modules per device |
| Visual | 2 RGB LEDs per module|
| IMU | Can be equipped with an IMU module|
| Electrotactile | Can be equipped with an electrotactile module|
| Vibrotactile | Can be equipped with a vibrotactile actuator|
| Communication | Wireless (Bluetooth, WiFi, LORA, ...) or wired (USB, Ethernet, ...) |
| Attachments | Standard, bracelet, mesh|
| Interface | GUI, LSL, python, C++ |

 </p>
</details>

# Diagram
![CleverHand](docs/diagram.svg)


