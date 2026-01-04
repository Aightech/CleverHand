# CleverHand — Hardware Module Checklist

This checklist defines the **minimum requirements** for introducing a new
hardware module into the CleverHand ecosystem.

Modules that do not satisfy these requirements may exist experimentally,
but **cannot be considered reference-grade or eligible for distribution**.

---

## 1. Identity & Scope
- [ ] Clear module purpose (sensor / feedback / interface / controller)
- [ ] Fits CleverHand modular architecture
- [ ] SKU defined and compliant with `specs/sku.schema.yaml`
- [ ] No overlap with existing module without justification

---

## 2. Hardware Design
- [ ] KiCad schematic complete and readable
- [ ] PCB layout clean, annotated, and versioned
- [ ] Power domains clearly defined
- [ ] Interfaces documented (connectors, pinout)
- [ ] No proprietary or NDA-bound components

---

## 3. Manufacturing
- [ ] BOM complete and reproducible
- [ ] PCB manufacturable with standard fabs
- [ ] Assembly feasible via manual or PCBA
- [ ] Known assembly risks documented

---

## 4. Documentation
- [ ] Module README present in hardware repo
- [ ] Datasheet created in `docs/modules/<SKU>.md`
- [ ] Intended use cases described
- [ ] Known limitations listed

---

## 5. Firmware / Software (if applicable)
- [ ] Firmware builds cleanly
- [ ] Communication protocol documented
- [ ] Example usage available (Python / C++ / GUI)

---

## 6. Quality Control
- [ ] QC metrics defined (noise, bandwidth, latency, etc.)
- [ ] Test procedure documented
- [ ] Pass/fail criteria defined
- [ ] Repeatability assessed

---

## 7. Ethics & Safety
- [ ] On-body risks considered
- [ ] Electrical safety constraints documented
- [ ] Clear statement of non-clinical use

---

A module that passes all sections may advance to **Reference** status.
