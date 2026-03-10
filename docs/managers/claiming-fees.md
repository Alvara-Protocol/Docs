# Claiming Fees

Managers earn fees on the assets under management in their BSKTs. These fees accrue over time and can be claimed at the manager's discretion.

## How Fees Work

Management fees are generated based on the BSKT's total value locked (TVL). The fee structure is defined at the protocol level.

Fees accrue continuously and are tracked by the smart contract. They do not need to be claimed at any specific interval. Managers can claim whenever they choose.

## How to Claim

1. Navigate to your BSKT's management dashboard
2. View your pending fee earnings
3. Click **Claim Fees**
4. Confirm the transaction in your wallet

Fees are paid out in ETH to your manager wallet.

## MEV Protection

Fee claiming involves converting accrued fees into ETH, which requires token swaps. Like all swap operations in the protocol, this is protected against MEV attacks through the backend signing service.

## Important Notes

- Fees can only be claimed by the wallet holding the management NFT
- There is no minimum claim amount
- Claiming fees does not affect the basket's TVL or LP token value. Fees are tracked separately from investor capital
- If a constituent token has been delisted or is no longer tradeable, the claim process handles this automatically
