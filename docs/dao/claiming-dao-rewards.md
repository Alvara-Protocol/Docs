# Claiming DAO Rewards

After each epoch, eligible veALVA holders can claim ALVA rewards based on their voting participation. Claims are processed on Ethereum mainnet.

## How Claims Work

DAO rewards use a **merkle proof** system:

1. At the end of each epoch, the protocol computes reward amounts for each eligible address
2. A merkle tree is generated and its root is published on-chain
3. Each eligible address receives a merkle proof that can be used to claim their ALVA

This system is gas-efficient — it allows batch reward distribution without requiring individual on-chain transactions for each recipient.

## How to Claim

1. Navigate to the **DAO** page in the app
2. Select the **Claim Rewards** tab
3. Ensure your wallet is connected and on **Ethereum mainnet**
4. You'll see a list of epochs with pending rewards and the ALVA amount for each
5. Click **Claim** on any individual epoch, or use **Claim All** to batch-claim all pending rewards
6. Confirm the transaction in your wallet

## Batch Claiming

If you have rewards from multiple epochs, you can claim them all in a single transaction using the **Claim All Rewards** button. This saves gas compared to claiming each epoch individually.

## Network Requirement

DAO reward claims happen on **Ethereum mainnet**. If your wallet is connected to a different network, the app will prompt you to switch before you can claim.

## Checking Your Rewards

The Claim Rewards tab shows:
- **Per-epoch breakdown** — Reward amount for each epoch
- **Total pending** — Sum of all unclaimed rewards
- **Claim status** — Whether each epoch's rewards have been claimed

The **My DAO Profile** tab (available when your wallet is connected) provides a summary of your total unclaimed DAO rewards alongside your veALVA balance and voting power.

## Important Notes

- You must have participated in gauge weight voting during an epoch to be eligible for that epoch's rewards
- Claims do not expire — you can claim rewards from past epochs at any time
- Claimed ALVA is sent directly to your wallet on Ethereum mainnet
