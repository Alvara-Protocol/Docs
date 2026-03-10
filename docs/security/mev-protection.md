# MEV Protection

All token swap operations in the Alvara Protocol are protected against MEV (Maximal Extractable Value) attacks.

## What is MEV?

MEV refers to the profit that can be extracted by reordering, inserting, or censoring transactions within a block. Common MEV attacks include:

- **Front-running** — An attacker sees your pending swap and places their own transaction before yours, moving the price against you
- **Sandwich attacks** — An attacker places transactions both before and after yours, profiting from the price movement they create
- **Back-running** — An attacker places a transaction immediately after yours to capture arbitrage opportunities

These attacks can result in worse execution prices for your transactions.

## How Alvara Protects You

Alvara uses a backend signing service to protect against MEV:

1. When you initiate a swap operation (deposit, redeem, rebalance, etc.), the transaction details are sent to the protocol's backend
2. The backend computes the optimal swap route
3. The backend signs the transaction data with a deadline
4. The signed transaction is submitted on-chain with MEV protection

This process happens automatically — you don't need to take any action or configure anything.

## Protected Operations

The following operations involve token swaps and are MEV-protected:

| Operation | Description |
| --- | --- |
| BSKT creation | Initial ETH → token swaps |
| Deposits | ETH → basket token swaps |
| ETH redemptions | Basket tokens → ETH swaps |
| Rebalancing | Selling old tokens, buying new tokens |
| Fee claiming | Converting fee tokens to ETH |
| Emergency stable | Converting to stablecoins |
| Revert emergency | Converting stablecoins back to portfolio tokens |

**Note:** Redeeming for underlying tokens (instead of ETH) does not involve swaps and therefore does not require MEV protection.

## Deadlines

Every signed transaction includes a deadline. If the transaction isn't confirmed on-chain within the deadline window, it reverts. This prevents stale transactions from executing at outdated prices.
