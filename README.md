# AIコーディング研修

## 目的

本研修では GitHub Copilot を利用し、

* AIチャット
* コード補完
* テスト生成
* エラー解析
* コードレビュー

を体験します。

また、AIに仕事を任せるだけではなく、

「どのような指示を出せば良い結果が得られるか」

を学習します。

---

# 事前準備

## 1. VS Codeを起動

本フォルダを VS Code で開いてください。

---

## 2. GitHub Copilotへログイン

右下またはCopilotアイコンからログインしてください。

---

## 3. Copilot Chatを開く

画面左側のCopilotアイコンをクリックし、

Copilot Chatを利用できることを確認してください。

---

# フォルダ構成

```text
ai-coding-training/
│
├─ prompts/
├─ exercise01/
├─ exercise02/
├─ exercise03/
├─ exercise05/
├─ exercise06/
└─ README.md
```

---

# フォルダの役割

## prompts

AIへ送信するプロンプトが格納されています。

演習ごとに該当ファイルを開き、
内容をCopilot Chatへ貼り付けてください。

例

```text
prompts/exercise01_bad.txt
prompts/exercise01_good.txt
```

---

## exerciseXX

実際に作業するフォルダです。

生成したコードや成果物を保存します。

---

# 演習一覧

## 演習①

良いプロンプトと悪いプロンプトを比較する

使用ファイル

```text
prompts/exercise01_bad.txt
prompts/exercise01_good.txt
```

保存先

```text
exercise01/bad_prompt
exercise01/good_prompt
```

---

## 演習②

Copilotコード補完を体験する

使用ファイル

```text
exercise02/utils.py
prompts/exercise02.txt
```

---

## 演習③

AIと対話しながらコードを改善する

使用ファイル

```text
exercise03/calculator.py
prompts/exercise03.txt
```

※ 同じチャットを使い続けてください

---

## 演習④

テストコードを生成する

使用ファイル

```text
exercise03/calculator.py
prompts/exercise04.txt
```

出力先

```text
exercise04/test_calculator.py
```

---

## 演習⑤

AIでエラー解析を行う

使用ファイル

```text
exercise05/calculator_bug.py
prompts/exercise05.txt
```

---

## 演習⑥

AIでコードレビューを行う

使用ファイル

```text
exercise06/review_target.py
prompts/exercise06.txt
```

---

# 演習時の注意

## AIを鵜呑みにしない

AIは間違えることがあります。

生成結果は必ず確認してください。

---

## エラーは学習のチャンス

エラーが発生した場合は、

* エラーメッセージ
* 該当コード

をAIへ渡してください。

---

## 良い結果は良い指示から生まれる

AIの性能だけではなく、

指示の出し方も重要です。

本研修で学習した

* 役割
* コンテキスト
* 出力形式
* 制約
* 評価基準

を意識して活用してください。

---

# 困ったとき

* 講師へ質問する
* エラーメッセージを確認する
* AIへ相談する

の順で対応してください。

---

それでは AI コーディングを楽しみましょう。
