from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class MovimientoCuentaCorriente:
    fecha: str
    descripcion: str
    documento: str
    cargo: Optional[int]
    abono: Optional[int]
    saldo: int