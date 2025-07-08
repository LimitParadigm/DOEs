from pandapower.plotting.plotly import simple_plotly, pf_res_plotly

class NetworkAbstract:
    def __init__(self, net):
        self.net = net
        
    def change_network(self, net):
        self.net = net

    def run_scenario(self, scenario):
        pass

    def summary(self):
        print(f"Number of transformers: {len(self.net.trafo)}. Type: {self.net.trafo.std_type.values[0]}")
        print(f"Number of busses: {len(self.net.bus)}")
        print(f"Number of lines: {len(self.net.line)}")
        print(f"Number of loads: {len(self.net.load)}")
        print(f"Number of generators: {len(self.net.gen)} (P-V), {len(self.net.sgen)} (P-Q)")
        print(f"Number of switches: {len(self.net.switch)}")

    def visualise(self):
        simple_plotly(self.net)
        pf_res_plotly(self.net)