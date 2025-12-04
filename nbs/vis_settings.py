panel_titles = [
    "A) Physical delay",
    "B) Counterfactual delay",
    "C) Accelerated emissions",
    "D) Upfront embodied emissions",
]

flux_types = {
    "baseline": "black",
    "net-effect": "#58BBCC",
    "removal": "#519E3E",
    "activity-emission": "#3B75AF",
    "CDR+baseline": "#8D69B8",
}

lag_colors = {
    "baseline": "black",
    "instant-removal-offsetting": "#F7DC9C",  #'#D98C00',#
    "physical-delay-offsetting": "#FE648D",
    "counterfactual-delay-offsetting": "#EB6E6C",
    "accelerated-emissions-offsetting": "#C23B22",
    "upfront-embodied-offsetting": "#F27234",
}

line_labels = {
    "baseline": "Fossil emissions to neutralize",
    "net-effect": "Net CDR activity",
    "removal": "Removal",
    "activity-emission": "CDR activity emissions",
    "CDR+baseline": "CDR + neutralized fossil emissions",
}

figsize=(14, 9)

mpl_settings =     {
        "font.family": "DejaVu Sans",
        "axes.grid": False,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.linewidth": 1.0,
        "legend.frameon": False,
        "font.size": 15,
        "axes.titlesize": 18,
        "axes.labelsize": 16,
        "legend.fontsize": 15,
        "xtick.labelsize": 14,
        "ytick.labelsize": 14,
        "lines.linewidth": 3,
    }
