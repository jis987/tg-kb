# Telegram 知识库 / TG Knowledge Base

> 一份用中文写、持续补充的 Telegram 知识库：从注册入门、客户端选择，到 Bot 开发、频道群组运营、隐私安全和自动化工具。
> 所有内容以 Markdown 维护，适合直接在 GitHub 阅读，也适合作为自己搭建 TG 机器人 / 运营频道时的速查手册。

## 这是什么

这个仓库不是链接收藏夹，而是一套按主题组织的学习笔记：

- **新手**：按 01 → 02 → 05 的顺序读，先把账号注册好、把两步验证和隐私设置做完。
- **想做 Bot 的人**：直接看 03 和 07，里面有可运行的最小示例、Webhook 与 Polling 的取舍、常见坑。
- **运营频道 / 群组的人**：重点看 04 和 06，包含权限、话题、防垃圾和搜索发现的方法。
- **遇到问题时**：先查 08 常见问题，再查 09 资源汇总里的官方文档入口。

## 目录

| 章节 | 内容 | 适合谁 |
| --- | --- | --- |
| [01 基础入门](./01-basics.md) | Telegram 是什么、核心概念、注册与用户名规则 | 新手 |
| [02 客户端与平台](./02-clients.md) | 官方 / 第三方客户端对比、多端同步、存储设置 | 所有人 |
| [03 Bot 开发](./03-bots.md) | 用 BotFather 建 Bot、Bot API、最小可运行示例、Webhook vs Polling | 开发者 |
| [04 频道与群组](./04-channels-groups.md) | 群组 / 超级群 / 频道区别、权限、话题、防垃圾 | 运营者 |
| [05 隐私与安全](./05-privacy-security.md) | 秘密聊天、两步验证、隐私清单、会话管理、防诈骗 | 所有人 |
| [06 搜索与发现](./06-search-discovery.md) | 全局搜索、频道内搜索、Saved Messages 工作流 | 所有人 |
| [07 自动化与工具](./07-automation.md) | Telethon / Pyrogram、导出、Webhook 调试、Bot 与用户号的区别 | 开发者 |
| [08 常见问题](./08-faq.md) | 验证码、封号、文件限制、Bot 读不到消息等问题 | 所有人 |
| [09 资源汇总](./09-resources.md) | 官方文档、开发库、学习路线 | 所有人 |

## 快速开始（做 Bot）

```bash
# 1. 在 Telegram 里找 @BotFather，用 /newbot 创建 Bot，拿到 Token
# 2. 本地准备 Python 环境
python3 -m venv .venv && source .venv/bin/activate
pip install python-telegram-bot

# 3. 把 Token 放进环境变量，不要写进代码、不要提交到 Git
export BOT_TOKEN="123456:ABC-DEF..."

# 4. 示例代码见 03-bots.md 的「最小可运行示例」
```

> ⚠️ Bot Token 等于 Bot 的密码。泄露后任何人都能冒充你的 Bot 发消息，第一时间去 @BotFather 用 `/revoke` 作废并换新。

## 如何贡献

见 [CONTRIBUTING.md](./CONTRIBUTING.md)：包括写作风格、提交方式和「不写什么」（不写绕过平台规则、批量骚扰、盗号之类内容）。

## 说明

- 本库为个人学习整理，与 Telegram 官方无关；功能和限制以 [官方文档](https://core.telegram.org) 为准，数字类信息（如文件大小、群人数上限）会随官方调整而变化。
- 引用官方或第三方资料时已尽量标注来源链接，见各章节末尾。
