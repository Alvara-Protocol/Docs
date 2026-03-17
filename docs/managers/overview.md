# Manager Overview

A Manager is any wallet that has created a BSKT. As a manager, you have exclusive control over your basket's investment strategy and earn fees on assets under management.

## What Managers Can Do

| Action | Description |
| --- | --- |
| **Rebalance** | Change the basket's token allocation at any time |
| **Emergency Stable** | Convert the basket entirely to stablecoins in an emergency |
| **Revert Emergency** | Restore the basket from emergency state to its normal allocation |
| **Claim Fees** | Collect accumulated management fees |
| **Update Notes** | Publish strategy notes visible to investors on the BSKT detail page |

## What Managers Cannot Do

- **Withdraw investor funds:** Only LP token holders can redeem their own share
- **Freeze redemptions:** Investors can always exit
- **Mint additional LP tokens:** LP supply is determined by deposits and redemptions only

This separation of powers ensures the system is non-custodial. Managers control the strategy; investors control their capital.

## Manager Dashboard

Access your management dashboard via the BSKT management page. This is a separate page from the BSKT detail page, accessible only to the manager wallet. You can find a link to it in your Portfolio page and on the BSKT detail page (visible only when your manager wallet is connected). The dashboard provides:

- Current allocation breakdown
- TVL and performance metrics
- Pending fee earnings
- Rebalance and emergency controls
- Manager notes editor

## Management Rights as NFTs

Your manager rights are represented as an ERC-721 NFT. This means:

- Management rights can be transferred to another wallet
- Rights could be sold on the BSKT Marketplace (a secondary market for management positions)
- Whoever holds the management NFT controls the basket

This creates a market for fund management positions. Successful managers with large AUM and strong track records hold a valuable asset.

## Building Your Reputation

The Alvara platform tracks manager performance transparently:

- **Leaderboard ranking** based on performance and AUM
- **Public profile** showing all BSKTs you manage
- **Identity verification** via X (Twitter) OAuth and Gitcoin Passport
- **Performance history** across all your baskets

A strong track record helps attract more investors and can earn you more gauge weight votes (and thus more ALVA rewards for your depositors).
