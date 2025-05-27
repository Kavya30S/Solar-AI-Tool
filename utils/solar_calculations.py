import pandas as pd

def calculate_solar_potential(roof_area, orientation, tilt, location="Singapore"):
    solar_irradiance = 5.0
    panel_efficiency = 0.20
    system_efficiency = 0.85
    effective_area = roof_area * 0.8
    daily_energy = effective_area * solar_irradiance * panel_efficiency * system_efficiency
    annual_energy = daily_energy * 365
    cost_per_watt = 2.0
    system_size_watts = daily_energy * 1000 / 5
    installation_cost = system_size_watts * cost_per_watt
    electricity_rate = 0.25
    annual_savings = annual_energy * electricity_rate
    payback_period = installation_cost / annual_savings if annual_savings > 0 else float('inf')
    return {
        "effective_area_m2": effective_area,
        "daily_energy_kwh": daily_energy,
        "annual_energy_kwh": annual_energy,
        "system_size_kw": system_size_watts / 1000,
        "installation_cost_usd": installation_cost,
        "annual_savings_usd": annual_savings,
        "payback_period_years": payback_period
    }