# Settings integration inventory

`normalized-manifest.json` consolidates 41 reviewed previews and the separate CA-R-1404 successor: 42 proposals over 42 predecessor sources. It records each source and candidate digest and whether the Summary changes. All source and preview hashes matched at inventory time; no two proposals edit the same source. Future concurrent edits require a new preflight; merge overlapping semantic edits into one reviewed successor rather than applying previews independently.

Two proposals are new-ID successors, not same-ID renames: CA-R-1750 and CA-R-1404. Allocate distinct IDs, retain their exact predecessor bytes and frozen versioned references, retire the superseded Current rules through the selected lifecycle, and reconcile operative references atomically. Existing preview placeholders are not publishable IDs.

The native Current carrier reader was applied to all text-search hits in non-derived Current source folders, excluding drafts, archives, projected methodology, analyses and completed plans; it returned no parse errors. The operative unversioned references are:

- CA-R-622 refers to CA-R-1750 twice, and CA-E-459 once. Their already-reviewed combined previews reconcile the old split and contain the successor placeholder. Replace that placeholder with the allocated CA-R-1750 successor ID; do not apply separate reference-only patches over their combined edits.
- CA-R-1981 references CA-R-1404. Its Summary and Claim identify the Framework Settings physical Carrier, whereas the proposed successor constrains the Project.Settings Property. A mechanical reference swap would conflate these targets. Hold this source for a semantic decision and use a new identity if its Summary must change, or retire it only under an authorized lifecycle.

These previews do not establish how existing physical TOML carriers move or reconcile conflicting values. The separately held settings sources, D387 carrier coordination and retry-lane work remain outside this inventory. No Current source or Git state was changed.
