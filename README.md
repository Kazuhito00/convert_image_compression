# convert_image_compression
OpenCVを使用して簡易に画像圧縮形式を変換するスクリプトです。

# Requirement
* opencv-python 4.5.2.52(or later)
* tqdm 4.48.2 (or later)

# Usage
```bash
python source_dir target_dir --mode=0
```
source_dir：変換元画像が格納されているディレクトリ<br>
target_dir：変換後の画像を保存するディレクトリ<br>
--mode：変換モード(0:JPG→PNG(デフォルト) 1:PNG→JPG)<br>

# Author
高橋かずひと(https://twitter.com/KzhtTkhs)
 
# License 
convert_image_compression is under [Apache 2 license](LICENSE).
