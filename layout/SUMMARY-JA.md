# PyUnicodeObject 配置依存調査

以前の PyPI 上位4,000パッケージ調査の保存済み資料を再利用しました。`PyUnicodeObject` の実際の Python 3 向け配置依存は **8パッケージ**で確認できました: cython、ddtrace、lxml、multidict、numba、numpy、py-spy、pyobjc-core。Cython GDB と py-spy はデバッガー／プロファイラーなので、8件をそのまま拡張モジュール数とは呼びません。

NumPy・multidict・lxml・PyObjC は構造体埋め込みやサイズに依存し、Numba はサイズ／オフセットを検査しています。ddtrace・py-spy・Cython GDB は内部フィールドやヘッダー直後のデータを読みます。補助構造体も調べると、orjson・ormsgpack・msgspec・JPype・pyjson5 の出力構築、MyPy/LibRT の length 書換え、ddtrace の state 内 taint 書込みなども確認できました。

全条件分岐・生成コード・互換実装・テスト・同梱CPythonを含めた直接配置依存の和集合は **67パッケージ**です。この数を独立した手書き実装数や実行確認済み件数とは扱いません。型名だけ、標準APIに渡すだけのキャスト、定義だけの複製構造体は区別しました。

3,788 sdists の保存資料から 131,701 ソース記録を調べ、309候補ファイル／4,057型名出現の分類を完了しました。sdist不在211件とメタデータ失敗1件は不明で、ゼロ扱いしていません。ビルド・インストール・追加ダウンロード・コミット・公開は実施していません。Frozendictのビルド選択情報欠落と既存検証にないリンクは明示しています。

[英語報告書](REPORT.md)、[CSV](data/cases.csv)、[JSON](data/cases.json)、[全4,000件のカバレッジ](data/coverage4000.csv)を別ディレクトリに保存しました。
