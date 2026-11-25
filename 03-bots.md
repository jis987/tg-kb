# 03 Bot 开发

## 创建 Bot

1. 与 @BotFather 对话
2. `/newbot` → 设置名称与用户名（必须以 bot 结尾）
3. 获得 Token：`123456:ABC-DEF...`

## Bot API

- HTTPS REST：`https://api.telegram.org/bot<TOKEN>/METHOD`
- 常用方法：sendMessage、sendPhoto、getUpdates、setWebhook

## Webhook vs Polling

- Polling：getUpdates 轮询，适合开发
- Webhook：Telegram 推送，适合生产

## 常用库

- Python: python-telegram-bot, aiogram, Telethon, Pyrogram
- Node: telegraf, grammy
- Go: gotd

## Bot 权限

Bot 在群组中默认无法读取消息，需在 BotFather 开启 Privacy Mode 关闭或设为管理员。
