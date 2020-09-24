library(tximport)
library(jsonlite)
library(reader)


# set args
args <- commandArgs(trailingOnly = T)
default_args <- c(".", "scaledTPM")
default_flg <- is.na(args[1:2])
args[default_flg] <- default_args[default_flg]

path <- args[1]
method <- args[2]
setwd(path)

# print setting
print("exec tximport...")
print(paste(c("input path:", path)))
print(paste(c("method:", method)))
print("")

# get filenames
salmon.files <- file.path(list.files(".", pattern="_exp"), 'quant.sf')
sample_name <- c(gsub("_exp/quant.sf", "", salmon.files))
names(salmon.files) <- sample_name

# transcription counts
tx.exp <- tximport(salmon.files, type="salmon", txOut=TRUE)
write.csv(tx.exp$counts, file='transcription_count.csv', row.names=TRUE)

# transcription to gene
tx2gene <- data.frame(
    TXNAME = rownames(tx.exp$counts),
    GENEID = sapply(strsplit(rownames(tx.exp$counts), '\\.'), '[', 1)
)

# gene counts
gene.count.exp <- summarizeToGene(tx.exp, tx2gene)
write.csv(gene.count.exp$counts, file='gene_count.csv', row.names=TRUE)

# normalized
gene.norm.exp <- summarizeToGene(tx.exp, tx2gene, countsFromAbundance = method)
write.csv(gene.norm.exp$counts, file='normalized_gene_count.csv', row.names=TRUE)
