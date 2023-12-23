import numpy as np

# Biblioteca que resolve o problema com workers 
from ortools.graph.python import min_cost_flow


# Instantiate a SimpleMinCostFlow solver.
smcf = min_cost_flow.SimpleMinCostFlow()

start_nodes = np.array([0, 0, 1, 1, 1, 2, 2, 3, 4])
end_nodes = np.array([1, 2, 2, 3, 4, 3, 4, 4, 2])
capacities = np.array([15, 8, 20, 4, 10, 15, 4, 20, 5])

# Diferente do código anterior, o fluxo atual possui um custo unitário para cada arco
unit_costs = np.array([4, 4, 2, 2, 6, 1, 3, 2, 3])

# Add arcs, capacities and costs in bulk using numpy.
all_arcs = smcf.add_arcs_with_capacity_and_unit_cost(
    start_nodes, end_nodes, capacities, unit_costs
)

# adicionar fornecimento para os nós necessários
smcf.set_nodes_supplies(np.arange(0, len(supplies)), supplies)



# Apresentando resultados
if status != smcf.OPTIMAL:
    print("There was an issue with the min cost flow input.")
    print(f"Status: {status}")
    exit(1)
print(f"Minimum cost: {smcf.optimal_cost()}")
print("")
print(" Arc    Flow / Capacity Cost")
solution_flows = smcf.flows(all_arcs)
costs = solution_flows * unit_costs
for arc, flow, cost in zip(all_arcs, solution_flows, costs):
    print(
        f"{smcf.tail(arc):1} -> {smcf.head(arc)}  {flow:3}  / {smcf.capacity(arc):3}       {cost}"
    )


