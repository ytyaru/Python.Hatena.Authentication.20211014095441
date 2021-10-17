# 用語

用語|意味
----|----
`Authentication`|認証。サービスへアクセスしてきたユーザが「本人であるかどうか」を検証する。
`Authorization`|承認。サービスへアクセスしてきた認証済みユーザが「指定したリソースへアクセスできるかどうか」を制御する。

# はてな認証

* Basic
* WSSE
* OAuth1

認証方法|はてなID|パスワード|API-KEY|consumer_key|consumer_secret|token|token_secret|scopes
--------|--------|----------|-------|------------|---------------|-----|------------|------
Basic|⭕|⭕|❌|❌|❌|❌|❌|❌
WSSE|⭕|❌|⭕|❌|❌|❌|❌|❌
OAuth1|⭕|❌|❌|⭕|⭕|⭕|⭕|⭕

## 安全性

順|認証方法|理由
--|--------|----
1|OAuth1|TokenやKeyが漏洩しても簡単に変更できるから。
2|WSSE|API-KEYが漏洩してもAPIを叩けるだけでログインはできないから。
3|Basic|パスワードが漏洩したらアカウントハックされてしまうから。

# OAuthアプリケーション

* 名称
* 説明
* URL
* ロゴ画像
* アイコン画像
* Keys
    * OAuth Consumer Key
    * OAuth Consumer Secret
* URLs
    * Temporary Credential Request URL	https://www.hatena.com/oauth/initiate
    * Resource Owner Authorization URL (PC)	https://www.hatena.ne.jp/oauth/authorize
    * Resource Owner Authorization URL (スマートフォン)	https://www.hatena.ne.jp/touch/oauth/authorize
    * Resource Owner Authorization URL (携帯電話)	http://www.hatena.ne.jp/mobile/oauth/authorize
    * Token Request URL	https://www.hatena.com/oauth/token
* Scopes
    * ✔ read_public	公開情報の読み取り
    * ✔ write_public	公開情報の読み取りと書き込み、削除
    * ✔ read_private	プライベート情報を含む情報の読み取り
    * ✔ write_private	プライベート情報を含む情報の読み取りと書き込み、削除
* 現在の状態
    * 発行日時
    * 状態（有効・無効）
    * 認証者数

