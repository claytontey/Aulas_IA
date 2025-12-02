from greedy import greedy_best_first_search
from a_star import a_star_search
from graphs import graph_ag
from heuristics import heuristic_ag

def run_ag():
    start, goal = 'Arad', 'Bucharest'
    print(f'=== {start}-{goal} GRAPH (start: {start} -> goal: {goal}) ===')
    g_path, g_order, g_cost = greedy_best_first_search(graph_ag, start, goal, heuristic_ag)
    print('[Greedy] path:', g_path, 'explored:', g_order, 'cost:', g_cost)
    a_path, a_order, a_cost = a_star_search(graph_ag, start, goal, heuristic_ag)
    print('[A*]     path:', a_path, 'explored:', a_order, 'cost:', a_cost)

if __name__ == '__main__':
    run_ag()
