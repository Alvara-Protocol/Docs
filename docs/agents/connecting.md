# Connecting Your AI

Instructions for connecting the Alvara MCP Server to common AI clients.

## Prerequisites

- Node.js 20 or later
- An MCP-compatible client (Claude Desktop, Cursor, Continue, etc.)
- A wallet on Base for write operations

## Install the Server

Clone the repository and build:

```bash
git clone https://github.com/Alvara-Protocol/alvara-mcp.git
cd alvara-mcp
npm install
npm run build
```

The compiled server lives at `dist/index.js`.

## Claude Desktop

Open your Claude Desktop config file.

- **macOS:** `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows:** `%APPDATA%\Claude\claude_desktop_config.json`

Add the Alvara server:

```json
{
  "mcpServers": {
    "alvara": {
      "command": "node",
      "args": ["/absolute/path/to/alvara-mcp/dist/index.js"],
      "env": {
        "ALVARA_API_URL": "https://base-api.alvara.xyz"
      }
    }
  }
}
```

Restart Claude Desktop. The Alvara tools appear in the tools menu.

## Cursor

Edit `~/.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "alvara": {
      "command": "node",
      "args": ["/absolute/path/to/alvara-mcp/dist/index.js"]
    }
  }
}
```

## Other MCP Clients

Any client supporting stdio transport can connect. Point it at `node /path/to/dist/index.js`. The server reads environment variables from the process, so set them in the client config.

## Environment Variables

| Variable | Required | Description |
|---|---|---|
| `ALVARA_API_URL` | No | API base URL. Defaults to `https://base-api.alvara.xyz` |
| `ALVARA_JWT` | No | Pre-authenticated session token. If unset, read-only tools still work |

## Authenticating

Some tools require authentication with an Alvara session token. The authentication flow is wallet-based:

1. The assistant calls `alvara_get_nonce` with your wallet address
2. You sign the returned nonce in your wallet
3. You paste the signature back into the conversation
4. The assistant calls `alvara_authenticate` with the signature
5. The session token is stored in the server process for the duration of the session

The session token expires after two hours. If you have an existing token from another session, set it as the `ALVARA_JWT` environment variable to skip the signing step.

## Verifying the Connection

Ask the assistant:

> List the top five Alvara baskets by TVL.

If the server is connected, the assistant calls `alvara_list_baskets` and returns a formatted list. If nothing happens, check that the path in your config is absolute and points to the compiled `dist/index.js`.

## Next Steps

- Review the full [Tool Reference](tool-reference.md) for everything the assistant can do
- See [Example Prompts](example-prompts.md) for ideas on what to ask
