def bfs(initial: T, goal_test: Callable[[T], bool], successors: Callable[[T],
    List[T]]) -> Optional[Node[T]]:
    # frontier is where we've yet to go
   frontier: Queue[Node[T]] = Queue()
   frontier.push(Node(initial, None))
 # explored is where we've been
   explored: Set[T] = {initial}
 # keep going while there is more to explore
 while not frontier.empty:
   current_node: Node[T] = frontier.pop()
   current_state: T = current_node.state
   # if we found the goal, we're done
   if goal_test(current_state):
       return current_node
   # check where we can go next and haven't explored
   for child in successors(current_state):
       if child in explored: # skip children we already explored
           continue
       explored.add(child)
       frontier.push(Node(child, current_node))
 return None # went through everything and never found goal
