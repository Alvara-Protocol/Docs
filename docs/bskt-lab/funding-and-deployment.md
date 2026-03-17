# Funding & Deployment

The final step in creating a BSKT is providing the initial capital and deploying the basket on-chain.

## Initial Funding

Enter the amount of ETH you want to seed the basket with. This ETH will be:

1. Split according to your allocation weights
2. Converted into the constituent tokens via DEX swaps
3. Deposited into the new BSKT smart contract

You receive LP tokens representing your initial contribution. This is your personal stake in the basket, not a fee.

### Minimum Deposit

The minimum initial funding is **0.1 ETH**. The basket needs enough liquidity to function from launch.

### Creation Fee

A small creation fee (a percentage of the initial deposit) is charged by the protocol. This fee is displayed clearly before you confirm the transaction.

## Deployment

Once you confirm and sign the transaction in your wallet:

1. The BSKT smart contract is deployed on Ethereum
2. Your ETH is swapped into the basket's tokens
3. LP tokens are minted to your wallet
4. The management NFT is minted to your wallet
5. Your BSKT goes live on the platform

The entire process happens in a single transaction.

## MEV Protection

The deployment process uses the protocol's MEV protection system. Before your transaction goes on-chain, the backend computes optimal swap routes and signs the transaction data. This prevents front-running and sandwich attacks that could result in worse execution prices for your initial swaps.

## After Deployment

Your BSKT is immediately visible on:
- The **Explore** page for all users to discover
- The **Leaderboard** where your performance will be tracked
- Your **Portfolio** under "Created BSKTs"

You can begin managing your basket right away. See [Rebalancing](../managers/rebalancing.md) and [Manager Overview](../managers/overview.md) for next steps.
