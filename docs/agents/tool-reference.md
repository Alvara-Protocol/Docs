# Tool Reference

Complete list of tools exposed by the Alvara MCP Server, grouped by purpose.

## Authentication

Used to obtain a session token for authenticated endpoints.

### `alvara_get_nonce`

Generates a signing nonce tied to a wallet address. The user must sign this nonce with their wallet before calling `alvara_authenticate`. Nonces expire after five minutes.

### `alvara_authenticate`

Exchanges a wallet signature for a session token. The token is stored in the server process and used automatically for subsequent calls. Expires after two hours.

## Observation

Read-only tools for discovering baskets, checking state, and analysing performance.

### Public (no authentication required)

| Tool | Purpose |
|---|---|
| `alvara_list_baskets` | Paginated list of all baskets, searchable and sortable |
| `alvara_get_basket` | Full detail for one basket: constituents, weights, TVL, price, performance |
| `alvara_get_nav` | Current NAV and TVL for a basket, or total platform TVL |
| `alvara_get_activity` | Transaction history for a basket: deposits, redemptions, rebalances, fee claims |
| `alvara_get_ohlcv` | Candlestick price history with configurable intervals |
| `alvara_get_fees` | Platform fee configuration |

### Authenticated

| Tool | Purpose |
|---|---|
| `alvara_get_tokens` | Available ERC-20 tokens for basket creation and rebalancing |
| `alvara_get_trending` | Trending baskets by volume and performance |
| `alvara_get_manager` | Fund manager profile and their baskets |
| `alvara_get_portfolio` | A user's basket positions: open, closed, created, or contributed |

## Intent

Tools that prepare on-chain transactions. Each returns unsigned transaction data and a server signature. The user's wallet signs and submits the transaction.

All intent tools require authentication.

### `alvara_rebalance_liquidate`

Phase 1 of a rebalance. Liquidates the basket's current constituents to WETH. Call this first, then call `alvara_rebalance_acquire` after the transaction confirms.

### `alvara_rebalance_acquire`

Phase 2 of a rebalance. Swaps WETH into the new target allocation. Must be called after `alvara_rebalance_liquidate` has been submitted on-chain.

### `alvara_emergency_rebalance`

Liquidates the basket into safe assets (ALVA and USDC). Requires explicit confirmation via a `confirm=true` parameter to prevent accidental triggers. Use only in genuine emergencies.

### `alvara_contribute`

Prepares a deposit of ETH into a basket. The ETH is swapped into the basket's constituents according to current weights.

### `alvara_redeem`

Prepares a withdrawal of LP tokens from a basket. The basket's tokens are swapped back to ETH for the user.

## Advisory

Optional safety checks that run before any transaction.

### `alvara_check_rebalance`

Pre-flight checks for a proposed rebalance. Surfaces warnings for:

- **Concentration:** single-token weights above 50% (warning) or 80% (critical)
- **Weight sum:** weights that do not sum to 10000 basis points
- **Turnover:** portfolio turnover above 80% (high swap costs)
- **Slippage:** tolerance above 2% (warning) or 5% (critical)
- **Low TVL:** baskets where gas costs may exceed the rebalance benefit

Warnings are advisory. The agent decides whether to proceed.

## Return Format

All tools return JSON. Errors are returned as MCP error responses with a human-readable message. The assistant surfaces these to the user.

Reads return the raw API response. Intent tools return a subset of the API response containing the fields a wallet needs to sign and submit the transaction: `swapData`, `signature`, `deadline`, `tokenAddresses`, `tokenWeights`.

## Rate Limits

Public endpoints follow the Alvara API's standard rate limits. Authenticated endpoints are scoped to the session token.
