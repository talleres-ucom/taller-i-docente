CASOS = [
    ("solapadas, B empieza después", (1, "19:00", "21:00"), (1, "20:00", "22:00"), True),
    ("distinto día", (1, "19:00", "21:00"), (2, "19:00", "21:00"), False),
    ("contiguas: A termina cuando B empieza", (1, "19:00", "21:00"), (1, "21:00", "22:30"), False),
    ("B termina antes de que empiece A", (1, "21:00", "22:30"), (1, "19:00", "20:00"), False),
    ("solapadas, B empieza antes", (1, "20:00", "22:00"), (1, "19:00", "21:00"), True),
    ("B contiene a A", (1, "20:00", "21:00"), (1, "19:00", "22:00"), True),
    ("idénticas", (1, "19:00", "21:00"), (1, "19:00", "21:00"), True),
]
