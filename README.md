# Organoid Cartography Database - Agent Releases

This repository distributes the Windows installer for **Organoid Cartography
Database**, a local Shiny application for cell-type annotation of
single-cell and spatial transcriptomics data.

The Windows installer is published as a GitHub Release asset; the git history
of this repo only contains this README and a project-level `.gitignore`.

## Latest release

See the Releases page for the latest `v*` tag.

## Source code

Full project source (R Shiny app, Python OCDAgent backend, Inno Setup build
pipeline) lives at:
<https://github.com/Ding-spec/organoid-cartography-database-app>

## Installation

1. Download the `Organoid-Cartography-Database-Setup.exe` asset from the
   latest release.
2. Double-click to install. No admin rights are required (lowest-privilege
   Inno Setup installer).
3. Launch **Organoid Cartography Database** from the Start menu or desktop
   shortcut. A private R runtime and all required CRAN packages are bundled
   - no need to install R separately.

## Feedback

Open an issue on the source repository:
<https://github.com/Ding-spec/organoid-cartography-database-app/issues>