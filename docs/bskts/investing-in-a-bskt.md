# Investing in a BSKT

Investing in a BSKT means depositing ETH into a tokenized portfolio managed by an on-chain fund manager. In return, you receive LP tokens representing your share of the basket.

## How to Invest

1. **Find a BSKT:** Browse the Explore page or Leaderboard to find a basket that aligns with your investment thesis
2. **Open the BSKT detail page:** Click on the BSKT to view its full details
3. **Enter your deposit amount:** Use the deposit widget on the detail page to specify how much ETH you want to invest
4. **Confirm the transaction:** Review the details and confirm in your wallet

Your ETH is automatically converted into the basket's constituent tokens according to the current allocation weights. You receive LP tokens representing your proportional share.

## What You Receive

After depositing, you hold **LP tokens** for that specific BSKT. These tokens:

- Represent your share of the basket's total value
- Fluctuate in value as the underlying tokens move
- Can be redeemed at any time (see [Redeeming Your Position](redeeming-your-position.md))
- Are standard ERC-20 tokens held in your wallet

## MEV Protection

All deposits are protected against MEV (Maximal Extractable Value) attacks. The protocol uses a backend signing service to compute optimal swap routes and prevent front-running or sandwich attacks on your transaction. This happens automatically. No action required on your part.

## Things to Consider

**Manager risk:** The BSKT manager controls the basket's allocation. If the manager makes poor rebalancing decisions, the basket's value may decline. Review the manager's track record on the Leaderboard before investing. A manager can also extract TVL by adding a honeypot or a token they have provided LP for and then removing the LP from DEX. It is important to carry out DD on your manager and invest at your own risk.

**Smart contract risk:** Your assets are held by the BSKT smart contract. While the contracts have been audited, all smart contract interactions carry inherent risk.

**Token risk:** The underlying tokens in a BSKT are subject to their own market risks. A basket holding volatile tokens will itself be volatile. Check the risk ratings on the BSKT detail page.

**Network:** BSKT deposits are available on Eth and Base. Ensure your wallet is connected to the correct network and that you have ETH on the correct chain for the deposit and gas fees.
