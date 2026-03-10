# Composing Your Allocation

The first step in creating a BSKT is selecting which tokens to include and how much weight each should have.

## Selecting Tokens

Search for and add ERC-20 tokens available on the Base network. The token list is sourced from validated registries, so you only see legitimate tokens.

For each token you add, you assign a **weight:** the percentage of the basket's total value that should be allocated to that token.

## ALVA Minimum

Every BSKT must include ALVA as part of its allocation. The minimum ALVA percentage is set by the protocol and is enforced automatically. This requirement:

- Creates consistent demand for the ALVA token
- Connects every basket to the Alvara ecosystem
- Ensures all BSKTs contribute to the protocol's tokenomics

The remaining allocation is entirely up to you.

## Weight Rules

- All weights must add up to exactly **100%**
- Each token must have a weight greater than 0%
- The ALVA minimum must be met
- There is no maximum number of tokens, but larger baskets may incur higher gas costs

## Token Tax Detection

Some tokens have built-in buy or sell taxes. The platform automatically detects these taxes during the composition step and adjusts slippage settings per-token to ensure transactions complete successfully.

If a token has a detected tax, you'll see it noted in the interface. You can also manually adjust per-token slippage if needed.

## Tips for Good Allocation Design

- **Diversification:** Spreading across multiple tokens reduces the impact of any single token's decline
- **Conviction weighting:** Assign higher weights to tokens you have the most confidence in
- **Liquidity awareness:** Tokens with very low liquidity may experience higher slippage during rebalancing
- **Rebalancing frequency:** Consider how often you plan to rebalance when choosing the number of tokens. More tokens means more complexity.
