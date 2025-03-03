def calc_Button(air_flow: int, t_in: int, t_out: int, density_t: float) -> float:
    calc = (0.278 * (air_flow * (density_t) * 1.005 * (t_in-t_out))) / 1000
    return str(round(calc, 2))
