from cosmpy.aerial.client import LedgerClient, NetworkConfig

cfg = NetworkConfig(
    chain_id="greenfield_5600-1",
    url="grpc+https://gnfd-testnet-fullnode-tendermint-us.bnbchain.org:443",
    fee_minimum_gas_price=1,
    fee_denomination="uatom",
    staking_denomination="uatom",
)

ledger_client = LedgerClient(cfg)


address: str = '0x89b7f5dBAde74CB8c2c78Af26B3841cFF8182945'
balances = ledger_client.query_bank_all_balances(address)
