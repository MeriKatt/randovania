from randovania.game_connection.connector.remote_connector_v2 import RemoteConnectorV2


class ConnectorBuilder:
    async def build_connector(self) -> RemoteConnectorV2 | None:
        """Attempts to build a connector based on the rules of the concrete implementation."""
        raise NotImplementedError()

    # TODO: this might be a signal?
    def get_status_message(self) -> str | None:
        """Returns a message indicating the status of the last build_connector call, or why it has returned None."""
        raise NotImplementedError()
   