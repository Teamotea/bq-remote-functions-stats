# bq-remote-functions-stats
BQ で統計的検定をするためのリモート関数を集めたレポジトリです。

## 使い方
以下の手順にしたがって、BQ 内にリモート関数を作成してください。
1. このレポジトリをクローンする。
2. `.env.template` ファイルを `.env` という名前でコピーする。
3. `.env` ファイルを編集し、`FUNCTION_NAME` と `PROJECT_ID` に Cloud Functions 名とプロジェクトID名を入れる（Cloud Functions 名は自分の付けたいもので問題なし）。
4. シェルから `make deploy` を実行し、Cloud Functions をデプロイする。 
5. [こちら](https://cloud.google.com/bigquery/docs/reference/standard-sql/remote-functions) のドキュメントを参考に BQ からのコネクションを作成。
   - 母比率の差の検定を行うときは `CREATE FUNCTION` の `OPTIONS` 内の `user_defined_context` で `("test_type", "prop.test")` を指定する

リモート関数の使用方法自体は以下の記事の「## 実際に検定をしてみる」に載っています。
https://timotimotimotimo.hatenablog.com/entry/2022/10/12/235842
