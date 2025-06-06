# Load data and compute static values
from shared import app_dir, tips
import faicons as fa


bill_rng = (min(tips.total_bill), max(tips.total_bill))

ICONS = {
    "user": fa.icon_svg("user", "regular"),
    "wallet": fa.icon_svg("wallet"),
    "currency-dollar": fa.icon_svg("dollar-sign"),
    "ellipsis": fa.icon_svg("ellipsis"),
}


