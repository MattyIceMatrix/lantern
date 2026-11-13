# Security Policy

```text
      .--------.
     / .------. \        Found a vulnerability?
    / /        \ \       Tell us privately first.
    | |        | |       We fix, then we disclose together.
   _| |________| |_
 .' |_|        |_| '.
 '._____ ____ _____.'
 |     .'____'.     |
 '.__.'.'    '.'.__.'
 '.__  | LOCK |  __.'
 |   '.'.____.'.'   |
 '.____'.____.'____.'
```

## Supported versions

| Version | Supported |
| --- | --- |
| `main` | Yes |
| tagged releases `>= 1.0.0` | Yes, latest minor only |
| anything older | No |

## Reporting a vulnerability

**Do not open a public issue.** Use GitHub's private vulnerability reporting:
*Security* tab -> *Report a vulnerability*.

Please include:
- the affected component (`guardian/`, `sync/`, `brain/` ...) and commit
- steps to reproduce, or a proof of concept
- the impact you expect (for example: bypass a Guardian rule, leak survivor data, forge a sync record)

## What to expect

| Step | Target time |
| --- | --- |
| Acknowledgement | 5 working days |
| First assessment and severity (CVSS v4) | 10 working days |
| Fix or mitigation plan | 30 days for High/Critical |
| Coordinated disclosure | after the fix ships, credited unless you ask otherwise |

LANTERN is a volunteer prototype maintained by one person, so these are targets, not guarantees.

## Scope

In scope: everything in this repository, especially the Guardian policy engine, audit log, privacy
pseudonymisation, and sync signing.

Out of scope: third-party dependencies (report upstream; we will track the advisory), map data providers,
and findings that need physical access to an unattended kit.

## Safe harbour

Good-faith research that follows this policy, avoids privacy violations and does not degrade anyone's
service will not be pursued by the maintainer.
