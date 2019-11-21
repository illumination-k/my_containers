import os 
import time
import shutil

from function import Command, update_params, print_single_logo, print_pair_logo


#TODO: 見通しが悪すぎるので、singleとpairを一つにまとめたい。ダミーリスト作ってzipで回すとかか？
#TODO: 共通するパラメータ∸先に定義しておいて、input_fileはペアかシングルでupdate_paramsすればよいのでは？？？？
def timer(func):
    """
    実効時間を表示するデコレータ
    """
    import functools
    import datetime
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = datetime.datetime.today()
        print('-------------------------------------------------------------')
        result = func(*args, **kwargs)
        end = datetime.datetime.today()
        print()
        print('running:', end - start)
        print()
        return result
    return wrapper


@timer
def timer_run(command, params, deco="#", deco_times=20):
    '''
    時間計測しつつコマンドを走らせる
    '''
    decoration = deco*deco_times
    command.parse_params_dict(params)
    print()
    print(decoration, command, decoration)
    command.run()


def make_use_files(in_files, args, end_type):
    if end_type=="single":
        file = in_files[0]
        basename = file.split(".")[0]
        basenames = [basename]
        input_files = [os.path.join(args.input, file)]
        trim_files = [basename + "_trim.fastq.gz"]
    elif end_type=="pair":
        file_1, file_2 = in_files
        basename = file_1.split(".")[0].rstrip("_1")
        basename_1 = file_1.split(".")[0]
        basename_2 = file_2.split(".")[0]
        input_file_1, input_file_2 = os.path.join(args.input, file_1), os.path.join(args.input, file_2)
        trim_file_1, trim_file_2 = basename_1 + "_trim.fastq.gz", basename_2 + "_trim.fastq.gz"
        basenames = [basename_1, basename_2]
        input_files = [input_file_1, input_file_2]
        trim_files = [trim_file_1, trim_file_2]
    else:
        raise ValueError("Unknown end type")

    return basename, basenames, input_files, trim_files


def fastqc_run(input_files, args, end_type):
    if end_type == "single":
        input_file = input_files[0]
        fastqc_command = Command("fastqc")
        fastqc_params = {"-o":os.path.join(args.output, "reports"), "-t":args.thread, "-k":"7", "":input_file}

    elif end_type == "pair":
        input_file_1, input_file_2 = input_files
        fastqc_command = Command("fastqc")
        fastqc_params = {"-o":os.path.join(args.output, "reports"), "-t":args.thread, "-k":"7", input_file_1+" "+input_file_2: ""}
        
    else:
        raise ValueError("Unknown end type")

    timer_run(fastqc_command, fastqc_params)


def fastp_run(input_files, trim_files, basenames, args, end_type):
    fastp_command = Command("fastp")
    if end_type == "single":
        input_file = input_files[0]
        trim_file = trim_files[0]
        basename = basenames[0]
        fastp_params = {"-i": input_file, "-o": trim_file, "-w": args.thread, 
                        "-h": os.path.join(args.output, "reports", basename+"_fastp.html"), 
                        "-j": os.path.join(args.output, "reports", basename+"_fastp.json")}
    
    elif end_type == "pair":
        input_file_1, input_file_2 = input_files
        trim_file_1, trim_file_2 = trim_files
        basename_1, basename_2 = basenames 
        fastp_params = {"-i": input_file_1, "-I": input_file_2, 
                        "-o": trim_file_1, "-O": trim_file_2, 
                        "-w": args.thread,
                        "-h": os.path.join(args.output, "reports", basename+"_fastp.html"),
                        "-j": os.path.join(args.output, "reports", basename+"_fastp.json")}
    else:
        raise ValueError("Unknown end type")

    if args.fastp is not None:
        fastp_params = update_params(fastp_params, args.fastp)
    timer_run(fastp_command, fastp_params)


def salmon_map_run(trim_files, basename, args, end_type):
    if args.salmon_ref is None:
        ref_path = "/local_volume/salmon_ref_index"
    else:
        ref_path = args.salmon_ref

    salmon_output = os.path.join(args.output, basename+"_exp")
    os.makedirs(salmon_output, exist_ok=True)
    salmon_command = Command("salmon quant")
    
    if end_type=="single":
        trim_file = trim_files[0]
        salmon_params = {
            "-i": ref_path,
            "-p": args.thread, 
            "-l": "A", "-r": trim_file, 
            "-o": salmon_output,
            "--gcBias":"", 
            "--validateMappings":"", 
            }

    elif end_type=="pair":
        trim_file_1, trim_file_2 = trim_files
        salmon_params = {
            "-i": ref_path,
            "-p": args.thread, 
            "-l": "A", 
            "-1": trim_file_1, "-2": trim_file_2, 
            "-o": salmon_output,
            "--gcBexias":"", 
            "--validateMappings":"", 
            }

    timer_run(salmon_command, salmon_params)


def hisat2_run(trim_files, basename, args, end_type):
    if args.hisat2_ref is None:
        ref_path = "/local_volume/hisat2_ref_index"
    else:
        ref_path = args.hisat2_ref
    os.makedir(os.path.join(args.input, "bam_files"), exit_ok=True)
    bam_file_name = basename + ".bam"
    bam_file = os.path.join(args.input, "bam_files", bam_file_name)
    hisat2_command = Command("hisat2")
    if end_type=="single":
        trim_file = trim_files[0]
        hisat2_params = {
            "-x": ref_path,
            "-U": trim_file,
            "-p": args.thread,
            "|":"",
            "samtools":"sort",
            "-@": args.thread,
            "-O": "BAM",
            "- >": bam_file,
            "&&":"",
            "samtools":"index",
            "-@": args.thread,
            bam_file:"",
        }
    else:
        trim_file_1, trim_file_2 = trim_files
        hisat2_params = {
            "-x": ref_path,
            "-1": trim_file_1,
            "-2": trim_file_2,
            "-p": args.thread,
            "|":"",
            "samtools":"sort",
            "-@": args.thread,
            "-O": "BAM",
            "- >": bam_file,
            "&&":"",
            "samtools":"index",
            "-@": args.thread,
            bam_file:"",
        }
    timer_run(hisat2_command, hisat2_params)
    return bam_file


def salmon_aln_run(bam_file, basename, args):
    if args.salmon_ref is None:
        ref_path = "/local_volume/salmon_ref_index"
    else:
        ref_path = args.salmon_ref

    salmon_output = os.path.join(args.output, basename+"_exp")
    os.makedirs(salmon_output, exist_ok=True)
    salmon_command = Command("salmon quant")
    salmon_params = {
        "-t": ref_path,
        "-l":"A",
        "-a":bam_file,
        "-o":salmon_output
        }

    timer_run(salmon_command, salmon_params)


def delete_intermidate(trim_files, end_type):
    if end_type=="single":
        trim_file = trim_files[0]
        os.remove(trim_file)
    elif end_type=="pair":
        trim_file_1, trim_file_2 = trim_files
        os.remove(trim_file_1)
        os.remove(trim_file_2)


@timer
def salmon_pipeline(in_files, args, end_type):
    basename, basenames, input_files, trim_files = make_use_files(in_files, args, end_type)
    fastqc_run(input_files, args, end_type)
    fastp_run(input_files, trim_files, basenames, args, end_type)
    if args.use_hisat2:
        bam_file = hisat2_run(trim_files, basename, args, end_type)
        salmon_aln_run(bam_file, basename, args)
    else:
        salmon_map_run(trim_files, basename, args, end_type)
    delete_intermidate(trim_files, end_type)


def test_pipeline(args):
    '''
    salmon及びhisat2+salmonを使ったパイプラインを実行する
    '''
    all_files = [file for file in os.listdir(args.input) if file.endswith(args.fastq_type)]
    files_1 = sorted([file for file in os.listdir(args.input) if file.endswith("_1"+args.fastq_type)])
    files_2 = sorted([file for file in os.listdir(args.input) if file.endswith("_2"+args.fastq_type)])

    single_files = list(set(all_files) - set(files_1) - set(files_2))

    # single
    print_single_logo()
    if len(single_files) == 0:
        print("#"*20, "No single files!", "#"*20)
        print()
    else:
        for in_file in single_files:
            salmon_pipeline([in_file], args, end_type="single")

    # pair
    print_pair_logo()
    if len(files_1) != len(files_2):
        raise ValueError("There are not complete pairs")
    elif len(files_1) == 0:
        print("#"*20, "No pair files!", "#"*20)
        print()
    else: 
        for in_file_1, in_file_2 in zip(files_1, files_2):
            salmon_pipeline([in_file_1, in_file_2], args, end_type="pair")

    # multiqc and delete other reports
    multiqc_command = Command("multiqc")
    multiqc_params = {args.output: "",
                      "-o": args.output}
    timer_run(multiqc_command, multiqc_params, deco="+")
    shutil.rmtree(os.path.join(args.output, "reports"))

    # tximport
    tximport_command = Command("Rscript quant2tsv.R")
    tximport_params = {args.output: "", args.method:""}
    timer_run(tximport_command, tximport_params, deco="*")


@timer
def exec_salmon_single(args, files):
    '''
    シングルエンドのファイルのsalmonのみのパイプライン
    '''
    for file in files:
        input_file = os.path.join(args.input, file)
        basename = file.split(".")[0]
        trim_file = basename + "_trim.fastq.gz"
        # fastqc
        fastqc_run([input_file], args, end_type="single")

        # fastp
        fastp_run([input_file], [trim_file], [basename], args, end_type="single")

        # salmon
        salmon_map_run([trim_file], basename, args, end_type="single")

        # delete intermediate files
        os.remove(trim_file)


@timer
def exec_salmon_pair(args, files_1, files_2):
    '''
    ペアエンドのファイルのsalmonのみのパイプライン
    '''
    if args.salmon_ref is None:
        ref_path = "/local_volume/salmon_ref_index"
    else:
        ref_path = args.salmon_ref

    for file_1, file_2 in zip(files_1, files_2):
        basename = file_1.split(".")[0].rstrip("_1")
        basename_1 = file_1.split(".")[0]
        basename_2 = file_2.split(".")[0]

        input_file_1, input_file_2 = os.path.join(args.input, file_1), os.path.join(args.input, file_2)
        trim_file_1, trim_file_2 = basename_1 + "_trim.fastq.gz", basename_2 + "_trim.fastq.gz"

        # fastqc
        fastqc_run([input_file_1, input_file_2], args, end_type="pair")

        # fastp
        fastp_run([input_file_1, input_file_2], [trim_file_1, trim_file_2], args, end_type="pair")

        #salmon
        salmon_map_run([trim_file_1, trim_file_2], basename, args, end_type="pair")

        #delete intermediate files
        os.remove(trim_file_1)
        os.remove(trim_file_2)


# singleとpair両方まとまったものにできるはず。具体的にはfile全部取得して、それを_1, _2がついているものはpairファイルにすればよい。それ以外がsingle
# TODO: そもそもfastq内部にメタデータないのか？確認するべき

def exec_pipeline(args):
    '''
    salmon及びhisat2+salmonを使ったパイプラインを実行する
    '''
    all_files = [file for file in os.listdir(args.input) if file.endswith(args.fastq_type)]
    files_1 = sorted([file for file in os.listdir(args.input) if file.endswith("_1"+args.fastq_type)])
    files_2 = sorted([file for file in os.listdir(args.input) if file.endswith("_2"+args.fastq_type)])

    single_files = list(set(all_files) - set(files_1) - set(files_2))

    # single
    print_single_logo()
    if len(single_files) == 0:
        print("#"*20, "No single files!", "#"*20)
        print()
    else:
        exec_salmon_single(args, single_files)

    # pair
    print_pair_logo()
    if len(files_1) != len(files_2):
        raise ValueError("There are not complete pairs")
    elif len(files_1) == 0:
        print("#"*20, "No pair files!", "#"*20)
        print()
    else: 
        exec_salmon_pair(args, files_1, files_2)

    # multiqc and delete other reports
    multiqc_command = Command("multiqc")
    multiqc_params = {args.output: "",
                      "-o": args.output}
    timer_run(multiqc_command, multiqc_params, deco="+")
    shutil.rmtree(os.path.join(args.output, "reports"))

    # tximport
    tximport_command = Command("Rscript quant2tsv.R")
    tximport_params = {args.output: "", args.method:""}
    timer_run(tximport_command, tximport_params, deco="*")


class PipeLine:
    def __init__(self, args):
        self.args = args
        all_files = [file for file in os.listdir(args.input) if file.endswith(args.fastq_type)]
        self.files_1 = sorted([file for file in os.listdir(args.input) if file.endswith("_1"+args.fastq_type)])
        self.files_2 = sorted([file for file in os.listdir(args.input) if file.endswith("_2"+args.fastq_type)])
        self.single_files = list(set(all_files) - set(files_1) - set(files_2))

    def __str__(self):
        return "PipeLine"

    def run(self):
        pass
