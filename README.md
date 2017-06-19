# Extreme-scale Simulation of Supernovae and Magnetars from Realistic Progenitors

What's the driving question? Is the neutrino mechanism the right mechanism? What's missing from it? Progenitor structure, for sure. (Maybe vector spherical harmonics.) But perhaps also MHD and rotation. All stars rotate and have B-fields. MRI: may not be important for slow rotators? May not need to FULLY resolve so long as it reaches saturation!

What's needed is MANY simulations in MULTIPLE progenitors...

Plus a Hero simulation...

Maybe go for a progenitor calculation?? Maybe MHD... Initialize with random field. Or mixed vector potential: Part poloidal part toroidal.

Modification of Tayler-Spruit dynamo for prediction of B-field evolution...

Connection to observations: nucleo and explosion energy (need late time)

3D perturbations - Progenitors

Include FieldLoop comparison with CT, including divB

SSP RK2 and SSP RK3

Kill your darlings - no RK3 in spark! but RK3 in M1 is GTG and stable to CFL 1.0\. Formally more accurate than sub-cycling.

Adaptive stepping with error control

Low-mass iron cores

Gravitational waves!

BH formation... in 3D!! Spin of black hole???

R-process

Marching cubes for EOS/EAS

A new fiducial test case model built off of VERACity work, etc.

Domain-specific task scheduler

Potential to scale to pre-exascale!

SIMpliPy + yt + in-situ

Predictions: The hero simulations provide CRUCIAL calibration!

Multi-D progenitors could explain remnants like Cas A and pre-SN eruptions.

## Objectives

List of simulations

- 3D non-rotating 20 Msun progenitor
- 3D rotating 20 Msun progenitor
- 3D magnetic rotating 20 Msun progenitor
- 3D magnetic rotating 12 Msun CCSN
- 3D magnetic rotating 15 Msun CCSN
- 3D magnetic rotating 20 Msun CCSN
- 3D magnetic rotating 25 Msun CCSN
- 3D CCSN with non-rotating 20 Msun progenitor
- 3D late-time CCSN for nucleo, etc.

Evan needs to write something about our neutrino opacity fidelity.

## Pre-Year 1

- 20-Msun 3D non-rotating (NR) progenitor simulation

## Year 1

What is required to form a magnetar?

### Mira 8192 run A (64M):

- 10 Msun MHD fast rot
- 10 Msun MHD slow rot
- 20 Msun MHD fast rot
- 20 Msun MHD slow rot

### Mira 8192 run B (20M):

- 10 Msun MHD fast rot progen sim
- 10 Msun MHD slow rot progen sim
- 20 Msun MHD fast rot progen sim
- 20 Msun MHD slow rot progen sim

### Mira 8192 run C (60M):

- Hero sim: 0.65 km throughout the gain region! 60 Million core-hours (most promising MHD)

### Theta capability run A (8M):

- 20 Msun NR 3D progen non-mag
- 20 Msun NR 1D progen non-mag
- 10 Msun NR 1D progen non-mag
- 15 Msun NR 1D progen non-mag

two progenitors, different rot/B

15 Million on progenitors. One capability job of multiple progenitor sims: 2048 nodes a piece

One M1 sim on Mira: 16 Million hours (0.65 km resolution)

Low-res sims on Mira (1.0 km out to 80 km): 2 Million core-hours

One M1 sim on Theta: 2 million hours (!!)

The non-rotating cases will be done by other SciDAC collabs

## Year 2

Use of NEW MHD solver (differential transforms or something)

Shift toward Theta as primary machine

Improved opacities/EOS from TEAMS

### Mira 8192 run A (64M):

Long time scales! Continue some of the medium res runs from Year 1\. Same physics.

- 10 Msun MHD fast rot late times
- 10 Msun MHD slow rot late times
- 20 Msun MHD fast rot late times
- 20 Msun MHD slow rot late times

### Mira 8192 run B (60M):

MRI in PNS run. Fast rot 3D progen with AMR trick at edge of PNS (15 km to 40 km). 60 million

### Mira 8192 run C (20M):

- 15 Msun MHD fast rot progen sim
- 15 Msun MHD slow rot progen sim
- 25 Msun MHD fast rot progen sim
- 25 Msun MHD slow rot progen sim

### Theta capability run A (8M):

- 10 Msun MHD fast rot 3D progen ccsn sim
- 10 Msun MHD slow rot 3D progen ccsn sim
- 20 Msun MHD fast rot 3D progen ccsn sim
- 20 Msun MHD slow rot 3D progen ccsn sim

### Theta capability run B (8M):

Some other parameter varied? - Inclusion of NES?

## Year 3

Incorporation of AMReX capability? Task parallelism? Parallel in time?

MRI sims to explosion phase - maybe derefine?

Progenitor sims now with MAESTRO - Do some 3D sims with those progenitors! Imposed B-fields....

No Mira. Mostly Theta and...

Aurora - All the Damn Sims I Want. Seriously. Like 20 3D M1 sims.

20M on Theta? 100M on Aurora..... Speak in terms of simulation goals.

Fit even better in MCDRAM

## Allocation pools available for this call:

- Titan (Cray XK7) [2018, 2019]
- Mira (IBM Blue Gene/Q) [2018, 2019]
- Theta (Cray XC40) [2018, 2019, 2020]
- Summit (IBM / nVIDIA) [2019, 2020]
- Aurora (Intel/Cray) [2020]
