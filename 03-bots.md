# 03 Bot 开发

## 创建 Bot

1. 在 Telegram 里打开 @BotFather（注意认准官方，用户名就是 `@BotFather`，带认证标识）。
2. 发送 `/newbot`，依次设置显示名称和用户名。用户名必须以 `bot` 结尾，如 `my_note_bot`，全局唯一。
3. BotFather 返回一个 Token，形如 `123456:ABC-DEF...`。

> ⚠️ Token 就是 Bot 的密码：不要写进代码仓库、不要发到群里、不要截图外传。泄露后用 `/revoke` 立刻作废。

常用 BotFather 命令：`/setdescription`（简介）、`/setabouttext`、`/setuserpic`（头像）、`/setcommands`（命令菜单）、`/deletebot`。

## Bot API 基础

- 接口形式：`https://api.telegram.org/bot<TOKEN>/METHOD`
- 常用方法：

| 方法 | 用途 |
| --- | --- |
| `getMe` | 验证 Token、获取 Bot 信息 |
| `sendMessage` | 发送文本消息 |
| `sendPhoto` / `sendDocument` | 发送图片 / 文件 |
| `getUpdates` | 拉取新消息（Polling 模式） |
| `setWebhook` / `deleteWebhook` | 设置 / 删除 Webhook |
| `answerCallbackQuery` | 响应按钮点击 |

手动验证 Token 是否有效（把 `<TOKEN>` 换成你的）：

```bash
curl "https://api.telegram.org/bot<TOKEN>/getMe"
```

返回 `"ok": true` 即 Token 可用。

## 最小可运行示例（Python，Polling）

```bash
pip install python-telegram-bot
export BOT_TOKEN="123456:ABC-DEF..."
```

```python
import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = os.environ["BOT_TOKEN"]  # 从环境变量读，绝不硬编码

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("你好，我是你的第一个 Bot。发送任意文字，我会复述它。")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(update.message.text)

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    app.run_polling()

if __name__ == "__main__":
    main()
```

运行后在 Telegram 里打开你的 Bot，发 `/start` 测试。

## Webhook vs Polling

| | Polling（轮询） | Webhook（推送） |
| --- | --- | --- |
| 原理 | 你的程序定时调 `getUpdates` 拉消息 | Telegram 主动 POST 到你的 HTTPS 地址 |
| 部署要求 | 能联网即可，不需要公网地址 | 需要公网 HTTPS 域名 / 证书 |
| 适合 | 本地开发、个人小 Bot、低频使用 | 生产环境、实时性要求高 |
| 注意 | 同一 Token 只能一个程序在拉，否则互相抢消息 | 切换前先 `deleteWebhook` / 反之亦然 |

本地开发想用 Webhook 调试，可用 ngrok / cloudflared 把本地端口临时暴露出去，见 [07 自动化与工具](./07-automation.md)。

## 常用库

| 语言 | 库 | 特点 |
| --- | --- | --- |
| Python | python-telegram-bot | 文档全，上手最稳，适合 Bot API |
| Python | aiogram | 异步，适合高并发 Bot |
| Python | Telethon / Pyrogram | 走 MTProto，能做用户号自动化，见 07 章 |
| Node.js | grammY / telegraf | TypeScript 支持好 |
| Go | gotd | MTProto 实现 |

## 群组里读不到消息？Privacy Mode

- Bot 默认开启 Privacy Mode：在群里只能收到命令、回复它的消息、以及 @ 它的消息，**收不到全部群消息**。
- 需要读全部消息时：BotFather → `/setprivacy` → Disable，或者把 Bot 设为群管理员（管理员 Bot 不受 Privacy Mode 限制）。
- 改完设置后，要把 Bot 移出群再重新拉进去才生效，这是最常见的坑。

## 安全与限额常识

- Token 只放环境变量或密钥管理服务，`.env` 文件务必写进 `.gitignore`。
- 群发 / 频繁调用会触发 API 限流（返回 429，按 `retry_after` 等待），不要用 Bot 做批量骚扰发送，会被封。
- Bot 不能主动给从未与它对话过的用户发私聊消息；用户必须先打开 Bot 并点 Start。

## 下一步

- 用户号自动化、导出、调试工具 → [07 自动化与工具](./07-automation.md)
- 官方完整 API → [09 资源汇总](./09-resources.md)
