# hello-world

> 從 Git 入門起步，轉型為 AI 技能庫（AI Skills Repository）

## 技能清單

### Tech_Stock_Valuation_And_Strategy_Analysis

針對兼具「景氣循環」與「結構性成長（AI、綠能）」特性的科技股，執行標準化的基本面健檢、雙軌情境估值與買賣策略矩陣分析的 LLM Agent 技能。

| 檔案 | 說明 |
|---|---|
| `skills/Tech_Stock_Valuation_And_Strategy_Analysis/system_prompt.md` | 框架無關的系統提示詞範本（含 4 個模板變數） |
| `skills/Tech_Stock_Valuation_And_Strategy_Analysis/agent_integration.py` | Anthropic SDK 整合範例與可執行 Demo |
| `skills/Tech_Stock_Valuation_And_Strategy_Analysis/example_ADATA_3260TW.md` | 威剛科技（3260.TW）完整示範輸出 |
| `.claude/commands/tech-stock-analysis.md` | Claude Code 斜線指令 `/tech-stock-analysis` |

#### 快速開始（Anthropic SDK）

```bash
pip install anthropic
export ANTHROPIC_API_KEY=your_key_here
python skills/Tech_Stock_Valuation_And_Strategy_Analysis/agent_integration.py
```

#### 快速開始（Claude Code 斜線指令）

在 Claude Code 中輸入：
```
/tech-stock-analysis 3260.TW 威剛 "NT$68.5 位於20MA上方" "Q2 EPS 3.21, 毛利率22.3%" "AI PC, DDR5, 低價庫存去化"
```

#### 整合目標

- **Claude Code**：`.claude/commands/` 斜線指令
- **Anthropic Python SDK**：`agent_integration.py` 直接可用
- **LangChain**：`PromptTemplate(template=..., input_variables=[...])` 讀取 `system_prompt.md`
- **Jinja2 / RAG 系統**：`{stock_symbol}` 等模板變數與大多數框架原生相容
