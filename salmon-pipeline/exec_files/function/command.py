import subprocess 

class Command:
    def __init__(self, name, params=None):
        self.name = name
        self.params = params
        self.cmd = [name] 
        if params is not None:
            self.cmd += self.params

    def _update_cmd(self):
        self.cmd =[self.name] + self.params

    def __str__(self):
        self._update_cmd()
        return " ".join(self.cmd)

    def update_params(self, params):
        no_hyphen, hyphen, double_hyphen = [], [], []
        no_hyphen = [param for param in params if not param.startswith("-")]
        hyphen = [param for param in params if (param.startswith("-") and (not param.startswith("--")))]
        double_hyphen = [param for param in params if param.startswith("--")] 
        params_dict = dict(zip(hyphen, no_hyphen))
        

    def parse_params_dict(self, D):
        self.params = []
        for k, v in D.items():
            if k != "":
                self.params.append(k)
            if v != "":
                self.params.append(v)
        self._update_cmd()


    def run(self, join=True, shell=True):
        if join:
            subprocess.run(" ".join(self.cmd), shell=shell)
        else:   
            subprocess.run(self.cmd)


