# CleverHand — Roadmap

This roadmap describes the remaining work required to transition CleverHand from a
broad experimental platform into a **stable, reference-grade, research-ready HMI system**.

The guiding principle is **qualification before expansion**:
new features are deprioritised in favour of evaluation, documentation, and reproducibility.

---

## Phase 0 — Baseline Stabilisation (NOW)

**Objective:** Ensure the existing platform is internally consistent and testable.

### Tooling

* [ ] Validate and freeze the configuration GUI (parameters, persistence, error handling)
* [ ] Ensure GUI reflects module metadata (SKU, readiness, capabilities)

### Metadata & CI

* [ ] Finalise readiness schema and CI enforcement
* [ ] Enforce:

  * valid SKU in every module
  * readiness declared in `description.yaml`
  * QC requirements for ALPHA / REFERENCE modules
* [ ] Add CI checks for missing QC artifacts on REFERENCE modules

---

## Phase 1 — Core Signal Qualification (Highest Priority)

**Objective:** Establish **measurement credibility** for CleverHand’s sensing and actuation.

### Modules — EMG (critical path)

* [ ] Evaluate ADS1293 module

  * noise floor
  * bandwidth
  * gain accuracy
  * stability (long run)
* [ ] Evaluate ADS1298 module
* [ ] Evaluate INA333 module
* [ ] Promote **one EMG module** to REFERENCE status (after FULL QC)

### Modules — IMU

* [ ] Evaluate ICM-20948 module

  * timing stability
  * drift
  * noise characteristics

### Modules — Electro-tactile

* [ ] Evaluate FES module

  * output range
  * waveform fidelity
  * safety envelope (research use)

### Modules — Vibro-tactile

* [ ] Evaluate STSPIN240 module

  * amplitude control
  * latency
  * repeatability

**Deliverables (Phase 1 exit criteria):**

* At least one **REFERENCE-grade sensor module**
* At least one **REFERENCE-grade actuator module**
* QC profiles + passing QC reports committed

---

## Phase 2 — Interface & Contact Evaluation

**Objective:** Understand and document **human–device coupling quality**.

### Interfaces

* [ ] Evaluate raw PCB pad impedance (skin contact)
* [ ] Evaluate copper spheres
* [ ] Evaluate gold-plated cylinders
* [ ] Evaluate jack extension module
* [ ] Compare repeatability and comfort across interfaces

**Deliverables:**

* Quantified comparison tables
* Clear recommendations per use case (EMG density vs comfort vs stability)

---

## Phase 3 — Mechanical Integration & Wearability

**Objective:** Make CleverHand **usable on the body**, not just on the bench.

### Casings & Supports

* [ ] Design casing for individual modules
* [ ] Design casing for controller
* [ ] Design semi-rigid placement grid (modular body layout)
* [ ] Design flexible bracelet for arm placement
* [ ] Design flexible mesh for torso placement

**Constraints:**

* No electrical redesign unless strictly required
* Mechanical designs must remain open and reproducible

---

## Phase 4 — Software & SDK Consolidation

**Objective:** Make CleverHand **easy to integrate into existing research workflows**.

### SDKs & Interfaces

* [ ] Validate C++ SDK
* [ ] Validate Python wrapper
* [ ] Create MATLAB wrapper
* [ ] Create ROS node
* [ ] Create LSL interface

**Priority order:**

1. Python
2. LSL
3. MATLAB
4. ROS

**Deliverables:**

* One “golden” acquisition pipeline per language
* Example scripts that match REFERENCE modules

---

## Phase 5 — Documentation & Externalisation

**Objective:** Enable **independent adoption** without direct support.

### Documentation

* [ ] Getting started guide (hardware + software)
* [ ] User manual
* [ ] Developer manual
* [ ] Maintenance manual
* [ ] Troubleshooting guide
* [ ] FAQ
* [ ] Glossary

Documentation must be:

* module-SKU aware
* aligned with readiness levels
* explicit about limitations and non-clinical use

---

## Phase 6 — Reference Stacks & Distribution Readiness

**Objective:** Transition from “platform” to **trusted reference system**.

* [ ] Define 1–2 **reference stacks**

  * controller + COM + sensor + interface (+ actuator)
* [ ] Validate full-stack operation end-to-end
* [ ] Freeze hardware revisions for reference stacks
* [ ] Enable shop access for REFERENCE modules only
* [ ] Publish QC-backed reference demos

---

## Explicit Non-Goals (Until Further Notice)

* ❌ Adding new sensing ICs
* ❌ Adding new communication buses
* ❌ Optimising for mass production
* ❌ Turning CleverHand into a consulting-driven product

---

## Success Criteria (Project-Level)

CleverHand can be considered **stable** when:

* REFERENCE modules exist and are QC-backed
* A new lab can reproduce a demo without direct support
* Documentation answers most onboarding questions
* Hardware, firmware, and software changes slow down naturally

