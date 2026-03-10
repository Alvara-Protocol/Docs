# Redeeming Your Position

You can exit a BSKT position at any time by redeeming your LP tokens. There are no lock-up periods or withdrawal queues.

## Two Redemption Options

### Redeem for ETH

Your LP tokens are burned, the basket's underlying tokens are sold for ETH, and you receive ETH back to your wallet. This is the most common redemption method.

**When to use:** You want a single asset (ETH) returned and don't want to manage multiple tokens.

### Redeem for Underlying Tokens

Your LP tokens are burned and you receive each of the basket's constituent tokens in proportion to your share. No swaps are performed.

**When to use:** You want to keep exposure to specific tokens in the basket, or you want to avoid any swap slippage.

## How to Redeem

1. Navigate to the BSKT detail page for the basket you're invested in
2. Open the redemption interface
3. Enter the amount of LP tokens you want to redeem (or select "Max")
4. Choose your redemption method (ETH or underlying tokens)
5. Confirm the transaction in your wallet

## MEV Protection

ETH redemptions involve token swaps and are protected against MEV attacks using the same backend signing service as deposits. Underlying token redemptions do not involve swaps and therefore do not require MEV protection.

## Important Notes

- Redemptions are processed instantly on-chain
- You can redeem a partial amount of your LP tokens — you don't have to exit the full position
- Gas fees on Base are required for the redemption transaction
- The value you receive is based on the current market prices of the underlying tokens at the time of redemption
