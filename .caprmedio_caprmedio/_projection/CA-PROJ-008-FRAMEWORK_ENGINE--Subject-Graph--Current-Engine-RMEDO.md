---
artifact_form: Projection
projection_id: CA-PROJ-008
type: Subject Graph
named_selection: Current-Engine-RMEDO
scope_unit: CA-SU-14
source_of_truth: Current Engine RMEDO source Atom main_subject fields
updated_at: 2026-11-10 22:20:23 +0400
source_atoms: 363
distinct_main_subjects: 75
source_manifest_sha256: f36a6a9289de584f1ae50767a86cd84613cfc010ba136c5141e3a24fb6c5ac51
---

# ENGINE main subjects tree

Built from **363 Current Engine RMEDO source Atoms**. Draft and Archived sources, old Tools, native plugin sources, deferred CA-E-684, held old Tool delegations, and the 501-source benchmark are excluded. Done and Canceled are Current. The source manifest records paths, hashes and exclusions.

This tree shows the exact main subjects used by source Atoms. Indentation groups parser-recognized expression fragments and preserves operators. `[n]` counts Atoms whose exact main subject ends at that node, not descendants. No Definition text is quoted.

## Main subjects

```text
MODEL
  //CAPRMEDIO
    <+ Actor
      /AI Agent [1]
    <+ Atom [1]
    <+ Carrier [1]
    <+ Execution
      /Step Run [1]
      /Workflow Run [2]
    <+ Project [3]
    <+ Projection [17]
    <+ Workspace [1]
PROJECT STRUCTURE
  //CAPRMEDIO [1]
    <+ Aspect
      //Visual Design [2]
    <+ Aspects
      <+ Documentation
        <+ Traceability [1]
      <+ Engineering
        <+ Delivery [1]
          <+ Change Readiness [2]
          <+ Packaging [2]
          <+ Reproducibility [1]
        <+ Development
          <+ Architecture
            <+ Communication [30]
              <+ Interface Contracts [25]
            <+ Component Structure [15]
          <+ Authoring
            <+ Code Authoring [10]
              <+ Python Code [11]
            <+ Prompt Authoring [15]
            <+ Query Authoring
              <+ SQL [2]
          <+ Frontend Engineering
            <+ Code Style [1]
            <+ Libraries and Frameworks [2]
        <+ Operation
          <+ Data Handling
            <+ Configuration [2]
            <+ Data Validation [5]
            <+ Indexing [5]
            <+ Output Publication [6]
            <+ Query Processing [7]
            <+ Schema [6]
            <+ Serialization [1]
            <+ Source Retrieval [4]
            <+ Source Selection [7]
            <+ State Synchronization [2]
          <+ Execution Control [43]
            <+ Code Hot Reload [2]
            <+ Effect Authorization [6]
            <+ Failure Handling [4]
            <+ Outcome Reporting [2]
            <+ Recovery [1]
            <+ Resource Limits [3]
          <+ Observability
            <+ Logging [5]
          <+ Storage [5]
            <+ Directory Layout [4]
            <+ Temporary State [6]
        <+ Quality
          <+ Performance
            <+ Measurement and Profiling [7]
          <+ Traceability [8]
            <+ Provenance [1]
          <+ Verification [1]
            <+ Coverage [3]
            <+ Dynamic Testing [16]
              <+ Canary Testing [1]
            <+ Static Analysis [10]
              <+ Python Code [5]
            <+ Test Data
              <+ Golden Corpora [1]
            <+ Test Design [6]
      <+ UX
        <+ Discovery and Navigation [1]
        <+ Entry [3]
        <+ Guidance [3]
        <+ Interaction [3]
          <+ Accessibility [1]
          <+ Decision [2]
        <+ Result and Status Presentation [5]
    <+ Scope Unit
      //AGENTIC [1]
      //APPS [1]
      //CODEX_EXTENSION [1]
      //CODEX_HOOK [1]
      //CONNECTOR_TOOLS [1]
      //MCP [1]
      //PROGRAMMATIC [1]
      //PROMPTS [1]
      //SKILLS [1]
      //WORKBENCH [1]
      //WORKBENCH_BACKEND [1]
      //WORKBENCH_FRONTEND [1]
```

## Checks

- 75 distinct main-subject expressions; 363 source occurrences.
- Zero missing, unexpected, duplicate, or unparseable selected sources against the reviewed adoption census plus CA-E-819.
- Parser acceptance establishes syntax, not model admission or semantic alignment.

## Source Atom index

| Exact main subject | Atoms | Source Atom IDs |
| --- | ---: | --- |
| MODEL//CAPRMEDIO <+ Actor/AI Agent | 1 | CA-E-817 |
| MODEL//CAPRMEDIO <+ Atom | 1 | CA-M-513 |
| MODEL//CAPRMEDIO <+ Carrier | 1 | CA-D-713 |
| MODEL//CAPRMEDIO <+ Execution/Step Run | 1 | CA-R-1845 |
| MODEL//CAPRMEDIO <+ Execution/Workflow Run | 2 | CA-E-815, CA-R-3016 |
| MODEL//CAPRMEDIO <+ Project | 3 | CA-E-599, CA-R-1900, CA-R-2903 |
| MODEL//CAPRMEDIO <+ Projection | 17 | CA-E-782, CA-E-783, CA-E-786, CA-R-2723, CA-R-2724, CA-R-2725, CA-R-2726, CA-R-2727, CA-R-2728, CA-R-2729, CA-R-2776, CA-R-2782, CA-R-2786, CA-R-2950, CA-R-2952, CA-R-2953, CA-R-2998 |
| MODEL//CAPRMEDIO <+ Workspace | 1 | CA-R-2902 |
| PROJECT STRUCTURE//CAPRMEDIO | 1 | CA-R-3022 |
| PROJECT STRUCTURE//CAPRMEDIO <+ Aspect//Visual Design | 2 | CA-M-469, CA-R-2775 |
| PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Documentation <+ Traceability | 1 | CA-R-2447 |
| PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Delivery | 1 | CA-D-250 |
| PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Delivery <+ Change Readiness | 2 | CA-E-639, CA-M-395 |
| PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Delivery <+ Packaging | 2 | CA-D-674, CA-R-1606 |
| PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Delivery <+ Reproducibility | 1 | CA-D-638 |
| PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development <+ Architecture <+ Communication | 30 | CA-D-523, CA-D-578, CA-D-704, CA-E-259, CA-E-273, CA-E-275, CA-E-279, CA-E-280, CA-E-286, CA-E-311, CA-E-375, CA-E-398, CA-E-584, CA-E-585, CA-E-798, CA-E-811, CA-M-167, CA-M-193, CA-M-341, CA-M-357, CA-M-506, CA-M-514, CA-M-515, CA-R-1096, CA-R-1105, CA-R-1816, CA-R-1884, CA-R-1885, CA-R-2008, CA-R-2449 |
| PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development <+ Architecture <+ Communication <+ Interface Contracts | 25 | CA-D-673, CA-D-706, CA-E-650, CA-E-673, CA-E-683, CA-E-753, CA-E-805, CA-E-806, CA-E-807, CA-E-808, CA-E-809, CA-E-814, CA-E-819, CA-M-222, CA-M-413, CA-M-418, CA-M-471, CA-M-517, CA-R-1107, CA-R-1108, CA-R-1111, CA-R-1112, CA-R-1116, CA-R-2151, CA-R-579 |
| PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development <+ Architecture <+ Component Structure | 15 | CA-E-357, CA-E-358, CA-E-454, CA-E-644, CA-E-648, CA-M-403, CA-M-408, CA-M-432, CA-M-495, CA-M-531, CA-R-1186, CA-R-1187, CA-R-1603, CA-R-1607, CA-R-2430 |
| PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development <+ Authoring <+ Code Authoring | 10 | CA-E-256, CA-E-356, CA-E-359, CA-E-367, CA-E-646, CA-M-402, CA-M-407, CA-M-421, CA-M-498, CA-M-526 |
| PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development <+ Authoring <+ Code Authoring <+ Python Code | 11 | CA-E-253, CA-E-254, CA-E-376, CA-E-377, CA-E-451, CA-E-452, CA-M-406, CA-M-415, CA-M-419, CA-M-423, CA-M-429 |
| PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development <+ Authoring <+ Prompt Authoring | 15 | CA-D-509, CA-D-544, CA-D-545, CA-E-564, CA-M-317, CA-M-326, CA-M-535, CA-R-1185, CA-R-1189, CA-R-1601, CA-R-1801, CA-R-1843, CA-R-1844, CA-R-2451, CA-R-3018 |
| PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development <+ Authoring <+ Query Authoring <+ SQL | 2 | CA-M-468, CA-M-501 |
| PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development <+ Frontend Engineering <+ Code Style | 1 | CA-M-467 |
| PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development <+ Frontend Engineering <+ Libraries and Frameworks | 2 | CA-M-466, CA-M-492 |
| PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Data Handling <+ Configuration | 2 | CA-M-284, CA-M-412 |
| PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Data Handling <+ Data Validation | 5 | CA-E-394, CA-E-812, CA-M-430, CA-M-536, CA-R-1110 |
| PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Data Handling <+ Indexing | 5 | CA-E-677, CA-E-681, CA-E-794, CA-M-465, CA-R-970308628 |
| PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Data Handling <+ Output Publication | 6 | CA-E-277, CA-E-282, CA-E-351, CA-M-329, CA-R-1109, CA-R-1114 |
| PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Data Handling <+ Query Processing | 7 | CA-E-674, CA-E-676, CA-E-784, CA-M-462, CA-M-516, CA-O-240, CA-R-970308627 |
| PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Data Handling <+ Schema | 6 | CA-D-672, CA-E-803, CA-E-804, CA-M-500, CA-M-509, CA-R-970308629 |
| PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Data Handling <+ Serialization | 1 | CA-D-710 |
| PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Data Handling <+ Source Retrieval | 4 | CA-E-675, CA-E-750, CA-M-464, CA-R-565 |
| PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Data Handling <+ Source Selection | 7 | CA-E-810, CA-E-813, CA-M-512, CA-R-1115, CA-R-3013, CA-R-517, CA-R-560 |
| PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Data Handling <+ State Synchronization | 2 | CA-E-781, CA-R-970308630 |
| PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Execution Control | 43 | CA-D-595, CA-E-260, CA-E-261, CA-E-262, CA-E-263, CA-E-264, CA-E-265, CA-E-267, CA-E-268, CA-E-269, CA-E-285, CA-E-309, CA-E-360, CA-E-361, CA-E-362, CA-E-366, CA-E-369, CA-E-370, CA-E-371, CA-E-378, CA-E-392, CA-E-533, CA-E-534, CA-E-565, CA-E-600, CA-E-601, CA-E-679, CA-E-680, CA-E-796, CA-M-322, CA-M-328, CA-M-409, CA-M-425, CA-M-504, CA-O-235, CA-R-1820, CA-R-1846, CA-R-1901, CA-R-3019, CA-R-561, CA-R-562, CA-R-578, CA-R-580 |
| PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Execution Control <+ Code Hot Reload | 2 | CA-E-797, CA-M-505 |
| PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Execution Control <+ Effect Authorization | 6 | CA-E-350, CA-E-399, CA-E-649, CA-E-651, CA-M-404, CA-R-1118 |
| PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Execution Control <+ Failure Handling | 4 | CA-E-566, CA-E-647, CA-E-752, CA-M-396 |
| PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Execution Control <+ Outcome Reporting | 2 | CA-E-645, CA-M-405 |
| PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Execution Control <+ Recovery | 1 | CA-E-352 |
| PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Execution Control <+ Resource Limits | 3 | CA-E-643, CA-M-410, CA-R-1117 |
| PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Observability <+ Logging | 5 | CA-D-709, CA-E-780, CA-E-787, CA-M-414, CA-M-534 |
| PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Storage | 5 | CA-D-711, CA-E-598, CA-M-470, CA-R-1899, CA-R-519 |
| PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Storage <+ Directory Layout | 4 | CA-D-437, CA-D-487, CA-D-488, CA-E-467 |
| PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Storage <+ Temporary State | 6 | CA-D-675, CA-E-785, CA-E-788, CA-M-422, CA-M-463, CA-R-1473 |
| PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Quality <+ Performance <+ Measurement and Profiling | 7 | CA-E-795, CA-E-799, CA-E-800, CA-M-416, CA-M-508, CA-M-525, CA-R-581 |
| PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Quality <+ Traceability | 8 | CA-D-510, CA-D-511, CA-D-708, CA-E-653, CA-M-191, CA-R-1094, CA-R-1095, CA-R-1802 |
| PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Quality <+ Traceability <+ Provenance | 1 | CA-M-399 |
| PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Quality <+ Verification | 1 | CA-R-566 |
| PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Quality <+ Verification <+ Coverage | 3 | CA-E-396, CA-E-524, CA-E-642 |
| PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Quality <+ Verification <+ Dynamic Testing | 16 | CA-E-255, CA-E-257, CA-E-258, CA-E-271, CA-E-272, CA-E-310, CA-E-372, CA-E-373, CA-E-374, CA-E-388, CA-E-390, CA-E-391, CA-E-393, CA-E-395, CA-E-397, CA-E-641 |
| PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Quality <+ Verification <+ Dynamic Testing <+ Canary Testing | 1 | CA-E-536 |
| PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Quality <+ Verification <+ Static Analysis | 10 | CA-E-270, CA-E-365, CA-E-385, CA-E-453, CA-E-455, CA-E-540, CA-E-792, CA-M-420, CA-M-427, CA-M-428 |
| PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Quality <+ Verification <+ Static Analysis <+ Python Code | 5 | CA-E-266, CA-E-363, CA-E-364, CA-E-368, CA-E-539 |
| PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Quality <+ Verification <+ Test Data <+ Golden Corpora | 1 | CA-E-563 |
| PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Quality <+ Verification <+ Test Design | 6 | CA-D-546, CA-E-389, CA-E-637, CA-M-327, CA-M-424, CA-M-472 |
| PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ UX <+ Discovery and Navigation | 1 | CA-R-1811 |
| PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ UX <+ Entry | 3 | CA-E-281, CA-R-1113, CA-R-2442 |
| PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ UX <+ Guidance | 3 | CA-R-563, CA-R-665, CA-R-694 |
| PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ UX <+ Interaction | 3 | CA-E-816, CA-E-818, CA-R-1626 |
| PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ UX <+ Interaction <+ Accessibility | 1 | CA-E-349 |
| PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ UX <+ Interaction <+ Decision | 2 | CA-R-1602, CA-R-699 |
| PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ UX <+ Result and Status Presentation | 5 | CA-D-639, CA-E-287, CA-E-640, CA-R-1119, CA-R-2446 |
| PROJECT STRUCTURE//CAPRMEDIO <+ Scope Unit//AGENTIC | 1 | CA-R-2661 |
| PROJECT STRUCTURE//CAPRMEDIO <+ Scope Unit//APPS | 1 | CA-R-2659 |
| PROJECT STRUCTURE//CAPRMEDIO <+ Scope Unit//CODEX_EXTENSION | 1 | CA-R-2901 |
| PROJECT STRUCTURE//CAPRMEDIO <+ Scope Unit//CODEX_HOOK | 1 | CA-R-3014 |
| PROJECT STRUCTURE//CAPRMEDIO <+ Scope Unit//CONNECTOR_TOOLS | 1 | CA-R-2656 |
| PROJECT STRUCTURE//CAPRMEDIO <+ Scope Unit//MCP | 1 | CA-R-2660 |
| PROJECT STRUCTURE//CAPRMEDIO <+ Scope Unit//PROGRAMMATIC | 1 | CA-R-2654 |
| PROJECT STRUCTURE//CAPRMEDIO <+ Scope Unit//PROMPTS | 1 | CA-R-2663 |
| PROJECT STRUCTURE//CAPRMEDIO <+ Scope Unit//SKILLS | 1 | CA-R-2662 |
| PROJECT STRUCTURE//CAPRMEDIO <+ Scope Unit//WORKBENCH | 1 | CA-R-2730 |
| PROJECT STRUCTURE//CAPRMEDIO <+ Scope Unit//WORKBENCH_BACKEND | 1 | CA-R-2763 |
| PROJECT STRUCTURE//CAPRMEDIO <+ Scope Unit//WORKBENCH_FRONTEND | 1 | CA-R-2764 |
