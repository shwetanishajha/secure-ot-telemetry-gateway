# Secure OT Telemetry Gateway — Architecture

## 1. Purpose

The Secure OT Telemetry Gateway provides a controlled and secure interface for collecting telemetry from industrial OT devices and exposing validated telemetry to authorised IT or cloud systems.

The solution demonstrates secure software engineering, networking, API security, containerisation, infrastructure-as-code and DevSecOps practices in an OT/ICS context.

## 2. High-Level Architecture

```text
┌─────────────────────────────────────────────────────────────┐
│                         IT / CLOUD                          │
│                                                             │
│  Applications / Analytics / Monitoring                     │
└───────────────────────────▲─────────────────────────────────┘
                            │
                     HTTPS / REST API
                            │
┌───────────────────────────┴─────────────────────────────────┐
│                           OT DMZ                            │
│                                                             │
│              Secure OT Telemetry Gateway                   │
│                                                             │
│  Python / FastAPI                                          │
│  ├── Authentication                                         │
│  ├── Input Validation                                       │
│  ├── Security Logging                                      │
│  └── Telemetry API                                         │
│                                                             │
└───────────────────────────▲─────────────────────────────────┘
                            │
                     Controlled OT Traffic
                            │
┌───────────────────────────┴─────────────────────────────────┐
│                      OT / ICS NETWORK                       │
│                                                             │
│       PLC / Industrial Devices / Sensors                   │
│                                                             │
└─────────────────────────────────────────────────────────────┘

## 3. Data Flow

1. Industrial devices such as PLCs generate telemetry.
2. Telemetry is sent across the controlled OT network towards the gateway.
3. The gateway authenticates the requesting system.
4. Incoming telemetry is validated against defined data constraints.
5. Valid telemetry is processed by the FastAPI application.
6. Authentication events are recorded in security logs.
7. Authorised IT or cloud systems consume telemetry through the API.

### Security Boundary

The OT DMZ acts as a controlled boundary between the industrial OT environment and the IT/cloud environment.

The gateway is the controlled entry and exit point rather than allowing direct connectivity between OT devices and external systems.

## 4. Security Controls

The gateway applies security controls at multiple layers:

| Control | Implementation |
|---|---|
| Authentication | API key authentication |
| Input validation | Pydantic data validation |
| Secret management | Environment variables |
| Audit logging | Authentication success/failure logging |
| Testing | Automated API security and validation tests |
| Network isolation | OT / DMZ / IT separation |
| Least privilege | Planned non-root container execution |
| Secure delivery | Planned CI/CD security checks |
| Infrastructure security | Planned Terraform-managed infrastructure |

### Security Principles

- Defence in depth
- Least privilege
- Network segmentation
- Secure-by-design development
- Separation of OT and IT environments
- Secrets must not be stored in source code
- Security controls should be automated where possible

## 5. Technology Architecture

| Technology | Role in the solution |
|---|---|
| Python | Core application language |
| FastAPI | REST API framework |
| Pydantic | Telemetry validation |
| Linux | Application/server operating environment |
| TCP/IP + HTTP/HTTPS | Network and API communication |
| Docker | Application containerisation |
| Terraform | Infrastructure as Code |
| GitHub | Source control |
| GitHub Actions | CI/CD automation |
| Security scanning | Automated security validation |
| OT/ICS concepts | Industrial architecture and security context |

### Technology Relationship

```text
                    GitHub
                       │
                       ▼
              GitHub Actions / CI
                       │
             ┌─────────┴─────────┐
             │                   │
          Testing            Security
             │                 Scans
             └─────────┬─────────┘
                       ▼
                    Docker
                       │
                       ▼
                    Linux
                       │
                       ▼
             FastAPI / Python
                       │
                       ▼
                OT DMZ Gateway
                       │
                       ▼
                 OT / ICS


## 6. Key Architecture Decisions

### 6.1 API Gateway Pattern

The telemetry gateway provides a controlled interface between OT systems and IT/cloud consumers.

This avoids exposing OT devices directly to external applications.

### 6.2 API Authentication

The API requires an API key before telemetry can be submitted.

This provides a basic authentication layer and can later be extended to stronger identity mechanisms.

### 6.3 Input Validation

Telemetry is validated before it enters the application.

This reduces the risk of malformed or unsafe data reaching downstream systems.

### 6.4 Environment-Based Secrets

Secrets are stored outside the source code using environment configuration.

This prevents credentials from being committed to source control.

### 6.5 Defence in Depth

Security is implemented across multiple layers rather than relying on a single control.

The target architecture combines application security, network segmentation, container security, infrastructure controls and automated security testing.

## 7. Deployment Architecture

The target deployment separates the application runtime from the underlying infrastructure.

```text
                    ┌─────────────────────┐
                    │     IT / Cloud      │
                    └──────────┬──────────┘
                               │
                            HTTPS
                               │
                    ┌──────────▼──────────┐
                    │       OT DMZ        │
                    │                     │
                    │  Linux Host         │
                    │      │              │
                    │   Docker            │
                    │      │              │
                    │  ┌───▼───────────┐  │
                    │  │ Telemetry     │  │
                    │  │ Gateway       │  │
                    │  │ FastAPI       │  │
                    │  └───────────────┘  │
                    └──────────┬──────────┘
                               │
                        Controlled traffic
                               │
                    ┌──────────▼──────────┐
                    │      OT Network     │
                    │                     │
                    │   PLCs / Devices    │
                    └─────────────────────┘


## 8. Implementation Roadmap

The solution will be implemented incrementally while maintaining the same target architecture.

### Completed

- Python/FastAPI telemetry API
- Input validation
- API key authentication
- Environment-based secret management
- Authentication audit logging
- Automated API tests
- Git/GitHub source control

### Next

1. Linux application environment
2. Networking and security boundaries
3. Docker containerisation
4. Container security
5. Terraform infrastructure-as-code
6. GitHub Actions CI/CD
7. Automated security scanning
8. OT/ICS threat modelling
9. NIS2, NCSC CAF and IEC 62443 security mapping
10. Final architecture and interview walkthrough