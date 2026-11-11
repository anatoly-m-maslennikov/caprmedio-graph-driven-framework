# AI Agent kind candidates

These are ID-free Claim previews, not native Drafts or Current authority. The Current Actor declaration CA-R-2542@2 declares Actor narrower than Continuant. No Current AI Agent Declaration was found. The old-format CA-R-1959@12 Draft defines an AI Agent as an Actor performing delegated work with an AI model; the parent preview carries that meaning into a Declaration. It adds no authority or permissions. Whether and how to retire or rebase that older Draft is an integration decision.

Both child previews declare an explicit NARROWER_THAN fact and inherit applicable parent constraints. They assert neither disjointness nor an exhaustive partition, and create no delegation permissions. Their semantics are proposed descriptions of the requested kinds; they do not assert an additional relationship or runtime behavior.

Native Draft creation requires IDs under the shared lock and appropriate metadata/carrier destinations. Subject path syntax is pending reconciliation: newer R1931@19 and R2471@8 Drafts reserve `/` for narrower kinds and `//` for a named instance, while older R2811 and R2475@6 Drafts describe `//` as narrowing. The requested names should not be encoded as instances accidentally. Bare kind names in the formal relation avoid relying on a path separator.

Pins (SHA-256):
- CA-R-2542@2: `6195aa835367e1dcd83d22f266c53177c578fd92023ec6a38d642b438ef3d594`
- CA-R-1959@12 Draft: `525831b0ef657b278869e49d665add4ec721d9ee361c885136e8f6a21fb7a6cb`
- ai-agent.preview.txt: `54d4df2d77b20f9847c57effb62be3103f4b507da25af2c6afd6d675c32637d4`
- subagent.preview.txt: `4618e66e4bdaf2dbd62b79d3ff71487e5906188d63db317c5625ffc850aa744d`
- main-agent.preview.txt: `8b4ec655233ef105608dd1b08cc23bd86b8a1630be9bc3ee493e5fdf4e3779d2`
