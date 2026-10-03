# Organoid Cartography Database Agent

Marker discovery, cell annotation and atlas exploration multi-agents for organoid and tissue single-cell and spatial transcriptomics.

## About

Organoid Cartography Database Agent is a desktop application for Windows. You install it on your own machine and open it from the Start menu. There is no server to deploy, no account to create, and no command line to learn.

It runs entirely on your computer. Datasets, marker lists and annotation results stay on your machine and are never uploaded anywhere, so unpublished or sensitive data remains under your own control.

You also control the reference data. The app ships with a built-in organoid atlas and a default marker set so you can start right away, and you can swap in your own `FindAllMarkers` output and reference marker files whenever you need to. Updating the reference data is your call, not something the application decides for you.

## Installation

Download the Windows installer from the [Releases](../../releases) page:

```
Organoid-Cartography-Database-Agent-Setup.exe  (~2.10 GB)
```

Double-click the installer. It does not require administrator rights and you do not need to install R yourself, because the installer carries its own R runtime and the CRAN packages the application needs.

When installation finishes, launch **Organoid Cartography Database Agent** from the Start menu or the desktop shortcut. The application opens in your default browser.

## Usage

### Annotation

- Upload your `FindAllMarkers` file (CSV/TSV/TXT/XLSX) and a reference Marker file.
- Preview matched markers, then set top-N, organism and p-value cutoff. Expert mode adds a cell-type whitelist and blacklist.
- Run the annotation and read the champion and ranking tables.
- Download `cluster_ct_ranking.csv`, the match tables, the plots and `reproduce_annotation.R`.

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
- About 3 GB free disk space for installation
- Web browser (Edge / Chrome / Firefox)
- Install takes roughly 4-8 minutes on an ordinary desktop
- The bundled demo run takes roughly 2-6 minutes on an ordinary desktop

## Citation

If Organoid Cartography Database Agent contributes to published work, please cite the source repository:

```
Organoid Cartography Database Agent.
https://github.com/Ding-spec/organoid-cartography-database-app
```

## License

This release distribution is licensed under the **GNU General Public License v3.0**. See the [LICENSE](LICENSE) file for details.
