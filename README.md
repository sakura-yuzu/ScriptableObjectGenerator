# ScriptableObjectGenerator

CSVからScriptableObjectを一括で生成します。

## Getting Started

 1. プロジェクトをローカルにクローンします。
 1. 作成したいScriptableObjectのサンプルをひとつ作成し、作ったオブジェクトのassetファイルの中身をtemplate.assetにコピーします。  
  詳しくはtemplate.assetを見てください。何か伝わるかもしれません。
   - csvから読み込むので全部 `%s` になります。
   - `%` はエスケープします `%%` 
 1. data.csvにデータを作成します。
 1. main.pyを走らせるとdestの下にファイルがいっぱいできるのでそれをUnityプロジェクトに突っ込みます

画像とかはIDがわからないとどうしようもないので手動です。  
多言語化のキーと一緒にスプレッドシートでまとめて作成しています。[参考](https://docs.google.com/spreadsheets/d/1HHGQFHJcoigDjmx84NPZgxaJ6_Rk0xW3K8GiPmvGY4c/edit?usp=sharing)

## Versioning
ver.1.0.0 2023/11/26 Python 3.11.6

## Authors

Yuzu Sakura

## License / ライセンス

CC-BY