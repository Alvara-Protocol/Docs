# Lock Types

Alvara offers two types of ALVA locks, each with different tradeoffs between flexibility and rewards.

## Time Lock

Lock your ALVA for a fixed duration. When the lock expires, you can withdraw your ALVA.

**Available periods:** 1 Week, 1 Month, 3 Months, 6 Months, 12 Months, 18 Months, 24 Months, 36 Months, 48 Months

### How Time Locks Work

1. Choose a lock period and deposit ALVA
2. Receive veALVA based on the lock multiplier
3. veALVA decays linearly over the lock period
4. When the lock expires, withdraw your ALVA

### veALVA Decay

Time lock veALVA decays as the lock approaches expiry. At the midpoint of a 12-month lock, you have roughly half your initial veALVA. At expiry, your veALVA balance reaches zero.

This decay mechanism creates an ongoing incentive to either:
- **Renew** your lock to reset the veALVA balance
- **Increase** your locked amount to boost veALVA

### Extending and Increasing

You can:
- **Add more ALVA** to an existing time lock, increasing your veALVA
- **Renew** a time lock to reset the duration and restore decayed veALVA

Both actions refresh your veALVA balance based on the new total locked amount and duration.

## Forever Lock

Permanently lock your ALVA. The tokens can never be withdrawn.

### How Forever Locks Work

1. Deposit ALVA into the forever lock pool
2. Receive veALVA at the 2.0x multiplier
3. veALVA never decays. Your governance power is permanent
4. Locked ALVA is permanently removed from circulating supply

### Why Lock Forever?

- **Maximum staking rewards:** Forever locks receive the highest SRV (Staking Reward Vote) percentage at 50%
- **Permanent governance power:** No decay means your voting power remains constant
- **Deflationary:** Forever-locked ALVA is effectively burned, reducing total circulating supply

### The Tradeoff

Forever locks offer the highest reward rates and permanent governance power, but the locked ALVA can never be recovered. Consider this carefully before committing.

## Staking Reward Vote (SRV) Rates

The SRV determines what share of the staking reward pool you're eligible for:

| Lock Period | SRV Rate |
| --- | --- |
| 1 Week | 0% |
| 1 Month | 0% |
| 3 Months | 0.5% |
| 6 Months | 1.25% |
| 12 Months | 2.75% |
| 18 Months | 4.5% |
| 24 Months | 8.5% |
| 36 Months | 12.5% |
| 48 Months | 20% |
| Forever | 50% |

Note: 1-week and 1-month locks do not earn staking rewards. So only meaningful commitments are rewarded.

## Choosing the Right Lock

| Priority | Recommended Lock |
| --- | --- |
| Maximum rewards + governance | Forever |
| Strong rewards with eventual exit | 24-48 Months |
| Moderate commitment | 6-18 Months |
| Short-term voting participation | 3-6 Months |
| Testing the system | 1 Week / 1 Month (no rewards) |
