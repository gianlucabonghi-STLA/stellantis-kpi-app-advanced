import pandas as pd

def match_dates(a, b):
    try: return pd.to_datetime(a) == pd.to_datetime(b)
    except: return False

def pv_matches_x2(pv, x2): return match_dates(pv, x2)

def ppap_matches_x3(ppap, x3): return match_dates(ppap, x3)

def readiness_indicator(value): return '🟢' if str(value).lower() == 'true' else '🔴'