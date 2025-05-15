from .chain import Chain


class ChainRegistry:
    _chains_by_slug: dict[str, Chain] = {}

    @classmethod
    def register(cls, chain: Chain) -> None:
        if not chain.slug:
            raise ValueError("Chain must have a slug to be registered.")
        if chain.slug in cls._chains_by_slug:
            raise ValueError(f"Chain with slug '{chain.slug}' already registered.")
        cls._chains_by_slug[chain.slug] = chain

    @classmethod
    def get(cls, slug: str) -> Chain:
        try:
            return cls._chains_by_slug[slug]
        except KeyError:
            raise ValueError(f"Chain with slug '{slug}' not found.")

    @classmethod
    def all(cls) -> list[Chain]:
        return list(cls._chains_by_slug.values())

    @classmethod
    def clear(cls) -> None:
        cls._chains_by_slug.clear()
