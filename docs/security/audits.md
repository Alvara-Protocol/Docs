# Smart Contract Audits

Alvara Protocol's smart contracts have been independently audited by three security firms: CertiK, QuillAudits, and Adevar Labs.

## Completed Audits

### CertiK — Staking & BSKT Contracts

Full security assessment of the staking platform and BSKT core contracts, covering BSKT.sol, Factory.sol, and BSKTPair.sol. Methods included formal verification, manual review, and static analysis.

**Auditor:** [CertiK](https://www.certik.com/)
**Date:** June 12, 2025
**Scope:** Staking, BSKT Factory, BSKT, BSKTPair (EVM Compatible)
**Findings:** 18 total — 14 resolved, 4 acknowledged. 1 critical (resolved), 2 major (1 resolved, 1 acknowledged), 4 medium (all resolved), 8 minor (6 resolved, 2 acknowledged), 2 informational (all resolved).
**Report:** [CertiK Audit Report (PDF)](https://github.com/Alvara-Protocol/Docs/blob/main/Alvara%20Protocol%20Security%20Assessment%20-%20CertiK.pdf)

### QuillAudits — BSKT Factory & BSKT Contracts

The core BSKT creation and management contracts have been audited. This covers the factory contract, basket token logic, deposit/redemption mechanics, and rebalancing functionality.

**Auditor:** [QuillAudits](https://www.quillaudits.com/)
**Report:** [BSKT Factory Audit Report (PDF)](https://github.com/Alvara-Protocol/Docs/blob/main/Alvara%20BTS%20%2B%20Factory%20Smart%20Contracts%20Audit%20Report%20-%20QuillAudits.pdf)

### QuillAudits — Staking Contract

The ALVA staking contract (time locks, forever locks, veALVA calculation, reward distribution) has been audited.

**Auditor:** [QuillAudits](https://www.quillaudits.com/)
**Report:** [Staking Audit Report (PDF)](https://github.com/Alvara-Protocol/Docs/blob/main/Alvara%20Staking%20Smart%20Contract%20Audit%20Report%20-%20QuillAudits.pdf)

### QuillAudits — ALVA Token (Avalanche)

The ALVA token deployment on Avalanche C-Chain has been audited.

**Auditor:** [QuillAudits](https://www.quillaudits.com/)
**Report:** [ALVA Token AVAX Audit Report (PDF)](https://github.com/Alvara-Protocol/Docs/blob/main/Alvara%20Token%20-%20AVAX%20Smart%20Contract%20Audit%20Report%20-%20QuillAudits%20.pdf)

### Adevar Labs — 1inch Integration (After Fix Review)

Security assessment focused on the 1inch swap integration, covering BSKT.sol, Factory.sol, BSKTPair.sol, and BSKTUtils.sol. Reviewed partial-fill handling, LP token accounting, fee calculation logic, and ETH recovery mechanisms.

**Auditor:** [Adevar Labs](https://www.adevar.io/)
**Date:** January 29, 2026
**Scope:** 1inch integration — BSKT, Factory, BSKTPair, BSKTUtils contracts
**Findings:** 6 total — 3 high (2 resolved, 1 partially resolved), 2 medium (2 partially resolved), 1 low (resolved). 2 enhancement opportunities noted.
**Report:** [Adevar Labs 1inch Integration Audit Report (PDF)](https://github.com/Alvara-Protocol/Docs/blob/main/Alvara%201inch%20Integration%20Audit%20Report%20-%20Adevar%20Labs.pdf)

## Audit Scope

The audits collectively cover:
- Smart contract logic and correctness
- Access control and permission models
- Reentrancy and common vulnerability checks
- Flashloan and price manipulation vectors
- Economic attack vectors (inflation, reserve manipulation)
- Centralization risks
- Gas optimization

## Important Note

Audits reduce risk but do not eliminate it. Smart contracts are complex software and may contain undiscovered vulnerabilities. All interactions with Alvara Protocol carry inherent smart contract risk. See [Risk Disclosures](risk-disclosures.md) for more information.
