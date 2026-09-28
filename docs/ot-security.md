# Secure OT Telemetry Gateway — OT Security Alignment

## Purpose

The gateway is designed as a security boundary between an OT environment and IT/cloud systems.

The design applies common OT security principles including network segmentation, defense in depth, least privilege and controlled communication.

## IEC 62443 Alignment

### Zones and Conduits

The architecture separates:

- OT devices / PLCs
- OT network
- OT DMZ
- IT / cloud environment

Communication between zones should occur through controlled conduits and explicitly permitted network paths.

### Defense in Depth

Security is implemented through multiple layers:

- Network segmentation
- Authentication
- Input validation
- Secure configuration
- Container isolation
- Dependency scanning
- Container vulnerability scanning
- Logging and monitoring

### Least Privilege

The gateway container runs as a non-root Linux user.

Production deployment should additionally restrict:

- Linux capabilities
- Filesystem access
- Network exposure
- Container resources

## NIS2 Alignment

The architecture supports several NIS2-relevant security practices:

- Risk management
- Access control
- Vulnerability management
- Incident detection and response
- Business continuity considerations
- Supply-chain security
- Security monitoring

NIS2 is a governance and risk-management framework rather than a specific implementation blueprint. The controls in this project represent technical measures that can contribute to those requirements.

## NCSC Cyber Assessment Framework Alignment

The project maps conceptually to the CAF areas:

### Governance

Security requirements and architectural decisions are documented.

### Protecting Against Cyber Attack

- Authentication
- Input validation
- Network segmentation
- Least privilege
- Dependency management
- Container hardening

### Detecting Cyber Security Events

Authentication failures are logged.

Production environments should forward security events to centralized monitoring or SIEM platforms.

### Minimising the Impact of Incidents

The architecture separates OT from IT systems and limits communication paths.

Production environments should additionally implement incident response, backup and recovery procedures.

## OT-Specific Security Considerations

OT environments differ from conventional IT environments because availability and safety can be critical.

Security controls therefore need to consider:

- Safety impact
- Availability requirements
- Deterministic communications
- Legacy systems
- Patch constraints
- Change management
- Asset inventory
- Incident response
- Recovery requirements

A production implementation should avoid introducing controls that could unintentionally disrupt critical industrial processes.

## POC Limitations

This project is a security-focused proof of concept.

It does not implement:

- A physical PLC
- A real industrial protocol such as Modbus/TCP or OPC UA
- A physical OT network
- Production firewall segmentation
- Production TLS certificates
- A real SIEM
- A production cloud deployment

The simulator uses HTTP locally to demonstrate the application and security controls.

The production architecture would place the gateway behind controlled network boundaries and use appropriate industrial protocols and encrypted communication where required.
