# 09 资源汇总

## 官方（遇到问题先查这里）

- 官网与下载：https://telegram.org
- 官方博客（功能更新）：https://telegram.org/blog
- 开发者文档总入口：https://core.telegram.org
- Bot API 文档：https://core.telegram.org/bots/api
- Bot 功能说明（命令、按钮、Web App 等）：https://core.telegram.org/bots/features
- MTProto 协议：https://core.telegram.org/mtproto
- 用户号 API 申请（api_id / api_hash）：https://my.telegram.org

查文档的方法：先在本库对应章节找中文说明和坑，细节参数再去官方文档对应页面确认 —— 官方文档永远是最终依据。

## 开发库

| 语言 | 库 | 文档 |
| --- | --- | --- |
| Python | python-telegram-bot | https://python-telegram-bot.org |
| Python | aiogram | https://docs.aiogram.dev |
| Python | Telethon | https://docs.telethon.dev |
| Python | Pyrogram | https://docs.pyrogram.org |
| Node.js | grammY | https://grammy.dev |
| Go | gotd | https://github.com/gotd/td |

选型一句话：做 Bot 优先 python-telegram-bot / aiogram / grammY；做个人号自动化才用 Telethon / Pyrogram，风险见 [07 自动化与工具](./07-automation.md)。

## 建议学习路线

1. **只用，不开发**：01 → 02 → 05 → 06，本库这四章足够日常用好。
2. **做第一个 Bot**：03 章示例跑通 → 给 Bot 加命令菜单和按钮 → 部署到一台小服务器（Webhook 模式）。
3. **运营社区**：04 章防垃圾清单落地 → 06 章 hashtag 目录法 → 用管理 Bot 做入群验证和自动规则。
4. **进阶自动化**：07 章先想清 Bot 能不能替代，确实需要用户号时再学 Telethon，并从只读监听开始。

## 本库维护约定

- 每章末尾尽量给出「下一步」或官方来源，方便继续深入。
- 数字类事实（上限、费率、功能状态）标注以官方为准，發現过期直接提 PR 修正，方式见 [CONTRIBUTING.md](./CONTRIBUTING.md)。
