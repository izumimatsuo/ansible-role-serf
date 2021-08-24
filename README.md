# ansible-role-serf

CentOS 7 に serf を導入する ansible role です。

## 設定項目

以下の設定項目は上書き可能。

| 項目名              | デフォルト値 | 説明                                                                |
| ------------------- | ------------ | ------------------------------------------------------------------- |
| serf_bind_host      | None         | bindするホスト名かIPアドレス（省略した場合は、ansible_host を使う） |
| serf_join_hosts     | []           | join するホスト名かIPアドレス                                       |
| serf_role_name      | None         | ロール名                                                            |
| serf_event_handlers | []           | イベントハンドラ                                                    |
