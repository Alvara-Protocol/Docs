# MCP Server Overview

The Alvara MCP Server lets AI assistants such as Claude, ChatGPT, and Cursor read data from the Alvara protocol and prepare basket transactions on a user's behalf. It is open source, self-hostable, and non-custodial.

## What MCP Is

Model Context Protocol (MCP) is an open standard created by Anthropic for connecting AI assistants to external tools and data. An MCP server exposes a set of tools; any MCP-compatible client can call those tools during a conversation. The Alvara MCP Server exposes seventeen tools covering the full basket lifecycle.

Because MCP is an open standard, one integration reaches every client that supports it. Users can bring their preferred assistant rather than being locked to a specific AI platform.

## What It Enables

With the Alvara MCP Server connected, an AI assistant can:

- Discover baskets, fetch current composition, and summarise performance
- Read price history, TVL, NAV, and activity for any basket
- Surface a user's portfolio positions across the platform
- Build contribute, redeem, and rebalance transactions
- Run pre-flight safety checks before any transaction is signed
- Authenticate the user through their existing wallet

The assistant does the reasoning. The MCP server provides the structured interface to Alvara.

## Non-Custodial by Design

The server never holds private keys. Write operations return unsigned transaction data and a server signature. The user's wallet signs and submits the transaction on-chain. The server is stateless and cannot move funds on its own.

This model keeps control with the user. An AI assistant can prepare a rebalance, but the user must approve it in their wallet before anything happens on-chain.

## Architecture

```
AI assistant + user's wallet
          |
          | MCP protocol (stdio)
          v
Alvara MCP Server (runs locally)
          |
          | HTTPS
          v
    Alvara REST API
          |
          v
User signs and submits transaction on Ethereum or Base
```

The server is a thin translation layer. Reads go through the public Alvara API. Writes return transaction data for the user to sign. No database, no custodial infrastructure, no dependency on Alvara hosting anything beyond the existing public API.

## Networks

Alvara is live on both Ethereum mainnet and Base. The MCP server supports either. Point `ALVARA_API_URL` at the endpoint for the chain you want to work with.

| Network | API endpoint |
|---|---|
| Ethereum mainnet | `https://web1-api.alvara.xyz` |
| Base | `https://base-api.alvara.xyz` |

See [Connecting Your AI](connecting.md) for configuration.

## Who This Is For

- **End users** who want to interact with Alvara baskets through a conversational interface
- **Power users** who want to build personal automations across their portfolio
- **Developers** who want to create agents that manage baskets for others
- **Strategy builders** who want to construct autonomous fund management systems on top of Alvara

## Open Source

The server is MIT licensed and available on GitHub. Any developer can clone the repository and run their own instance. No approval, no whitelist, no API keys to request for public endpoints.

## Getting Started

See [Connecting Your AI](connecting.md) for setup instructions with Claude Desktop, Cursor, and other MCP clients.
