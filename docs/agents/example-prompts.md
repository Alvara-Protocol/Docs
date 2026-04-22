# Example Prompts

Once your AI client is connected to the Alvara MCP Server, you can ask it to do anything the tools support. These examples show the kinds of requests that work well.

## Discovery

> List the top ten Alvara baskets by TVL and summarise what each one holds.

> Show me baskets with more than 50% exposure to ETH and a 24-hour performance above 5%.

> Which Alvara managers have the best 30-day performance?

## Analysis

> What is the current composition of basket 69b853736e181528926f81ca? Include constituent weights and recent price changes.

> Pull the 30-day OHLCV for this basket and summarise the trend. Is the price range tightening or widening?

> Compare the performance of basket A and basket B over the last 7 days. Which had higher volatility?

## Portfolio

> Show me all baskets I have contributed to and my current position in each. Address: 0x...

> What is my total P&L across open Alvara positions?

> List the baskets I have created and their fee earnings so far.

## Planning a Rebalance

> I want to rebalance my basket to 60% ETH and 40% USDC with 0.5% slippage tolerance. Run the safety checks first and show me any warnings before we proceed.

> This basket is currently 80% in one token. Propose a more diversified allocation and explain the trade-offs.

> What would a rebalance cost me in gas and slippage if I rotate this basket into a momentum-weighted allocation?

## Executing a Rebalance

Once you are ready to rebalance, the assistant calls the intent tools in sequence:

> Good, the warnings look fine. Build the liquidation transaction.

The assistant returns the transaction data. You sign it in your wallet and submit it. After it confirms:

> The liquidation transaction confirmed. Now build the acquisition phase with the allocation we discussed.

## Contribute and Redeem

> I want to contribute 0.1 ETH to basket 69b853736e181528926f81ca with 0.5% slippage. Prepare the transaction.

> Redeem 50% of my LP tokens from this basket. Show me what I will receive before I sign.

## Strategy Conversations

> Based on the last 30 days of price action across my Alvara baskets, which positions should I consider rebalancing?

> I am running a momentum strategy. Review my current baskets and suggest rotations based on 14-day returns.

> Monitor this basket's drift from my target weights and tell me when it exceeds 5%.

## Tips for Good Prompts

- Be specific about slippage and size when asking for transactions
- Ask the assistant to run `alvara_check_rebalance` before executing a rebalance
- Provide wallet addresses when asking about portfolios
- Use basket IDs (the 24-character hex strings) for precision; names work but are ambiguous

## What the Assistant Cannot Do

- Sign or submit transactions on your behalf. Every write goes through your wallet.
- Move funds without your explicit approval in your wallet.
- Access private keys or seed phrases.
- See anything about your wallet beyond what you share in the conversation.

The assistant is a planning and execution assistant. You remain in control of every on-chain action.
