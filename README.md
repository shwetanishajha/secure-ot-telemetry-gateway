# Secure OT Telemetry Gateway

A security-focused Python gateway for securely receiving telemetry from Operational Technology (OT) environments and exposing controlled data to IT/cloud systems.

This project demonstrates practical software engineering, application security, Linux, networking, Docker, DevSecOps, infrastructure-as-code and OT security architecture.

## Architecture

```text
OT Devices / PLCs
       |
       v
   OT Network
       |
       v
Controlled Boundary
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
HTTPS / REST
       |
       v
IT / Cloud
The gateway acts as a controlled application boundary between OT and IT environments.

## Technology Stack
Area	Technology
Language	Python
API	FastAPI
Validation	Pydantic
Application server	Uvicorn / ASGI
Operating system	Linux
Networking	TCP/IP, HTTP/HTTPS
Authentication	API key
Containerisation	Docker
Infrastructure as Code	Terraform
CI/CD	GitHub Actions
Dependency security	pip-audit
Container security	Trivy
Testing	pytest
Version control	Git / GitHub
## Security Controls

The project demonstrates:

API authentication
Input validation
Authentication audit logging
Environment-based secret configuration
Secrets excluded from source control
Non-root container execution
Dependency vulnerability scanning
Container image vulnerability scanning
Network segmentation architecture
Least privilege
Defense in depth

Detailed security documentation:

docs/threat-model.md — STRIDE threat model
docs/owasp-mapping.md — OWASP security mapping
docs/ot-security.md — IEC 62443, NIS2 and NCSC CAF alignment
docs/architecture.md — solution architecture
## DevSecOps Pipeline

Changes pushed to GitHub trigger:

Git Push
   |
   v
Automated Tests
   |
   v
Dependency Security Scan
   |
   v
Docker Build
   |
   v
Container Vulnerability Scan

The pipeline is implemented using GitHub Actions.

## Infrastructure as Code

Terraform defines the target AWS network architecture:

AWS VPC
 |
 +-- OT DMZ Subnet

The Terraform configuration is located in:

terraform/main.tf

The configuration has been validated locally using:

terraform fmt
terraform validate

The POC does not provision an AWS environment.

## Running Locally
### Configure the API key

Create .env:

OT_API_KEY=your-api-key

The .env file is excluded from Git.

### Install dependencies
pip install -r requirements.txt
### Start the API
uvicorn app.main:app --host 0.0.0.0 --port 8000
### Check health
curl http://localhost:8000/health

Expected response:

{"status":"healthy"}
### Send telemetry
curl -X POST http://localhost:8000/telemetry \
  -H "Content-Type: application/json" \
  -H "X-API-Key: your-api-key" \
  -d '{
    "device_id": "PLC-001",
    "temperature": 25.5,
    "pressure": 5.2,
    "status": "NORMAL"
  }'
## Running with Docker

Build the image:

docker build -t secure-ot-gateway .

Run the container:

docker run --rm \
  -p 8000:8000 \
  --env-file .env \
  secure-ot-gateway

The container runs the application as a non-root user.

## Testing

Run:

pytest

The test suite covers:

API health endpoint
Input validation
Authentication enforcement
## OT Security Model

The target production architecture applies:

OT/IT separation
OT DMZ
Controlled network conduits
Defense in depth
Least privilege
Authentication
Input validation
Security monitoring
Vulnerability management

The design is aligned conceptually with:

IEC 62443
NIS2
NCSC Cyber Assessment Framework
OWASP security principles
## Threat Model

The project uses STRIDE to consider:

Spoofing
Tampering
Repudiation
Information Disclosure
Denial of Service
Elevation of Privilege

The detailed threat model is available in:

docs/threat-model.md

## Production Considerations

A production implementation would additionally consider:

TLS/mTLS
Managed secret storage
Firewall policies
Network allow-listing
Rate limiting
Centralized logging / SIEM
Container resource limits
Read-only container filesystem
Linux capability restrictions
Vulnerability management
Incident response
Backup and recovery
High availability where required
Real OT protocols such as Modbus/TCP or OPC UA

OT environments require particular consideration of safety, availability, legacy systems and controlled change management.

## POC Limitations

This repository is a proof of concept rather than a production OT deployment.

It does not implement:

A physical PLC
A production OT network
A production firewall
A real industrial protocol
A production SIEM
A production cloud deployment

The simulator uses HTTP locally to demonstrate the application and security controls.

The architecture documents show how these components would fit into a production-oriented design.

## Project Objective

The objective is not simply to demonstrate a Python API.

The project demonstrates how an engineer can take a system requirement and consider it end-to-end:

Requirements
     |
     v
Architecture
     |
     v
Application Design
     |
     v
Security Controls
     |
     v
Linux / Networking
     |
     v
Containerisation
     |
     v
Testing
     |
     v
DevSecOps
     |
     v
Infrastructure as Code
     |
     v
OT Security

This reflects a secure-by-design engineering approach.
