# Rebalancing

Rebalancing allows managers to change their BSKT's token allocation. This is the core tool for executing an investment strategy: rotating into new positions, adjusting weights, or responding to market conditions.

## How Rebalancing Works

Rebalancing is a two-phase process:

### Phase 1: Initialize
The basket's current tokens are sold into an intermediate asset (WETH). This liquidates the existing allocation in preparation for the new one.

### Phase 2: Rebalance
The intermediate WETH is used to purchase the new tokens according to the updated allocation weights. The basket now holds the new portfolio.

Both phases happen as separate on-chain transactions. The manager must complete both phases for the rebalance to finish.

## When to Rebalance

Common reasons to rebalance:

- **Conviction change:** You've identified better opportunities and want to rotate the portfolio
- **Risk management:** Market conditions have changed and you want to reduce exposure to certain assets
- **Weight drift:** Token price movements have caused the actual weights to diverge significantly from your target weights
- **New tokens:** You want to add tokens that weren't in the original allocation

## MEV Protection

Like all BSKT operations, rebalancing is MEV-protected. The protocol's backend computes optimal swap routes and signs the transaction data before it goes on-chain. This prevents front-running and ensures better execution prices for the swaps involved.

## Important Considerations

- **Slippage:** Large rebalances involving low-liquidity tokens may experience slippage. The protocol accounts for this automatically, but be mindful of the size of your swaps relative to available liquidity.
- **Gas costs:** Each rebalance requires gas on Base. More tokens in the basket means more swaps and higher gas costs.
- **Investor impact:** Rebalancing changes the composition of every LP token holder's position. Rebalance thoughtfully and consider publishing manager notes explaining your rationale.
- **Frequency:** There's no limit on how often you can rebalance, but frequent rebalancing incurs gas costs and may erode investor confidence if changes appear erratic.
