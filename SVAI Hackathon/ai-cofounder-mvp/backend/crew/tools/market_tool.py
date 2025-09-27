
# Simple market info tool. Uses yfinance for price and a demo headline from a lightweight endpoint.
# In restricted environments yfinance may fallback; handle gracefully.
import datetime as dt
from crewai_tools import tool

try:
    import yfinance as yf
except Exception:
    yf = None

@tool("get-stock-price")
def get_stock_price(ticker: str) -> str:
    """Return the latest price for a ticker."""
    if yf is None:
        return "Could not import yfinance; price unavailable."
    try:
        t = yf.Ticker(ticker)
        p = t.fast_info.last_price
        if p is None:
            return "Price unavailable."
        return f"{ticker.upper()} ${p:.2f} (approx, {dt.datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')})"
    except Exception as e:
        return f"Error fetching price: {e}"

@tool("get-market-headline")
def get_market_headline(ticker: str) -> str:
    """Return a demo one-liner headline placeholder. Replace with a real news API if desired."""
    return f"Latest quick-take on {ticker.upper()}: steady interest; watch macro data releases."
