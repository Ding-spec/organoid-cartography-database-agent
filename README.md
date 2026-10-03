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

1. **Welcome** - read the application overview.
2. **Data import** - load your `FindAllMarkers` file (CSV/TSV/TXT/XLSX) and a reference marker file (Excel/CSV).
3. **Marker preview** - check the matched markers; expand a row for scores, paper titles and journal impact factors.
4. **Parameter settings** - pick normal or expert mode, top-N, organism and p-value cutoff. Expert mode adds cell-type whitelist and blacklist.
5. **Run annotation** - start the annotation and read the champion table, ranking table and detailed marker matches.
6. **Visualizations** - bar, heatmap, count and dot plots, in a 9-colour scheme.
7. **Downloads** - export `cluster_ct_ranking.csv`, detailed match tables, a metrics ZIP, four high-resolution PDF plots and a self-contained `reproduce_annotation.R`.

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
