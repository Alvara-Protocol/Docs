# Token Overview

ALVA is the native utility token of the Alvara Protocol. It serves as the foundation for governance, staking, and the BSKT ecosystem.

## Core Functions

### 1. Governance
Lock ALVA to receive veALVA, the protocol's governance token. veALVA holders vote in gauge weight elections each epoch, directing ALVA rewards to BSKTs. veALVA is also used for Snapshot governance proposals.

### 2. BSKT Requirement
Every BSKT must include a minimum percentage of ALVA in its allocation. This creates organic, continuous demand for the token as new baskets are created and existing ones grow in TVL.

### 3. Staking Rewards
Stakers earn ALVA rewards proportional to their lock duration and amount. The reward system incentivizes long-term commitment to the protocol.

## Token Properties

| Property | Detail |
| --- | --- |
| Standard | ERC-20 |
| Maximum Supply | Fixed cap (not mintable beyond max supply) |
| Burnable | Yes, forever-locked ALVA is effectively removed from supply |
| Inflationary | No, supply is capped and deflationary via burning/locking |

## Multi-Chain Availability

ALVA is available on multiple chains:

- **Ethereum Mainnet:** BSKT Lab, staking platform, governance, and DAO reward claims
- **Base:** ALVA trading and DEX liquidity available; BSKT Lab deployment planned Q1 2026
- **Avalanche:** ALVA trading and DEX liquidity available

ALVA can be bridged between Ethereum, Base and Avalanche via cross-chain bridges (Axelar / Squidrouter). DEX liquidity for ALVA is available on each supported chain. Your total ALVA balance across all chains is displayed in your Portfolio.

## Deflationary Mechanics

ALVA has multiple deflationary forces:

1. **Forever locks:** ALVA locked permanently in the staking contract is removed from circulating supply
2. **BSKT allocation:** ALVA locked inside BSKTs reduces available supply
3. **Fixed cap:** No additional ALVA can be minted beyond the maximum supply

Over time, the effective circulating supply decreases as more ALVA is locked in staking contracts and BSKTs.
