# Emergency Controls

Managers have access to emergency controls that allow them to quickly de-risk a BSKT in adverse market conditions.

## Emergency Stables

The Emergency Stables function converts the entire basket into approximately 95% USDT and 5% ALVA. The 5% ALVA allocation is retained to ensure the basket continues to hold at least two assets, avoiding single-asset composition which could raise regulatory classification concerns. This is designed for situations where:

- Constituent tokens are experiencing extreme volatility
- A token in the basket has a critical vulnerability
- Market conditions require immediate de-risking

When triggered, the BSKT enters a suspended state where normal operations (deposits, rebalancing) are paused. LP token holders retain their LP tokens, but the underlying assets are now held as stablecoins.

## Revert Emergency

Once conditions stabilize, the manager can revert the emergency and restore the basket to its previous token allocation (or a new one). This re-enables normal operations.

The revert process works similarly to a rebalance: stablecoins are swapped back into the target tokens according to the specified allocation.

## When to Use Emergency Controls

Emergency controls are a last resort. They should be used when:

- **Immediate action is required** and a standard rebalance would be too slow
- **A constituent token is compromised** (exploit, depegging, rug pull)
- **Extreme market conditions** make holding the current allocation dangerously risky

They should **not** be used for routine portfolio adjustments. Use standard rebalancing for that.

## Impact on Investors

- LP tokens remain valid during emergency state
- The basket's value is preserved in stablecoins
- Redemptions may still be available depending on the contract state
- The manager should communicate via manager notes why the emergency was triggered
