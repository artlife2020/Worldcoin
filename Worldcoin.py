```python
from dataclasses import dataclass
from datetime import datetime
import json
import logging
import uuid


logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s | %(message)s"
)


@dataclass
class NetworkConfig:
    name: str
    rpc_endpoint: str


@dataclass
class ContractInfo:
    address: str


class Metadata:

    def __init__(self):
        self.protocol = "Worldcoin"
        self.asset = "WLD"

    def generate(self):
        return {
            "id": str(uuid.uuid4()),
            "created": datetime.utcnow().isoformat(),
            "protocol": self.protocol,
            "asset": self.asset
        }


class InteractionRequest:

    def __init__(
        self,
        network,
        contract
    ):
        self.network = network
        self.contract = contract
        self.metadata = Metadata()

    def build(self):

        return {
            "network": self.network.name,
            "endpoint": self.network.rpc_endpoint,
            "contract": self.contract.address,
            "payload": self.metadata.generate()
        }


class Validator:

    REQUIRED = (
        "network",
        "endpoint",
        "contract",
        "payload"
    )

    @classmethod
    def check(cls, request):

        for field in cls.REQUIRED:
            if field not in request:
                raise ValueError(
                    f"Missing: {field}"
                )

        return True


class Serializer:

    @staticmethod
    def to_json(data):

        return json.dumps(
            data,
            indent=2,
            sort_keys=True
        )


class Reporter:

    @staticmethod
    def display(request):

        print("=" * 50)
        print("Interaction Preview")
        print("=" * 50)
        print(
            Serializer.to_json(request)
        )
        print("=" * 50)


def load_network():

    return NetworkConfig(
        name="Educational Network",
        rpc_endpoint="https://example.invalid"
    )


def load_contract():

    return ContractInfo(
        address="0x1234567890123456789012345678901234567890"
    )


def main():

    logging.info(
        "Preparing interaction"
    )

    network = load_network()
    contract = load_contract()

    request = InteractionRe
