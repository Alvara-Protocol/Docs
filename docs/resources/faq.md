# FAQ

## General

**What is Alvara Protocol?**
Alvara is a decentralized asset management platform where anyone can create, manage, and invest in tokenized investment portfolios (BSKTs) on-chain. It combines permissionless fund creation with gauge weight governance to create an open, competitive fund management ecosystem.

**Do I need to sign up or create an account?**
No. Alvara is a decentralized application. You only need a Web3 wallet (MetaMask, Coinbase Wallet, etc.) to interact with the platform. No email, KYC, or registration required.

**Which chains does Alvara support?**
BSKTs operate on Base. Staking and DAO governance operate on Ethereum mainnet. ALVA is also available on Avalanche.

---

## BSKTs

**What is a BSKT?**
A BSKT is a tokenized portfolio of ERC-20 tokens, built on the ERC-7621 standard. It functions like an on-chain index fund or ETF, managed by a single wallet address.

**Can I lose money investing in a BSKT?**
Yes. BSKTs hold volatile crypto assets whose value can decrease. The manager's allocation decisions may not always perform well. Only invest what you can afford to lose.

**Can the manager steal my funds?**
No. BSKTs are non-custodial. The manager can change the basket's token allocation (rebalance), but cannot withdraw investor funds. Only you can redeem your LP tokens.

**Can I withdraw at any time?**
Yes. There are no lock-up periods for BSKT investments. You can redeem your LP tokens for ETH or underlying tokens at any time.

**Why does every BSKT need ALVA?**
The minimum ALVA requirement connects every basket to the Alvara ecosystem, creates organic demand for the token, and ensures all BSKTs contribute to the protocol's tokenomics.

---

## Creating & Managing BSKTs

**How much does it cost to create a BSKT?**
The minimum seed capital is 0.1 ETH, plus a small creation fee (percentage of the deposit) and gas fees on Base.

**Can I manage multiple BSKTs?**
Yes. There is no limit on the number of BSKTs a single wallet can create and manage.

**Can I transfer management rights?**
Yes. Management rights are represented as an NFT and can be transferred to another wallet.

---

## Staking & veALVA

**What is veALVA?**
veALVA (vote-escrowed ALVA) is the governance token earned by locking ALVA. It provides voting power in gauge weight elections and earns staking rewards.

**Can I unlock my staked ALVA early?**
For time locks: No. You must wait until the lock period expires to withdraw. For forever locks: No. Forever locks are permanent and irreversible.

**Does veALVA decay?**
For time locks, yes, veALVA decays linearly as the lock approaches expiry. For forever locks, no, veALVA is permanent.

**Which locks earn staking rewards?**
Locks of 3 months or longer earn staking rewards. 1-week and 1-month locks provide veALVA governance power but no staking rewards.

**Can I add more ALVA to an existing lock?**
Yes. You can increase the locked amount at any time, which increases your veALVA balance.

---

## DAO & Governance

**How does gauge weight voting work?**
Each epoch, veALVA holders vote to allocate ALVA rewards across BSKTs. BSKTs that receive more votes earn a larger share of rewards, which flow to their depositors.

**How often are epochs?**
Typically one week per epoch.

**How do I claim DAO rewards?**
Navigate to the DAO page in the app, select the Claim Rewards tab, and claim per-epoch or batch-claim all pending rewards. Claims happen on Ethereum mainnet.

**Do I need a minimum veALVA to vote?**
No minimum is required to vote. However, creating governance proposals requires more than 2,000 veALVA.

---

## Security

**Have the contracts been audited?**
Yes. QuillAudits has audited the BSKT Factory, Staking, and ALVA token contracts. Reports are available on the [Security](../security/audits.md) page.

**What is MEV protection?**
MEV protection prevents front-running and sandwich attacks on your transactions. All swap operations in Alvara are MEV-protected automatically.
