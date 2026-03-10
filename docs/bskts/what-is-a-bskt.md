# What is a BSKT?

A BSKT (pronounced "basket") is a tokenized investment portfolio on the blockchain. Each BSKT holds a collection of ERC-20 tokens in defined proportions, managed by a single on-chain fund manager.

## How BSKTs Work

A BSKT works like an on-chain index fund or ETF. A manager selects a set of tokens and assigns each a target weight (e.g., 40% ETH, 30% LINK, 25% AAVE, 5% ALVA). Investors can deposit ETH into the BSKT, which is automatically converted into the basket's constituent tokens according to those weights.

In return, investors receive **LP tokens:** fungible tokens representing their proportional share of the basket. These LP tokens can be redeemed at any time.

## Key Properties

### Non-Custodial
The BSKT smart contract holds all underlying assets. The manager can change the basket's allocation (rebalance), but cannot withdraw investor funds. Only LP token holders can redeem their own share.

### Transparent
Every BSKT's allocation, performance, and transaction history is fully visible on-chain. The Alvara app displays real-time data including current holdings, price history, and manager activity.

### ALVA Requirement
Every BSKT must include a minimum percentage of ALVA in its allocation. This creates organic demand for the ALVA token and connects every basket to the broader Alvara ecosystem.

### Manager-Controlled
Each BSKT has a single manager who controls the investment strategy. Managers can:
- Rebalance token allocations at any time
- Trigger emergency controls if needed
- Earn management fees on assets under management

### Open to All
Anyone with a Web3 wallet and 0.1 ETH can create a BSKT. There are no applications, licenses, or minimum track records required.

## BSKT vs. Traditional Funds

| Feature | Traditional Fund | BSKT |
| --- | --- | --- |
| Minimum to start managing | $100K+ and legal setup | 0.1 ETH |
| Custody | Third-party custodian | Smart contract (non-custodial) |
| Transparency | Quarterly reports | Real-time, on-chain |
| Investor redemption | Lock-up periods common | Instant, any time |
| Fees | 2% management + 20% performance typical | Set by protocol |
| Regulatory overhead | Extensive | Permissionless |
