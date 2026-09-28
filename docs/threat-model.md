# Secure OT Telemetry Gateway — Threat Model

## 1. Scope

This threat model covers the telemetry flow from OT devices through the OT network and OT DMZ to the Secure OT Telemetry Gateway and downstream IT/cloud systems.

## 2. Architecture

```text
OT Devices / PLCs
       |
       v
   OT Network
       |
       v
Firewall / Controlled Boundary
       |
       v
     OT DMZ
       |
       v
Linux Host + Docker
       |
       v
Secure OT Telemetry Gateway
       |
       v
HTTPS / REST API
       |
       v
IT / Cloud
