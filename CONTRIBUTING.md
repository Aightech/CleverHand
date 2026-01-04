# Contributing to CleverHand

Thank you for your interest in contributing to **CleverHand**.
CleverHand is an open-source, research-oriented **Human–Machine Interface (HMI) platform**, spanning hardware, firmware, software, and documentation.

Contributions are welcome — but to keep the project usable, reproducible, and maintainable, we follow a few clear rules.

Please read this document before opening issues or pull requests.

---

## Project principles (read first)

CleverHand is guided by the following principles:

* **Open by design**
  All contributions must be compatible with the project’s open-source licenses.

* **Research-grade, not consumer-grade**
  Signal quality, traceability, and clarity matter more than convenience or speed.

* **Stability over churn**
  We prefer fewer, well-documented modules over many experimental ones.

* **Architecture first**
  New features must fit the existing modular architecture.

If your contribution conflicts with these principles, it is unlikely to be accepted.

---

## What you can contribute

### Hardware

* New modules (sensing, feedback, interfaces)
* Improvements to existing KiCad designs
* Manufacturing or test-jig improvements
* Documentation inside module directories

### Firmware

* Module firmware
* Communication improvements
* New firmware profiles
* Bug fixes and performance improvements

### Software

* Host-side APIs (Python, C++, LSL)
* Tools for configuration, streaming, or analysis
* Documentation and examples

### Documentation

* Module datasheets
* Tutorials and experiments
* Diagrams and clarifications
* Typo fixes and readability improvements

---

## What is *not* accepted

* Closed-source or partially closed contributions
* Features that break backward compatibility without strong justification
* One-off hacks tied to a specific experiment without general value
* Undocumented hardware or firmware changes
* SKU or naming changes without updating the relevant specs

---

## Repository structure (high level)

Please respect the project structure:

```
hardware/        → physical designs (KiCad, manufacturing)
firmware/        → embedded code
software/        → host-side tools and libraries
docs/            → user-facing documentation
catalog/         → module and bundle registry (YAML source of truth)
specs/           → rules (SKU format, QC requirements, readiness levels)
tools/           → generators and validators (no heavy frameworks)
```

Generated files (`*.json`, `*.csv`) must **never** be edited by hand.

---

## Contribution workflow

### 1. Open an issue (recommended)

Before starting significant work:

* describe what you want to add or change
* explain the motivation and expected impact
* link to relevant modules or specs

This avoids wasted effort and misalignment.

---

### 2. Fork and branch

* Fork the repository
* Create a feature branch with a clear name:

  ```
  feat/emg-qc-improvement
  fix/imu-timing-bug
  docs/emg-datasheet
  ```

---

### 3. Follow project conventions

#### Naming & SKUs

* All new modules must follow the SKU format defined in `specs/sku.schema.yaml`
* SKUs are **immutable once published**
* Assembly, colour, or packaging must be metadata — not part of the SKU

#### Documentation

* Every module **must** have:

  * a module README (hardware)
  * a SKU-linked datasheet in `docs/modules/`
* Claims about performance must be measurable or clearly marked as expected

#### Hardware

* KiCad files only (no PDFs as source)
* Schematics and PCB must be readable and annotated
* Electrical changes require a new revision or SKU

#### Firmware / Software

* Prefer clarity over cleverness
* Avoid unnecessary dependencies
* Include minimal examples where relevant

---

### 4. Test your changes

Before submitting a PR:

* ensure existing functionality still works
* run relevant tools or scripts
* update documentation if behaviour changes

If your contribution affects data quality, include:

* measurement method
* test setup
* limitations

---

### 5. Open a Pull Request

In your PR description, include:

* what changed
* why it changed
* which modules are affected
* any breaking changes

PRs without a clear description may be closed.

---

## Licensing (important)

By contributing to CleverHand, you agree that your contributions will be licensed under the project’s existing licenses:

* **Software / firmware:** Apache License 2.0
* **Hardware designs:** CERN Open Hardware Licence v2 – Strongly Reciprocal
* **Documentation:** Creative Commons Attribution 4.0

You must have the right to contribute the material you submit.

---

## Code of conduct

Be respectful and constructive.

CleverHand is a technical, research-oriented project.
Discussions should stay focused on engineering, science, and usability.

Harassment, hostility, or bad-faith behaviour will not be tolerated.

---

## Contact

If you are unsure whether your contribution fits the project, or if you want to discuss a larger idea:

* Open an issue
* Or contact the maintainer directly via GitHub

Thoughtful contributions are always welcome.

---

**Thank you for helping build an open, reproducible HMI platform.**
