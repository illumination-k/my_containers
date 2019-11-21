from function import Command, update_params
import argparse 

parser = argparse.ArgumentParser()
parser.add_argument("--fastqc", nargs="*")
args = parser.parse_args()

fastqc_dict = {"-o":"test", "-t":"2", "-k":"7", "":"FILENAME"}
fastqc_command = Command("fastqc")
fastqc_command.parse_params_dict(fastqc_dict)
print(fastqc_command)

update_fastqc_params = args.fastqc
updated_dict = update_params(fastqc_dict, update_fastqc_params)
fastqc_command.parse_params_dict(updated_dict)
print(updated_dict)


