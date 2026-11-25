# TG Knowledge Base / Telegram 知识库

一个牛逼的 Telegram 知识库系统：自动采集、智能分类、全文搜索、向量检索、AI 摘要。

## ✨ 特性

- 📥 **多源采集**：支持群组/频道/私聊历史消息批量导入
- 🔍 **全文搜索**：基于 SQLite FTS5 的极速全文检索
- 🧠 **语义检索**：向量嵌入 + 相似度搜索
- 🏷️ **智能标签**：自动分类、主题聚类、关键词提取
- 📝 **AI 摘要**：长文自动摘要、对话总结
- 📊 **可视化**：活跃度、话题趋势、用户统计
- 🔐 **隐私优先**：本地存储、可选加密
- 🌐 **Web UI**：现代化界面，开箱即用

## 🏗️ 架构

```
tg-kb/
├── collector/     # Telegram 采集器 (Telethon)
├── indexer/       # 索引与向量化
├── search/        # 搜索引擎
├── ai/            # AI 摘要与分类
├── api/           # FastAPI 后端
├── web/           # 前端界面
├── storage/       # 数据存储层
└── cli/           # 命令行工具
```

## 🚀 快速开始

```bash
# 安装依赖
pip install -r requirements.txt

# 配置
cp .env.example .env
# 填入 API_ID / API_HASH / BOT_TOKEN

# 采集消息
python -m tgkb collect --chat @channel --limit 10000

# 启动 Web
python -m tgkb serve
```

## 📄 License

MIT
