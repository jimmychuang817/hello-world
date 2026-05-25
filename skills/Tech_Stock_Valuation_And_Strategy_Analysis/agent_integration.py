"""
Tech_Stock_Valuation_And_Strategy_Analysis — Anthropic SDK Integration

Usage:
    pip install anthropic
    export ANTHROPIC_API_KEY=your_key
    python agent_integration.py

Or import and call analyze_stock() in your own application.
"""

import anthropic
from pathlib import Path

SYSTEM_PROMPT_PATH = Path(__file__).parent / "system_prompt.md"


def load_system_prompt() -> str:
    return SYSTEM_PROMPT_PATH.read_text(encoding="utf-8")


def fill_template(template: str, **kwargs: str) -> str:
    """Safe template filler — replaces only the known 4 variables.

    Avoids Python's .format() KeyError when financial_data or other inputs
    contain literal curly braces (e.g. JSON snippets).
    """
    for key, value in kwargs.items():
        template = template.replace(f"{{{key}}}", value)
    return template


def analyze_stock(
    stock_symbol: str,
    current_price: str,
    financial_data: str,
    catalyst_keywords: str,
    model: str = "claude-sonnet-4-6",
    max_tokens: int = 4096,
) -> str:
    """Run the Tech_Stock_Valuation_And_Strategy_Analysis skill.

    Parameters
    ----------
    stock_symbol : e.g. "3260.TW 威剛科技"
    current_price : e.g. "NT$68.5，位於20日均線 NT$65.2 上方"
    financial_data : e.g. "Q2 EPS NT$3.21，累計 EPS NT$5.87，毛利率 22.3%，存貨週轉 45 天"
    catalyst_keywords : e.g. "AI PC換機潮, DDR5需求增, 低價庫存去化完成"

    Returns
    -------
    str : Full analysis report in Markdown format
    """
    client = anthropic.Anthropic()

    raw_template = load_system_prompt()
    system_prompt = fill_template(
        raw_template,
        stock_symbol=stock_symbol,
        current_price=current_price,
        financial_data=financial_data,
        catalyst_keywords=catalyst_keywords,
    )

    message = client.messages.create(
        model=model,
        max_tokens=max_tokens,
        system=system_prompt,
        messages=[
            {
                "role": "user",
                "content": (
                    "請依照 Tech_Stock_Valuation_And_Strategy_Analysis 框架，"
                    "完整執行四步驟分析並輸出報告。\n\n"
                    f"股票代號：{stock_symbol}\n"
                    f"當前股價：{current_price}\n"
                    f"財報數據：{financial_data}\n"
                    f"催化劑關鍵字：{catalyst_keywords}"
                ),
            }
        ],
    )

    return message.content[0].text


if __name__ == "__main__":
    # Demo: 威剛科技 3260.TW
    result = analyze_stock(
        stock_symbol="3260.TW 威剛科技（ADATA Technology）",
        current_price="NT$68.5，20日均線 NT$65.2，60日均線 NT$58.8，接近年線壓力區",
        financial_data=(
            "2024 Q2 單季 EPS NT$3.21（歷史次高）；"
            "H1 累計 EPS NT$5.87；"
            "Q2 毛利率 22.3%（QoQ +3.1pp，YoY +8.4pp）；"
            "存貨週轉天數 45 天（前季 72 天，去化明顯）；"
            "Q2 營業利益率 8.7%"
        ),
        catalyst_keywords=(
            "AI PC換機潮帶動DDR5需求, "
            "LPCAMM2模組進入量產, "
            "低價DRAM庫存去化完成推升ASP, "
            "伺服器DRAM需求回溫, "
            "工控與車用模組佔比提升"
        ),
    )
    print(result)
