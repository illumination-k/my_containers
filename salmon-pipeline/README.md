# RNA-seq Pipeline on Docker

## 概要

簡単にRNA-seq解析を行う環境を構築し、そのパイプラインをワンライナーで動かせるようにしました。RNA-seq解析をする際に、ぜひご利用ください。

**dockerのインストールが必要です**  
インストール方法に関してはこちらを参考にしてください。

- mac: https://qiita.com/kurkuru/items/127fa99ef5b2f0288b81
- windows: https://ops.jig-saw.com/techblog/docker-for-windows-install/

**BAMファイルは出力しないパイプラインです。Transcripts、GeneごとのカウントデータおよびScaledTPMによって正規化されたカウントデータを出力します。**

## Usage

まず、DockerのSettingを変更してください。  
Docker -> Settings(or Preferences) -> Advances -> メモリを8GB以上に設定

解析したい`fastq.gz`ファイルを1つのディレクトリにまとめてください。

下記のコマンドを順に実行してください。多少時間はかかります。${input_path}に解析したいファイルをまとめたディレクトリのパスを入力してください。

```bash
docker pull illumination27/salmon-pipeline:v0.7
docker run --rm -it -v ${input_path}:/local_volume illumination27/salmon-pipeline:v0.7 bash
# docker内部でpipelineを実行
python salmon_pipeline.py -i /local_volume -o /local_volume -r ./ref_index
# usage
python salmon_pipeline.py -h
```

### Output files

- transcript_count.csv: Transcriptごとのカウントデータ
- gene_count.csv: Geneごとのカウントデータ
- scaledTPM_gene_cout: scaledTPMによって正規化されたGeneごとのカウントデータ

## 詳細

- Quality check: fastQC <sup>1</sup>
- Quality control: fastp <sup>2</sup>
- Mapping and quantify: salmon <sup>3</sup>
- Count expression: tximport <sup>4</sup>
- Integration of reports: multiqc <sup>5</sup>

## Reference

1. Andrews S. (2010). FastQC: a quality control tool for high throughput sequence data.
2. fastp: an ultra-fast all-in-one FASTQ preprocessor Shifu Chen, Yanqing Zhou, Yaru Chen, Jia Gu Bioinformatics, Volume 34, Issue 17, 1 September 2018, Pages i884–i890,
3. Patro R, Duggal G, Love MI, Irizarry RA, Kingsford C. Salmon provides fast and bias-aware quantification of transcript expression. Nat Methods. 2017;14(4):417-419.
4. Soneson C, Love MI, Robinson MD. Differential analyses for RNA-seq: transcript-level estimates improve gene-level inferences. F1000Research. 2015, 7(3):562-78.
5. MultiQC: Summarize analysis results for multiple tools and samples in a single report
Philip Ewels, Måns Magnusson, Sverker Lundin and Max Käller Bioinformatics (2016)
