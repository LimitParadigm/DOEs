import pandapower as pp
from Code.Networks.network_abstract import NetworkAbstract

class Network1(NetworkAbstract):
    def __init__(self):
        self.net = self.create_network()

    def create_network(self):
        #create empty net
        net = pp.create_empty_network()

        # Per unit (3-phase values)
        Pbase = 100  # MVA
        Vbase_high = 110 # kV
        Vbase_medium = 20 # kV
        Vbase_low = 0.4 # kV

        X_km = 0.0376
        R_km = 0.037

        #create buses
        b0 = pp.create_bus(net, vn_kv=Vbase_high, name="Bus 1", geodata=(-10,10))
        b1 = pp.create_bus(net, vn_kv=Vbase_medium, name="Bus 2", geodata=(-5,10))
        b2 = pp.create_bus(net, vn_kv=Vbase_medium, name="Bus 3", geodata=(0,10))
        b3 = pp.create_bus(net, vn_kv=Vbase_low, name="Bus 4", geodata=(-5,0))
        b4 = pp.create_bus(net, vn_kv=Vbase_low, name="Bus 5", geodata=(0,0))
        b5 = pp.create_bus(net, vn_kv=Vbase_low, name="Bus 6", geodata=(3,3))
        b6 = pp.create_bus(net, vn_kv=Vbase_low, name="Bus 7", geodata=(-4,2))
        b7 = pp.create_bus(net, vn_kv=Vbase_low, name="Bus 8", geodata=(-4,3))

        #create lines
        pp.create_line(net, name="line1", from_bus = b1, to_bus = b2,
                length_km=10, std_type= '490-AL1/64-ST1A 110.0')
        pp.create_line(net, name="line2", from_bus = b3, to_bus = b6,
                length_km=0.23, std_type = '94-AL1/15-ST1A 0.4')
        pp.create_line(net, name="line3", from_bus = b4, to_bus = b5,
                length_km=0.45, std_type = "94-AL1/15-ST1A 0.4")
        pp.create_line(net, name="line3", from_bus = b4, to_bus = b5,
                length_km=0.45, std_type = "94-AL1/15-ST1A 0.4")
        pp.create_line(net, name="line4", from_bus = b4, to_bus = b7,
                    length_km=0.45, std_type = "94-AL1/15-ST1A 0.4")


        #create transformers

        pp.create_transformer(net, b0, b1, name="trfo1", std_type="25 MVA 110/20 kV")
        pp.create_transformer(net, b1, b3, name="trfo2", std_type="0.4 MVA 20/0.4 kV")
        pp.create_transformer(net, b2, b4, name="trfo3", std_type="0.4 MVA 20/0.4 kV")


        #create bus elements
        pp.create_ext_grid(net, bus=b0, vm_pu=1.00, name="Grid Connection")
        pp.create_load(net, bus=b6, p_mw=0.01, q_mvar=0.01, name="Load")
        pp.create_load(net, bus=b7, p_mw=0.01, q_mvar=0.01, name="Load")
        pp.create_gen(net, bus=b6, p_mw=0.02, vm_pu=1.00, name="PV", max_q_mvar=200, min_q_mvar=0, max_p_mw=300, min_p_mw=0)

        return net