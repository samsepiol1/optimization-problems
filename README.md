# Otimização Combinatória

Otimização Combinatória é um ramo da ciência da computação e da matemática aplicada que estuda problemas de otimização em conjuntos finitos. Em um problema de otimização temos uma função objetivo e um conjunto de restrições, ambos relacionados às variáveis de decisão.

Grande parte dos problemas computacionais são de natureza discreta e envolvem a
busca por uma solução atendendo certas propriedades, sendo que as possíveis alternativas crescem de forma combinatória. Um exemplo clássico é o problema de ordenação, onde se deseja encontrar uma permutação de uma sequência com ordenação
não-decrescente. Além disso, problemas reais deste tipo tornam-se ainda mais complexos quando existe limitação nos recursos disponíveis e se quer otimizar alguma medida
específica.



## Problemas de Fluxo de Redes

A maioria dos problemas relativos a ciência da computação podem ser representados com o auxilio de grafos. Grafos possuem nós e links entre eles e, no contexto de otimização, os fluxos de rede podem ser representados por esse tipo de estrutura. A otimização, em resumo, visa transportar os dados entre dois pontos com o menor custo possível e respeitando a capacidade máxima do que pode ser transportado entre esses pontos. 

### Problema de fluxos máximos

O problema do fluxo máximo é encontrar um fluxo em que a soma dos valores do fluxo para toda a rede seja a maior possível. 
Você quer transportar o material do nó 0 (a origem) para o nó 4 (o coletor). Os números ao lado dos arcos são as capacidades deles. A capacidade de um arco é a quantidade máxima que pode ser transportada por ele em um período fixo. As capacidades são as restrições para o problema.


```python
"""From Taha 'Introduction to Operations Research', example 6.4-2."""
import numpy as np

from ortools.graph.python import max_flow


def main():
    """MaxFlow simple interface example."""
    # Instantiate a SimpleMaxFlow solver.
    smf = max_flow.SimpleMaxFlow()

    # Define three parallel arrays: start_nodes, end_nodes, and the capacities
    # between each pair. For instance, the arc from node 0 to node 1 has a
    # capacity of 20.
    start_nodes = np.array([0, 0, 0, 1, 1, 2, 2, 3, 3])
    end_nodes = np.array([1, 2, 3, 2, 4, 3, 4, 2, 4])
    capacities = np.array([20, 30, 10, 40, 30, 10, 20, 5, 20])

    # Add arcs in bulk.
    #   note: we could have used add_arc_with_capacity(start, end, capacity)
    all_arcs = smf.add_arcs_with_capacity(start_nodes, end_nodes, capacities)

    # Find the maximum flow between node 0 and node 4.
    status = smf.solve(0, 4)

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


if __name__ == "__main__":
    main()
```

### Problema do Custo minímo

O problema do custo minímo diz respeito a encontrar o fluxo com menor custo possível de transporte em cada arco. No problema de custo minimo existem tipos de nós especiais onde cada nó vai ter a função de demanda e fornecimento. 

```python
"""From Bradley, Hax and Maganti, 'Applied Mathematical Programming', figure 8.1."""
import numpy as np

from ortools.graph.python import min_cost_flow


def main():
    """MinCostFlow simple interface example."""
    # Instantiate a SimpleMinCostFlow solver.
    smcf = min_cost_flow.SimpleMinCostFlow()

    # Define four parallel arrays: sources, destinations, capacities,
    # and unit costs between each pair. For instance, the arc from node 0
    # to node 1 has a capacity of 15.
    start_nodes = np.array([0, 0, 1, 1, 1, 2, 2, 3, 4])
    end_nodes = np.array([1, 2, 2, 3, 4, 3, 4, 4, 2])
    capacities = np.array([15, 8, 20, 4, 10, 15, 4, 20, 5])
    unit_costs = np.array([4, 4, 2, 2, 6, 1, 3, 2, 3])

    # Define an array of supplies at each node.
    supplies = [20, 0, 0, -5, -15]

    # Add arcs, capacities and costs in bulk using numpy.
    all_arcs = smcf.add_arcs_with_capacity_and_unit_cost(
        start_nodes, end_nodes, capacities, unit_costs
    )

    # Add supply for each nodes.
    smcf.set_nodes_supplies(np.arange(0, len(supplies)), supplies)

    # Find the min cost flow.
    status = smcf.solve()

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


if __name__ == "__main__":
    main()

```


## Referências

https://developers.google.com/optimization/introduction/python?hl=pt-br
https://developers.google.com/optimization/flow/mincostflow?hl=pt-br





 



