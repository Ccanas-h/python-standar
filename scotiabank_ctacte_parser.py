import re
from typing import List, Optional
from models import MovimientoCuentaCorriente


class ScotiabankCuentaCorrienteParser:
    """
    Parser específico para cartolas de Cuenta Corriente Scotiabank Chile.
    """

    LINE_REGEX = re.compile(
        r"(?P<fecha>\d{2}/\d{2}/\d{4})\s+"
        r"(?P<descripcion>.+?)\s+"
        r"(?P<documento>\d{6,})\s+"
        r"(?P<cargo>[\d\.]+)?\s*"
        r"(?P<abono>[\d\.]+)?\s*"
        r"(?P<saldo>[\d\.]+)$"
    )

    def parse(self, pages_text: List[str]) -> List[MovimientoCuentaCorriente]:
        movimientos: List[MovimientoCuentaCorriente] = []

        for page in pages_text:
            for line in page.splitlines():
                match = self.LINE_REGEX.match(line.strip())

                if not match:
                    continue

                data = match.groupdict()

                movimientos.append(
                    MovimientoCuentaCorriente(
                        fecha=self._normalize_date(data["fecha"]),
                        descripcion=data["descripcion"].strip(),
                        documento=data["documento"],
                        cargo=self._to_int(data["cargo"]),
                        abono=self._to_int(data["abono"]),
                        saldo=self._to_int(data["saldo"]) or 0,
                    )
                )

        return movimientos

    def _to_int(self, value: Optional[str]) -> Optional[int]:
        if not value:
            return None
        return int(value.replace(".", ""))

    def _normalize_date(self, date_str: str) -> str:
        d, m, y = date_str.split("/")
        return f"{y}-{m}-{d}"