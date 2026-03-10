# Core Concepts

Before using the platform, here are the key building blocks of the Alvara ecosystem.

## BSKT (Basket Token)

A BSKT is a tokenized investment portfolio built on the ERC-7621 standard. Each BSKT holds a basket of ERC-20 tokens in defined proportions and is managed by a single wallet address (the Manager).

When you invest in a BSKT, you receive **LP tokens** representing your proportional share of the basket's underlying assets. These LP tokens can be redeemed at any time for ETH or for the underlying tokens directly.

**Key properties:**
- Fully on-chain and non-custodial
- Manager controls allocation but cannot access investor funds
- Any ERC-20 token on supported chains can be included
- Including ALVA in the allocation unlocks reduced platform fees

## Manager

A Manager is the wallet that created a BSKT. Managers have exclusive control over their basket's allocation. They can rebalance token weights, trigger emergency controls, and earn management fees.

Managers do not have custody of depositor funds. They can only change what the basket holds, not withdraw other people's capital.

Management rights are represented as an NFT, meaning they can be transferred or sold on the BSKT Marketplace.

## ALVA

ALVA is the native ERC-20 utility token of the Alvara Protocol. It serves three core functions:

1. **Governance:** Lock ALVA to receive veALVA voting power
2. **Fee Reduction:** Including ALVA in a BSKT unlocks reduced platform fees
3. **Staking Rewards:** Stakers earn ALVA rewards via buybacks funded by a percentage of platform fees

ALVA has a fixed maximum supply and is deflationary: tokens locked forever in the staking contract are permanently removed from circulating supply.

## veALVA (Vote-Escrowed ALVA)

veALVA is the governance token of the Alvara DAO. You receive veALVA by locking ALVA tokens in the staking contract. The amount of veALVA you receive depends on:

- **How much** ALVA you lock
- **How long** you lock it for

Longer commitments earn disproportionately more veALVA. veALVA is non-transferable. It can only be earned through staking.

## Epoch

An epoch is a recurring governance cycle (typically one week) during which veALVA holders cast gauge weight votes. At the end of each epoch, votes are tallied and ALVA rewards are allocated to BSKTs based on the voting results.

## Gauge Weight Voting

The mechanism by which veALVA holders direct ALVA rewards. Each epoch, voters allocate their voting power to specific BSKTs. The BSKTs that receive the most votes earn a larger share of the epoch's reward pool. This incentivizes managers to create high-performing baskets and voters to identify the best strategies.

## LP Token

When you invest in a BSKT, you receive LP (Liquidity Provider) tokens. These represent your share of the basket's total value. LP tokens can be:

- **Redeemed for ETH:** Sell your share back for ETH at current market value
- **Redeemed for underlying tokens:** Receive the basket's constituent tokens in proportion to your share
- **Held:** Continue holding exposure to the manager's strategy
