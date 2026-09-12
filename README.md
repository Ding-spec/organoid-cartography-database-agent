# Organoid Cartography Database: Local cell-type annotation for spatial and single-cell transcriptomics

**NOTE**: This repository distributes the official Windows installer for
**Organoid Cartography Database**. The full project source code (R Shiny
frontend + Python OCDAgent backend + Inno Setup build pipeline) lives in a
separate development repository
(<https://github.com/Ding-spec/organoid-cartography-database-app>).

### Organoid Cartography Database

[](https://github.com/Ding-spec/organoid-cartography-database-agent#organoid-cartography-database)

A local, GUI-driven cell-type annotation environment for organoid and tissue
single-cell / spatial transcriptomics.

### Installation

[](https://github.com/Ding-spec/organoid-cartography-database-agent#installation)

Download the Windows installer from the
[Releases](../../releases) page:

```
Organoid-Cartography-Database-Setup.exe  (~2.11 GB)
```

Double-click the installer; the installer is **lowest-privilege and no admin
rights required**. The installer ships its own R runtime and required
CRAN packages, and no need to install R separately.

After installation, launch **Organoid Cartography Database** from the Start
menu or the desktop shortcut. The application opens in your default browser.

### Usage

[](https://github.com/Ding-spec/organoid-cartography-database-agent#usage)

The typical workflow inside the app:

1. **Welcome** - review application overview.
2. **Data import** - upload your `FindAllMarkers` CSV/TSV/TXT/XLSX and your
   reference Marker Excel/CSV.
3. **Marker preview** - inspect matched markers; expand rows to see marker
   scores, paper titles and journal IFs.
4. **Parameter settings** - choose expert vs normal mode, top-N, organism,
   p-value filter and (in expert mode) whitelist/blacklist cell types.
5. **Run annotation** - launch the annotation; review the champion table,
   ranking table and detailed marker matches.
6. **Visualizations** - inspect bar / heatmap / count / dot plots (9-color
   scheme).
7. **Downloads** - export `cluster_ct_ranking.csv`, detailed match tables,
   metrics ZIP, four high-resolution PDF plots, and a self-contained
   `reproduce_annotation.R`.

### System requirements

[](https://github.com/Ding-spec/organoid-cartography-database-agent#system-requirements)

- Windows 10 / 11 (x64)
- ~3 GB free disk space for installation
- Web browser (Edge / Chrome / Firefox)

### Citation

[](https://github.com/Ding-spec/organoid-cartography-database-agent#citation)

If you use Organoid Cartography Database in published research, please cite
the source repository:

```
Organoid Cartography Database.
https://github.com/Ding-spec/organoid-cartography-database-app
```

### License

[](https://github.com/Ding-spec/organoid-cartography-database-agent#license)

This release distribution is licensed under the **GNU General Public License
v3.0** - see the [LICENSE](LICENSE) file for details.