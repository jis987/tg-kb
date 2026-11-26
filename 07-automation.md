# 07 自动化与工具

## 先分清：Bot API vs 用户号自动化

| | Bot API（03 章） | MTProto 用户号（本章） |
| --- | --- | --- |
| 身份 | 独立的 Bot 账号 | 你的个人账号本身 |
| 能力 | 收发消息、按钮、命令等官方接口 | 能做个人账号能做的一切：读历史、监听所有聊天 |
| 风险 | 低，按官方规则用即可 | 高：行为像真人批量操作容易触发限制甚至封号 |
| 适合 | 对外服务、群管理、通知 | 个人归档、数据导出、个人效率工具 |

**原则**：能用 Bot 做的绝不用用户号。用户号自动化只用于你自己账号的个人用途，低频、克制。

## Telethon 最小示例（用户号，只读监听）

需要先在 https://my.telegram.org 申请 `api_id` / `api_hash`（这是账号级凭据，保密级别等同密码）。

```bash
pip install telethon
export TG_API_ID="123456"
export TG_API_HASH="abcdef..."
```

```python
import os
from telethon import TelegramClient, events

client = TelegramClient("my_session", int(os.environ["TG_API_ID"]), os.environ["TG_API_HASH"])

@client.on(events.NewMessage(chats="me"))  # 只监听发给「保存的消息」的新消息
async def handler(event):
    print("Saved:", event.raw_text)

client.start()          # 首次运行会要求输入手机号和验证码
client.run_until_disconnected()
```

注意：

- `my_session.session` 文件等于登录凭据，泄露 = 账号被接管，务必加入 `.gitignore`，不要上传。
- 首次登录的验证码只输进你自己运行的程序，不要经过任何第三方网站。

Pyrogram 用法类似，API 风格不同，二选一即可，不要混用。

## 数据导出

- 轻量：Desktop 端官方导出（设置 → 高级 → 导出 Telegram 数据），见 [05 隐私与安全](./05-privacy-security.md)。
- 编程式：用 Telethon 拉取指定聊天的历史消息存为 JSON / 入库，适合做个人归档和检索。控制频率，遇到 `FloodWait` 必须按提示等待，硬重试会加重限制。

## Webhook 调试

本地开发 Bot 的 Webhook 模式时，把本地端口临时暴露到公网：

```bash
# 任选其一
ngrok http 8080
cloudflared tunnel --url http://localhost:8080
```

拿到临时 HTTPS 地址后调用 `setWebhook` 指过去即可。临时地址每次重启会变，只适合调试，生产环境用固定域名 + 正式证书。

Telegram 还提供 Bot API 测试环境（test server），适合做破坏性实验，避免污染正式 Bot。

## 常用官方 / 半官方 Bot

| Bot | 用途 |
| --- | --- |
| @BotFather | 创建和管理 Bot |
| @userinfobot | 查询用户 / 群的 ID（第三方，注意隐私） |
| @stickers | 贴纸包管理 |
| @SpamBot | 查询账号是否被限制、申诉入口 |

## 红线

- 不做批量加群、批量私聊、刷量、绕过平台限制的脚本 —— 这是封号和本库明确不写的内容。
- 任何自动化都先在小号 / 测试群验证，再碰主账号和正式群。
