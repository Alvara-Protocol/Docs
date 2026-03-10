# Glossary

**ALVA**
The native ERC-20 utility token of the Alvara Protocol. Used for governance (via veALVA staking), BSKT allocation requirements, and staking rewards.

**AUM (Assets Under Management)**
The total value of assets managed by a specific manager across all their BSKTs.

**BSKT (Basket Token)**
A tokenized investment portfolio built on the ERC-7621 standard. Each BSKT holds a collection of ERC-20 tokens in defined proportions.

**BSKT Lab**
The interface for creating new BSKTs. A three-step process: Compose (select tokens), Design (name and brand), Fund (seed and deploy).

**Epoch**
A recurring governance cycle (typically one week) during which veALVA holders cast gauge weight votes. At the end of each epoch, rewards are calculated and distributed.

**ERC-7621**
The Basket Token Standard — an Ethereum Improvement Proposal defining how tokenized investment portfolios can be implemented as smart contracts.

**Forever Lock**
A permanent ALVA staking option where tokens can never be withdrawn. Provides a 2.0x veALVA multiplier and 50% SRV rate. Effectively burns the locked ALVA.

**Gauge Weight Voting**
The governance mechanism by which veALVA holders direct ALVA reward emissions to specific BSKTs each epoch.

**LP Token (Liquidity Provider Token)**
A token representing proportional ownership of a BSKT's underlying assets. Received when depositing into a BSKT, redeemable for ETH or underlying tokens.

**Manager**
The wallet address that created a BSKT. Has exclusive control over the basket's allocation (rebalancing) and earns management fees.

**Management NFT**
An ERC-721 token representing management rights over a BSKT. Whoever holds this NFT controls the basket. Can be transferred or sold.

**Merkle Proof**
A cryptographic proof used to verify eligibility for DAO reward claims without storing all claim data on-chain. Enables gas-efficient batch reward distribution.

**MEV (Maximal Extractable Value)**
Profit extracted by reordering or inserting transactions within a block. Common MEV attacks include front-running and sandwich attacks. Alvara protects against MEV through its backend signing service.

**Rebalancing**
The process by which a manager changes a BSKT's token allocation. Involves selling existing tokens and purchasing new ones according to updated weights.

**SRV (Staking Reward Vote)**
A percentage that determines a staker's share of the staking reward pool. Higher SRV rates are earned by longer lock periods.

**Time Lock**
A temporary ALVA staking option where tokens are locked for a fixed period (1 week to 48 months). veALVA decays linearly until expiry, at which point the ALVA can be withdrawn.

**TVL (Total Value Locked)**
The total USD value of all assets held within a BSKT or across the protocol.

**veALVA (Vote-Escrowed ALVA)**
The non-transferable governance token received by locking ALVA. Used for gauge weight voting and qualifying for staking rewards. Amount determined by lock size and duration.

**Xerberus Risk Rating**
A third-party credit-style risk rating system (AAA to D) that evaluates the risk profile of individual tokens within BSKTs.
