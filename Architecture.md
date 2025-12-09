# 🏗 DMA CLI – Architecture Overview

DMA CLI follows a modular architecture designed for maintainability and extensibility.

## 🔷 High-Level Structure
automation_project/
 ├── dma/                    # Python package containing all automation modules
 ├── scripts/                # Dev-side helper scripts (auto-push, bump version)
 ├── data/                   # Input CSVs, AI insights, generated reports
 ├── build_deb/              # Debian package filesystem tree
 ├── docs/                   # Internal documentation
 ├── schedule/               # Cron-like scheduler runtime
 └── logs/                   # System logs & reports

## 🔥 Core Principles
- Package-first: everything under `dma/` forms the public Python API
- CLI-driven execution (`marketing-cli`)
- Modular task execution (analyze / report / visualize / email)
- Debian package deployable (`dma-cli`)
- Zero manual configuration (auto paths)
