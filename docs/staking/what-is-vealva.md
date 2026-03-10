# What is veALVA?

veALVA (vote-escrowed ALVA) is the governance and rewards token of the Alvara Protocol. You receive veALVA by locking ALVA tokens in the staking contract on Ethereum mainnet.

## Why veALVA Exists

veALVA aligns incentives between token holders and the protocol's long-term health. By requiring users to lock their ALVA to gain governance power, the protocol ensures that those with the most influence are also the most committed.

Short-term speculators who buy ALVA without locking have no voting power. Long-term participants who lock for extended periods gain outsized influence.

## What veALVA Gives You

### Voting Power
veALVA is your voting weight in gauge weight voting. Each epoch, veALVA holders direct ALVA rewards to specific BSKTs. More veALVA means more influence over reward allocation.

### Staking Rewards
Stakers earn ALVA rewards proportional to their lock commitment. Longer locks receive a higher share of the staking reward pool (measured by SRV — Staking Reward Vote percentage).

### DAO Participation
veALVA is required to participate in Alvara DAO governance. Proposals on Snapshot are weighted by veALVA balance.

## How veALVA is Calculated

The amount of veALVA you receive depends on two factors:

1. **How much ALVA** you lock
2. **How long** you lock it for

Longer lock periods earn disproportionately more veALVA per ALVA locked. This is by design — it rewards commitment.

| Lock Period | veALVA Multiplier |
| --- | --- |
| 1 Week | 0.01x |
| 1 Month | 0.05x |
| 3 Months | 0.2x |
| 6 Months | 0.5x |
| 12 Months | 1.0x |
| 18 Months | 2.0x |
| 24 Months | 4.0x |
| 36 Months | 8.0x |
| 48 Months | 10.0x |
| Forever | 2.0x |

**Example:** Locking 1,000 ALVA for 12 months gives you 1,000 veALVA. Locking the same amount for 48 months gives you 10,000 veALVA — ten times the governance power.

## Key Properties

- **Non-transferable** — veALVA cannot be sent, sold, or traded. It is bound to the wallet that locked the ALVA.
- **Decay (time locks)** — For time-based locks, veALVA decays linearly as the lock approaches expiry. At expiry, veALVA reaches zero and the ALVA can be withdrawn.
- **No decay (forever locks)** — Forever locks maintain their veALVA balance permanently. The locked ALVA is effectively removed from circulating supply.
