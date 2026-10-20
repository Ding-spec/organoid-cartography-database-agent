# Organoid Cartography Database Agent

Marker discovery, cell annotation and atlas exploration multi-agents for organoid and tissue single-cell and spatial transcriptomics.

## About

Organoid Cartography Database Agent is a desktop application for marker discovery, cell-type annotation and atlas exploration in organoid and tissue single-cell and spatial transcriptomics.

The application runs on your own machine and processes data locally, so nothing is sent to an external service. Reference data is yours to manage: the installer includes a skin organoid atlas and a default marker database, and both can be replaced or extended with your own files.

## Installation

Download the installer from the [Releases](../../releases) page.

### Windows

```
Organoid-Cartography-Database-Agent-Setup.exe  (~2.10 GB)
```

Run the installer. Administrator rights are not required, and R does not need to be installed separately, because the installer includes the R runtime and the packages the application depends on.

After installation, start **Organoid Cartography Database Agent** from the Start menu or the desktop shortcut. The interface opens in your default browser.

### macOS

Requirements: macOS 15.0 or later, Apple Silicon (`arm64`) or Intel (`x86_64`).

Download **both** files for your architecture from the `macos-2026.10.07` release into the same folder, and keep the names as they are:

```
Organoid-Cartography-Database-Agent-macOS-arm64.dmg
Organoid-Cartography-Database-Agent-macOS-arm64.002.dmgpart
```

The Intel build uses the same file names with `x86_64` instead of `arm64`. The `.dmg` is the first segment of a segmented disk image, so the `.002.dmgpart` file must sit next to it; if it is missing or renamed, macOS reports that there is no mountable file system.

Open the `.dmg`, run the `.pkg` inside it and keep the default destination. The application must be installed in `/Applications` to start correctly. The package is not notarized, so macOS blocks it on first launch: allow it under **System Settings > Privacy & Security > Open Anyway**.

The interface is served locally at `http://127.0.0.1:3838`.

## Usage

### Annotation

- Upload your `FindAllMarkers` file (CSV/TSV/TXT/XLSX) and a reference Marker file.
- Preview matched markers, then set top-N, organism and p-value cutoff. Expert mode adds a cell-type whitelist and blacklist.
- Run the annotation and read the champion and ranking tables.
- Export `cluster_ct_ranking.csv`, the match tables, the plots and `reproduce_annotation.R`.

### OCDAgent

- Search papers and extract markers. View the paper list at the bottom right.
- Upload papers to extract cell types and markers with their references.
- Review the Marker CSV, then use it alone or with OCD for annotation. The original database stays unchanged.

### Explore

- **Organoid Atlas** - Open the Skin atlas or upload your own data to view gene expression, cell annotations and UMAP.
- **Marker Database** - Search for markers. Results appear from highest to lowest score by default.
- **Marker Comparison** - Compare two marker sets, with results sorted by score. Click a Venn region to change the word cloud, then click a marker to find its row in the table.

## System requirements

- Windows 10 / 11 (x64)
- macOS 15.0 or later (Apple Silicon or Intel)
- About 3 GB free disk space on Windows; about 9 GB for the macOS install, including the 2.6 GB download
- Web browser (Edge / Chrome / Firefox)
- Installation takes 4-8 minutes on a typical desktop
- The bundled demo run takes 2-6 minutes on a typical desktop

## Citation

If this software contributes to published work, cite the source repository:

```
Organoid Cartography Database Agent.
https://github.com/Ding-spec/organoid-cartography-database-agent
```

## License

Released under the GNU General Public License v3.0. See [LICENSE](LICENSE).
