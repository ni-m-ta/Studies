# Overview
- a Unix-like operating system kernel first created by Linus Torvalds in 1991. 
- an open-source, community-driven project that has become the basis for many different operating systems, commonly referred to as Linux distributions or distros. Linux is known for its stability, security, and flexibility and is widely used in various environments, from servers and embedded systems to desktop computers and mobile devices.
- open-source
- kernel
    - the core component of OS, responsible for managing hardware resources, providing essential services, and fcilitating communication between software and hardware
- CLI and Shell
- Multitask, multiuser

# Distros
- Red Hat Enterprise Linux
    - a Linux distribution developed by Red Hat, Inc
    - a reliable and scalable platform for business-critical applications, data center operations, and cloud environments

# Security
- Audit subsystem
    - responsible for tracking security-related events on the system
    - capture a wide range of activities, such as system calls, file access, user logins, and more.
    - Audit rules
        - define the conditions under which events are logged
    - Audit events
        - audit.log
    - Event types
        - covers various categories, i
    - Common fields in audit logs
        - Type: Type of audit event (e.g. SYSCALL)
        - Timestamp
        - User
        - Success/Failure
        - Details
    - SELinux integration
        - On systems with Security-Enhanced Linux (SELinux) enabled, the audit logs often include information related to SELinux contexts and permissions
    - 
