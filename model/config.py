from cadCAD.configuration.utils import config_sim
from cadCAD.configuration import Experiment
from model.state import state
from model.psubs import psubs

simulation_parameters = {
    'T': range(9),
    'N': 1,
}

exp = Experiment()

c = config_sim(simulation_parameters)

exp.append_configs(
    model_id="default",
    initial_state=state,
    partial_state_update_blocks=psubs,
    sim_configs=c
)