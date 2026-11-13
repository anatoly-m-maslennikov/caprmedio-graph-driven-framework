"""Bind a Model instance check after its Python source has been reviewed."""

from collections.abc import Callable, Mapping
from hashlib import sha256

from .native_model_claim import parse_native_model_claim


def bind_reviewed_instance_check(
    claim: str, *, reference: str, reviewed_claim_sha256: str, model_types: Mapping[str, type],
) -> Callable[[object], bool]:
    """Bind the exact reviewed Claim using Model types supplied by the Engine."""
    if sha256(claim.encode("utf-8")).hexdigest() != reviewed_claim_sha256:
        raise ValueError(f"{reference}: Claim differs from the reviewed source")
    declaration = parse_native_model_claim(claim)
    check = declaration and declaration.get("instance_check")
    if check is None:
        raise ValueError(f"{reference}: Claim has no instance check")
    model_name = check["parameter_type"]
    model_type = model_types.get(model_name)
    if not isinstance(model_type, type):
        raise ValueError(f"{reference}: unbound Model type {model_name}")

    namespace = {model_name: model_type}
    exec(compile(check["source"], reference, "exec"), namespace)
    callback = namespace[check["name"]]

    def validate(instance: object) -> bool:
        if not isinstance(instance, model_type):
            raise TypeError(f"{reference}: instance check requires {model_name}")
        result = callback(instance)
        if type(result) is not bool:
            raise TypeError(f"{reference}: instance check must return bool")
        return result

    return validate
