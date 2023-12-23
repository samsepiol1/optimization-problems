import numpy as np
from ortools.graph.python import max_flow


# Instância de um Worker.
smf = max_flow.SimpleMaxFlow()


## Definição do Grafo
start_nodes = np.array([0, 0, 0, 1, 1, 2, 2, 3, 3])
end_nodes = np.array([1, 2, 3, 2, 4, 3, 4, 2, 4])
capacities = np.array([20, 30, 10, 40, 30, 10, 20, 5, 20])

## Para cada arco criado é necessário atribuir uma capacidade máxima, para definir o arco basta usar essa linha de código

# Add arcs in bulk.
all_arcs = smf.add_arcs_with_capacity(start_nodes, end_nodes, capacities)

# A biblioteca possui solucionadores 

# Find the maximum flow between node 0 and node 4.
status = smf.solve(0, 4)

# Exibição do resultados

if status != smf.OPTIMAL:
    print("There was an issue with the max flow input.")
    print(f"Status: {status}")
    exit(1)
print("Max flow:", smf.optimal_flow())
print("")
print(" Arc    Flow / Capacity")
solution_flows = smf.flows(all_arcs)
for arc, flow, capacity in zip(all_arcs, solution_flows, capacities):
    print(f"{smf.tail(arc)} / {smf.head(arc)}   {flow:3}  / {capacity:3}")
print("Source side min-cut:", smf.get_source_side_min_cut())
print("Sink side min-cut:", smf.get_sink_side_min_cut())

